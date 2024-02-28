# Generated from d://antlr4//sample//Assignment2//src//main//zcode//parser//ZCode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete listener for a parse tree produced by ZCodeParser.
class ZCodeListener(ParseTreeListener):

    # Enter a parse tree produced by ZCodeParser#program.
    def enterProgram(self, ctx:ZCodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by ZCodeParser#program.
    def exitProgram(self, ctx:ZCodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by ZCodeParser#decl_list.
    def enterDecl_list(self, ctx:ZCodeParser.Decl_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#decl_list.
    def exitDecl_list(self, ctx:ZCodeParser.Decl_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#nl_type.
    def enterNl_type(self, ctx:ZCodeParser.Nl_typeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#nl_type.
    def exitNl_type(self, ctx:ZCodeParser.Nl_typeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#nl_nullable_list.
    def enterNl_nullable_list(self, ctx:ZCodeParser.Nl_nullable_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#nl_nullable_list.
    def exitNl_nullable_list(self, ctx:ZCodeParser.Nl_nullable_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#nl_list.
    def enterNl_list(self, ctx:ZCodeParser.Nl_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#nl_list.
    def exitNl_list(self, ctx:ZCodeParser.Nl_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#declaration.
    def enterDeclaration(self, ctx:ZCodeParser.DeclarationContext):
        pass

    # Exit a parse tree produced by ZCodeParser#declaration.
    def exitDeclaration(self, ctx:ZCodeParser.DeclarationContext):
        pass


    # Enter a parse tree produced by ZCodeParser#variable_stat.
    def enterVariable_stat(self, ctx:ZCodeParser.Variable_statContext):
        pass

    # Exit a parse tree produced by ZCodeParser#variable_stat.
    def exitVariable_stat(self, ctx:ZCodeParser.Variable_statContext):
        pass


    # Enter a parse tree produced by ZCodeParser#dtype.
    def enterDtype(self, ctx:ZCodeParser.DtypeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#dtype.
    def exitDtype(self, ctx:ZCodeParser.DtypeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#explicit_declare.
    def enterExplicit_declare(self, ctx:ZCodeParser.Explicit_declareContext):
        pass

    # Exit a parse tree produced by ZCodeParser#explicit_declare.
    def exitExplicit_declare(self, ctx:ZCodeParser.Explicit_declareContext):
        pass


    # Enter a parse tree produced by ZCodeParser#primitive_declare.
    def enterPrimitive_declare(self, ctx:ZCodeParser.Primitive_declareContext):
        pass

    # Exit a parse tree produced by ZCodeParser#primitive_declare.
    def exitPrimitive_declare(self, ctx:ZCodeParser.Primitive_declareContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_declare.
    def enterArray_declare(self, ctx:ZCodeParser.Array_declareContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_declare.
    def exitArray_declare(self, ctx:ZCodeParser.Array_declareContext):
        pass


    # Enter a parse tree produced by ZCodeParser#numlit_list.
    def enterNumlit_list(self, ctx:ZCodeParser.Numlit_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#numlit_list.
    def exitNumlit_list(self, ctx:ZCodeParser.Numlit_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#numlit_tail.
    def enterNumlit_tail(self, ctx:ZCodeParser.Numlit_tailContext):
        pass

    # Exit a parse tree produced by ZCodeParser#numlit_tail.
    def exitNumlit_tail(self, ctx:ZCodeParser.Numlit_tailContext):
        pass


    # Enter a parse tree produced by ZCodeParser#implicit_declare.
    def enterImplicit_declare(self, ctx:ZCodeParser.Implicit_declareContext):
        pass

    # Exit a parse tree produced by ZCodeParser#implicit_declare.
    def exitImplicit_declare(self, ctx:ZCodeParser.Implicit_declareContext):
        pass


    # Enter a parse tree produced by ZCodeParser#function_stat.
    def enterFunction_stat(self, ctx:ZCodeParser.Function_statContext):
        pass

    # Exit a parse tree produced by ZCodeParser#function_stat.
    def exitFunction_stat(self, ctx:ZCodeParser.Function_statContext):
        pass


    # Enter a parse tree produced by ZCodeParser#function_definition.
    def enterFunction_definition(self, ctx:ZCodeParser.Function_definitionContext):
        pass

    # Exit a parse tree produced by ZCodeParser#function_definition.
    def exitFunction_definition(self, ctx:ZCodeParser.Function_definitionContext):
        pass


    # Enter a parse tree produced by ZCodeParser#function_declaration.
    def enterFunction_declaration(self, ctx:ZCodeParser.Function_declarationContext):
        pass

    # Exit a parse tree produced by ZCodeParser#function_declaration.
    def exitFunction_declaration(self, ctx:ZCodeParser.Function_declarationContext):
        pass


    # Enter a parse tree produced by ZCodeParser#param_list.
    def enterParam_list(self, ctx:ZCodeParser.Param_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#param_list.
    def exitParam_list(self, ctx:ZCodeParser.Param_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#param_list_tail.
    def enterParam_list_tail(self, ctx:ZCodeParser.Param_list_tailContext):
        pass

    # Exit a parse tree produced by ZCodeParser#param_list_tail.
    def exitParam_list_tail(self, ctx:ZCodeParser.Param_list_tailContext):
        pass


    # Enter a parse tree produced by ZCodeParser#parameter.
    def enterParameter(self, ctx:ZCodeParser.ParameterContext):
        pass

    # Exit a parse tree produced by ZCodeParser#parameter.
    def exitParameter(self, ctx:ZCodeParser.ParameterContext):
        pass


    # Enter a parse tree produced by ZCodeParser#statement.
    def enterStatement(self, ctx:ZCodeParser.StatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#statement.
    def exitStatement(self, ctx:ZCodeParser.StatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#statement_list.
    def enterStatement_list(self, ctx:ZCodeParser.Statement_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#statement_list.
    def exitStatement_list(self, ctx:ZCodeParser.Statement_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#return_stat.
    def enterReturn_stat(self, ctx:ZCodeParser.Return_statContext):
        pass

    # Exit a parse tree produced by ZCodeParser#return_stat.
    def exitReturn_stat(self, ctx:ZCodeParser.Return_statContext):
        pass


    # Enter a parse tree produced by ZCodeParser#break_stat.
    def enterBreak_stat(self, ctx:ZCodeParser.Break_statContext):
        pass

    # Exit a parse tree produced by ZCodeParser#break_stat.
    def exitBreak_stat(self, ctx:ZCodeParser.Break_statContext):
        pass


    # Enter a parse tree produced by ZCodeParser#continue_stat.
    def enterContinue_stat(self, ctx:ZCodeParser.Continue_statContext):
        pass

    # Exit a parse tree produced by ZCodeParser#continue_stat.
    def exitContinue_stat(self, ctx:ZCodeParser.Continue_statContext):
        pass


    # Enter a parse tree produced by ZCodeParser#block_stat.
    def enterBlock_stat(self, ctx:ZCodeParser.Block_statContext):
        pass

    # Exit a parse tree produced by ZCodeParser#block_stat.
    def exitBlock_stat(self, ctx:ZCodeParser.Block_statContext):
        pass


    # Enter a parse tree produced by ZCodeParser#comment.
    def enterComment(self, ctx:ZCodeParser.CommentContext):
        pass

    # Exit a parse tree produced by ZCodeParser#comment.
    def exitComment(self, ctx:ZCodeParser.CommentContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expression.
    def enterExpression(self, ctx:ZCodeParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expression.
    def exitExpression(self, ctx:ZCodeParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ZCodeParser#relation_operation.
    def enterRelation_operation(self, ctx:ZCodeParser.Relation_operationContext):
        pass

    # Exit a parse tree produced by ZCodeParser#relation_operation.
    def exitRelation_operation(self, ctx:ZCodeParser.Relation_operationContext):
        pass


    # Enter a parse tree produced by ZCodeParser#relational_expr.
    def enterRelational_expr(self, ctx:ZCodeParser.Relational_exprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#relational_expr.
    def exitRelational_expr(self, ctx:ZCodeParser.Relational_exprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#logical_expr.
    def enterLogical_expr(self, ctx:ZCodeParser.Logical_exprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#logical_expr.
    def exitLogical_expr(self, ctx:ZCodeParser.Logical_exprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#adding_expr.
    def enterAdding_expr(self, ctx:ZCodeParser.Adding_exprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#adding_expr.
    def exitAdding_expr(self, ctx:ZCodeParser.Adding_exprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#multiplying_expr.
    def enterMultiplying_expr(self, ctx:ZCodeParser.Multiplying_exprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#multiplying_expr.
    def exitMultiplying_expr(self, ctx:ZCodeParser.Multiplying_exprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#not_logical.
    def enterNot_logical(self, ctx:ZCodeParser.Not_logicalContext):
        pass

    # Exit a parse tree produced by ZCodeParser#not_logical.
    def exitNot_logical(self, ctx:ZCodeParser.Not_logicalContext):
        pass


    # Enter a parse tree produced by ZCodeParser#sign_expr.
    def enterSign_expr(self, ctx:ZCodeParser.Sign_exprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#sign_expr.
    def exitSign_expr(self, ctx:ZCodeParser.Sign_exprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#index_expr.
    def enterIndex_expr(self, ctx:ZCodeParser.Index_exprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#index_expr.
    def exitIndex_expr(self, ctx:ZCodeParser.Index_exprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#parenthesis_expr.
    def enterParenthesis_expr(self, ctx:ZCodeParser.Parenthesis_exprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#parenthesis_expr.
    def exitParenthesis_expr(self, ctx:ZCodeParser.Parenthesis_exprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#term.
    def enterTerm(self, ctx:ZCodeParser.TermContext):
        pass

    # Exit a parse tree produced by ZCodeParser#term.
    def exitTerm(self, ctx:ZCodeParser.TermContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_expr.
    def enterArray_expr(self, ctx:ZCodeParser.Array_exprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_expr.
    def exitArray_expr(self, ctx:ZCodeParser.Array_exprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#function_expr.
    def enterFunction_expr(self, ctx:ZCodeParser.Function_exprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#function_expr.
    def exitFunction_expr(self, ctx:ZCodeParser.Function_exprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expression_list.
    def enterExpression_list(self, ctx:ZCodeParser.Expression_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expression_list.
    def exitExpression_list(self, ctx:ZCodeParser.Expression_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expression_list_tail.
    def enterExpression_list_tail(self, ctx:ZCodeParser.Expression_list_tailContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expression_list_tail.
    def exitExpression_list_tail(self, ctx:ZCodeParser.Expression_list_tailContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expression_nonempty_list.
    def enterExpression_nonempty_list(self, ctx:ZCodeParser.Expression_nonempty_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expression_nonempty_list.
    def exitExpression_nonempty_list(self, ctx:ZCodeParser.Expression_nonempty_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expression_nonempty_tail.
    def enterExpression_nonempty_tail(self, ctx:ZCodeParser.Expression_nonempty_tailContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expression_nonempty_tail.
    def exitExpression_nonempty_tail(self, ctx:ZCodeParser.Expression_nonempty_tailContext):
        pass


    # Enter a parse tree produced by ZCodeParser#control_stat.
    def enterControl_stat(self, ctx:ZCodeParser.Control_statContext):
        pass

    # Exit a parse tree produced by ZCodeParser#control_stat.
    def exitControl_stat(self, ctx:ZCodeParser.Control_statContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elif_stmt_list.
    def enterElif_stmt_list(self, ctx:ZCodeParser.Elif_stmt_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elif_stmt_list.
    def exitElif_stmt_list(self, ctx:ZCodeParser.Elif_stmt_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#ifst_component.
    def enterIfst_component(self, ctx:ZCodeParser.Ifst_componentContext):
        pass

    # Exit a parse tree produced by ZCodeParser#ifst_component.
    def exitIfst_component(self, ctx:ZCodeParser.Ifst_componentContext):
        pass


    # Enter a parse tree produced by ZCodeParser#loop_stat.
    def enterLoop_stat(self, ctx:ZCodeParser.Loop_statContext):
        pass

    # Exit a parse tree produced by ZCodeParser#loop_stat.
    def exitLoop_stat(self, ctx:ZCodeParser.Loop_statContext):
        pass


    # Enter a parse tree produced by ZCodeParser#assignment.
    def enterAssignment(self, ctx:ZCodeParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ZCodeParser#assignment.
    def exitAssignment(self, ctx:ZCodeParser.AssignmentContext):
        pass



del ZCodeParser