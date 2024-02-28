// Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ZCodeParser}.
 */
public interface ZCodeListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(ZCodeParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(ZCodeParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#decl_list}.
	 * @param ctx the parse tree
	 */
	void enterDecl_list(ZCodeParser.Decl_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#decl_list}.
	 * @param ctx the parse tree
	 */
	void exitDecl_list(ZCodeParser.Decl_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#nl_type}.
	 * @param ctx the parse tree
	 */
	void enterNl_type(ZCodeParser.Nl_typeContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#nl_type}.
	 * @param ctx the parse tree
	 */
	void exitNl_type(ZCodeParser.Nl_typeContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#nl_nullable_list}.
	 * @param ctx the parse tree
	 */
	void enterNl_nullable_list(ZCodeParser.Nl_nullable_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#nl_nullable_list}.
	 * @param ctx the parse tree
	 */
	void exitNl_nullable_list(ZCodeParser.Nl_nullable_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#nl_list}.
	 * @param ctx the parse tree
	 */
	void enterNl_list(ZCodeParser.Nl_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#nl_list}.
	 * @param ctx the parse tree
	 */
	void exitNl_list(ZCodeParser.Nl_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration(ZCodeParser.DeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration(ZCodeParser.DeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#variable_stat}.
	 * @param ctx the parse tree
	 */
	void enterVariable_stat(ZCodeParser.Variable_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#variable_stat}.
	 * @param ctx the parse tree
	 */
	void exitVariable_stat(ZCodeParser.Variable_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#dtype}.
	 * @param ctx the parse tree
	 */
	void enterDtype(ZCodeParser.DtypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#dtype}.
	 * @param ctx the parse tree
	 */
	void exitDtype(ZCodeParser.DtypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#primitiveDtype}.
	 * @param ctx the parse tree
	 */
	void enterPrimitiveDtype(ZCodeParser.PrimitiveDtypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#primitiveDtype}.
	 * @param ctx the parse tree
	 */
	void exitPrimitiveDtype(ZCodeParser.PrimitiveDtypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#arrayDtype}.
	 * @param ctx the parse tree
	 */
	void enterArrayDtype(ZCodeParser.ArrayDtypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#arrayDtype}.
	 * @param ctx the parse tree
	 */
	void exitArrayDtype(ZCodeParser.ArrayDtypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#explicit_declare}.
	 * @param ctx the parse tree
	 */
	void enterExplicit_declare(ZCodeParser.Explicit_declareContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#explicit_declare}.
	 * @param ctx the parse tree
	 */
	void exitExplicit_declare(ZCodeParser.Explicit_declareContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#primitive_declare}.
	 * @param ctx the parse tree
	 */
	void enterPrimitive_declare(ZCodeParser.Primitive_declareContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#primitive_declare}.
	 * @param ctx the parse tree
	 */
	void exitPrimitive_declare(ZCodeParser.Primitive_declareContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#array_declare}.
	 * @param ctx the parse tree
	 */
	void enterArray_declare(ZCodeParser.Array_declareContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#array_declare}.
	 * @param ctx the parse tree
	 */
	void exitArray_declare(ZCodeParser.Array_declareContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#numlit_list}.
	 * @param ctx the parse tree
	 */
	void enterNumlit_list(ZCodeParser.Numlit_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#numlit_list}.
	 * @param ctx the parse tree
	 */
	void exitNumlit_list(ZCodeParser.Numlit_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#numlit_tail}.
	 * @param ctx the parse tree
	 */
	void enterNumlit_tail(ZCodeParser.Numlit_tailContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#numlit_tail}.
	 * @param ctx the parse tree
	 */
	void exitNumlit_tail(ZCodeParser.Numlit_tailContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#implicit_declare}.
	 * @param ctx the parse tree
	 */
	void enterImplicit_declare(ZCodeParser.Implicit_declareContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#implicit_declare}.
	 * @param ctx the parse tree
	 */
	void exitImplicit_declare(ZCodeParser.Implicit_declareContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#function_stat}.
	 * @param ctx the parse tree
	 */
	void enterFunction_stat(ZCodeParser.Function_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#function_stat}.
	 * @param ctx the parse tree
	 */
	void exitFunction_stat(ZCodeParser.Function_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#function_definition}.
	 * @param ctx the parse tree
	 */
	void enterFunction_definition(ZCodeParser.Function_definitionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#function_definition}.
	 * @param ctx the parse tree
	 */
	void exitFunction_definition(ZCodeParser.Function_definitionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#function_declaration}.
	 * @param ctx the parse tree
	 */
	void enterFunction_declaration(ZCodeParser.Function_declarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#function_declaration}.
	 * @param ctx the parse tree
	 */
	void exitFunction_declaration(ZCodeParser.Function_declarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#param_list}.
	 * @param ctx the parse tree
	 */
	void enterParam_list(ZCodeParser.Param_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#param_list}.
	 * @param ctx the parse tree
	 */
	void exitParam_list(ZCodeParser.Param_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#param_list_tail}.
	 * @param ctx the parse tree
	 */
	void enterParam_list_tail(ZCodeParser.Param_list_tailContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#param_list_tail}.
	 * @param ctx the parse tree
	 */
	void exitParam_list_tail(ZCodeParser.Param_list_tailContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#parameter}.
	 * @param ctx the parse tree
	 */
	void enterParameter(ZCodeParser.ParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#parameter}.
	 * @param ctx the parse tree
	 */
	void exitParameter(ZCodeParser.ParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(ZCodeParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(ZCodeParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#statement_list}.
	 * @param ctx the parse tree
	 */
	void enterStatement_list(ZCodeParser.Statement_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#statement_list}.
	 * @param ctx the parse tree
	 */
	void exitStatement_list(ZCodeParser.Statement_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#return_stat}.
	 * @param ctx the parse tree
	 */
	void enterReturn_stat(ZCodeParser.Return_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#return_stat}.
	 * @param ctx the parse tree
	 */
	void exitReturn_stat(ZCodeParser.Return_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#break_stat}.
	 * @param ctx the parse tree
	 */
	void enterBreak_stat(ZCodeParser.Break_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#break_stat}.
	 * @param ctx the parse tree
	 */
	void exitBreak_stat(ZCodeParser.Break_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#continue_stat}.
	 * @param ctx the parse tree
	 */
	void enterContinue_stat(ZCodeParser.Continue_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#continue_stat}.
	 * @param ctx the parse tree
	 */
	void exitContinue_stat(ZCodeParser.Continue_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#block_stat}.
	 * @param ctx the parse tree
	 */
	void enterBlock_stat(ZCodeParser.Block_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#block_stat}.
	 * @param ctx the parse tree
	 */
	void exitBlock_stat(ZCodeParser.Block_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#function_call}.
	 * @param ctx the parse tree
	 */
	void enterFunction_call(ZCodeParser.Function_callContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#function_call}.
	 * @param ctx the parse tree
	 */
	void exitFunction_call(ZCodeParser.Function_callContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#comment}.
	 * @param ctx the parse tree
	 */
	void enterComment(ZCodeParser.CommentContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#comment}.
	 * @param ctx the parse tree
	 */
	void exitComment(ZCodeParser.CommentContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(ZCodeParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(ZCodeParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#relation_operation}.
	 * @param ctx the parse tree
	 */
	void enterRelation_operation(ZCodeParser.Relation_operationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#relation_operation}.
	 * @param ctx the parse tree
	 */
	void exitRelation_operation(ZCodeParser.Relation_operationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#relational_expr}.
	 * @param ctx the parse tree
	 */
	void enterRelational_expr(ZCodeParser.Relational_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#relational_expr}.
	 * @param ctx the parse tree
	 */
	void exitRelational_expr(ZCodeParser.Relational_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#logical_expr}.
	 * @param ctx the parse tree
	 */
	void enterLogical_expr(ZCodeParser.Logical_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#logical_expr}.
	 * @param ctx the parse tree
	 */
	void exitLogical_expr(ZCodeParser.Logical_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#adding_expr}.
	 * @param ctx the parse tree
	 */
	void enterAdding_expr(ZCodeParser.Adding_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#adding_expr}.
	 * @param ctx the parse tree
	 */
	void exitAdding_expr(ZCodeParser.Adding_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#multiplying_expr}.
	 * @param ctx the parse tree
	 */
	void enterMultiplying_expr(ZCodeParser.Multiplying_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#multiplying_expr}.
	 * @param ctx the parse tree
	 */
	void exitMultiplying_expr(ZCodeParser.Multiplying_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#not_logical}.
	 * @param ctx the parse tree
	 */
	void enterNot_logical(ZCodeParser.Not_logicalContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#not_logical}.
	 * @param ctx the parse tree
	 */
	void exitNot_logical(ZCodeParser.Not_logicalContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#sign_expr}.
	 * @param ctx the parse tree
	 */
	void enterSign_expr(ZCodeParser.Sign_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#sign_expr}.
	 * @param ctx the parse tree
	 */
	void exitSign_expr(ZCodeParser.Sign_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#index_expr}.
	 * @param ctx the parse tree
	 */
	void enterIndex_expr(ZCodeParser.Index_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#index_expr}.
	 * @param ctx the parse tree
	 */
	void exitIndex_expr(ZCodeParser.Index_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#parenthesis_expr}.
	 * @param ctx the parse tree
	 */
	void enterParenthesis_expr(ZCodeParser.Parenthesis_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#parenthesis_expr}.
	 * @param ctx the parse tree
	 */
	void exitParenthesis_expr(ZCodeParser.Parenthesis_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(ZCodeParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(ZCodeParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#array_expr}.
	 * @param ctx the parse tree
	 */
	void enterArray_expr(ZCodeParser.Array_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#array_expr}.
	 * @param ctx the parse tree
	 */
	void exitArray_expr(ZCodeParser.Array_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#function_expr}.
	 * @param ctx the parse tree
	 */
	void enterFunction_expr(ZCodeParser.Function_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#function_expr}.
	 * @param ctx the parse tree
	 */
	void exitFunction_expr(ZCodeParser.Function_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#expression_list}.
	 * @param ctx the parse tree
	 */
	void enterExpression_list(ZCodeParser.Expression_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#expression_list}.
	 * @param ctx the parse tree
	 */
	void exitExpression_list(ZCodeParser.Expression_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#expression_list_tail}.
	 * @param ctx the parse tree
	 */
	void enterExpression_list_tail(ZCodeParser.Expression_list_tailContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#expression_list_tail}.
	 * @param ctx the parse tree
	 */
	void exitExpression_list_tail(ZCodeParser.Expression_list_tailContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#expression_nonempty_list}.
	 * @param ctx the parse tree
	 */
	void enterExpression_nonempty_list(ZCodeParser.Expression_nonempty_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#expression_nonempty_list}.
	 * @param ctx the parse tree
	 */
	void exitExpression_nonempty_list(ZCodeParser.Expression_nonempty_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#expression_nonempty_tail}.
	 * @param ctx the parse tree
	 */
	void enterExpression_nonempty_tail(ZCodeParser.Expression_nonempty_tailContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#expression_nonempty_tail}.
	 * @param ctx the parse tree
	 */
	void exitExpression_nonempty_tail(ZCodeParser.Expression_nonempty_tailContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#control_stat}.
	 * @param ctx the parse tree
	 */
	void enterControl_stat(ZCodeParser.Control_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#control_stat}.
	 * @param ctx the parse tree
	 */
	void exitControl_stat(ZCodeParser.Control_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#elif_stmt_list}.
	 * @param ctx the parse tree
	 */
	void enterElif_stmt_list(ZCodeParser.Elif_stmt_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#elif_stmt_list}.
	 * @param ctx the parse tree
	 */
	void exitElif_stmt_list(ZCodeParser.Elif_stmt_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#ifst_component}.
	 * @param ctx the parse tree
	 */
	void enterIfst_component(ZCodeParser.Ifst_componentContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#ifst_component}.
	 * @param ctx the parse tree
	 */
	void exitIfst_component(ZCodeParser.Ifst_componentContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#loop_stat}.
	 * @param ctx the parse tree
	 */
	void enterLoop_stat(ZCodeParser.Loop_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#loop_stat}.
	 * @param ctx the parse tree
	 */
	void exitLoop_stat(ZCodeParser.Loop_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(ZCodeParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(ZCodeParser.AssignmentContext ctx);
}