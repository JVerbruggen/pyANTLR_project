// Generated from JurjenLang.g4 by ANTLR 4.9.3
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link JurjenLangParser}.
 */
public interface JurjenLangListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link JurjenLangParser#startRule}.
	 * @param ctx the parse tree
	 */
	void enterStartRule(JurjenLangParser.StartRuleContext ctx);
	/**
	 * Exit a parse tree produced by {@link JurjenLangParser#startRule}.
	 * @param ctx the parse tree
	 */
	void exitStartRule(JurjenLangParser.StartRuleContext ctx);
	/**
	 * Enter a parse tree produced by {@link JurjenLangParser#func}.
	 * @param ctx the parse tree
	 */
	void enterFunc(JurjenLangParser.FuncContext ctx);
	/**
	 * Exit a parse tree produced by {@link JurjenLangParser#func}.
	 * @param ctx the parse tree
	 */
	void exitFunc(JurjenLangParser.FuncContext ctx);
	/**
	 * Enter a parse tree produced by {@link JurjenLangParser#func_def}.
	 * @param ctx the parse tree
	 */
	void enterFunc_def(JurjenLangParser.Func_defContext ctx);
	/**
	 * Exit a parse tree produced by {@link JurjenLangParser#func_def}.
	 * @param ctx the parse tree
	 */
	void exitFunc_def(JurjenLangParser.Func_defContext ctx);
	/**
	 * Enter a parse tree produced by {@link JurjenLangParser#func_return}.
	 * @param ctx the parse tree
	 */
	void enterFunc_return(JurjenLangParser.Func_returnContext ctx);
	/**
	 * Exit a parse tree produced by {@link JurjenLangParser#func_return}.
	 * @param ctx the parse tree
	 */
	void exitFunc_return(JurjenLangParser.Func_returnContext ctx);
	/**
	 * Enter a parse tree produced by {@link JurjenLangParser#scope}.
	 * @param ctx the parse tree
	 */
	void enterScope(JurjenLangParser.ScopeContext ctx);
	/**
	 * Exit a parse tree produced by {@link JurjenLangParser#scope}.
	 * @param ctx the parse tree
	 */
	void exitScope(JurjenLangParser.ScopeContext ctx);
	/**
	 * Enter a parse tree produced by {@link JurjenLangParser#stats}.
	 * @param ctx the parse tree
	 */
	void enterStats(JurjenLangParser.StatsContext ctx);
	/**
	 * Exit a parse tree produced by {@link JurjenLangParser#stats}.
	 * @param ctx the parse tree
	 */
	void exitStats(JurjenLangParser.StatsContext ctx);
	/**
	 * Enter a parse tree produced by {@link JurjenLangParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterStat(JurjenLangParser.StatContext ctx);
	/**
	 * Exit a parse tree produced by {@link JurjenLangParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitStat(JurjenLangParser.StatContext ctx);
	/**
	 * Enter a parse tree produced by {@link JurjenLangParser#retstat}.
	 * @param ctx the parse tree
	 */
	void enterRetstat(JurjenLangParser.RetstatContext ctx);
	/**
	 * Exit a parse tree produced by {@link JurjenLangParser#retstat}.
	 * @param ctx the parse tree
	 */
	void exitRetstat(JurjenLangParser.RetstatContext ctx);
	/**
	 * Enter a parse tree produced by {@link JurjenLangParser#ass}.
	 * @param ctx the parse tree
	 */
	void enterAss(JurjenLangParser.AssContext ctx);
	/**
	 * Exit a parse tree produced by {@link JurjenLangParser#ass}.
	 * @param ctx the parse tree
	 */
	void exitAss(JurjenLangParser.AssContext ctx);
	/**
	 * Enter a parse tree produced by {@link JurjenLangParser#e}.
	 * @param ctx the parse tree
	 */
	void enterE(JurjenLangParser.EContext ctx);
	/**
	 * Exit a parse tree produced by {@link JurjenLangParser#e}.
	 * @param ctx the parse tree
	 */
	void exitE(JurjenLangParser.EContext ctx);
	/**
	 * Enter a parse tree produced by {@link JurjenLangParser#prio_e}.
	 * @param ctx the parse tree
	 */
	void enterPrio_e(JurjenLangParser.Prio_eContext ctx);
	/**
	 * Exit a parse tree produced by {@link JurjenLangParser#prio_e}.
	 * @param ctx the parse tree
	 */
	void exitPrio_e(JurjenLangParser.Prio_eContext ctx);
	/**
	 * Enter a parse tree produced by {@link JurjenLangParser#variable}.
	 * @param ctx the parse tree
	 */
	void enterVariable(JurjenLangParser.VariableContext ctx);
	/**
	 * Exit a parse tree produced by {@link JurjenLangParser#variable}.
	 * @param ctx the parse tree
	 */
	void exitVariable(JurjenLangParser.VariableContext ctx);
	/**
	 * Enter a parse tree produced by {@link JurjenLangParser#integer}.
	 * @param ctx the parse tree
	 */
	void enterInteger(JurjenLangParser.IntegerContext ctx);
	/**
	 * Exit a parse tree produced by {@link JurjenLangParser#integer}.
	 * @param ctx the parse tree
	 */
	void exitInteger(JurjenLangParser.IntegerContext ctx);
}