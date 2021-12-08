from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JurjenLangParser import JurjenLangParser
else:
    from JurjenLangParser import JurjenLangParser
from JurjenLangListener import *

from src.ScopeStack import *
from src.Scope import *
from src.Variable import *
from src.Cache import *

class JurjenLangCustomListener(JurjenLangListener):
    def __init__(self, debug_enabled=True):
        self.debug_enabled = debug_enabled
        self.scope_stack = ScopeStack()
        self.cache = Cache()

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

    def _get_expression_child_value(self, child_obj) -> int:
        child=None
        if type(child_obj) is JurjenLangParser.VariableContext:
            variable_name = str(child_obj.getChild(0))
            print("LF: " + variable_name)
            variable = self.scope_stack.latest().get_variable(variable_name)
            print(f"found: {variable}")
            child = variable.value
        elif type(child_obj) is JurjenLangParser.IntegerContext:
            print("Got expression value from integer")
            child = int(str(child_obj.getChild(0)))
        else: # its another expression
            print("Got expression value from cache")
            value = self.cache.pop()
            child = int(str(value))
        return child

    def exitE(self, ctx:JurjenLangParser.EContext):
        if ctx.getChildCount() == 1:
            child_obj = ctx.getChild(0)

            if type(child_obj) is JurjenLangParser.IntegerContext:
                self.cache.push(ctx, child_obj.getChild(0))
                self.debug(f"added {child_obj.getChild(0)} (integer) to cache")
            elif type(child_obj) is JurjenLangParser.VariableContext:
                var_name = str(child_obj.getChild(0))
                var_val = self.scope_stack.latest().get_variable(var_name).value

                self.cache.push(ctx, var_val)
                self.debug(f"added {var_val} (from variable {var_name}) to cache")
            elif type(child_obj) is JurjenLangParser.Prio_eContext:
                self.debug(f"prio e found {child_obj}")
        else:
            child1_obj = self.cache.value(ctx.getChild(0))
            child2_obj = self.cache.value(ctx.getChild(2))

            print(f"child1type {type(child1_obj)}")

            child1 = self._get_expression_child_value(child1_obj)
            child2 = self._get_expression_child_value(child2_obj)
            operator = str(ctx.getChild(1))

            res = None
            if operator == '+':
                res = child1 + child2
            elif operator == '-':
                res = child1 - child2
            elif operator == '*':
                res = child1 * child2
            elif operator == '/':
                res = child1 / child2
            
            self.cache.remove(ctx.getChild(0))
            self.cache.remove(ctx.getChild(2))
            self.cache.push(ctx, res)

            self.debug(f"operated {child1} {operator} {child2} = {res} to cache")

    def exitFunc_return(self, ctx:JurjenLangParser.Func_returnContext):
        returnval = ctx.getChild(1)
        print(f"returning: {returnval}")

    def exitAss(self, ctx:JurjenLangParser.AssContext):
        receiving_name = str(ctx.getChild(0).getChild(0))
        sending = ctx.getChild(2)               # Expression
        scope = self.scope_stack.latest()

        print(f"sending: {sending} ({type(sending)})")
        if type(sending) is JurjenLangParser.EContext:
            print("ITS AN EXPRESSION")
            # Assignment is from an expression

            print(str(self.cache))

            value = self.cache.next()

            var = Variable(receiving_name, value)
            scope.add_local_variable(var)

            print(str(scope))


        else:
            print("ITS A VAR")
            # Assignment is from another variable

            sending_name = str(sending.getChild(0))
            sending_variable = scope.get_variable(sending_name)
            if sending_variable is None:
                raise ValueError("ERROR VARIABLE IS NOT DEFINED")

            sending_variable_value = sending_variable.value
            var = Variable(receiving_name, sending_variable_value)
            scope.add_local_variable(var)

            print(str(scope))
