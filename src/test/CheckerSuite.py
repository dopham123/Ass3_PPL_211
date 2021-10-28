import unittest
from TestUtils import TestChecker
from AST import *

#---------------------Ten: Pham Van Do-----------------------
#---------------------MSSV: 1711035--------------------------
#------------------------------------------------------------

class CheckerSuite(unittest.TestCase):
    
    def test_diff_numofparam_stmt(self):
        """More complex program"""
        input = """ class fact{

                    }
                    class Function extends fact {
                        static int main(int a,b){
                            a:=6*5;
                        }
                        int foo(){
                            int c;
                            c := Function.main(2.5, 3);
                        }
                    }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(Function),Id(main),[FloatLit(2.5),IntLit(3)])"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclare_1(self):
        """Simple program: int main() {} """
        input = Program([ClassDecl(Id("main"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Instance(),ConstDecl(Id("v"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),VarDecl(Id("a"),IntType(),IntLiteral(5)))])])
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclare_2(self):
        """Simple program: int main() {} """
        input = """class main {
                    int a = 5;
                    final int v = 6;
                    float a;
                }"""
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_redeclare_3(self):
        """Simple program: int main() {} """
        input = """class main {
                    int a = 5;
                    final int v = 6;
                }
                class main {

                }"""
        expect = "Redeclared Class: main"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclare_4(self):
        """Simple program: int main() {} """
        input = """class main {
                    int a = 5;
                    final int v = 6;
                    int f(int c){

                    }
                    float f(){

                    }
                }"""
        expect = "Redeclared Method: f"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_redeclare_5(self):
        """Simple program: int main() {} """
        input = """class main {
                    int a = 5;
                    final int v = 6;
                    int f(int c; float c){

                    }
                }"""
        expect = "Redeclared Parameter: c"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_redeclare_6(self):
        """Simple program: int main() {} """
        input = """class main {
                    int a = 5;
                    final int v = 6;
                    int f(int c){
                        float d;
                        float d;
                    }
                }"""
        expect = "Redeclared Variable: d"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_redeclare_7(self):
        """Simple program: int main() {} """
        input = """class main {
                    int a = 5;
                    final int v = 6;
                    int f(int c){
                        final float d = 5;
                        final float d = 6;
                    }
                }"""
        expect = "Redeclared Constant: d"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_redeclare_8(self):
        """Simple program: int main() {} """
        input = """class main {
                    int a = 5;
                    final int v = 6;
                    int f(int c){
                        final float d = 5;
                        float d = 6;
                    }
                }"""
        expect = "Redeclared Variable: d"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_redeclare_9(self):
        """Simple program: int main() {} """
        input = """class main {
                    int a = 5;
                    final int v = 6;
                    int f(int c){
                        final float d = 5;
                        float e = 6;
                    }
                }
                class f extends main{
                    int k(int c; float d){
                        final float d = 5;
                        float e = 6;
                    }
                }"""
        expect = "Redeclared Constant: d"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_redeclare_10(self):
        """Simple program: int main() {} """
        input = """class main {
                    int a = 5;
                    final int v = 6;
                    int f(int c){
                        final float d = 5;
                        float e = 6;
                    }
                }
                class main extends main{
                    int k(int c; float d){
                        final float d = 5;
                        float e = 6;
                    }
                }"""
        expect = "Redeclared Class: main"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_undeclare_1(self):
        """Simple program: int main() {} """
        input = """class main {
                    int a = 5;
                    final int v = 6;
                    int f(int c){
                        b := 5;
                    }
                }
                class l extends main{
                    int k(int c; float d){
                        final float d = 5;
                        float e = 6;
                    }
                }"""
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_undeclare_2(self):
        """Simple program: int main() {} """
        input = """class main {
                    int a = 5;
                    final int v = 6;
                    int f(int c){
                        c := main.k;
                    }
                }"""
        expect = "Undeclared Attribute: k"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_undeclare_3(self):
        """Simple program: int main() {} """
        input = """class main {
                    int a = 5;
                    final int v = 6;
                    int f(int c){
                        c := main.k();
                    }
                }"""
        expect = "Undeclared Method: k"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_undeclare_4(self):
        """Simple program: int main() {} """
        input = """class main {
                    int a = 5;
                    final int v = 6;
                    int f(int c){
                        c := mai.k();
                    }
                }"""
        expect = "Undeclared Identifier: mai"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_undeclare_5(self):
        """Simple program: int main() {} """
        input = """class main {
                    int a = 5;
                    final int v = 6;
                    int f(int c){
                        c := main.a;
                    }
                }
                class b extends a{

                }"""
        expect = "Undeclared Class: a"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_undeclare_6(self):
        """Simple program: int main() {} """
        input = """class main {
                    int a = 5;
                    final int v = 6;
                    int f(int c){

                    }
                }
                class b extends main{
                    int fa(int c){
                        c := b.k;
                    }
                }"""
        expect = "Undeclared Attribute: k"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_undeclare_7(self):
        """Simple program: int main() {} """
        input = """class main {
                    int a = 5;
                    final int v = 6;
                    static int f(int c){

                    }
                }
                class b extends main{
                    int fa(int c){
                        c := b.f(c);
                        b.t() := 5;
                    }
                }"""
        expect = "Undeclared Method: t"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_undeclare_8(self):
        """Simple program: int main() {} """
        input = """class main {
                    int a = 5;
                    final int v = 6;
                    static int f(int c){

                    }
                }
                class b extends main{
                    int fa(int c){
                        c := b.f(c);
                        k.t() := 5;
                    }
                }"""
        expect = "Undeclared Identifier: k"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_undeclare_9(self):
        """Simple program: int main() {} """
        input = """class main {
                    int a = 5;
                    final int v = 6;
                    static int f(int c){

                    }
                }
                class b extends m{
                    int fa(int c){
                        c := b.f(c);
                    }
                }"""
        expect = "Undeclared Class: m"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_undeclare_10(self):
        """Simple program: int main() {} """
        input = """class main {
                    int a = 5;
                    final int v = 6;
                    static int f(int c){

                    }
                }
                class b extends main{
                    int fa(int c){
                        c := b.t;
                    }
                }"""
        expect = "Undeclared Attribute: t"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_CannotAssignToConstant_1(self):
        """Simple program: int main() {} """
        input = """class main {
                    int a = 5;
                    static final int v = 6;
                    static int f(int c){

                    }
                }
                class b extends main{
                    int fa(int c){
                        b.v := c;
                    }
                }"""
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Id(b),Id(v)),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_CannotAssignToConstant_2(self):
        """Simple program: int main() {} """
        input = """class main {
                    int a = 5;
                    static final int v = 6;
                    static int f(int c){

                    }
                }
                class b extends main{
                    int fa(int c){
                        final int s = 5;
                        s := true;
                    }
                }"""
        expect = "Cannot Assign To Constant: AssignStmt(Id(s),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_CannotAssignToConstant_3(self):
        """Simple program: int main() {} """
        input = """class main {
                    static final int a = 5;
                    static final int v = 6;
                    static int f(int c){

                    }
                }
                class b extends main{
                    int fa(int c){
                        final int s = 5;
                        b.a := 3.5;
                        s := true;
                    }
                }"""
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Id(b),Id(a)),FloatLit(3.5))"
        self.assertTrue(TestChecker.test(input,expect,423))

    
    def test_CannotAssignToConstant_4(self):
        """Simple program: int main() {} """
        input = """class main {
                    int a = 5;
                    static final int v = 6;
                    static int f(int c){
                        main.v := c;
                    }
                }"""
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Id(main),Id(v)),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_CannotAssignToConstant_5(self):
        """Simple program: int main() {} """
        input = """class main {
                    int a = 5;
                    static final int v = 6;
                    static int f(int c){
                        final float g = 2;
                        g := c;
                    }
                }"""
        expect = "Cannot Assign To Constant: AssignStmt(Id(g),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_CannotAssignToConstant_6(self):
        """Simple program: int main() {} """
        input = """class main {
                    static final int a = 5;
                    static final int v = 6;
                    static int f(int c){

                    }
                }
                class b extends main{
                    int fa(int c){
                        final int s = 5;
                        b.a := main.f(5);
                    }
                }"""
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Id(b),Id(a)),CallExpr(Id(main),Id(f),[IntLit(5)]))"
        self.assertTrue(TestChecker.test(input,expect,426))
   
    def test_CannotAssignToConstant_7(self):
        """Simple program: int main() {} """
        input = """class main {
                    int a = 5;
                    static final int v = 6;
                    static int f(int c){
                        c := 12;
                    }
                }
                class s extends main{
                    static final float j = 3;
                    static int fa(int c){
                        s.j := 5.6;
                    }
                }"""
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Id(s),Id(j)),FloatLit(5.6))"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_CannotAssignToConstant_8(self):
        """Simple program: int main() {} """
        input = """class main {
                    int a = 5;
                    static final int v = 6;
                    static int f(int c){
                        final float g = 2;
                        main.v := g;
                    }
                }"""
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Id(main),Id(v)),Id(g))"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_CannotAssignToConstant_9(self):
        """Simple program: int main() {} """
        input = """class main {
                    static final int a = 5;
                    static final int v = 6;
                    static int f(int c){

                    }
                }
                class b extends main{
                    int fa(int c){
                        final int s = 5;
                        main.v := b.f(5);
                    }
                }"""
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Id(main),Id(v)),CallExpr(Id(b),Id(f),[IntLit(5)]))"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_CannotAssignToConstant_10(self):
        """Simple program: int main() {} """
        input = """class main {
                    static final int a = 5;
                    static final int v = 6;
                    static int f(int c){

                    }
                }
                class b extends main{
                    int fa(int c){
                        final int s = 5;
                        b.a := b.f(5);
                    }
                }"""
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Id(b),Id(a)),CallExpr(Id(b),Id(f),[IntLit(5)]))"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_TypeMismatchInStmt_1(self):
        """Simple program: int main() {} """
        input = """class main {
                    static final int a = 5;
                    static final int v = 6;
                    static int f(int c){

                    }
                }
                class b extends main{
                    int fa(int c){
                        final int s = 5;
                        if c+s then c := 5;
                    }
                }"""
        expect = "Type Mismatch In Statement: If(BinaryOp(+,Id(c),Id(s)),AssignStmt(Id(c),IntLit(5)))"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_TypeMismatchInStmt_2(self):
        """Simple program: int main() {} """
        input = """class Function {
                        void main(float i; int n){
                            for i := 100 downto n do {
                            }
                        }
                    }
                """
        expect = "Type Mismatch In Statement: For(Id(i),IntLit(100),Id(n),False,Block([],[])])"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_TypeMismatchInStmt_3(self):
        """Simple program: int main() {} """
        input = """class Function {
                        void main(int i; int n){
                            for i := 100.1 downto n do {
                            }
                        }
                    }
                """
        expect = "Type Mismatch In Statement: For(Id(i),FloatLit(100.1),Id(n),False,Block([],[])])"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_TypeMismatchInStmt_4(self):
        """Simple program: int main() {} """
        input = """class Function {
                        void main(int i; float n){
                            for i := 10 downto n do {
                            }
                        }
                    }
                """
        expect = "Type Mismatch In Statement: For(Id(i),IntLit(10),Id(n),False,Block([],[])])"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_TypeMismatchInStmt_5(self):
        """Simple program: int main() {} """
        input = """class Function {
                        void main(int i,n){
                            for i := 10 downto n do {
                                n := 5.6;
                            }
                        }
                    }
                """
        expect = "Type Mismatch In Statement: AssignStmt(Id(n),FloatLit(5.6))"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_TypeMismatchInStmt_6(self):
        """Simple program: int main() {} """
        input = """class Function {
                        static void main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                n := g;
                            }
                        }
                    }
                """
        expect = "Type Mismatch In Statement: AssignStmt(Id(n),Id(g))"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_TypeMismatchInStmt_7(self):
        """Simple program: int main() {} """
        input = Program([ClassDecl(Id("Function"),[MethodDecl(Static(),Id("main"),[VarDecl(Id("i"),IntType()),VarDecl(Id("n"),IntType())],IntType(),Block([VarDecl(Id("g"),FloatType(),FloatLiteral(5.6))],[For(Id("i"),IntLiteral(10),Id("n"),False,Block([],[Assign(Id("n"),IntLiteral(5)),CallStmt(Id("Function"),Id("main"),[IntLiteral(1),IntLiteral(2)])]))]))])])
        expect = "Type Mismatch In Statement: Call(Id(Function),Id(main),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_TypeMismatchInStmt_8(self):
        """Simple program: int main() {} """
        input = """class Function {
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                n := 5;
                                return 4.5;
                            }
                        }
                    }
                """
        expect = "Type Mismatch In Statement: Return(FloatLit(4.5))"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_TypeMismatchInStmt_9(self):
        """Simple program: int main() {} """
        input = Program([ClassDecl(Id("Function"),[MethodDecl(Static(),Id("main"),[VarDecl(Id("i"),IntType()),VarDecl(Id("n"),IntType())],VoidType(),Block([VarDecl(Id("g"),FloatType(),FloatLiteral(5.6))],[For(Id("i"),IntLiteral(10),Id("n"),False,Block([],[Assign(Id("n"),IntLiteral(5)),CallStmt(Id("Function"),Id("main"),[IntLiteral(1),FloatLiteral(2.5)])]))]))])])
        expect = "Type Mismatch In Statement: Call(Id(Function),Id(main),[IntLit(1),FloatLit(2.5)])"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_TypeMismatchInStmt_10(self):
        """Simple program: int main() {} """
        input = Program([ClassDecl(Id("Function"),[MethodDecl(Static(),Id("main"),[VarDecl(Id("i"),IntType()),VarDecl(Id("n"),IntType())],VoidType(),Block([VarDecl(Id("g"),FloatType(),FloatLiteral(5.6))],[For(Id("i"),IntLiteral(10),Id("n"),False,Block([],[Assign(Id("n"),IntLiteral(5)),CallStmt(Id("Function"),Id("main"),[IntLiteral(1)])]))]))])])
        expect = "Type Mismatch In Statement: Call(Id(Function),Id(main),[IntLit(1)])"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_TypeMismatchInExp_1(self):
        """Simple program: int main() {} """
        input = """class Function {
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                                E[3] := 5.5;
                            }
                        }
                    }
                """
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(E),IntLit(3)),FloatLit(5.5))"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_TypeMismatchInExp_2(self):
        """Simple program: int main() {} """
        input = """class Function {
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                                E[3.5] := 5;
                            }
                        }
                    }
                """
        expect = "Type Mismatch In Expression: ArrayCell(Id(E),FloatLit(3.5))"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_TypeMismatchInExp_3(self):
        """Simple program: int main() {} """
        input = """class Function {
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                                i[3] := 5;
                            }
                        }
                    }
                """
        expect = "Type Mismatch In Expression: ArrayCell(Id(i),IntLit(3))"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_TypeMismatchInExp_4(self):
        """Simple program: int main() {} """
        input = """class Function {
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                                E[3] := 5 + 4.4;
                            }
                        }
                    }
                """
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(E),IntLit(3)),BinaryOp(+,IntLit(5),FloatLit(4.4)))"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_TypeMismatchInExp_5(self):
        """Simple program: int main() {} """
        input = """class Function {
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                                E[3] := 5 + true;
                            }
                        }
                    }
                """
        expect = "Type Mismatch In Expression: BinaryOp(+,IntLit(5),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_TypeMismatchInExp_6(self):
        """Simple program: int main() {} """
        input = """class Function {
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                                E[3] := - true;
                            }
                        }
                    }
                """
        expect = "Type Mismatch In Expression: UnaryOp(-,BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_TypeMismatchInExp_7(self):
        """Simple program: int main() {} """
        input = """class Function {
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                                E[3] := 5 \ 4.5;
                            }
                        }
                    }
                """
        expect = "Type Mismatch In Expression: BinaryOp(\,IntLit(5),FloatLit(4.5))"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_TypeMismatchInExp_8(self):
        """Simple program: int main() {} """
        input = """class Function {
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                                E[3] := true * false;
                            }
                        }
                    }
                """
        expect = "Type Mismatch In Expression: BinaryOp(*,BooleanLit(True),BooleanLit(False))"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_TypeMismatchInExp_9(self):
        """Simple program: int main() {} """
        input = """class Function {
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                                E[3] := Function.main();
                            }
                        }
                    }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(Function),Id(main),[])"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_TypeMismatchInExp_10(self):
        """Simple program: int main() {} """
        input = """class Function {
                        int a = 5;
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                                E[3] := Function.main(1,2).a;
                            }
                        }
                    }
                """
        expect = "Type Mismatch In Expression: FieldAccess(CallExpr(Id(Function),Id(main),[IntLit(1),IntLit(2)]),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_TypeMismatchInConst_1(self):
        """Simple program: int main() {} """
        input = """class Function {
                        final int a = 5.5;
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                            }
                        }
                    }
                """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,FloatLit(5.5))"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_TypeMismatchInConst_2(self):
        """Simple program: int main() {} """
        input = """class Function {
                        final int a = true;
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                            }
                        }
                    }
                """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_TypeMismatchInConst_3(self):
        """Simple program: int main() {} """
        input = """class Function {
                        final int a = "buon the";
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                            }
                        }
                    }
                """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,StringLit(buon the))"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_TypeMismatchInConst_4(self):
        """Simple program: int main() {} """
        input = """class Function {
                        final int a = {1,2,3};
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                            }
                        }
                    }
                """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,[IntLit(1),IntLit(2),IntLit(3)])"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_TypeMismatchInConst_5(self):
        """Simple program: int main() {} """
        input = """class Function {
                        static final float a = 5;
                        static final int b = Function.a;
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                            }
                        }
                    }
                """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(b),IntType,FieldAccess(Id(Function),Id(a)))"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_TypeMismatchInConst_6(self):
        """Simple program: int main() {} """
        input = """class Function {
                        static final float a = 5;
                        static final int b = 1;
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                final int c = Function.a;
                                int [3] E = {1,2,3};
                            }
                        }
                    }
                """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(c),IntType,FieldAccess(Id(Function),Id(a)))"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_TypeMismatchInConst_7(self):
        """Simple program: int main() {} """
        input = """class Function {
                        static final float a = 5;
                        static final int b = 1;
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                final int c = Function.a + Function.b;
                                int [3] E = {1,2,3};
                            }
                        }
                    }
                """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(c),IntType,BinaryOp(+,FieldAccess(Id(Function),Id(a)),FieldAccess(Id(Function),Id(b))))"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_TypeMismatchInConst_8(self):
        """Simple program: int main() {} """
        input = """class Function {
                        final float a = 5;
                        static final int b = true;
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                            }
                        }
                    }
                """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(b),IntType,BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_TypeMismatchInConst_9(self):
        """Simple program: int main() {} """
        input = """class Function {
                        final float a = 5;
                        static final int b = {true, false};
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                            }
                        }
                    }
                """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(b),IntType,[BooleanLit(True),BooleanLit(False)])"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_TypeMismatchInConst_10(self):
        """Simple program: int main() {} """
        input = """class Function {
                        final float a = 5;
                        static final int b = "dopham";
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                            }
                        }
                    }
                """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(b),IntType,StringLit(dopham))"
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_brnotInLoop_1(self):
        """Simple program: int main() {} """
        input = """class Function {
                        final float a = 5;
                        static int main(int i,n){
                            float g = 5.6;
                            break;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                            }
                        }
                    }
                """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_brnotInLoop_2(self):
        """Simple program: int main() {} """
        input = """class Function {
                        final float a = 5;
                        static int main(int i,n){
                            float g = 5.6;
                            continue;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                            }
                        }
                    }
                """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_brnotInLoop_3(self):
        """Simple program: int main() {} """
        input = """class Function {
                        final float a = 5;
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                            }
                            break;
                        }
                    }
                """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_brnotInLoop_4(self):
        """Simple program: int main() {} """
        input = """class Function {
                        final float a = 5;
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                            }
                            continue;
                        }
                    }
                """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_brnotInLoop_5(self):
        """Simple program: int main() {} """
        input = """class Function {
                        final float a = 5;
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                            }
                        }
                    }
                    class b extends Function{
                        float j(){
                            break;
                        }
                    }
                """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_brnotInLoop_6(self):
        """Simple program: int main() {} """
        input = """class Function {
                        final float a = 5;
                        static int main(int i,n){
                            float g = 5.6;
                            continue;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                            }
                        }
                    }
                    class b extends Function{
                        float j(){
                            continue;
                        }
                    }
                """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_brnotInLoop_7(self):
        """Simple program: int main() {} """
        input = """class Function {
                        final float a = 5;
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                            }
                            break;
                        }
                    }
                    class b extends Function{
                        float j(){
                            continue;
                        }
                    }
                """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_brnotInLoop_8(self):
        """Simple program: int main() {} """
        input = """class Function {
                        final float a = 5;
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                            }
                            continue;
                        }
                    }
                    class b extends Function{
                        float j(){
                            break;
                        }
                    }
                """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_brnotInLoop_9(self):
        """Simple program: int main() {} """
        input = """class Function {
                        final float a = 5;
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                                break;
                            }
                            
                        }
                    }
                    class b extends Function{
                        float j(){
                            continue;
                        }
                    }
                """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_brnotInLoop_10(self):
        """Simple program: int main() {} """
        input = """class Function {
                        final float a = 5;
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                                continue;
                            }
                            
                        }
                    }
                    class b extends Function{
                        float j(){
                            break;
                        }
                    }
                """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_IllegalConstantExpression_1(self):
        """Simple program: int main() {} """
        input = """class Function {
                        final float a = 5;
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                                final int r = i;
                                continue;
                            }
                            
                        }
                    }
                    class b extends Function{
                        float j(){
                        }
                    }
                """
        expect = "Illegal Constant Expression: Id(i)"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_IllegalConstantExpression_2(self):
        """Simple program: int main() {} """
        input = """class Function {
                        final float a = 5;
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                                final int r;
                                continue;
                            }
                            
                        }
                    }
                    class b extends Function{
                        float j(){
                        }
                    }
                """
        expect = "Illegal Constant Expression: None"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_IllegalConstantExpression_3(self):
        """Simple program: int main() {} """
        input = """class Function {
                        final float a = 5;
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                                final int r = i+n;
                                continue;
                            }
                            
                        }
                    }
                    class b extends Function{
                        float j(){
                        }
                    }
                """
        expect = "Illegal Constant Expression: BinaryOp(+,Id(i),Id(n))"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_IllegalConstantExpression_4(self):
        """Simple program: int main() {} """
        input = """class Function {
                        final float a;
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                                final int r = 7;
                                continue;
                            }
                            
                        }
                    }
                    class b extends Function{
                        float j(){
                        }
                    }
                """
        expect = "Illegal Constant Expression: None"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_IllegalConstantExpression_5(self):
        """Simple program: int main() {} """
        input = """class Function {
                        static int a;
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                                final int r = Function.a;
                                continue;
                            }
                            
                        }
                    }
                    class b extends Function{
                        float j(){
                        }
                    }
                """
        expect = "Illegal Constant Expression: FieldAccess(Id(Function),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_IllegalConstantExpression_6(self):
        """Simple program: int main() {} """
        input = """class Function {
                        final float a = 5;
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                                
                                continue;
                            }
                            
                        }
                    }
                    class b extends Function{
                        final int r;
                        float j(){
                        }
                    }
                """
        expect = "Illegal Constant Expression: None"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_IllegalConstantExpression_7(self):
        """Simple program: int main() {} """
        input = """class Function {
                        final float a = 5;
                        static int i;
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                                
                                continue;
                            }
                            
                        }
                    }
                    class b extends Function{
                        final int r = Function.i;
                        float j(){
                        }
                    }
                """
        expect = "Illegal Constant Expression: FieldAccess(Id(Function),Id(i))"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_IllegalConstantExpression_8(self):
        """Simple program: int main() {} """
        input = """class Function {
                        
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                                final int r = 7;
                                continue;
                            }
                            
                        }
                    }
                    class b extends Function{
                        final int t;
                        float j(){
                        }
                    }
                """
        expect = "Illegal Constant Expression: None"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_IllegalConstantExpression_9(self):
        """Simple program: int main() {} """
        input = """class Function {
                        final float a = 5;
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                                
                                continue;
                            }
                            
                        }
                    }
                    class b extends Function{
                        final int r;
                        float j(){
                        }
                    }
                """
        expect = "Illegal Constant Expression: None"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_IllegalConstantExpression_10(self):
        """Simple program: int main() {} """
        input = """class Function {
                        static int a;
                        static int main(int i,n){
                            float g = 5.6;
                            for i := 10 downto n do {
                                int [3] E = {1,2,3};
                                final int r = 7;
                                continue;
                            }
                            
                        }
                    }
                    class b extends Function{
                        final int t = Function.a;
                        float j(){
                        }
                    }
                """
        expect = "Illegal Constant Expression: FieldAccess(Id(Function),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_IllegalArrayLiteral_1(self):
        """Simple program: int main() {} """
        input = Program([ClassDecl(Id("Function"),[AttributeDecl(Instance(),VarDecl(Id("b"),ArrayType(5,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),FloatLiteral(3.5)]))),MethodDecl(Static(),Id("main"),[VarDecl(Id("i"),IntType()),VarDecl(Id("n"),IntType())],IntType(),Block([],[]))])])
        expect = "Illegal Array Literal: [IntLit(1),IntLit(2),FloatLit(3.5)]"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_IllegalArrayLiteral_2(self):
        """Simple program: int main() {} """
        input = Program([ClassDecl(Id("Function"),[AttributeDecl(Instance(),VarDecl(Id("b"),ArrayType(5,IntType()),ArrayLiteral([IntLiteral(1),BooleanLiteral(False),IntLiteral(2),FloatLiteral(3.5)]))),MethodDecl(Static(),Id("main"),[VarDecl(Id("i"),IntType()),VarDecl(Id("n"),IntType())],IntType(),Block([],[]))])])
        expect = "Illegal Array Literal: [IntLit(1),BooleanLit(False),IntLit(2),FloatLit(3.5)]"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_IllegalArrayLiteral_3(self):
        """Simple program: int main() {} """
        input = Program([ClassDecl(Id("Function"),[AttributeDecl(Instance(),VarDecl(Id("b"),ArrayType(5,IntType()),ArrayLiteral([BooleanLiteral(True),IntLiteral(2)])))])])
        expect = "Illegal Array Literal: [BooleanLit(True),IntLit(2)]"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_IllegalArrayLiteral_4(self):
        """Simple program: int main() {} """
        input = Program([ClassDecl(Id("Function"),[AttributeDecl(Instance(),VarDecl(Id("b"),ArrayType(5,IntType()),ArrayLiteral([FloatLiteral(3.5),BooleanLiteral(False)])))])])
        expect = "Illegal Array Literal: [FloatLit(3.5),BooleanLit(False)]"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_IllegalArrayLiteral_5(self):
        """Simple program: int main() {} """
        input = Program([ClassDecl(Id("Function"),[AttributeDecl(Instance(),VarDecl(Id("b"),ArrayType(5,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),FloatLiteral(3.5)]))),MethodDecl(Static(),Id("main"),[VarDecl(Id("i"),IntType()),VarDecl(Id("n"),IntType())],IntType(),Block([],[]))])])
        expect = "Illegal Array Literal: [IntLit(1),IntLit(2),FloatLit(3.5)]"
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_IllegalArrayLiteral_6(self):
        """Simple program: int main() {} """
        input = Program([ClassDecl(Id("Function"),[AttributeDecl(Instance(),VarDecl(Id("b"),ArrayType(5,IntType()),ArrayLiteral([IntLiteral(1),BooleanLiteral(False),IntLiteral(2),FloatLiteral(3.5)]))),MethodDecl(Static(),Id("main"),[VarDecl(Id("i"),IntType()),VarDecl(Id("n"),IntType())],IntType(),Block([],[]))])])
        expect = "Illegal Array Literal: [IntLit(1),BooleanLit(False),IntLit(2),FloatLit(3.5)]"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_IllegalArrayLiteral_7(self):
        """Simple program: int main() {} """
        input = Program([ClassDecl(Id("Function"),[AttributeDecl(Instance(),VarDecl(Id("b"),ArrayType(5,IntType()),ArrayLiteral([BooleanLiteral(True),IntLiteral(2)])))])])
        expect = "Illegal Array Literal: [BooleanLit(True),IntLit(2)]"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_IllegalArrayLiteral_8(self):
        """Simple program: int main() {} """
        input = Program([ClassDecl(Id("Function"),[AttributeDecl(Instance(),VarDecl(Id("b"),ArrayType(5,IntType()),ArrayLiteral([FloatLiteral(3.5),BooleanLiteral(False)])))])])
        expect = "Illegal Array Literal: [FloatLit(3.5),BooleanLit(False)]"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_IllegalArrayLiteral_9(self):
        """Simple program: int main() {} """
        input = Program([ClassDecl(Id("Function"),[AttributeDecl(Instance(),VarDecl(Id("b"),ArrayType(5,IntType()),ArrayLiteral([BooleanLiteral(True),IntLiteral(2)])))])])
        expect = "Illegal Array Literal: [BooleanLit(True),IntLit(2)]"
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_IllegalArrayLiteral_10(self):
        """Simple program: int main() {} """
        input = Program([ClassDecl(Id("Function"),[AttributeDecl(Instance(),VarDecl(Id("b"),ArrayType(5,IntType()),ArrayLiteral([FloatLiteral(3.5),BooleanLiteral(False)])))])])
        expect = "Illegal Array Literal: [FloatLit(3.5),BooleanLit(False)]"
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_IllegalMemberAccess_1(self):
        """Simple program: int main() {} """
        input = Program([ClassDecl(Id("Function"),[AttributeDecl(Instance(),VarDecl(Id("b"),ArrayType(5,IntType()),ArrayLiteral([FloatLiteral(3.5),BooleanLiteral(False)])))])])
        expect = "Illegal Array Literal: [FloatLit(3.5),BooleanLit(False)]"
        self.assertTrue(TestChecker.test(input,expect,491))

    # def test_diff_numofparam_expr(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn(getInt(4));
    #     }"""
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),List(IntLiteral(4)))"
    #     self.assertTrue(TestChecker.test(input,expect,402))

    # def test_undeclared_function_use_ast(self):
    #     """Simple program: int main() {} """
    #     input = Program([FuncDecl(Id("main"),[],IntType(),Block([],[
    #         CallExpr(Id("foo"),[])]))])
    #     expect = "Undeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,403))

    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],IntType(),Block([],[
    #                 CallExpr(Id("putIntLn"),[
    #                     CallExpr(Id("getInt"),[IntLiteral(4)])
    #                     ])]))])
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),List(IntLiteral(4)))"
    #     self.assertTrue(TestChecker.test(input,expect,404))

    # def test_diff_numofparam_stmt_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],IntType(),Block([],[
    #                 CallExpr(Id("putIntLn"),[])]))])
    #     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),List())"
    #     self.assertTrue(TestChecker.test(input,expect,405))
    