
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

# from main.bkool.utils.AST import ArrayType, BoolType, FloatType, IntType, StringType

# from main.bkool.utils.AST import ArrayType, Block, BoolType, ClassType, Continue, FieldAccess, FloatType, IntType, StringType, VoidType

# from main.bkool.utils.AST import IntType

# from main.bkool.utils.AST import BoolType, ClassType, FloatType, IntType, MethodDecl, Static, StringType, VarDecl, VoidType

# class Type(ABC):
#     __metaclass__ = ABCMeta
#     pass
class NullType(Type):
    def __str__(self):
        return "NullType"

class MType:
    def __init__(self,partype: None,rettype):
        self.partype = (partype if partype else [])#list param type: []
        self.rettype = rettype #kiểu trả về của method

class ConstType:
    def __init__(self,rettype):
        self.rettype = rettype #kiểu trả về của biến

class VarType:
    def __init__(self,rettype):
        self.rettype = rettype #list[]: [kiểu trả về của biến, True/False: value]

# # @dataclass
# class ArrayType(Type):
#     dimen: int #số lượng phần tử trong mảng
#     eletype: Type #kiểu của mỗi phần tử

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
            'instance_method': [],
            'super_class': None
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
                c.append(Symbol(x.classname.name, ClassType(x.classname.name), {
                    "static_attrib": [],
                    "instance_attrib": [],
                    'static_method': [],
                    'instance_method': [],
                    'super_class': None
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
                                if y.name.name in [child.name for child in (z.value.get("static_attrib") + z.value.get("instance_attrib") + z.value.get("static_method") + z.value.get("instance_method"))]:
                                    raise Redeclared(Method(), y.name.name)
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
                                        raise Redeclared(Attribute(), y.decl.constant.name)
                                    else:
                                        #kiểm tra kiểu của khai báo const
                                        if y.decl.value:
                                            typexp = self.visit(y.decl.value, [[],c])
                                            typexp = self.returnTypeExp(typexp)

                                            if type(typexp[0]) in [IntType, FloatType, BoolType, StringType, ArrayType]:
                                                # print('==============check type const ==================')
                                                # print(type(y.decl.constType))
                                                # print(typexp)
                                                # print(self.checkType2Ele(y.decl.constType, typexp, c))
                                                if self.checkType2Ele(y.decl.constType, typexp, c): #check type constdecl
                                                    if type(y.kind) is Static:
                                                        field = 'static_attrib'
                                                    else:
                                                        field = 'instance_attrib'
                                                    z.value.get(field).append(Symbol(y.decl.constant.name, ConstType(y.decl.constType), True))
                                                else:
                                                    raise TypeMismatchInConstant(y.decl)

                                                #kiểm tra value gắn cho const:
                                                if not typexp[1]:
                                                    raise IllegalConstantExpression(y.decl.value)
                                            else:
                                                raise IllegalConstantExpression(y.decl.value)
                                        else:
                                            raise IllegalConstantExpression(None)
                                        
                                #không phải ConstDecl thì là VarDecl
                                else:
                                    #kiểm tra khai báo trùng id
                                    if y.decl.variable.name in [child.name for child in (z.value.get("static_attrib") + z.value.get("instance_attrib") + z.value.get("static_method") + z.value.get("instance_method"))]:
                                        raise Redeclared(Attribute(), y.decl.variable.name)
                                    else:
                                        if type(y.kind) is Static:
                                            field = 'static_attrib'
                                        else:
                                            field = 'instance_attrib'
                                        value = False
                                        if y.decl.varInit:
                                            self.visit(y.decl.varInit, [[],c])
                                            value = True
                                        z.value.get(field).append(Symbol(y.decl.variable.name, VarType(y.decl.varType), value))
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
                                #copy môi trường
                                z.value = copy.deepcopy(k.value) #copy con của class cha và gắn vào class con

                                #cập nhật tên class cha
                                z.value['super_class'] = k.name 

                        for y in x.memlist: #y: MethodDecl or AttributeDecl
                            #kiểm tra nếu là MethodDecl
                            if isinstance(y, MethodDecl):
                                if y.name.name in [child.name for child in (z.value.get("static_attrib") + z.value.get("instance_attrib") + z.value.get("static_method") + z.value.get("instance_method"))]:
                                    raise Redeclared(Method(), y.name.name)
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
                                        raise Redeclared(Attribute(), y.decl.constant.name)
                                    else:
                                        #kiểm tra kiểu của khai báo const
                                        if y.decl.value:
                                            typexp = self.visit(y.decl.value, [[],c])
                                            typexp = self.returnTypeExp(typexp)

                                            if type(typexp[0]) in [IntType, FloatType, BoolType, StringType, ArrayType]:
                                                # print('==============check type const ==================')
                                                # print(type(y.decl.constType))
                                                # print(typexp)
                                                # print(self.checkType2Ele(y.decl.constType, typexp, c))
                                                if self.checkType2Ele(y.decl.constType, typexp, c): #check type constdecl
                                                    if type(y.kind) is Static:
                                                        field = 'static_attrib'
                                                    else:
                                                        field = 'instance_attrib'
                                                    z.value.get(field).append(Symbol(y.decl.constant.name, ConstType(y.decl.constType), True))
                                                else:
                                                    raise TypeMismatchInConstant(y.decl)

                                                #kiểm tra value gắn cho const:
                                                if not typexp[1]:
                                                    raise IllegalConstantExpression(y.decl.value)
                                            else:
                                                raise IllegalConstantExpression(y.decl.value)
                                        else:
                                            raise IllegalConstantExpression(None)
                                #không phải ConstDecl thì là VarDecl
                                else:
                                    #kiểm tra khai báo trùng id
                                    if y.decl.variable.name in [child.name for child in (z.value.get("static_attrib") + z.value.get("instance_attrib") + z.value.get("static_method") + z.value.get("instance_method"))]:
                                        raise Redeclared(Attribute(), y.decl.variable.name)
                                    else:
                                        if type(y.kind) is Static:
                                            field = 'static_attrib'
                                        else:
                                            field = 'instance_attrib'
                                        value = False
                                        if y.decl.varInit:
                                            self.visit(y.decl.varInit, [[],c])
                                            value = True
                                        z.value.get(field).append(Symbol(y.decl.variable.name, VarType(y.decl.varType), value))
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
        # print('##############################')
        # print(c[2].name)
        # print(c[2].value.get('static_method'))        
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

        obj = [[]] + o
        for x in ast.param:
            for y in obj[0]:
                if x.variable.name == y.name:
                    raise Redeclared(Parameter(), x.variable.name)
            obj[0].append(Symbol(x.variable.name, VarType(x.varType), False))
            # self.visit(x, obj)

        p = {
            'rettype': ast.returnType,
            'inloop': False
        }

        self.visit(ast.body, [obj, p])

    def visitVarDecl(self, ast, o):
        # variable : Id
        # varType : Type
        # varInit : Expr = None # None if there is no initial
        for x in o[0]:
            if ast.variable.name == x.name:
                raise Redeclared(Variable(), ast.variable.name)

        value = False
        if ast.varInit:
            self.visit(ast.varInit, o)
            value = True
        
        # if ast.varType != self.visit(ast.varInit, o):
        #     raise 

        o[0].append(Symbol(ast.variable.name, VarType(ast.varType), value))

    def visitConstDecl(self, ast, o):
        # constant : Id
        # constType : Type
        # value : Expr
        for x in o[0]:
            if ast.constant.name == x.name:
                raise Redeclared(Constant(), ast.constant.name)
        if ast.value:
            typevalue = self.visit(ast.value, o)
            typevalue = self.returnTypeExp(typevalue)
            # print('===============typevalue==============')
            # print(typevalue)

            if type(typevalue[0]) in [IntType, FloatType, BoolType, StringType, ArrayType]:
                # print(self.checkType2Ele(ast.constType, typevalue, o))
                # print(type(ast.constType))
                if not self.checkType2Ele(ast.constType, typevalue, o):
                    raise TypeMismatchInConstant(ast)

                if not typevalue[1]:
                    raise IllegalConstantExpression(ast.value)
            else:
                raise IllegalConstantExpression(ast.value)
        else:
            raise IllegalConstantExpression(None)

        o[0].append(Symbol(ast.constant.name, ConstType(ast.constType), True))
    
    def visitBlock(self, ast, obj):
        o = obj[0]
        p = obj[1]
        p = copy.deepcopy(p)
        # decl:List[StoreDecl]
        # stmt:List[Stmt]
        [self.visit(x, o) for x in ast.decl]

        for x in ast.stmt:
            if type(x) is Block:
                obj = [[]] + o
                self.visit(x, [obj, p])
            else:
                self.visit(x, [o, p])
    
    def visitBinaryOp(self, ast, o):
        # op:str
        # left:Expr
        # right:Expr
        # if type(ast.left) in [Id, FieldAccess]:
        #     type1 = self.visit(ast.left, o).rettype
        # else:
        #     type1 = self.visit(ast.left, o)
        
        # if type(ast.right) in [Id, FieldAccess]:
        #     type2 = self.visit(ast.right, o).rettype
        # else:
        #     type2 = self.visit(ast.right, o)

        type1 = self.visit(ast.left, o)
        type1 = self.returnTypeExp(type1)

        type2 = self.visit(ast.right, o)
        type2 = self.returnTypeExp(type2)
        #type: [type, value:Bool)]

        if ast.op in ['\\', '%']:
            if type(type1[0]) is not IntType or type(type2[0]) is not IntType:
                raise TypeMismatchInExpression(ast)
            return [IntType(), type1[1] and type2[1]]

        elif ast.op in ['+', '-', '*', '/']:
            if type(type1[0]) not in [IntType, FloatType] or type(type2[0]) not in [IntType, FloatType]:
                raise TypeMismatchInExpression(ast)
            elif type(type1[0]) != type(type2[0]) or ast.op == '/':
                return [FloatType(), type1[1] and type2[1]]
            else:
                return type1

        elif ast.op in ['&&', '||', '!']:
            if type(type1[0]) is BoolType and type(type2[0]) is BoolType:
                return [BoolType(), type1[1] and type2[1]]
            else:
                raise TypeMismatchInExpression(ast)

        elif ast.op in ['==', '!=']:
            if type(type1[0]) not in [IntType, BoolType] or type(type2[0]) not in [IntType, BoolType] or type1 != type2:
                raise TypeMismatchInExpression(ast)
            else:
                return [BoolType(), type1[1] and type2[1]]

        elif ast.op in ['>', '<', '>=', '<=']:
            if type(type1[0]) not in [IntType, FloatType] or type(type2[0]) not in [IntType, FloatType]:
                raise TypeMismatchInExpression(ast)
            else:
                return [BoolType(), type1[1] and type2[1]]

        elif ast.op in ['^']:
            if type(type1[0]) is not StringType or type(type2[0]) is not StringType:
                raise TypeMismatchInExpression(ast)
            else:
                return [StringType(), type1[1] and type2[1]]
        
    def visitUnaryOp(self, ast, o):
        # op:str
        # body:Expr
        typexp = self.visit(ast.body, o)
        typexp = self.returnTypeExp(typexp)

        if type(typexp[0]) not in [IntType, FloatType]:
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
            typeobj = self.returnTypeExp(typeobj)
            # class ClassType(Type):
            #     classname:Id
            
            #kiểm tra có phải classtype không
            if type(typeobj[0]) is not ClassType and ast.obj.name not in [x.name for x in o[-1]]:
                raise TypeMismatchInExpression(ast)

            for x in o[-1]: # get class env
                if ast.obj.name == x.name:
                    for y in x.value.get('static_method'):
                        #trường hợp tìm được method trong môi trường
                        # print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                        # print(y.name)
                        # print(ast.method.name)
                        if y.name == ast.method.name:
                            #check param của method     note: y: Symbol
                            if not self.checkParam(y.mtype.partype, [self.visit(l, o) for l in ast.param], o):
                                raise TypeMismatchInExpression(ast)
                            
                            #check return type is void?:
                            if type(y.mtype.rettype) is VoidType:
                                raise TypeMismatchInExpression(ast)
                            
                            return [y.mtype.rettype, True]
                    
                    #if don't exist in static_method
                    #check if exist in instance_method
                    for y in x.value.get('instance_method'):
                        if y.name == ast.method.name:
                            raise IllegalMemberAccess(ast)
                    
                    #if don't exist method in class
                    raise Undeclared(Method(), ast.method.name)
            
            #if don't exist classname:
            # raise Undeclared(Class(), ast.obj.name)

        #trường hợp là expr:
        else:
            typeobj = self.visit(ast.obj, o) #có thể raise undeclare identity
            typeobj = self.returnTypeExp(typeobj)

            if type(typeobj[0]) is not ClassType:
                raise TypeMismatchInExpression(ast)
            for x in o[-1]:
                if x.name == typeobj[0].classname.name:
                    for y in x.value.get('instance_method'):
                        #trường hợp tìm được method trong môi trường
                        if y.name == ast.method.name:
                            #check param của method
                            if not self.checkParam(y.mtype.partype, [self.visit(l, o) for l in ast.param], o):
                                raise TypeMismatchInExpression(ast)
                            
                            #check return type is void?:
                            if type(y.mtype.rettype) is VoidType:
                                raise TypeMismatchInExpression(ast)
                            
                            return [y.mtype.rettype, True]
                    
                    #if don't exist in instance_method
                    #check if exist in static_method:
                    for y in x.value.get('static_method'):
                        if y.name == ast.method.name:
                            raise IllegalMemberAccess(ast)
                    
                    #if don't exist method in class
                    raise Undeclared(Method(), ast.method.name)
        
    #check param in func match each other
    def checkParam(self, list1, list2, o):
        # print('==============checkparam================')
        # print(len(list1))
        # print(len(list2))
        if len(list1) != len(list2):
            return False
        for i in range(len(list1)):
            if not self.checkType2Ele(list1[i], list2[i], o):
                return False
            # if type(list1[i]) is FloatType and type(list2[i]) not in [IntType, FloatType]:
            #     return False
            # elif type(list1[i]) != type(list2[i]):
            #     return False
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

    def visitFieldAccess(self, ast, o):
        # obj:Expr
        # fieldname:Id
        # print('===========fieldaccess===========')
        # print(o)
        typeobj = self.visit(ast.obj, o) #có thể raise undeclare identity
        typeobj = self.returnTypeExp(typeobj)

        #access static attrib
        if type(ast.obj) is Id:
            if type(typeobj[0]) is not ClassType and ast.obj.name not in [x.name for x in o[-1]]: #vế sau khi kiếm dc id không phải classtype nhưng có class id
                raise TypeMismatchInExpression(ast)

            for x in o[-1]: # get class env
                if ast.obj.name == x.name:
                    for y in x.value.get('static_attrib'):
                        #trường hợp tìm được attrib trong môi trường
                        # print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                        # print(y.name)
                        # print(ast.fieldname.name)
                        # print(y.value)
                        if y.name == ast.fieldname.name:
                            return [y.mtype, y.value]
                    
                    #if don't exist in static_attrib
                    #check if exist in instance_attrib
                    for y in x.value.get('instance_attrib'):
                        if y.name == ast.fieldname.name:
                            raise IllegalMemberAccess(ast)
                    
                    #if don't exist attrib in class
                    raise Undeclared(Attribute(), ast.fieldname.name)

        #trường hợp là expr: access instance attrib
        else:
            if type(typeobj[0]) is not ClassType:
                raise TypeMismatchInExpression(ast)

            for x in o[-1]: # get class env
                if ast.obj.name == x.name:
                    for y in x.value.get('instance_attrib'):
                        #trường hợp tìm được attrib trong môi trường
                        # print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                        # print(y.name)
                        # print(ast.fieldname.name)
                        if y.name == ast.fieldname.name:
                            return [y.mtype, y.value]
                    
                    #if don't exist in static_attrib
                    #check if exist in instance_attrib
                    for y in x.value.get('static_attrib'):
                        if y.name == ast.fieldname.name:
                            raise IllegalMemberAccess(ast)
                    
                    #if don't exist attrib in class
                    raise Undeclared(Attribute(), ast.fieldname.name)

    def visitId(self, ast, o):
        for env in o[:-2]:
            flag = False
            for decl in env: #Symbol
                if ast.name == decl.name:
                    flag = True
                    return [decl.mtype, decl.value]
            if flag:
                break
        
        # tìm trong class env
        for decl in o[-1]:
            # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
            # print(ast)
            # print(o[-1])
            # print(decl)
            if ast.name == decl.name:
                return [decl.mtype, False]

        raise Undeclared(Identifier(), ast.name)
    
    def visitNewExpr(self, ast, o):
        # classname:Id
        # param:List[Expr]
        x = self.findClassInEnv(ast.classname.name, o[-1])
        if not x:
            raise Undeclared(Class(), ast.classname.name)

        flag = False
        for decl in x.value.get('instance_method'):
            if decl.name == ast.classname.name:
                if not self.checkParam(decl.mtype.partype, [self.visit(i) for i in ast.param], o):
                    raise TypeMismatchInExpression(ast)
                flag = True
                break
        if not flag:
            raise Undeclared(Method(), ast.classname.name)
        return [x.mtype, False]

    def visitArrayCell(self, ast, o):
        # arr:Expr
        # idx:Expr
        typearr = self.visit(ast.arr, o)
        typearr = self.returnTypeExp(typearr)

        typeidx = self.visit(ast.idx)
        typeidx = self.returnTypeExp(typeidx)

        if type(typearr[0]) is not ArrayType or type(typeidx[0]) is not IntType:
            raise TypeMismatchInExpression(ast)
        return [typearr[0].eleType, typearr[1]]

    def visitIntLiteral(self,ast, o): 
        return [IntType(), True]

    def visitFloatLiteral(self,ast, o): 
        return [FloatType(), True]

    def visitNullLiteral(self, ast, o):
        return [NullType(), False]

    def visitStringLiteral(self, ast, o):
        return [StringType(), True]
    
    def visitBooleanLiteral(self, ast, o):
        return [BoolType(), True]

    def visitArrayLiteral(self, ast, o):
        # value: List[Literal]
        eletyp = self.visit(ast.value[0], o)
        eletyp = self.returnTypeExp(eletyp)
        for x in ast.value:
            typeother = self.visit(x, o)
            if not self.checkType2Ele(eletyp, typeother, o):
                raise IllegalArrayLiteral(ast)
        return [ArrayType(len(ast.value), eletyp[0]), True]
#note: Id and FieldAccess return ConstType or VarType
    def visitAssign(self, ast, obj):
        o = obj[0]
        p = obj[1]
        p = copy.deepcopy(p)
        # lhs:Expr
        # exp:Expr

        # Id or FieldAccess
        # if type(ast.lhs) in [Id, FieldAccess]:
        #     type1 = self.visit(ast.lhs, o).rettype
        # else:
        #     type1 = self.visit(ast.lhs, o)
        
        # if type(ast.right) in [Id, FieldAccess]:
        #     type2 = self.visit(ast.right, o).rettype
        # else:
        #     type2 = self.visit(ast.right, o)
        # print('========ASSIGN===========')
        # print(o)
        type1 = self.visit(ast.lhs, o)
        # print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        type2 = self.visit(ast.exp, o)
        #check assign to constant
        if type(type1[0]) is ConstType:
            raise CannotAssignToConstant(ast)

        # if type(type1[0]) is VarType:
        #     type1 = type1.rettype

        # if type(type2) in [ConstType, VarType]:
        #     type2 = type2.rettype
        
        #check if lhs is voidtype
        if type(type1[0]) is VoidType:
            raise TypeMismatchInStatement(ast)

        #check type
        if not self.checkType2Ele(type1, type2, o):
            raise TypeMismatchInStatement(ast)

    def visitIf(self, ast, obj):
        o = obj[0]
        p = obj[1]
        p = copy.deepcopy(p)
        # expr:Expr
        # thenStmt:Stmt
        # elseStmt:Stmt = None # None if there is no else branch
        typexpr = self.visit(ast.expr, o)
        typexpr = self.returnTypeExp(typexpr)
        # if type(typexpr) in [ConstType, VarType]:
        #     typexpr = typexpr.rettype

        if type(typexpr[0]) is not BoolType:
            raise TypeMismatchInStatement(ast)

        if type(ast.thenStmt) is Block:
            obj = [[]] + o
            self.visit(ast.thenStmt, [obj, p])
        else:
            self.visit(ast.thenStmt, [o, p])

        if ast.elseStmt:
            if type(ast.elseStmt) is Block:
                obj = [[]] + o
                self.visit(ast.elseStmt, [obj, p])
            else:
                self.visit(ast.elseStmt, [o, p])

    def visitFor(self, ast, obj):
        o = obj[0]
        p = obj[1]
        p = copy.deepcopy(p)
        # id:Id
        # expr1:Expr
        # expr2:Expr
        # up: bool #True => increase; False => decrease
        # loop:Stmt  
        typeid = self.visit(ast.id, o)
        typeid = self.returnTypeExp(typeid)

        if type(typeid[0]) is not IntType:
            raise TypeMismatchInStatement(ast)

        typexp1 = self.visit(ast.expr1, o)
        typexp1 = self.returnTypeExp(typexp1)

        typexp2 = self.visit(ast.expr2, o)
        typexp2 = self.returnTypeExp(typexp2)

        if type(typexp1[0]) is not IntType or type(typexp2[0]) is not IntType:
            raise TypeMismatchInStatement(ast)

        p['inloop'] = True
        if type(ast.loop) is Block:
            obj = [[]] + o
            self.visit(ast.loop, [obj, p])
        else:
            self.visit(ast.loop, [o, p])

    def visitCallStmt(self, ast, obj):
        o = obj[0]
        p = obj[1]
        p = copy.deepcopy(p)
        # obj: Expr  
        # method:Id
        # param:List[Expr]

        if type(ast.obj) is Id: #call static_method
            typeobj = self.visit(ast.obj, o) #có thể raise undeclare identity
            typeobj = self.returnTypeExp(typeobj)
            # class ClassType(Type):
            #     classname:Id
            
            #kiểm tra có phải classtype không
            if type(typeobj[0]) is not ClassType and ast.obj.name not in [x.name for x in o[-1]]:
                raise TypeMismatchInStatement(ast)

            for x in o[-1]: # get class env
                if ast.obj.name == x.name:
                    for y in x.value.get('static_method'):
                        #trường hợp tìm được method trong môi trường
                        # print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                        # print(y.name)
                        # print(ast.method.name)
                        if y.name == ast.method.name:
                            #check param của method     note: y: Symbol
                            if not self.checkParam(y.mtype.partype, [self.visit(l, o) for l in ast.param], o):
                                raise TypeMismatchInStatement(ast)
                            
                            #check return type is void?:
                            if type(y.mtype.rettype) is not VoidType:
                                raise TypeMismatchInStatement(ast)
                            
                            # return y.mtype.rettype
                    
                    #if don't exist in static_method
                    #check if exist in instance_method
                    for y in x.value.get('instance_method'):
                        if y.name == ast.method.name:
                            raise IllegalMemberAccess(ast)
                    
                    #if don't exist method in class
                    raise Undeclared(Method(), ast.method.name)
            
            #if don't exist classname:
            # raise Undeclared(Class(), ast.obj.name)

        #trường hợp là expr:
        else:
            typeobj = self.visit(ast.obj, o) #có thể raise undeclare identity
            typeobj = self.returnTypeExp(typeobj)

            if type(typeobj[0]) is not ClassType:
                raise TypeMismatchInStatement(ast)
            for x in o[-1]:
                if x.name == typeobj[0].classname.name:
                    for y in x.value.get('instance_method'):
                        #trường hợp tìm được method trong môi trường
                        if y.name == ast.method.name:
                            #check param của method
                            if not self.checkParam(y.mtype.partype, [self.visit(l, o) for l in ast.param], o):
                                raise TypeMismatchInStatement(ast)
                            
                            #check return type is void?:
                            if type(y.mtype.rettype) is not VoidType:
                                raise TypeMismatchInStatement(ast)
                            
                            # return y.mtype.rettype
                    
                    #if don't exist in instance_method
                    #check if exist in static_method:
                    for y in x.value.get('static_method'):
                        if y.name == ast.method.name:
                            raise IllegalMemberAccess(ast)
                    
                    #if don't exist method in class
                    raise Undeclared(Method(), ast.method.name)

    def visitReturn(self, ast, obj):
        o = obj[0]
        p = obj[1]
        p = copy.deepcopy(p)
        # expr:Expr
        typexp = self.visit(ast.expr, o)
        typexp = self.returnTypeExp(typexp)

        if not self.checkType2Ele(p.get('rettype'), typexp):
            raise TypeMismatchInStatement(ast)

    def visitBreak(self, ast, obj):
        o = obj[0]
        p = obj[1]
        p = copy.deepcopy(p)
        if not p.get('inloop'):
            raise MustInLoop(ast)

    def visitContinue(self, ast, obj):
        o = obj[0]
        p = obj[1]
        p = copy.deepcopy(p)
        if not p.get('inloop'):
            raise MustInLoop(ast)

    #giong nhau: True    |   khac nhau: False
    def checkType2Ele(self, type1, type2, o): #Int, Float,...,Array,Class.
        if type(type1) is list:
            type1 = type1[0]
        if type(type2) is list:
            type2 = type2[0]

        if type(type1) is VarType:
            type1 = type1.rettype

        if type(type2) in [ConstType, VarType]:
            type2 = type2.rettype
        # print('===========checkType2ele==========')
        # print(type(type1) is FloatType)
        # print(type(type2) not in [IntType, FloatType])
        if type(type1) is FloatType and type(type2) in [IntType, FloatType]:
            return True
        elif type(type1) is ArrayType and type2 is ArrayType:
            # size : int
            # eleType:Type
            if type1.size != type2.size:
                return False
            elif type(type1.eleType) is FloatType and type(type2.eleType) not in [IntType, FloatType]:
                return False
            elif type(type1.eleType) != type(type2.eleType):
                return False
        elif type(type1) is ClassType and type(type2) is ClassType:
            # classname:Id
            classname1 = type1.classname.name
            classname2 = type2.classname.name
            classenv1 = self.findClassInEnv(classname1, o[-1])
            classenv2 = self.findClassInEnv(classname2, o[-1])
            if classenv2.name not in [classenv1.name, classenv2.value.get('super_class')]:
                return False
        elif type(type1) != type(type2):
            return False
        return True

    def returnTypeExp(self, typexp):
        if type(typexp) is list:
            if type(typexp[0]) in [VarType, ConstType]:
                return [typexp[0].rettype, typexp[1]]
            else:
                return typexp
        else:
            if type(typexp) in [VarType, ConstType]:
                return typexp.rettype
            else:
                return typexp 

    #tìm class trong môi trường, trả về Symbol hoặc None
    def findClassInEnv(self, classname, c): #với c là danh sách các classenv
        for x in c:
            if classname==x.name:
                return x
        return None