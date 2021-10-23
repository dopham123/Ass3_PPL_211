
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
import copy

from main.bkool.utils.AST import BoolType, FloatType, IntType, MethodDecl, StringType, VarDecl

class Type(ABC):
    __metaclass__ = ABCMeta
    pass
class Prim(Type):
    __metaclass__ = ABCMeta
    pass
class ClassTyp(Type):
    def __init__(self, classname, parrentname = None):
        self.classname = classname
        self.parrentname = parrentname

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype #list param type: []
        self.rettype = rettype #kiểu trả về của method

@dataclass
class ArrayType(Type):
    dimen: int #số lượng phần tử trong mảng
    eletype: Type #kiểu của mỗi phần tử

class Symbol:
    def __init__(self, name, mtype, value = None):
        self.name = name
        self.mtype = mtype
        self.value = value #dict if class

class StaticChecker(BaseVisitor,Utils):

    global_envi = [
        Symbol("io", ClassType("io"), {
            "global_sc_child": [
                Symbol("readInt",MType([],IntType())),
                Symbol("writeInt",MType([IntType()],VoidType())),
                Symbol("writeIntLn",MType([IntType()],VoidType())),
                Symbol("readFloat",MType([],FloatType())),
                Symbol("writeFloat",MType([FloatType()],VoidType())),
                Symbol("writeFloatLn",MType([FloatType()],VoidType())),
                Symbol("readBool",MType([],BoolType())),
                Symbol("writeBool",MType([BoolType()],VoidType())),
                Symbol("writeBoolLn",MType([BoolType()],VoidType())),
                Symbol("readStr",MType([],StringType())),
                Symbol("writeStr",MType([StringType()],VoidType())),
                Symbol("writeStrLn",MType([StringType()],VoidType()))
            ],
            "class_sc_child": []
        })    
    ]
            
    
    def __init__(self,ast):
        self.ast = ast

    def visit(self,ast,param):
        return ast.accept(self,param)
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, c): 
        obj = [[]] + [c]
        #lưu tên của class first
        for x in ast.decl:
            if x.classname.name not in c:
                c.append(Symbol(x.classname.name, ClassTyp(x.classname.name, None), {
                    "global_sc_child": [],
                    "class_sc_child": []
                }))
            else:
                raise Redeclared(Class(), x.classname.name)
        
        #lưu tên memdecl vào <symbol>.value nếu là super class
        for x in ast.decl:
            if not x.parentname:
                for z in c:
                    if z.name==x.classname.name: #tìm class trong env ứng với x
                        for y in x.memlist: #y: MethodDecl or AttributeDecl
                            #kiểm tra nếu là MethodDecl
                            if isinstance(y, MethodDecl):
                                if y.name in [child.name for child in z.value.get("global_sc_child")]:
                                    raise Redeclared(Method(), y.name)
                                else:
                                    z.value.get("global_sc_child").append(Symbol(y.name, MType(self.returnParamType(y.param), y.returnType)))
                            #Ngược lại là AttributeDecl
                            else:
                                #Static
                                if isinstance(y.kind, Static): #y.kind: SIKind(Static or Instance)
                                    if isinstance(y.decl, ConstDecl): #y.decl: StoreDecl(ConstDecl or VarDecl)
                                        #kiểm tra khai báo trùng id
                                        if y.decl.constant.name in [child.name for child in z.value.get("global_sc_child")]:
                                            raise Redeclared(Method(), y.name)
                                        else:
                                            #kiểm tra kiểu của khai báo const
                                            if y.decl.constType == self.visit(y.decl.value, c): #check type constdecl
                                                z.value.get("global_sc_child").append(Symbol(y.decl.constant.name, y.decl.constType, y.decl.constType))
                                            else:
                                                raise TypeMismatchInConstant(y)
                                    #không phải ConstDecl thì là VarDecl
                                    else:
                                        #kiểm tra khai báo trùng id
                                        if y.decl.variable.name in [child.name for child in z.value.get("global_sc_child")]:
                                            raise Redeclared(Method(), y.name)
                                        else:
                                            if y.decl.varInit:
                                                self.visit(y.decl.varInit, c)
                                            z.value.get("global_sc_child").append(Symbol(y.decl.variable.name, y.decl.varType))
                                #Instance
                                else:
                                    if isinstance(y.decl, ConstDecl): #y.decl: StoreDecl(ConstDecl or VarDecl)
                                        #kiểm tra khai báo trùng id
                                        if y.decl.constant.name in [child.name for child in z.value.get("class_sc_child")]:
                                            raise Redeclared(Method(), y.name)
                                        else:
                                            #kiểm tra kiểu của khai báo const
                                            print(type(y.decl.constType))
                                            print('==================')
                                            print(isinstance(type(y.decl.constType), type(self.visit(y.decl.value, c))))
                                            print(type(self.visit(y.decl.value, c)))
                                            if y.decl.constType == self.visit(y.decl.value, c): #check type constdecl
                                                z.value.get("class_sc_child").append(Symbol(y.decl.constant.name, y.decl.constType, y.decl.constType))
                                            else:
                                                raise TypeMismatchInConstant(y)
                                    #không phải ConstDecl thì là VarDecl
                                    else:
                                        #kiểm tra khai báo trùng id
                                        if y.decl.variable.name in [child.name for child in z.value.get("class_sc_child")]:
                                            raise Redeclared(Method(), y.decl.variable.name)
                                        else:
                                            if y.decl.varInit:
                                                self.visit(y.decl.varInit, c)
                                            z.value.get("class_sc_child").append(Symbol(y.decl.variable.name, y.decl.varType))
                        break

        #cập nhật môi trường cho subclass
        for x in ast.decl:
            if x.parentname:
                for z in c:
                    if z.name==x.classname.name: #tìm class trong env ứng với x
                        for k in c: # tìm class trong env ứng với class cha của x
                            if x.parentname.name == k.name:
                                z.value = copy.deepcopy() #copy con của class cha và gắn vào class con
                        for y in x.memlist: #y: MethodDecl or AttributeDecl
                            #kiểm tra nếu là MethodDecl
                            if isinstance(y, MethodDecl):
                                if y.name in [child.name for child in z.value.get("global_sc_child")]:
                                    raise Redeclared(Method(), y.name)
                                else:
                                    z.value.get("global_sc_child").append(Symbol(y.name, MType(self.returnParamType(y.param), y.returnType)))
                            #Ngược lại là AttributeDecl
                            else:
                                #Static
                                if isinstance(y.kind, Static): #y.kind: SIKind(Static or Instance)
                                    if isinstance(y.decl, ConstDecl): #y.decl: StoreDecl(ConstDecl or VarDecl)
                                        #kiểm tra khai báo trùng id
                                        if y.decl.constant.name in [child.name for child in z.value.get("global_sc_child")]:
                                            raise Redeclared(Method(), y.name)
                                        else:
                                            #kiểm tra kiểu của khai báo const
                                            if y.decl.constType == self.visit(y.decl.value, c): #check type constdecl
                                                z.value.get("global_sc_child").append(Symbol(y.decl.constant.name, y.decl.constType, y.decl.constType))
                                            else:
                                                raise TypeMismatchInConstant(y)
                                    #không phải ConstDecl thì là VarDecl
                                    else:
                                        #kiểm tra khai báo trùng id
                                        if y.decl.variable.name in [child.name for child in z.value.get("global_sc_child")]:
                                            raise Redeclared(Method(), y.name)
                                        else:
                                            if y.decl.varInit:
                                                self.visit(y.decl.varInit, c)
                                            z.value.get("global_sc_child").append(Symbol(y.decl.variable.name, y.decl.varType))
                                #Instance
                                else:
                                    if isinstance(y.decl, ConstDecl): #y.decl: StoreDecl(ConstDecl or VarDecl)
                                        #kiểm tra khai báo trùng id
                                        if y.decl.constant.name in [child.name for child in z.value.get("class_sc_child")]:
                                            raise Redeclared(Method(), y.name)
                                        else:
                                            #kiểm tra kiểu của khai báo const
                                            if y.decl.constType == self.visit(y.decl.value, c): #check type constdecl
                                                z.value.get("class_sc_child").append(Symbol(y.decl.constant.name, y.decl.constType, y.decl.constType))
                                            else:
                                                raise TypeMismatchInConstant(y)
                                    #không phải ConstDecl thì là VarDecl
                                    else:
                                        #kiểm tra khai báo trùng id
                                        if y.decl.variable.name in [child.name for child in z.value.get("class_sc_child")]:
                                            raise Redeclared(Method(), y.name)
                                        else:
                                            if y.decl.varInit:
                                                self.visit(y.decl.varInit, c)
                                            z.value.get("class_sc_child").append(Symbol(y.decl.variable.name, y.decl.varType))
                        break

        return [self.visit(x,c) for x in ast.decl]

    def returnParamType(param): #param: list[VarDecl]
        [x.varType for x in param]

    def visitClassDecl(self, ast, c):
        # classname : Id
        # memlist : List[MemDecl]
        # parentname : Id = None # None if there is no parent
        for x in ast.memlist:
            if type(x) is MethodDecl:
                obj = [[]] + [c]
                self.visit(x, obj)

    def visitMethodDecl(self, ast, o):
        # kind: SIKind
        # name: Id
        # param: List[VarDecl]
        # returnType: Type  # None for constructor
        # body: Block
        for x in ast.param:
            self.visit(x, o)

        self.visit(ast.body, o)

    def visitVarDecl(self, ast, o):
        # variable : Id
        # varType : Type
        # varInit : Expr = None # None if there is no initial
        for x in o[0]:
            if ast.variable.name == x.name:
                raise Redeclared(Variable(), ast.variable.name)

        if ast.varInit:
            self.visit(ast.varInit, o)
        
        # if ast.varType != self.visit(ast.varInit, o):
        #     raise 

        o[0].append(Symbol(ast.variable.name, ast.varType))

    def visitConstDecl(self, ast, o):
        # constant : Id
        # constType : Type
        # value : Expr
        for x in o[0]:
            if ast.constant.name == x.name:
                raise Redeclared(Constant(), ast.constant.name)

        if ast.constType != self.visit(ast.value, o):
            raise TypeMismatchInConstant(ast)

        o[0].append(Symbol(ast.constant.name, ast.constType, ast.constType))
    
    def visitBlock(self, ast, o):
        # decl:List[StoreDecl]
        # stmt:List[Stmt]
        [self.visit(x, o) for x in ast.decl]

        [self.visit(x, o) for x in ast.stmt]
    
    def visitBinaryOp(self, ast, o):
        # op:str
        # left:Expr
        # right:Expr
        type1 = self.visit(ast.left, o)
        type2 = self.visit(ast.right, o)
        if ast.op in ['\\', '%']:
            if type(type1) is not IntType or type(type2) is not IntType:
                raise TypeMismatchInExpression(ast)
            return IntType()

        elif ast.op in ['+', '-', '*', '/']:
            if type(type1) not in [IntType, FloatType] or type(type2) not in [IntType, FloatType]:
                raise TypeMismatchInExpression(ast)
            elif type1!=type2 or ast.op == '/':
                return FloatType()
            else:
                return type1

        elif ast.op in ['&&', '||', '!']:
            if type(type1) is BoolType and type(type2) is BoolType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)

        elif ast.op in ['==', '!=']:
            if type(type1) not in [IntType, BoolType] or type(type2) not in [IntType, BoolType] or type1 != type2:
                raise TypeMismatchInExpression(ast)
            else:
                return BoolType()

        elif ast.op in ['>', '<', '>=', '<=']:
            if type(type1) not in [IntType, FloatType] or type(type2) not in [IntType, FloatType]:
                raise TypeMismatchInExpression(ast)
            else:
                return BoolType()

        elif ast.op in ['^']:
            if type(type1) is not StringType or type(type2) is not StringType:
                raise TypeMismatchInExpression(ast)
            else:
                return StringType()
        
        

    def visitFuncDecl(self,ast, c): 
        return list(map(lambda x: self.visit(x,(c,True)),ast.body.stmt)) 
    

    def visitCallExpr(self, ast, c): 
        at = [self.visit(x,(c[0],False)) for x in ast.param]
        
        res = self.lookup(ast.method.name,c[0],lambda x: x.name)
        if res is None or not type(res.mtype) is MType:
            raise Undeclared(Function(),ast.method.name)
        elif len(res.mtype.partype) != len(at):
            if c[1]:
                raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInExpression(ast)
        else:
            return res.mtype.rettype

    def visitIntLiteral(self,ast, c): 
        return IntType()
    

