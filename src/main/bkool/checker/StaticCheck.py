
"""
 * @author nhphung
"""

#---------------------Ten: Pham Van Do-----------------------
#---------------------MSSV: 1711035--------------------------
#------------------------------------------------------------

from AST import * 
from Visitor import *
# from Utils import Utils
from StaticError import *
import copy

# from main.bkool.utils.AST import IntType

# from main.bkool.utils.AST import BoolType, ClassType, FloatType, IntType, MethodDecl, Static, StringType, VarDecl, VoidType

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
    def __init__(self,partype: None,rettype):
        self.partype = (partype if partype else [])#list param type: []
        self.rettype = rettype #kiểu trả về của method

# @dataclass
class ArrayType(Type):
    dimen: int #số lượng phần tử trong mảng
    eletype: Type #kiểu của mỗi phần tử

class Symbol:
    def __init__(self, name, mtype, value = None):
        self.name = name
        self.mtype = mtype
        self.value = value #dict if class

class StaticChecker(BaseVisitor):

    global_envi = [
        Symbol("io", ClassType("io"), {
            "static_attrib": [
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
            "instance_attrib": [],
            'static_method': [],
            'instance_method': []
        })    
    ]
            
    
    def __init__(self,ast):
        self.ast = ast

    def visit(self,ast,param):
        return ast.accept(self,param)
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, c): 
        #lưu tên của class first
        c = copy.deepcopy(c)
        # print([y.name for y in c])
        for x in ast.decl:
            if x.classname.name not in [y.name for y in c]:
                c.append(Symbol(x.classname.name, ClassTyp(x.classname.name, None), {
                    "static_attrib": [],
                    "instance_attrib": [],
                    'static_method': [],
                    'instance_method': []
                }))
            else:
                # print('#################')
                raise Redeclared(Class(), x.classname.name)
        
        #lưu tên memdecl vào <symbol>.value nếu là super class
        for x in ast.decl:
            if not x.parentname:
                for z in c:
                    if z.name==x.classname.name: #tìm class trong env ứng với x
                        for y in x.memlist: #y: MethodDecl or AttributeDecl
                            #kiểm tra nếu là MethodDecl
                            if isinstance(y, MethodDecl):
                                # kind: SIKind
                                # name: Id
                                # param: List[VarDecl]
                                # returnType: Type  # None for constructor
                                # body: Block

                                #kiểm tra khai báo lại
                                if y.name in [child.name for child in (z.value.get("static_attrib") + z.value.get("instance_attrib") + z.value.get("static_method") + z.value.get("instance_method"))]:
                                    raise Redeclared(Method(), y.name)
                                else:
                                    if type(y.kind) is Static:
                                        field = "static_method"
                                    else:
                                        field = 'instance_method'
                                    z.value.get(field).append(Symbol(y.name.name, MType(self.returnParamType(y.param), y.returnType)))
                            #Ngược lại là AttributeDecl
                            # kind: SIKind #Instance or Static
                            # decl: StoreDecl # VarDecl for mutable or ConstDecl for immutable
                            else:
                                #Static
                                # if type(y.kind) is Static: #y.kind: SIKind(Static or Instance)
                                if type(y.decl) is ConstDecl: #y.decl: StoreDecl(ConstDecl or VarDecl)
                                    #kiểm tra khai báo trùng id
                                    if y.decl.constant.name in [child.name for child in (z.value.get("static_attrib") + z.value.get("instance_attrib") + z.value.get("static_method") + z.value.get("instance_method"))]:
                                        raise Redeclared(Attribute(), y.name)
                                    else:
                                        #kiểm tra kiểu của khai báo const
                                        # print(type(y.decl.constType))
                                        # k = IntType()
                                        # print(type(k))
                                        # print(type(y.decl.constType) == type(k))
                                        # print(type(y.decl.constType) == type(self.visit(y.decl.value, c)))
                                        if type(y.decl.constType) == type(self.visit(y.decl.value, c)): #check type constdecl
                                            if type(y.kind) is Static:
                                                field = 'static_attrib'
                                            else:
                                                field = 'instance_attrib'
                                            z.value.get(field).append(Symbol(y.decl.constant.name, y.decl.constType, y.decl.constType))
                                        else:
                                            raise TypeMismatchInConstant(y.decl)
                                #không phải ConstDecl thì là VarDecl
                                else:
                                    #kiểm tra khai báo trùng id
                                    if y.decl.variable.name in [child.name for child in (z.value.get("static_attrib") + z.value.get("instance_attrib") + z.value.get("static_method") + z.value.get("instance_method"))]:
                                        raise Redeclared(Attribute(), y.decl.variable.name)
                                    else:
                                        if y.decl.varInit:
                                            self.visit(y.decl.varInit, c)
                                        if type(y.kind) is Static:
                                            field = 'static_attrib'
                                        else:
                                            field = 'instance_attrib'
                                        z.value.get(field).append(Symbol(y.decl.variable.name, y.decl.varType))
                                #Instance
                                # else:
                                #     print('===========================$$$$$$$$$$$')
                                #     print(type(y.decl))
                                #     print(type(y.decl) in [ConstDecl])
                                #     if type(y.decl) is ConstDecl: #y.decl: StoreDecl(ConstDecl or VarDecl)
                                #         # constant : Id
                                #         # constType : Type
                                #         # value : Expr
                                        
                                #         #kiểm tra khai báo trùng id
                                #         if y.decl.constant.name in [child.name for child in z.value.get("instance_attrib")]:
                                #             raise Redeclared(Attribute(), y.name)
                                #         else:
                                #             #kiểm tra kiểu của khai báo const
                                #             print(type(y.decl.constType))
                                #             print('==================')
                                #             print(isinstance(type(y.decl.constType), type(self.visit(y.decl.value, c))))
                                #             print(type(self.visit(y.decl.value, c)))
                                #             if y.decl.constType == self.visit(y.decl.value, c): #check type constdecl
                                #                 z.value.get("instance_attrib").append(Symbol(y.decl.constant.name, y.decl.constType, y.decl.constType))
                                #             else:
                                #                 raise TypeMismatchInConstant(y)
                                #     #không phải ConstDecl thì là VarDecl
                                #     else:
                                #         #kiểm tra khai báo trùng id
                                #         if y.decl.variable.name in [child.name for child in z.value.get("instance_attrib")]:
                                #             raise Redeclared(Attribute(), y.decl.variable.name)
                                #         else:
                                #             if y.decl.varInit:
                                #                 self.visit(y.decl.varInit, c)
                                #             z.value.get("instance_attrib").append(Symbol(y.decl.variable.name, y.decl.varType))
                        break

        #cập nhật môi trường cho subclass
        for x in ast.decl:
            if x.parentname:
                for z in c:
                    if z.name==x.classname.name: #tìm class trong env ứng với x
                        #check exist super class?
                        if x.parentname.name not in [k.name for k in c]:
                            raise Undeclared(Class(), x.parentname.name)

                        for k in c: # tìm class trong env ứng với class cha của x
                            if x.parentname.name == k.name:
                                z.value = copy.deepcopy(k.value) #copy con của class cha và gắn vào class con
                        for y in x.memlist: #y: MethodDecl or AttributeDecl
                            #kiểm tra nếu là MethodDecl
                            if isinstance(y, MethodDecl):
                                if y.name in [child.name for child in (z.value.get("static_attrib") + z.value.get("instance_attrib") + z.value.get("static_method") + z.value.get("instance_method"))]:
                                    raise Redeclared(Method(), y.name)
                                else:
                                    if type(y.kind) is Static:
                                        field = "static_method"
                                    else:
                                        field = 'instance_method'
                                    z.value.get(field).append(Symbol(y.name.name, MType(self.returnParamType(y.param), y.returnType)))
                            #Ngược lại là AttributeDecl
                            else:
                                #Static
                                # if type(y.kind) is Static: #y.kind: SIKind(Static or Instance)
                                if type(y.decl) is ConstDecl: #y.decl: StoreDecl(ConstDecl or VarDecl)
                                    #kiểm tra khai báo trùng id
                                    if y.decl.constant.name in [child.name for child in (z.value.get("static_attrib") + z.value.get("instance_attrib") + z.value.get("static_method") + z.value.get("instance_method"))]:
                                        raise Redeclared(Attribute(), y.name)
                                    else:
                                        #kiểm tra kiểu của khai báo const
                                        if type(y.decl.constType) == type(self.visit(y.decl.value, c)): #check type constdecl
                                            if type(y.kind) is Static:
                                                field = 'static_attrib'
                                            else:
                                                field = 'instance_attrib'
                                            z.value.get(field).append(Symbol(y.decl.constant.name, y.decl.constType, y.decl.constType))
                                        else:
                                            raise TypeMismatchInConstant(y.decl)
                                #không phải ConstDecl thì là VarDecl
                                else:
                                    #kiểm tra khai báo trùng id
                                    if y.decl.variable.name in [child.name for child in (z.value.get("static_attrib") + z.value.get("instance_attrib") + z.value.get("static_method") + z.value.get("instance_method"))]:
                                        raise Redeclared(Attribute(), y.decl.variable.name)
                                    else:
                                        if y.decl.varInit:
                                            self.visit(y.decl.varInit, c)
                                        if type(y.kind) is Static:
                                            field = 'static_attrib'
                                        else:
                                            field = 'instance_attrib'
                                        z.value.get(field).append(Symbol(y.decl.variable.name, y.decl.varType))
                                #Instance
                                # else:
                                #     print('===========================$$$$$$$$$$$')
                                #     print(type(y.decl))
                                #     print(type(y.decl) in [ConstDecl])
                                #     if type(y.decl) is ConstDecl: #y.decl: StoreDecl(ConstDecl or VarDecl)
                                #         #kiểm tra khai báo trùng id
                                #         if y.decl.constant.name in [child.name for child in z.value.get("instance_attrib")]:
                                #             raise Redeclared(Attribute(), y.name)
                                #         else:
                                #             #kiểm tra kiểu của khai báo const
                                #             print(type(y.decl.constType))
                                #             print('==================')
                                #             print(isinstance(type(y.decl.constType), type(self.visit(y.decl.value, c))))
                                #             print(type(self.visit(y.decl.value, c)))
                                #             if y.decl.constType == self.visit(y.decl.value, c): #check type constdecl
                                #                 z.value.get("instance_attrib").append(Symbol(y.decl.constant.name, y.decl.constType, y.decl.constType))
                                #             else:
                                #                 raise TypeMismatchInConstant(y)
                                #     #không phải ConstDecl thì là VarDecl
                                #     else:
                                #         #kiểm tra khai báo trùng id
                                #         if y.decl.variable.name in [child.name for child in z.value.get("instance_attrib")]:
                                #             raise Redeclared(Attribute(), y.decl.variable.name)
                                #         else:
                                #             if y.decl.varInit:
                                #                 self.visit(y.decl.varInit, c)
                                #             z.value.get("instance_attrib").append(Symbol(y.decl.variable.name, y.decl.varType))
                        break
        print('##############################')
        print(c[2].name)
        print(c[2].value.get('static_method'))        
        return [self.visit(x,c) for x in ast.decl]

    def returnParamType(self, param): #param: list[VarDecl]
        return [x.varType for x in param]

    def visitClassDecl(self, ast, c):
        # classname : Id
        # memlist : List[MemDecl]
        # parentname : Id = None # None if there is no parent
        for i in c: #tìm class env trong c
            if i.name == ast.classname.name:
                for x in ast.memlist:
                    if type(x) is MethodDecl:
                        obj = [[]] + [i] + [c]
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
        
    def visitUnaryOp(self, ast, o):
        # op:str
        # body:Expr
        typexp = self.visit(ast.body, o)
        if type(typexp) not in [IntType, FloatType]:
            raise TypeMismatchInExpression(ast)
        return typexp

    # def visitFuncDecl(self,ast, c): 
    #     return list(map(lambda x: self.visit(x,(c,True)),ast.body.stmt)) 
    
    def visitCallExpr(self, ast, o): 
        # obj: Expr
        # method:Id
        # param:List[Expr]

        if type(ast.obj) is Id: #call static_method
            typeobj = self.visit(ast.obj, o) #có thể raise undeclare identity
            # class ClassType(Type):
            #     classname:Id
            
            #kiểm tra có phải classtype không
            if type(typeobj) is not ClassType and ast.obj.name not in [x.name for x in o[-1]]:
                raise TypeMismatchInExpression(ast)

            for x in o[-1]: # get class env
                if ast.obj.name == x.name:
                    for y in x.value.get('static_method'):
                        #trường hợp tìm được method trong môi trường
                        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                        print(y.name)
                        print(ast.method.name)
                        if y.name == ast.method.name:
                            #check param của method     note: y: Symbol
                            if not self.checkParam(y.mtype.partype, [self.visit(l, o) for l in ast.param]):
                                raise TypeMismatchInExpression(ast)
                            
                            #check return type is void?:
                            if type(y.mtype.rettype) is VoidType:
                                raise TypeMismatchInExpression(ast)
                            
                            return y.mtype.rettype
                    
                    #if don't exist in static_method
                    for y in x.value.get('instance_method'):
                        if y.name == ast.method.name:
                            raise TypeMismatchInExpression(ast)
                    
                    #if don't exist method in class
                    raise Undeclared(Method(), ast.method.name)
            
            #if don't exist classname:
            # raise Undeclared(Class(), ast.obj.name)

        #trường hợp là expr:
        else:
            typeobj = self.visit(ast.obj, o) #có thể raise undeclare identity
            if type(typeobj) is not ClassType:
                raise TypeMismatchInExpression(ast)
            for x in o[-1]:
                if x.name == typeobj.classname.name:
                    for y in x.value.get('instance_method'):
                        #trường hợp tìm được method trong môi trường
                        if y.name == ast.method.name:
                            #check param của method
                            if not self.checkParam(y.mtype.partype, [self.visit(l, o) for l in ast.param]):
                                raise TypeMismatchInExpression(ast)
                            
                            #check return type is void?:
                            if type(y.mtype.rettype) is VoidType:
                                raise TypeMismatchInExpression(ast)
                            
                            return y.mtype.rettype
                    
                    #if don't exist in instance_method
                    for y in x.value.get('static_method'):
                        if y.name == ast.method.name:
                            raise TypeMismatchInExpression(ast)
                    
                    #if don't exist method in class
                    raise Undeclared(Method(), ast.method.name)
        
    def checkParam(self, list1, list2):
        print('==============checkparam================')
        print(len(list1))
        print(len(list2))
        if len(list1) != len(list2):
            return False
        for i in range(len(list1)):
            if type(list1[i]) != type(list2[i]):
                return False
        return True
            
        
        
        # at = [self.visit(x,(c[0],False)) for x in ast.param]
        
        # res = self.lookup(ast.method.name,c[0],lambda x: x.name)
        # if res is None or not type(res.mtype) is MType:
        #     raise Undeclared(Function(),ast.method.name)
        # elif len(res.mtype.partype) != len(at):
        #     if c[1]:
        #         raise TypeMismatchInStatement(ast)
        #     else:
        #         raise TypeMismatchInExpression(ast)
        # else:
        #     return res.mtype.rettype

    def visitIntLiteral(self,ast, c): 
        return IntType()

    def visitFloatLiteral(self,ast, c): 
        return FloatType()
    

