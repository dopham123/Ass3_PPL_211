from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *
from functools import *

class ASTGeneration(BKOOLVisitor):

    def visitProgram(self,ctx:BKOOLParser.ProgramContext):
        return Program(self.visit(ctx.list_class_dec()))

    def visitList_class_dec(self, ctx:BKOOLParser.List_class_decContext):
        if ctx.list_class_dec():
            return [self.visit(ctx.class_dec())] + self.visit(ctx.list_class_dec())
        else:
            return [self.visit(ctx.class_dec())]

    #Start : Type : ==================================================================================
    def visitMptype(self, ctx:BKOOLParser.MptypeContext):
        if ctx.primitive_type():
            return self.visit(ctx.primitive_type())
        else:
            return self.visit(ctx.array_type())

    def visitCommon_type(self, ctx:BKOOLParser.Common_typeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        else:
            return StringType()

    def visitPrimitive_type(self, ctx:BKOOLParser.Primitive_typeContext):
        if ctx.common_type():
            return self.visit(ctx.common_type())
        else:
            return VoidType()

    def visitArray_type(self, ctx:BKOOLParser.Array_typeContext):
        return ArrayType(int(ctx.INT_LIT().getText()), self.visit(ctx.common_type()))
    #End : ^^^ : Type : ##################################################################################

    def visitClass_dec(self,ctx:BKOOLParser.Class_decContext):
        if not ctx.EXTENDS():
            return ClassDecl(Id(ctx.ID(0).getText()),self.visit(ctx.list_member()), None)
        else:
            return ClassDecl(Id(ctx.ID(0).getText()), self.visit(ctx.list_member()), Id(ctx.ID(1).getText()))

    def visitList_member(self, ctx:BKOOLParser.List_memberContext):
        return self.visit(ctx.list_attrib_dec()) + self.visit(ctx.list_method_dec())

    def visitList_attrib_dec(self, ctx:BKOOLParser.List_attrib_decContext):
        if ctx.attrib_dec():
            return self.visit(ctx.attrib_dec()) + self.visit(ctx.list_attrib_dec())
        else:
            return []

    def visitList_method_dec(self, ctx:BKOOLParser.List_method_decContext):
        if ctx.method_dec():
            return [self.visit(ctx.method_dec())] + self.visit(ctx.list_method_dec())
        else:
            return []

    #Start: Attribute_decl: ===========================================================================
    def visitAttrib_dec(self,ctx:BKOOLParser.Attrib_decContext):
        if ctx.STATIC():
            return [AttributeDecl(Static(), x) for x in self.visit(ctx.decl_var())]
        else:
            return [AttributeDecl(Instance(), x) for x in self.visit(ctx.decl_var())]

    def visitDecl_var(self, ctx:BKOOLParser.Decl_varContext):
        if ctx.FINAL():
            return [ConstDecl(x[0], self.visit(ctx.mptype()), x[1]) for x in self.visit(ctx.list_attrib_const())]
        else:
            return [VarDecl(x[0], self.visit(ctx.mptype()), x[1]) for x in self.visit(ctx.list_attrib_var())]

    #Start: ConstDecl: ============================================================================
    def visitList_attrib_const(self, ctx:BKOOLParser.List_attrib_constContext):
        if ctx.list_attrib_const():
            return [self.visit(ctx.attrib_const())] + self.visit(ctx.list_attrib_const())
        else:
            return [self.visit(ctx.attrib_const())]

    def visitAttrib_const(self, ctx:BKOOLParser.Attrib_constContext):
        return [Id(ctx.ID().getText()), self.visit(ctx.exp()) if ctx.exp() else None]
    #End: ^^^ : ConstDecl: ######################################################################

    #Start: VarDecl: ==============================================================================
    def visitList_attrib_var(self, ctx:BKOOLParser.List_attrib_varContext):
        if ctx.list_attrib_var():
            return [self.visit(ctx.attrib_var())] + self.visit(ctx.list_attrib_var())
        else:
            return [self.visit(ctx.attrib_var())]

    def visitAttrib_var(self, ctx:BKOOLParser.Attrib_varContext):
        if ctx.exp():
            return [Id(ctx.ID().getText()), self.visit(ctx.exp())]
        else:
            return [Id(ctx.ID().getText()), None]
    #End: ^^^ : VarDecl: ######################################################################

    # End: ^^^ : Attribute_decl: ######################################################################

    #Start: Method_decl: ===============================================================================
    def visitMethod_dec(self, ctx:BKOOLParser.Method_decContext):
        if ctx.STATIC():
            return MethodDecl(Static(), Id(ctx.ID().getText()), self.visit(ctx.list_para()) if ctx.list_para() else [], self.visit(ctx.mptype()), self.visit(ctx.block_state()))
        else:
            return MethodDecl(Instance(), Id(ctx.ID().getText()), self.visit(ctx.list_para()) if ctx.list_para() else [],
                              self.visit(ctx.mptype()) if ctx.mptype() else None, self.visit(ctx.block_state()))

    def visitList_para(self, ctx:BKOOLParser.List_paraContext):
        return self.visit(ctx.para_dec()) + (self.visit(ctx.list_para()) if ctx.list_para() else [])

    def visitPara_dec(self, ctx:BKOOLParser.Para_decContext):
        return [VarDecl(x, self.visit(ctx.mptype()), None) for x in self.visit(ctx.list_id())]

    def visitList_id(self, ctx:BKOOLParser.List_idContext):
        return [Id(ctx.ID().getText())] + (self.visit(ctx.list_id()) if ctx.list_id() else [])
    #End: ^^^ : Method_decl : ##############################################################################

    # def visitBkooltype(self,ctx:BKOOLParser.BkooltypeContext):
    #     return IntType() if ctx.INTTYPE() else VoidType()

    #Start : Expression : ===================================================================================
    def visitExp(self, ctx:BKOOLParser.ExpContext):
        if ctx.LTHAN():
            return BinaryOp(ctx.LTHAN().getText(), self.visit(ctx.exp1(0)), self.visit(ctx.exp1(1)))
        elif ctx.GTHAN():
            return BinaryOp(ctx.GTHAN().getText(), self.visit(ctx.exp1(0)), self.visit(ctx.exp1(1)))
        elif ctx.LEQUAL():
            return BinaryOp(ctx.LEQUAL().getText(), self.visit(ctx.exp1(0)), self.visit(ctx.exp1(1)))
        elif ctx.GEQUAL():
            return BinaryOp(ctx.GEQUAL().getText(), self.visit(ctx.exp1(0)), self.visit(ctx.exp1(1)))
        else:
            return self.visit(ctx.exp1(0))

    def visitExp1(self, ctx:BKOOLParser.Exp1Context):
        if ctx.EQUAL():
            return BinaryOp(ctx.EQUAL().getText(), self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        elif ctx.NOT_EQUAL():
            return BinaryOp(ctx.NOT_EQUAL().getText(), self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        else:
            return self.visit(ctx.exp2(0))

    def visitExp2(self, ctx:BKOOLParser.Exp2Context):
        if ctx.AND():
            return BinaryOp(ctx.AND().getText(), self.visit(ctx.exp2()), self.visit(ctx.exp3()))
        elif ctx.OR():
            return BinaryOp(ctx.OR().getText(), self.visit(ctx.exp2()), self.visit(ctx.exp3()))
        else:
            return self.visit(ctx.exp3())

    def visitExp3(self, ctx:BKOOLParser.Exp3Context):
        if ctx.ADD():
            return BinaryOp(ctx.ADD().getText(), self.visit(ctx.exp3()), self.visit(ctx.exp4()))
        elif ctx.SUB():
            return BinaryOp(ctx.SUB().getText(), self.visit(ctx.exp3()), self.visit(ctx.exp4()))
        else:
            return self.visit(ctx.exp4())

    def visitExp4(self, ctx:BKOOLParser.Exp4Context):
        if ctx.MUL():
            return BinaryOp(ctx.MUL().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        elif ctx.FDIV():
            return BinaryOp(ctx.FDIV().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        elif ctx.IDIV():
            return BinaryOp(ctx.IDIV().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        elif ctx.MOD():
            return BinaryOp(ctx.MOD().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        else:
            return self.visit(ctx.exp5())

    def visitExp5(self, ctx:BKOOLParser.Exp5Context):
        if ctx.CONCATE():
            return BinaryOp(ctx.CONCATE().getText(), self.visit(ctx.exp5()), self.visit(ctx.exp6()))
        else:
            return self.visit(ctx.exp6())

    def visitExp6(self, ctx:BKOOLParser.Exp6Context):
        if ctx.NOT():
            return UnaryOp(ctx.NOT().getText(), self.visit(ctx.exp6()))
        else:
            return self.visit(ctx.exp7())

    def visitExp7(self, ctx:BKOOLParser.Exp7Context):
        if ctx.SUB():
            return UnaryOp(ctx.SUB().getText(), self.visit(ctx.exp7()))
        elif ctx.ADD():
            return UnaryOp(ctx.ADD().getText(), self.visit(ctx.exp7()))
        else:
            return self.visit(ctx.exp8())

    def visitExp8(self, ctx:BKOOLParser.Exp8Context):
        if ctx.exp8():
            return ArrayCell(self.visit(ctx.exp8()), self.visit(ctx.exp()))
        else:
            return self.visit(ctx.exp9())

    def visitExp9(self, ctx:BKOOLParser.Exp9Context):
        if ctx.DOT():
            if ctx.list_arg():
                return CallExpr(self.visit(ctx.exp9()), Id(ctx.ID().getText()), self.visit(ctx.list_arg()))
            else:
                return FieldAccess(self.visit(ctx.exp9()), Id(ctx.ID().getText()))
        else:
            return self.visit(ctx.exp10())

    def visitExp10(self, ctx:BKOOLParser.Exp10Context):
        return NewExpr(Id(ctx.ID().getText()), self.visit(ctx.list_arg())) if ctx.NEW() else self.visit(ctx.exp11())

    def visitExp11(self, ctx:BKOOLParser.Exp11Context):
        if ctx.exp():
            return self.visit(ctx.exp())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.literals():
            return self.visit(ctx.literals())
        else:
            return ctx.THIS().getText()

    #Start: Literals : ==================================================================================
    def visitLiterals(self, ctx:BKOOLParser.LiteralsContext):
        if ctx.INT_LIT():
            return IntLiteral(int(ctx.INT_LIT().getText()))
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.BOOL_LIT():
            if str(ctx.BOOL_LIT().getText())[0] == "t":
                return BooleanLiteral(True)
            else:
                return BooleanLiteral(False)
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        else:
            return self.visit(ctx.array_lit())

    def visitArray_lit(self, ctx:BKOOLParser.Array_litContext):
        return ArrayLiteral(self.visit(ctx.list_lit()))

    def visitList_lit(self, ctx:BKOOLParser.List_litContext):
        if ctx.list_int():
            return self.visit(ctx.list_int())
        elif ctx.list_float():
            return self.visit(ctx.list_float())
        elif ctx.list_bool():
            return self.visit(ctx.list_bool())
        else:
            return self.visit(ctx.list_string())

    def visitList_int(self, ctx:BKOOLParser.List_intContext):
        return [ctx.INT_LIT().getText()] + (self.visit(ctx.list_int()) if ctx.list_int() else [])

    def visitList_float(self, ctx:BKOOLParser.List_floatContext):
        return [ctx.FLOAT_LIT().getText()] + (self.visit(ctx.list_float()) if ctx.list_float() else [])

    def visitList_bool(self, ctx:BKOOLParser.List_boolContext):
        return [ctx.BOOL_LIT().getText()] + (self.visit(ctx.list_bool()) if ctx.list_bool() else [])

    def visitList_string(self, ctx:BKOOLParser.List_stringContext):
        return [ctx.STRING_LIT().getText()] + (self.visit(ctx.list_string()) if ctx.list_string() else [])
    #End : ^^^ : Literals : ##################################################################################

    def visitList_arg(self, ctx:BKOOLParser.List_argContext):
        return self.visit(ctx.listexp()) if ctx.listexp() else []

    def visitListexp(self, ctx:BKOOLParser.ListexpContext):
        return [self.visit(ctx.exp())] + (self.visit(ctx.listexp()) if ctx.listexp() else [])
    #End : ^^^ : Expression : ##################################################################################

    #Start : Statement : =======================================================================================
    def visitAll_state(self, ctx:BKOOLParser.All_stateContext):
        if ctx.assign_state():
            return self.visit(ctx.assign_state())
        elif ctx.if_state():
            return self.visit(ctx.if_state())
        elif ctx.for_state():
            return self.visit(ctx.for_state())
        elif ctx.break_state():
            return self.visit(ctx.break_state())
        elif ctx.continue_state():
            return self.visit(ctx.continue_state())
        elif ctx.return_state():
            return self.visit(ctx.return_state())
        else:
            return self.visit(ctx.invocation_state())

    def visitList_state(self, ctx:BKOOLParser.List_stateContext):
        return ([self.visit(ctx.all_state())] + self.visit(ctx.list_state())) if ctx.list_state() else []

    def visitList_decl_var(self, ctx:BKOOLParser.List_decl_varContext):
        return (self.visit(ctx.decl_var()) + self.visit(ctx.list_decl_var())) if ctx.list_decl_var() else []

    def visitBlock_state(self, ctx:BKOOLParser.Block_stateContext):
        return Block(self.visit(ctx.list_decl_var()), self.visit(ctx.list_state()))

    def visitExp_state(self, ctx: BKOOLParser.Exp_stateContext):
        return self.visit(ctx.all_state()) if ctx.all_state() else self.visit(ctx.block_state())

    def visitAssign_state(self, ctx:BKOOLParser.Assign_stateContext):
        return Assign(self.visit(ctx.exp(0)), self.visit(ctx.exp(1)))

    def visitIf_state(self, ctx:BKOOLParser.If_stateContext):
        if not ctx.ELSE():
            return If(self.visit(ctx.exp()), self.visit(ctx.exp_state(0)), None)
        else:
            return If(self.visit(ctx.exp()), self.visit(ctx.exp_state(0)), self.visit(ctx.exp_state(1)))

    def visitFor_state(self, ctx:BKOOLParser.For_stateContext):
        if ctx.TO():
            return For(Id(ctx.ID().getText()), self.visit(ctx.exp(0)), self.visit(ctx.exp(1)), True,
                       self.visit(ctx.exp_state()))
        else:
            return For(Id(ctx.ID().getText()), self.visit(ctx.exp(0)), self.visit(ctx.exp(1)), False,
                       self.visit(ctx.exp_state()))

    def visitBreak_state(self, ctx:BKOOLParser.Break_stateContext):
        return Break()

    def visitContinue_state(self, ctx:BKOOLParser.Continue_stateContext):
        return Continue()

    def visitReturn_state(self, ctx:BKOOLParser.Return_stateContext):
        return Return(self.visit(ctx.exp()))

    def visitInvocation_state(self, ctx:BKOOLParser.Invocation_stateContext):
        return CallExpr(self.visit(ctx.exp()), Id(ctx.ID().getText()), self.visit(ctx.list_arg()))