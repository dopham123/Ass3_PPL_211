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
    