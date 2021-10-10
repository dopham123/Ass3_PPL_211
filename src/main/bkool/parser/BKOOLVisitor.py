# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_class_dec.
    def visitList_class_dec(self, ctx:BKOOLParser.List_class_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mptype.
    def visitMptype(self, ctx:BKOOLParser.MptypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_dec.
    def visitClass_dec(self, ctx:BKOOLParser.Class_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_member.
    def visitList_member(self, ctx:BKOOLParser.List_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_attrib_dec.
    def visitList_attrib_dec(self, ctx:BKOOLParser.List_attrib_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_method_dec.
    def visitList_method_dec(self, ctx:BKOOLParser.List_method_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#decl_var.
    def visitDecl_var(self, ctx:BKOOLParser.Decl_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attrib_dec.
    def visitAttrib_dec(self, ctx:BKOOLParser.Attrib_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_attrib_const.
    def visitList_attrib_const(self, ctx:BKOOLParser.List_attrib_constContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_attrib_var.
    def visitList_attrib_var(self, ctx:BKOOLParser.List_attrib_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attrib_const.
    def visitAttrib_const(self, ctx:BKOOLParser.Attrib_constContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attrib_var.
    def visitAttrib_var(self, ctx:BKOOLParser.Attrib_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_dec.
    def visitMethod_dec(self, ctx:BKOOLParser.Method_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_para.
    def visitList_para(self, ctx:BKOOLParser.List_paraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#para_dec.
    def visitPara_dec(self, ctx:BKOOLParser.Para_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_id.
    def visitList_id(self, ctx:BKOOLParser.List_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_lit.
    def visitArray_lit(self, ctx:BKOOLParser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_lit.
    def visitList_lit(self, ctx:BKOOLParser.List_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_int.
    def visitList_int(self, ctx:BKOOLParser.List_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_float.
    def visitList_float(self, ctx:BKOOLParser.List_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_bool.
    def visitList_bool(self, ctx:BKOOLParser.List_boolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_string.
    def visitList_string(self, ctx:BKOOLParser.List_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#common_type.
    def visitCommon_type(self, ctx:BKOOLParser.Common_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#primitive_type.
    def visitPrimitive_type(self, ctx:BKOOLParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_type.
    def visitArray_type(self, ctx:BKOOLParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp.
    def visitExp(self, ctx:BKOOLParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp1.
    def visitExp1(self, ctx:BKOOLParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp2.
    def visitExp2(self, ctx:BKOOLParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp3.
    def visitExp3(self, ctx:BKOOLParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp4.
    def visitExp4(self, ctx:BKOOLParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp5.
    def visitExp5(self, ctx:BKOOLParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp6.
    def visitExp6(self, ctx:BKOOLParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp7.
    def visitExp7(self, ctx:BKOOLParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp8.
    def visitExp8(self, ctx:BKOOLParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp9.
    def visitExp9(self, ctx:BKOOLParser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp10.
    def visitExp10(self, ctx:BKOOLParser.Exp10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp11.
    def visitExp11(self, ctx:BKOOLParser.Exp11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#literals.
    def visitLiterals(self, ctx:BKOOLParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_arg.
    def visitList_arg(self, ctx:BKOOLParser.List_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#listexp.
    def visitListexp(self, ctx:BKOOLParser.ListexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#all_state.
    def visitAll_state(self, ctx:BKOOLParser.All_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_state.
    def visitList_state(self, ctx:BKOOLParser.List_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_decl_var.
    def visitList_decl_var(self, ctx:BKOOLParser.List_decl_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#block_state.
    def visitBlock_state(self, ctx:BKOOLParser.Block_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp_state.
    def visitExp_state(self, ctx:BKOOLParser.Exp_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assign_state.
    def visitAssign_state(self, ctx:BKOOLParser.Assign_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#if_state.
    def visitIf_state(self, ctx:BKOOLParser.If_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#for_state.
    def visitFor_state(self, ctx:BKOOLParser.For_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#break_state.
    def visitBreak_state(self, ctx:BKOOLParser.Break_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#continue_state.
    def visitContinue_state(self, ctx:BKOOLParser.Continue_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#return_state.
    def visitReturn_state(self, ctx:BKOOLParser.Return_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#invocation_state.
    def visitInvocation_state(self, ctx:BKOOLParser.Invocation_stateContext):
        return self.visitChildren(ctx)



del BKOOLParser