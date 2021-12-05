from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JurjenLangParser import JurjenLangParser
else:
    from JurjenLangParser import JurjenLangParser
from JurjenLangListener import *

class JurjenLangCustomListener(JurjenLangListener):
    cache = dict()

    def __init__(self, debug_enabled=False):
        self.debug_enabled = debug_enabled

    def debug(self, msg):
        if self.debug_enabled:
            print(msg)

    def getResult(self):
        return self.cache[next(iter(self.cache))]

    def enterE(self, ctx:JurjenLangParser.EContext):
        pass

    def exitE(self, ctx:JurjenLangParser.EContext):
        if ctx.getChildCount() == 1:
            self.cache[ctx] = ctx.getChild(0)
            self.debug(f"added {ctx.getChild(0)} to cache")
        else:
            child1 = int(str(self.cache[ctx.getChild(0)]))
            operator = str(ctx.getChild(1))
            child2 = int(str(self.cache[ctx.getChild(2)]))

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