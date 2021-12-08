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
    def __init__(self, debug_enabled=False, debug_scope_enabled=False):
        self.debug_enabled = debug_enabled
        self.debug_scope_enabled = debug_scope_enabled
        self.scope_stack = ScopeStack()
        self.cache = Cache()

    def debug_scope(self, msg):
        if self.debug_scope_enabled:
            print(msg)

    def debug(self, msg):
        if self.debug_enabled:
            print(msg)

    def enterScope(self, ctx:JurjenLangParser.ScopeContext):
        self.scope_stack.push()
    
    def exitScope(self, ctx:JurjenLangParser.ScopeContext):
        self.scope_stack.pop()

    def _get_expression_child_value(self, child_obj) -> int:
        child=None
        if type(child_obj) is JurjenLangParser.VariableContext:
            variable_name = str(child_obj.getChild(0))
            self.debug("LF: " + variable_name)
            variable = self.scope_stack.latest().get_variable(variable_name)
            self.debug(f"found: {variable}")
            child = variable.value
        elif type(child_obj) is JurjenLangParser.IntegerContext:
            self.debug("Got expression value from integer")
            child = int(str(child_obj.getChild(0)))
        else: # its another expression
            self.debug("Got expression value from cache")
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
                var_obj = self.scope_stack.latest().get_variable(var_name)
                if var_obj is None:
                    raise ValueError("ERROR VARIABLE IS NOT DEFINED")
                var_val = var_obj.value

                self.cache.push(ctx, var_val)
                self.debug(f"added {var_val} (from variable {var_name}) to cache")
        elif ctx.getChildCount() == 2:
            child_obj = self.cache.value(ctx.getChild(0))
            child = self._get_expression_child_value(child_obj)
            operator = str(ctx.getChild(1))

            res = None
            if operator == '!':
                res = 1
                for i in range(2, child+1):
                    res *= i
                    
            self.cache.remove(ctx.getChild(0))
            self.cache.push(ctx, res)
            self.debug(f"operated {child} {operator} = {res} to cache")
            
        elif ctx.getChildCount() == 3:
            child1_obj = self.cache.value(ctx.getChild(0))
            child2_obj = self.cache.value(ctx.getChild(2))

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
            elif operator == '^':
                res = child1 ** child2
            
            self.cache.remove(ctx.getChild(0))
            self.cache.remove(ctx.getChild(2))
            self.cache.push(ctx, res)

            self.debug(f"operated {child1} {operator} {child2} = {res} to cache")

    def exitFunc_return(self, ctx:JurjenLangParser.Func_returnContext):
        returnval = ctx.getChild(1)
        self.debug(f"returning: {returnval}")

    def exitAss(self, ctx:JurjenLangParser.AssContext):
        receiving_name = str(ctx.getChild(0).getChild(0))
        sending = ctx.getChild(2)               # Expression
        scope = self.scope_stack.latest()

        self.debug(f"sending: {sending} ({type(sending)})")
        if type(sending) is JurjenLangParser.EContext:
            # Assignment is from an expression
            self.debug(str(self.cache))

            value = self.cache.next()
            var = Variable(receiving_name, value)
            scope.add_local_variable(var)

            self.debug_scope(str(scope))
        else:
            # Assignment is from another variable

            sending_name = str(sending.getChild(0))
            sending_variable = scope.get_variable(sending_name)
            if sending_variable is None:
                raise ValueError("ERROR VARIABLE IS NOT DEFINED")

            sending_variable_value = sending_variable.value
            var = Variable(receiving_name, sending_variable_value)
            scope.add_local_variable(var)

            self.debug_scope(str(scope))
    
    def exitPrintstat(self, ctx:JurjenLangParser.PrintstatContext):
        e_child = ctx.getChild(0)
        value = self._get_expression_child_value(e_child)
        print(value)
