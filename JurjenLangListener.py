# Generated from JurjenLang.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JurjenLangParser import JurjenLangParser
else:
    from JurjenLangParser import JurjenLangParser

# This class defines a complete listener for a parse tree produced by JurjenLangParser.
class JurjenLangListener(ParseTreeListener):

    # Enter a parse tree produced by JurjenLangParser#startRule.
    def enterStartRule(self, ctx:JurjenLangParser.StartRuleContext):
        pass

    # Exit a parse tree produced by JurjenLangParser#startRule.
    def exitStartRule(self, ctx:JurjenLangParser.StartRuleContext):
        pass


    # Enter a parse tree produced by JurjenLangParser#func.
    def enterFunc(self, ctx:JurjenLangParser.FuncContext):
        pass

    # Exit a parse tree produced by JurjenLangParser#func.
    def exitFunc(self, ctx:JurjenLangParser.FuncContext):
        pass


    # Enter a parse tree produced by JurjenLangParser#func_def.
    def enterFunc_def(self, ctx:JurjenLangParser.Func_defContext):
        pass

    # Exit a parse tree produced by JurjenLangParser#func_def.
    def exitFunc_def(self, ctx:JurjenLangParser.Func_defContext):
        pass


    # Enter a parse tree produced by JurjenLangParser#func_return.
    def enterFunc_return(self, ctx:JurjenLangParser.Func_returnContext):
        pass

    # Exit a parse tree produced by JurjenLangParser#func_return.
    def exitFunc_return(self, ctx:JurjenLangParser.Func_returnContext):
        pass


    # Enter a parse tree produced by JurjenLangParser#scope.
    def enterScope(self, ctx:JurjenLangParser.ScopeContext):
        pass

    # Exit a parse tree produced by JurjenLangParser#scope.
    def exitScope(self, ctx:JurjenLangParser.ScopeContext):
        pass


    # Enter a parse tree produced by JurjenLangParser#stats.
    def enterStats(self, ctx:JurjenLangParser.StatsContext):
        pass

    # Exit a parse tree produced by JurjenLangParser#stats.
    def exitStats(self, ctx:JurjenLangParser.StatsContext):
        pass


    # Enter a parse tree produced by JurjenLangParser#stat.
    def enterStat(self, ctx:JurjenLangParser.StatContext):
        pass

    # Exit a parse tree produced by JurjenLangParser#stat.
    def exitStat(self, ctx:JurjenLangParser.StatContext):
        pass


    # Enter a parse tree produced by JurjenLangParser#printstat.
    def enterPrintstat(self, ctx:JurjenLangParser.PrintstatContext):
        pass

    # Exit a parse tree produced by JurjenLangParser#printstat.
    def exitPrintstat(self, ctx:JurjenLangParser.PrintstatContext):
        pass


    # Enter a parse tree produced by JurjenLangParser#retstat.
    def enterRetstat(self, ctx:JurjenLangParser.RetstatContext):
        pass

    # Exit a parse tree produced by JurjenLangParser#retstat.
    def exitRetstat(self, ctx:JurjenLangParser.RetstatContext):
        pass


    # Enter a parse tree produced by JurjenLangParser#ass.
    def enterAss(self, ctx:JurjenLangParser.AssContext):
        pass

    # Exit a parse tree produced by JurjenLangParser#ass.
    def exitAss(self, ctx:JurjenLangParser.AssContext):
        pass


    # Enter a parse tree produced by JurjenLangParser#e.
    def enterE(self, ctx:JurjenLangParser.EContext):
        pass

    # Exit a parse tree produced by JurjenLangParser#e.
    def exitE(self, ctx:JurjenLangParser.EContext):
        pass


    # Enter a parse tree produced by JurjenLangParser#prio_e.
    def enterPrio_e(self, ctx:JurjenLangParser.Prio_eContext):
        pass

    # Exit a parse tree produced by JurjenLangParser#prio_e.
    def exitPrio_e(self, ctx:JurjenLangParser.Prio_eContext):
        pass


    # Enter a parse tree produced by JurjenLangParser#variable.
    def enterVariable(self, ctx:JurjenLangParser.VariableContext):
        pass

    # Exit a parse tree produced by JurjenLangParser#variable.
    def exitVariable(self, ctx:JurjenLangParser.VariableContext):
        pass


    # Enter a parse tree produced by JurjenLangParser#integer.
    def enterInteger(self, ctx:JurjenLangParser.IntegerContext):
        pass

    # Exit a parse tree produced by JurjenLangParser#integer.
    def exitInteger(self, ctx:JurjenLangParser.IntegerContext):
        pass



del JurjenLangParser