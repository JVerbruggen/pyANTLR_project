from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JurjenLangParser import JurjenLangParser
else:
    from JurjenLangParser import JurjenLangParser
from JurjenLangListener import *

from src.ScopeStack import *
from src.Scope import *
from src.Variable import *

class JurjenLangCustomListener(JurjenLangListener):
    cache = dict()

    def __init__(self, debug_enabled=False):
        self.debug_enabled = debug_enabled
        self.scope_stack = ScopeStack()

    def debug(self, msg):
        if self.debug_enabled:
            print(msg)

    def getResult(self):
        # if len(self.retstack) == 0: return None
        # return self.retstack[-1]
        # return self.cache[next(iter(self.cache))]
        pass

    def enterScope(self, ctx:JurjenLangParser.ScopeContext):
        self.scope_stack.push()
    
    def exitScope(self, ctx:JurjenLangParser.ScopeContext):
        self.scope_stack.pop()

    def exitE(self, ctx:JurjenLangParser.EContext):
        if ctx.getChildCount() == 1:
            self.cache[ctx] = ctx.getChild(0)
            self.debug(f"added {ctx.getChild(0)} to cache")
        else:
            child1_obj = self.cache[ctx.getChild(0)]
            child2_obj = self.cache[ctx.getChild(2)]

            print(f"child1type {type(child1_obj)}")

            child1 = None
            child2 = None

            if type(child1_obj) is JurjenLangParser.VariableContext:
                variable_name = str(child1_obj.getChild(0))
                print("LF: " + variable_name)
                variable = self.scope_stack.latest().get_variable(variable_name)
                print(f"found: {variable}")
                child1 = variable.value
            else:
                child1 = int(str(child1_obj))

            operator = str(ctx.getChild(1))
            child2 = int(str(child2_obj))

            res = None
            if operator == '+':
                res = child1 + child2
            elif operator == '-':
                res = child1 - child2
            elif operator == '*':
                res = child1 * child2
            elif operator == '/':
                res = child1 / child2
            
            del self.cache[ctx.getChild(0)]
            del self.cache[ctx.getChild(2)]
            self.cache[ctx] = res

            self.debug(f"operated {child1} {operator} {child2} = {res} to cache")

    def exitFunc_return(self, ctx:JurjenLangParser.Func_returnContext):
        returnval = ctx.getChild(1)
        print(f"returning: {returnval}")

    def exitAss(self, ctx:JurjenLangParser.AssContext):
        receiving_name = str(ctx.getChild(0).getChild(0))
        sending = ctx.getChild(2)
        scope = self.scope_stack.latest()

        print(f"sending: {sending} ({type(sending)})")
        if type(sending) is JurjenLangParser.EContext:
            print("ITS AN EXPRESSION")
            # Assignment is from an expression

            print(str(self.cache))

            value = self.cache[next(iter(self.cache))]
            var = Variable(receiving_name, value)
            scope.add_local_variable(var)

            print(str(scope))


        else:
            print("ITS A VAR")
            # Assignment is from another variable

            sending_name = str(sending)
            sending_variable = scope.get_variable(sending_name)
            if sending_variable is None:
                raise ValueError("ERROR VARIABLE IS NOT DEFINED")

            sending_variable_value = sending_variable.value
            var = Variable(receiving_name, sending_variable_value)
            scope.add_local_variable(var)

            print(str(scope))
