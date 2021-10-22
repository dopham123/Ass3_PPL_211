
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
import copy

class Type(ABC):
    __metaclass__ = ABCMeta
    pass
class Prim(Type):
    __metaclass__ = ABCMeta
    pass
class IntType(Prim):
    pass
class FloatType(Prim):
    pass
class StringType(Prim):
    pass
class BoolType(Prim):
    pass
class VoidType(Type):
    pass
class Unknown(Type):
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
            "static_method": [
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
            ]
        })    
    ]
            
    
    def __init__(self,ast):
        self.ast = ast

 
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, c): 
        obj = [[]] + [c]
        #lưu tên của class first
        for x in ast.decl:
            if x.classname.name not in c:
                c.append(Symbol(x.classname.name, ClassTyp(x.classname.name, None), {}))
            else:
                raise Redeclared(Class(), x.classname.name)
        
        #lưu tên memdecl vào <symbol>.value nếu là super class
        for x in ast.decl:
            if not x.parentname.name:
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
                                            if isinstance(y.decl.constType, self.visit(y.decl.value)): #check type constdecl
                                                z.value.get("global_sc_child").append(Symbol(y.decl.constant.name, y.decl.constType, y.decl.constType))
                                            else:
                                                raise TypeMismatchInConstant(y)
                                    #không phải ConstDecl thì là VarDecl
                                    else:
                                        #kiểm tra khai báo trùng id
                                        if y.decl.variable.name in [child.name for child in z.value.get("global_sc_child")]:
                                            raise Redeclared(Method(), y.name)
                                        else:
                                            z.value.get("global_sc_child").append(Symbol(y.decl.variable.name, y.decl.varType))
                                #Instance
                                else:
                        break

        return [self.visit(x,c) for x in ast.decl]

    def returnParamType(param): #param: list[VarDecl]
        [x.varType for x in param]

    
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
    

