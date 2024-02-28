import unittest
from TestUtils import TestAST
from AST import *
                
class ASTGenSuite(unittest.TestCase):
	def test_declare_1(self):
		input = """number hello[3] <- [1,2,3,[3]]
            dynamic world <- [1,2,3]
            number list[5] <- [5,4,3,2,1]
        """
		expect = """Program([VarDecl(Id(hello), ArrayType([3.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), ArrayLit(NumLit(3.0)))), VarDecl(Id(world), None, dynamic, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0))), VarDecl(Id(list), ArrayType([5.0], NumberType), None, ArrayLit(NumLit(5.0), NumLit(4.0), NumLit(3.0), NumLit(2.0), NumLit(1.0)))])"""
		self.assertTrue(TestAST.test(input,expect,301))

	def test2(self):
		input = """number l1[1,3,2] <- [[[[1,2,3,4],[66.5,23.3,12.4,23.e3]],[1e-1, 2e-2, 3e-3]],[0]]
        bool l2[2] <- [[true,false,true,false,true]]
        string l3[20] <- [\"12345\",\"\",\"Saysomething\\n\"]
        dynamic dym <- [1,2,3]
        var abc <- [1,2,3,4]
        """
		expect = """Program([VarDecl(Id(l1), ArrayType([1.0, 3.0, 2.0], NumberType), None, ArrayLit(ArrayLit(ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0)), ArrayLit(NumLit(66.5), NumLit(23.3), NumLit(12.4), NumLit(23000.0))), ArrayLit(NumLit(0.1), NumLit(0.02), NumLit(0.003))), ArrayLit(NumLit(0.0)))), VarDecl(Id(l2), ArrayType([2.0], BoolType), None, ArrayLit(ArrayLit(BooleanLit(True), BooleanLit(False), BooleanLit(True), BooleanLit(False), BooleanLit(True)))), VarDecl(Id(l3), ArrayType([20.0], StringType), None, ArrayLit(StringLit(12345), StringLit(), StringLit(Saysomething\\n))), VarDecl(Id(dym), None, dynamic, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0))), VarDecl(Id(abc), None, var, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0)))])"""
		self.assertTrue(TestAST.test(input,expect,302))

	def test3(self):
		input = """string question <- \"This is the testcase'\"Say hello world'\"\"

        
        """
		expect = """Program([VarDecl(Id(question), StringType, None, StringLit(This is the testcase'"Say hello world'"))])"""
		self.assertTrue(TestAST.test(input,expect,303))

	def test4(self):
		input = """string str <- \"hello world\"
        string String <- \" Is this legit\\'?\"

        var abc <- [1,2,3]
        
        """
		expect = """Program([VarDecl(Id(str), StringType, None, StringLit(hello world)), VarDecl(Id(String), StringType, None, StringLit( Is this legit\\'?)), VarDecl(Id(abc), None, var, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))])"""
		self.assertTrue(TestAST.test(input,expect,304))

	def test5(self):
		input = """func testfunctiondeclare(string a)
        """
		expect = """Program([FuncDecl(Id(testfunctiondeclare), [VarDecl(Id(a), StringType, None, None)], None)])"""
		self.assertTrue(TestAST.test(input,expect,305))

	def test6(self):
		input = """func unclosedfunc(number b, string c)
                begin 
                end
        """
		expect = """Program([FuncDecl(Id(unclosedfunc), [VarDecl(Id(b), NumberType, None, None), VarDecl(Id(c), StringType, None, None)], Block([]))])"""
		self.assertTrue(TestAST.test(input,expect,306))

	def test7(self):
		input = """func test()
                begin
                    bbbllll(a,b) 
                end
        """
		expect = """Program([FuncDecl(Id(test), [], Block([CallStmt(Id(bbbllll), [Id(a), Id(b)])]))])"""
		self.assertTrue(TestAST.test(input,expect,307))

	def test8(self):
		input = """func main(number a[10,10], bool b[10,20])
                return 1e-3
        """
		expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), ArrayType([10.0, 10.0], NumberType), None, None), VarDecl(Id(b), ArrayType([10.0, 20.0], BoolType), None, None)], Return(NumLit(0.001)))])"""
		self.assertTrue(TestAST.test(input,expect,308))

	def test9(self):
		input = """func main() begin
            string a <- "Hello World"
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), StringType, None, StringLit(Hello World))]))])"""
		self.assertTrue(TestAST.test(input,expect,309))

	def test10(self):
		input = """func main() begin
            number a <-10e-3
            number b <- 10e-4
            bool c[1,2,3] <- [[1,2,3],2,3,4]
        
        end 


        """
		expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, NumLit(0.01)), VarDecl(Id(b), NumberType, None, NumLit(0.001)), VarDecl(Id(c), ArrayType([1.0, 2.0, 3.0], BoolType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), NumLit(2.0), NumLit(3.0), NumLit(4.0)))]))])"""
		self.assertTrue(TestAST.test(input,expect,310))

	def test11(self):
		input = """func main() begin
            number a <- [1,2,3]
        end 

        func t1() return "Hello World"

        func t2() begin

        end

        func t3()
        """
		expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))])), FuncDecl(Id(t1), [], Return(StringLit(Hello World))), FuncDecl(Id(t2), [], Block([])), FuncDecl(Id(t3), [], None)])"""
		self.assertTrue(TestAST.test(input,expect,311))

	def test12(self):
		input = """func main() begin
        begin
        end
        end 
        func test() return 5.
        """
		expect = """Program([FuncDecl(Id(main), [], Block([Block([])])), FuncDecl(Id(test), [], Return(NumLit(5.0)))])"""
		self.assertTrue(TestAST.test(input,expect,312))

	def test13(self):
		input = """func main() 
        begin
            foo(1,2,f1(2,3,f2(3,4)))
        end 
        """
		expect = """Program([FuncDecl(Id(main), [], Block([CallStmt(Id(foo), [NumLit(1.0), NumLit(2.0), CallExpr(Id(f1), [NumLit(2.0), NumLit(3.0), CallExpr(Id(f2), [NumLit(3.0), NumLit(4.0)])])])]))])"""
		self.assertTrue(TestAST.test(input,expect,313))

	def test14(self):
		input = """func main() 
        begin
            bool b <- true and true or true and not false
            printLine(b)
        end 
        """
		expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(b), BoolType, None, BinaryOp(and, BinaryOp(or, BinaryOp(and, BooleanLit(True), BooleanLit(True)), BooleanLit(True)), UnaryOp(not, BooleanLit(False)))), CallStmt(Id(printLine), [Id(b)])]))])"""
		self.assertTrue(TestAST.test(input,expect,314))

	def test15(self):
		input = """func main() begin

            bool b <- true and (false and true)


            bool c <- b - true
            printLine(c)
        end 
        """
		expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(b), BoolType, None, BinaryOp(and, BooleanLit(True), BinaryOp(and, BooleanLit(False), BooleanLit(True)))), VarDecl(Id(c), BoolType, None, BinaryOp(-, Id(b), BooleanLit(True))), CallStmt(Id(printLine), [Id(c)])]))])"""
		self.assertTrue(TestAST.test(input,expect,315))

	def test16(self):
		input = """dynamic global
        var a <- "Say something"
        """
		expect = """Program([VarDecl(Id(global), None, dynamic, None), VarDecl(Id(a), None, var, StringLit(Say something))])"""
		self.assertTrue(TestAST.test(input,expect,316))

	def test17(self):
		input = """number a <- 1000
        """
		expect = """Program([VarDecl(Id(a), NumberType, None, NumLit(1000.0))])"""
		self.assertTrue(TestAST.test(input,expect,317))

	def test18(self):
		input = """func main(number a[1,2,3])
        begin 
            f1(a, b) 
            f2(a) 
        end
        """
		expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), ArrayType([1.0, 2.0, 3.0], NumberType), None, None)], Block([CallStmt(Id(f1), [Id(a), Id(b)]), CallStmt(Id(f2), [Id(a)])]))])"""
		self.assertTrue(TestAST.test(input,expect,318))

	def test19(self):
		input = """func main(string a)
        begin 
            f1(b)
            f2(a) 
        end
        """
		expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), StringType, None, None)], Block([CallStmt(Id(f1), [Id(b)]), CallStmt(Id(f2), [Id(a)])]))])"""
		self.assertTrue(TestAST.test(input,expect,319))

	def test20(self):
		input = """func main()
        begin 
            number c[1,2,3] <- [1,2,3]
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(c), ArrayType([1.0, 2.0, 3.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))]))])"""
		self.assertTrue(TestAST.test(input,expect,320))

	def test21(self):
		input = """func main()
        begin 
            b <- -1000E-10
            d <- 1 * 2 % 10 / 56.4E-2 + e
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(b), UnaryOp(-, NumLit(1e-07))), AssignStmt(Id(d), BinaryOp(+, BinaryOp(/, BinaryOp(%, BinaryOp(*, NumLit(1.0), NumLit(2.0)), NumLit(10.0)), NumLit(0.564)), Id(e)))]))])"""
		self.assertTrue(TestAST.test(input,expect,321))

	def test22(self):
		input = """func main() begin 
            number a <- "string"
            main()
            main()


            a <- numb(1,2,3, "Hello World")
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, StringLit(string)), CallStmt(Id(main), []), CallStmt(Id(main), []), AssignStmt(Id(a), CallExpr(Id(numb), [NumLit(1.0), NumLit(2.0), NumLit(3.0), StringLit(Hello World)]))]))])"""
		self.assertTrue(TestAST.test(input,expect,322))

	def test23(self):
		input = """func main() begin 

            t <- (60 - 40 + (array[100,101,102,103])* 20)
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(t), BinaryOp(+, BinaryOp(-, NumLit(60.0), NumLit(40.0)), BinaryOp(*, ArrayCell(Id(array), [NumLit(100.0), NumLit(101.0), NumLit(102.0), NumLit(103.0)]), NumLit(20.0))))]))])"""
		self.assertTrue(TestAST.test(input,expect,323))

	def test24(self):
		input = """func main() begin 
            c <- a...b
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(c), BinaryOp(..., Id(a), Id(b)))]))])"""
		self.assertTrue(TestAST.test(input,expect,324))

	def test25(self):
		input = """func main() begin 
            IF <- 1
            FoR <- "This string is for loop"
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(IF), NumLit(1.0)), AssignStmt(Id(FoR), StringLit(This string is for loop))]))])"""
		self.assertTrue(TestAST.test(input,expect,325))

	def test26(self):
		input = """func main() begin 
            for i until ("saysomething" == "a") by 10
                printLine("hello world")
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(==, StringLit(saysomething), StringLit(a)), NumLit(10.0), CallStmt(Id(printLine), [StringLit(hello world)]))]))])"""
		self.assertTrue(TestAST.test(input,expect,326))

	def test27(self):
		input = """func main() begin 
            for numb until numb < 0 by -1
            begin
                a[foo(2,3) + 3] <- (a[foo(2,3) + 3] + num) % ((2))
            end
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([For(Id(numb), BinaryOp(<, Id(numb), NumLit(0.0)), UnaryOp(-, NumLit(1.0)), Block([AssignStmt(ArrayCell(Id(a), [BinaryOp(+, CallExpr(Id(foo), [NumLit(2.0), NumLit(3.0)]), NumLit(3.0))]), BinaryOp(%, BinaryOp(+, ArrayCell(Id(a), [BinaryOp(+, CallExpr(Id(foo), [NumLit(2.0), NumLit(3.0)]), NumLit(3.0))]), Id(num)), NumLit(2.0)))]))]))])"""
		self.assertTrue(TestAST.test(input,expect,327))

	def test28(self):
		input = """func main() 
        begin 
            for i until i != 1000 by 2
                if (i/a=b) printLine(i)
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(!=, Id(i), NumLit(1000.0)), NumLit(2.0), If((BinaryOp(=, BinaryOp(/, Id(i), Id(a)), Id(b)), CallStmt(Id(printLine), [Id(i)])), [], None))]))])"""
		self.assertTrue(TestAST.test(input,expect,328))

	def test29(self):
		input = """func main() 
        begin 
            for a until foo(2,3)[temp1(20)] > 1000 by 5.3E-3 
            

            begin
                begin
                    break
                    continue
                end
            end
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([For(Id(a), BinaryOp(>, ArrayCell(CallExpr(Id(foo), [NumLit(2.0), NumLit(3.0)]), [CallExpr(Id(temp1), [NumLit(20.0)])]), NumLit(1000.0)), NumLit(0.0053), Block([Block([Break, Continue])]))]))])"""
		self.assertTrue(TestAST.test(input,expect,329))

	def test30(self):
		input = """func main() begin 
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([]))])"""
		self.assertTrue(TestAST.test(input,expect,330))

	def test31(self):
		input = """func error() begin 
            for i until (num1*num2=0) by 10
            begin
            end
        end
        """
		expect = """Program([FuncDecl(Id(error), [], Block([For(Id(i), BinaryOp(=, BinaryOp(*, Id(num1), Id(num2)), NumLit(0.0)), NumLit(10.0), Block([]))]))])"""
		self.assertTrue(TestAST.test(input,expect,331))

	def test32(self):
		input = """func main() begin
            for i until true by 1 return 0
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([For(Id(i), BooleanLit(True), NumLit(1.0), Return(NumLit(0.0)))]))])"""
		self.assertTrue(TestAST.test(input,expect,332))

	def test33(self):
		input = """func main() 
        begin
            for i until (temp1*temp2%(temp3-temp4)=temp5) by 1e-3 
            begin
                if (fee()) then<-5
                elif (fee()) eles<-10
                else i<-i/2
            end
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(=, BinaryOp(%, BinaryOp(*, Id(temp1), Id(temp2)), BinaryOp(-, Id(temp3), Id(temp4))), Id(temp5)), NumLit(0.001), Block([If((CallExpr(Id(fee), []), AssignStmt(Id(then), NumLit(5.0))), [(CallExpr(Id(fee), []), AssignStmt(Id(eles), NumLit(10.0)))], AssignStmt(Id(i), BinaryOp(/, Id(i), NumLit(2.0))))]))]))])"""
		self.assertTrue(TestAST.test(input,expect,333))

	def test34(self):
		input = """func main() begin
            for i until 1 by 1 begin
                begin
                    begin
                        begin
                            if (i%2=0) i<-i+1
                            elif (true) begin 
                            end
                            elif (true) begin
                            end
                            else i<-i+1
                        end
                    end
                end
            end
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([For(Id(i), NumLit(1.0), NumLit(1.0), Block([Block([Block([Block([If((BinaryOp(=, BinaryOp(%, Id(i), NumLit(2.0)), NumLit(0.0)), AssignStmt(Id(i), BinaryOp(+, Id(i), NumLit(1.0)))), [(BooleanLit(True), Block([])), (BooleanLit(True), Block([]))], AssignStmt(Id(i), BinaryOp(+, Id(i), NumLit(1.0))))])])])]))]))])"""
		self.assertTrue(TestAST.test(input,expect,334))

	def test35(self):
		input = """func main() begin
        end
        func test(number a, number b[12]) begin
            for i until i<10 by 1 print(i)
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([])), FuncDecl(Id(test), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), ArrayType([12.0], NumberType), None, None)], Block([For(Id(i), BinaryOp(<, Id(i), NumLit(10.0)), NumLit(1.0), CallStmt(Id(print), [Id(i)]))]))])"""
		self.assertTrue(TestAST.test(input,expect,335))

	def test36(self):
		input = """func main() begin
            for i until i<0 by funcfunc()
                i <- i-1
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(<, Id(i), NumLit(0.0)), CallExpr(Id(funcfunc), []), AssignStmt(Id(i), BinaryOp(-, Id(i), NumLit(1.0))))]))])"""
		self.assertTrue(TestAST.test(input,expect,336))

	def test37(self):
		input = """func lossComponent() begin
            for i until 3 by 1
            begin 
            end
        end
        """
		expect = """Program([FuncDecl(Id(lossComponent), [], Block([For(Id(i), NumLit(3.0), NumLit(1.0), Block([]))]))])"""
		self.assertTrue(TestAST.test(input,expect,337))

	def test38(self):
		input = """func main() 
        begin
            for i until hi by funcfunc()
            begin
            end
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([For(Id(i), Id(hi), CallExpr(Id(funcfunc), []), Block([]))]))])"""
		self.assertTrue(TestAST.test(input,expect,338))

	def test39(self):
		input = """func main() begin
            for i until i < noneed by 1
            begin
            end
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(<, Id(i), Id(noneed)), NumLit(1.0), Block([]))]))])"""
		self.assertTrue(TestAST.test(input,expect,339))

	def test40(self):
		input = """func main() 
        begin
            for i until i < foo(2,3) by 1
                break
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(<, Id(i), CallExpr(Id(foo), [NumLit(2.0), NumLit(3.0)])), NumLit(1.0), Break)]))])"""
		self.assertTrue(TestAST.test(input,expect,340))

	def test41(self):
		input = """func main() begin
            if (i = -1) break
            elif (i = 1) continue
            else continue
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([If((BinaryOp(=, Id(i), UnaryOp(-, NumLit(1.0))), Break), [(BinaryOp(=, Id(i), NumLit(1.0)), Continue)], Continue)]))])"""
		self.assertTrue(TestAST.test(input,expect,341))

	def test42(self):
		input = """func main() begin
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([]))])"""
		self.assertTrue(TestAST.test(input,expect,342))

	def test43(self):
		input = """func main() begin
                return t1 and t2
        end
        func t1(number a, number b) return 

        func t2(bool c) begin
            begin
                begin
                    return abc
                end
            end
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([Return(BinaryOp(and, Id(t1), Id(t2)))])), FuncDecl(Id(t1), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Return()), FuncDecl(Id(t2), [VarDecl(Id(c), BoolType, None, None)], Block([Block([Block([Return(Id(abc))])])]))])"""
		self.assertTrue(TestAST.test(input,expect,343))

	def test44(self):
		input = """
        func temp(bool a[1,2,3], string b[1,2,3]) return nothing__
        func temp2() return temp(temp())
        """
		expect = """Program([FuncDecl(Id(temp), [VarDecl(Id(a), ArrayType([1.0, 2.0, 3.0], BoolType), None, None), VarDecl(Id(b), ArrayType([1.0, 2.0, 3.0], StringType), None, None)], Return(Id(nothing__))), FuncDecl(Id(temp2), [], Return(CallExpr(Id(temp), [CallExpr(Id(temp), [])])))])"""
		self.assertTrue(TestAST.test(input,expect,344))

	def test45(self):
		input = """func main() begin
            number i <- 100
            number thres <- 100
            for i until i < thres by 10
                printLine(i)
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), NumberType, None, NumLit(100.0)), VarDecl(Id(thres), NumberType, None, NumLit(100.0)), For(Id(i), BinaryOp(<, Id(i), Id(thres)), NumLit(10.0), CallStmt(Id(printLine), [Id(i)]))]))])"""
		self.assertTrue(TestAST.test(input,expect,345))

	def test46(self):
		input = """
        func main() return a/b = 2/1
        """
		expect = """Program([FuncDecl(Id(main), [], Return(BinaryOp(=, BinaryOp(/, Id(a), Id(b)), BinaryOp(/, NumLit(2.0), NumLit(1.0)))))])"""
		self.assertTrue(TestAST.test(input,expect,346))

	def test47(self):
		input = """
        func main() begin
            for i until i <= arr_length() by 1 begin
                print(output)
            end
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(<=, Id(i), CallExpr(Id(arr_length), [])), NumLit(1.0), Block([CallStmt(Id(print), [Id(output)])]))]))])"""
		self.assertTrue(TestAST.test(input,expect,347))

	def test48(self):
		input = """
        func error() begin
            for a until a < 100 by 1 push(a)
        end
        """
		expect = """Program([FuncDecl(Id(error), [], Block([For(Id(a), BinaryOp(<, Id(a), NumLit(100.0)), NumLit(1.0), CallStmt(Id(push), [Id(a)]))]))])"""
		self.assertTrue(TestAST.test(input,expect,348))

	def test49(self):
		input = """
        func main() begin
            number s <- calS(r)
        end

        func calS(number r, number pi) return 2*pi*r*r
        """
		expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(s), NumberType, None, CallExpr(Id(calS), [Id(r)]))])), FuncDecl(Id(calS), [VarDecl(Id(r), NumberType, None, None), VarDecl(Id(pi), NumberType, None, None)], Return(BinaryOp(*, BinaryOp(*, BinaryOp(*, NumLit(2.0), Id(pi)), Id(r)), Id(r))))])"""
		self.assertTrue(TestAST.test(input,expect,349))

	def test50(self):
		input = """func main() begin
            if (a()) return 0
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([If((CallExpr(Id(a), []), Return(NumLit(0.0))), [], None)]))])"""
		self.assertTrue(TestAST.test(input,expect,350))

	def test51(self):
		input = """func t1() begin
            for i until int() by 2
            begin
            end
        end
        """
		expect = """Program([FuncDecl(Id(t1), [], Block([For(Id(i), CallExpr(Id(int), []), NumLit(2.0), Block([]))]))])"""
		self.assertTrue(TestAST.test(input,expect,351))

	def test52(self):
		input = """func nothing() begin
            if (saysomething) return 0
        end
        """
		expect = """Program([FuncDecl(Id(nothing), [], Block([If((Id(saysomething), Return(NumLit(0.0))), [], None)]))])"""
		self.assertTrue(TestAST.test(input,expect,352))

	def test53(self):
		input = """func main() begin
            if (x < 5) 
                if (y < 10) print("Say hello")
                    if (true)
                        if(true) a()
            else print("Say no hello")
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([If((BinaryOp(<, Id(x), NumLit(5.0)), If((BinaryOp(<, Id(y), NumLit(10.0)), CallStmt(Id(print), [StringLit(Say hello)])), [], None)), [], None), If((BooleanLit(True), If((BooleanLit(True), CallStmt(Id(a), [])), [], CallStmt(Id(print), [StringLit(Say no hello)]))), [], None)]))])"""
		self.assertTrue(TestAST.test(input,expect,353))

	def test54(self):
		input = """func main() begin
            for i until i < 10 by 1
                for j until j < 10 by 1
                    print("*")
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(<, Id(i), NumLit(10.0)), NumLit(1.0), For(Id(j), BinaryOp(<, Id(j), NumLit(10.0)), NumLit(1.0), CallStmt(Id(print), [StringLit(*)])))]))])"""
		self.assertTrue(TestAST.test(input,expect,354))

	def test55(self):
		input = """func main() begin
            begin
                main()       
            end
            begin
                main()
            end
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([Block([CallStmt(Id(main), [])]), Block([CallStmt(Id(main), [])])]))])"""
		self.assertTrue(TestAST.test(input,expect,355))

	def test56(self):
		input = """func main() begin
            string s <- \"abc\\n\\t'\"\"
            string ss <- \"123.\\t\\b\"
            s <- s...ss
            s <- s...ss
            return s
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(s), StringType, None, StringLit(abc\\n\\t'")), VarDecl(Id(ss), StringType, None, StringLit(123.\\t\\b)), AssignStmt(Id(s), BinaryOp(..., Id(s), Id(ss))), AssignStmt(Id(s), BinaryOp(..., Id(s), Id(ss))), Return(Id(s))]))])"""
		self.assertTrue(TestAST.test(input,expect,356))

	def test57(self):
		input = """func main() 
        begin
            begin
                return 2
            end
            begin
                return 1
            end
        end

        func factorial(number n) begin
            if (n = 0) return 1
            else return n * factorial(n-1)
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([Block([Return(NumLit(2.0))]), Block([Return(NumLit(1.0))])])), FuncDecl(Id(factorial), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(=, Id(n), NumLit(0.0)), Return(NumLit(1.0))), [], Return(BinaryOp(*, Id(n), CallExpr(Id(factorial), [BinaryOp(-, Id(n), NumLit(1.0))]))))]))])"""
		self.assertTrue(TestAST.test(input,expect,357))

	def test58(self):
		input = """
        func main() 
        begin
            for i until i < 0 by 1
                if (num() > 1) inc(i)
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(<, Id(i), NumLit(0.0)), NumLit(1.0), If((BinaryOp(>, CallExpr(Id(num), []), NumLit(1.0)), CallStmt(Id(inc), [Id(i)])), [], None))]))])"""
		self.assertTrue(TestAST.test(input,expect,358))

	def test59(self):
		input = """ number a <- 1
        func inc(number a) return a+1
        """
		expect = """Program([VarDecl(Id(a), NumberType, None, NumLit(1.0)), FuncDecl(Id(inc), [VarDecl(Id(a), NumberType, None, None)], Return(BinaryOp(+, Id(a), NumLit(1.0))))])"""
		self.assertTrue(TestAST.test(input,expect,359))

	def test60(self):
		input = """ func main() return

        func function() begin
            foo(a,b,temp()[2,foo(function(2,3))])
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Return()), FuncDecl(Id(function), [], Block([CallStmt(Id(foo), [Id(a), Id(b), ArrayCell(CallExpr(Id(temp), []), [NumLit(2.0), CallExpr(Id(foo), [CallExpr(Id(function), [NumLit(2.0), NumLit(3.0)])])])])]))])"""
		self.assertTrue(TestAST.test(input,expect,360))

	def test61(self):
		input = """ func main() return function
        func function() begin
            for a until (n1 + n2)*2 = 10 by 2
            begin
                foo[1,2,3] <- a[foo(1)] + n1 * n2
                begin
                    if (true) printline("a")
                    else printline("b")
                end
            end
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Return(Id(function))), FuncDecl(Id(function), [], Block([For(Id(a), BinaryOp(=, BinaryOp(*, BinaryOp(+, Id(n1), Id(n2)), NumLit(2.0)), NumLit(10.0)), NumLit(2.0), Block([AssignStmt(ArrayCell(Id(foo), [NumLit(1.0), NumLit(2.0), NumLit(3.0)]), BinaryOp(+, ArrayCell(Id(a), [CallExpr(Id(foo), [NumLit(1.0)])]), BinaryOp(*, Id(n1), Id(n2)))), Block([If((BooleanLit(True), CallStmt(Id(printline), [StringLit(a)])), [], CallStmt(Id(printline), [StringLit(b)]))])]))]))])"""
		self.assertTrue(TestAST.test(input,expect,361))

	def test62(self):
		input = """func main()
        begin
            for i until i < 0 by i + 1



                begin
                    print("Hello World")
                    print("Say something")
                end


                
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(<, Id(i), NumLit(0.0)), BinaryOp(+, Id(i), NumLit(1.0)), Block([CallStmt(Id(print), [StringLit(Hello World)]), CallStmt(Id(print), [StringLit(Say something)])]))]))])"""
		self.assertTrue(TestAST.test(input,expect,362))

	def test63(self):
		input = """func main()
        begin
            begin
                for i until i >= size(arr) by 1
                    print(ext(arr[i],arr[i]))
            end
        end

        func extract(string a, number b)
            return a[b]
        """
		expect = """Program([FuncDecl(Id(main), [], Block([Block([For(Id(i), BinaryOp(>=, Id(i), CallExpr(Id(size), [Id(arr)])), NumLit(1.0), CallStmt(Id(print), [CallExpr(Id(ext), [ArrayCell(Id(arr), [Id(i)]), ArrayCell(Id(arr), [Id(i)])])]))])])), FuncDecl(Id(extract), [VarDecl(Id(a), StringType, None, None), VarDecl(Id(b), NumberType, None, None)], Return(ArrayCell(Id(a), [Id(b)])))])"""
		self.assertTrue(TestAST.test(input,expect,363))

	def test64(self):
		input = """func main() 
        
        
        begin                
            funccall(i, test)                
        end

        func funccall(number i, number test) 
        
        begin

            if (i = test) return true
                elif (i > test) return false 
                    elif ((i<test) and (test%i=0)) return true
                        else return false

        end

        """
		expect = """Program([FuncDecl(Id(main), [], Block([CallStmt(Id(funccall), [Id(i), Id(test)])])), FuncDecl(Id(funccall), [VarDecl(Id(i), NumberType, None, None), VarDecl(Id(test), NumberType, None, None)], Block([If((BinaryOp(=, Id(i), Id(test)), Return(BooleanLit(True))), [(BinaryOp(>, Id(i), Id(test)), Return(BooleanLit(False))), (BinaryOp(and, BinaryOp(<, Id(i), Id(test)), BinaryOp(=, BinaryOp(%, Id(test), Id(i)), NumLit(0.0))), Return(BooleanLit(True)))], Return(BooleanLit(False)))]))])"""
		self.assertTrue(TestAST.test(input,expect,364))

	def test65(self):
		input = """func main() return
        """
		expect = """Program([FuncDecl(Id(main), [], Return())])"""
		self.assertTrue(TestAST.test(input,expect,365))

	def test66(self):
		input = """func main() return f1(n1) and f2(n2) or f3(n3)
        func f1(number a)
        func f1(number a) begin
            return a
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Return(BinaryOp(or, BinaryOp(and, CallExpr(Id(f1), [Id(n1)]), CallExpr(Id(f2), [Id(n2)])), CallExpr(Id(f3), [Id(n3)])))), FuncDecl(Id(f1), [VarDecl(Id(a), NumberType, None, None)], None), FuncDecl(Id(f1), [VarDecl(Id(a), NumberType, None, None)], Block([Return(Id(a))]))])"""
		self.assertTrue(TestAST.test(input,expect,366))

	def test67(self):
		input = """func f1() return f1(f1(f1(f1(n1))))
        """
		expect = """Program([FuncDecl(Id(f1), [], Return(CallExpr(Id(f1), [CallExpr(Id(f1), [CallExpr(Id(f1), [CallExpr(Id(f1), [Id(n1)])])])])))])"""
		self.assertTrue(TestAST.test(input,expect,367))

	def test68(self):
		input = """func main() 


        begin
            number c
            c<-au*bc+100/1000

            return c[3]
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(c), NumberType, None, None), AssignStmt(Id(c), BinaryOp(+, BinaryOp(*, Id(au), Id(bc)), BinaryOp(/, NumLit(100.0), NumLit(1000.0)))), Return(ArrayCell(Id(c), [NumLit(3.0)]))]))])"""
		self.assertTrue(TestAST.test(input,expect,368))

	def test69(self):
		input = """func main() begin
            number b <- 1
            begin
            end
            begin
            end
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(b), NumberType, None, NumLit(1.0)), Block([]), Block([])]))])"""
		self.assertTrue(TestAST.test(input,expect,369))

	def test70(self):
		input = """


        func main() begin
            number numbers[5] <- [num[1],[2],[3]]
            print(\"We have array number: \",result)
        end 
        """
		expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(numbers), ArrayType([5.0], NumberType), None, ArrayLit(ArrayCell(Id(num), [NumLit(1.0)]), ArrayLit(NumLit(2.0)), ArrayLit(NumLit(3.0)))), CallStmt(Id(print), [StringLit(We have array number: ), Id(result)])]))])"""
		self.assertTrue(TestAST.test(input,expect,370))

	def test71(self):
		input = """func testExpr() begin
            if ((a <= a) and (b!= b) or (d > d )) x <- 1
        end
        """
		expect = """Program([FuncDecl(Id(testExpr), [], Block([If((BinaryOp(or, BinaryOp(and, BinaryOp(<=, Id(a), Id(a)), BinaryOp(!=, Id(b), Id(b))), BinaryOp(>, Id(d), Id(d))), AssignStmt(Id(x), NumLit(1.0))), [], None)]))])"""
		self.assertTrue(TestAST.test(input,expect,371))

	def test72(self):
		input = """func m1() begin
        begin
            saysomething()
            end
            begin
            helloworld()
        end
        end

        """
		expect = """Program([FuncDecl(Id(m1), [], Block([Block([CallStmt(Id(saysomething), [])]), Block([CallStmt(Id(helloworld), [])])]))])"""
		self.assertTrue(TestAST.test(input,expect,372))

	def test73(self):
		input = """func main() begin
            a <- -1-b-s-2-3-s*2*3*4/1/2/3
        end

        """
		expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(a), BinaryOp(-, BinaryOp(-, BinaryOp(-, BinaryOp(-, BinaryOp(-, UnaryOp(-, NumLit(1.0)), Id(b)), Id(s)), NumLit(2.0)), NumLit(3.0)), BinaryOp(/, BinaryOp(/, BinaryOp(/, BinaryOp(*, BinaryOp(*, BinaryOp(*, Id(s), NumLit(2.0)), NumLit(3.0)), NumLit(4.0)), NumLit(1.0)), NumLit(2.0)), NumLit(3.0))))]))])"""
		self.assertTrue(TestAST.test(input,expect,373))

	def test74(self):
		input = """func my_func() 
        
        begin
            foo(my_func, a/b, not my_func())
        end

        """
		expect = """Program([FuncDecl(Id(my_func), [], Block([CallStmt(Id(foo), [Id(my_func), BinaryOp(/, Id(a), Id(b)), UnaryOp(not, CallExpr(Id(my_func), []))])]))])"""
		self.assertTrue(TestAST.test(input,expect,374))

	def test75(self):
		input = """func my_func() 
        
        
        begin

            x <- a[b[2],c[2]]
            a[[b[1 + c]]] <- x
        end

        """
		expect = """Program([FuncDecl(Id(my_func), [], Block([AssignStmt(Id(x), ArrayCell(Id(a), [ArrayCell(Id(b), [NumLit(2.0)]), ArrayCell(Id(c), [NumLit(2.0)])])), AssignStmt(ArrayCell(Id(a), [ArrayLit(ArrayCell(Id(b), [BinaryOp(+, NumLit(1.0), Id(c))]))]), Id(x))]))])"""
		self.assertTrue(TestAST.test(input,expect,375))

	def test76(self):
		input = """func main() begin
            var x <- readInteger()
            for x until x < 0 by -1 begin
                printInteger(res)
            end
        end

        """
		expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(x), None, var, CallExpr(Id(readInteger), [])), For(Id(x), BinaryOp(<, Id(x), NumLit(0.0)), UnaryOp(-, NumLit(1.0)), Block([CallStmt(Id(printInteger), [Id(res)])]))]))])"""
		self.assertTrue(TestAST.test(input,expect,376))

	def test77(self):
		input = """func my_func() begin
            x <- ((("Say"..." ")..."Something!")..."\\\\!!!\\\\")
        end
        """
		expect = """Program([FuncDecl(Id(my_func), [], Block([AssignStmt(Id(x), BinaryOp(..., BinaryOp(..., BinaryOp(..., StringLit(Say), StringLit( )), StringLit(Something!)), StringLit(\\\\!!!\\\\)))]))])"""
		self.assertTrue(TestAST.test(input,expect,377))

	def test78(self):
		input = """func funct(number _, number __) begin
            s <- __()
        end

        func main() begin
            a <- _funct + __funct
        end

        """
		expect = """Program([FuncDecl(Id(funct), [VarDecl(Id(_), NumberType, None, None), VarDecl(Id(__), NumberType, None, None)], Block([AssignStmt(Id(s), CallExpr(Id(__), []))])), FuncDecl(Id(main), [], Block([AssignStmt(Id(a), BinaryOp(+, Id(_funct), Id(__funct)))]))])"""
		self.assertTrue(TestAST.test(input,expect,378))

	def test79(self):
		input = """func main() begin
            aba1232 <- fun()
        end

        """
		expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(aba1232), CallExpr(Id(fun), []))]))])"""
		self.assertTrue(TestAST.test(input,expect,379))

	def test80(self):
		input = """
        func main() begin
            ## this function to let program start
            ## This will help program run
            number a <- 1
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, NumLit(1.0))]))])"""
		self.assertTrue(TestAST.test(input,expect,380))

	def test81(self):
		input = """number a<-main(50)
        bool a <- main(a) + main(a*2+main(a))
        func main(number a) begin
            return a*2+1
        end
        """
		expect = """Program([VarDecl(Id(a), NumberType, None, CallExpr(Id(main), [NumLit(50.0)])), VarDecl(Id(a), BoolType, None, BinaryOp(+, CallExpr(Id(main), [Id(a)]), CallExpr(Id(main), [BinaryOp(+, BinaryOp(*, Id(a), NumLit(2.0)), CallExpr(Id(main), [Id(a)]))]))), FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None)], Block([Return(BinaryOp(+, BinaryOp(*, Id(a), NumLit(2.0)), NumLit(1.0)))]))])"""
		self.assertTrue(TestAST.test(input,expect,381))

	def test82(self):
		input = """number a<-fun(50)
        func fun(number a)
        """
		expect = """Program([VarDecl(Id(a), NumberType, None, CallExpr(Id(fun), [NumLit(50.0)])), FuncDecl(Id(fun), [VarDecl(Id(a), NumberType, None, None)], None)])"""
		self.assertTrue(TestAST.test(input,expect,382))

	def test83(self):
		input = """func main(number a) begin
            begin
                return foo[5,foo(123)]
            end
        end
        """
		expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None)], Block([Block([Return(ArrayCell(Id(foo), [NumLit(5.0), CallExpr(Id(foo), [NumLit(123.0)])]))])]))])"""
		self.assertTrue(TestAST.test(input,expect,383))

	def test84(self):
		input = """func main() begin
        printLine("----")
        printLine(fun())
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([CallStmt(Id(printLine), [StringLit(----)]), CallStmt(Id(printLine), [CallExpr(Id(fun), [])])]))])"""
		self.assertTrue(TestAST.test(input,expect,384))

	def test85(self):
		input = """func main() begin
            number a <- true
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, BooleanLit(True))]))])"""
		self.assertTrue(TestAST.test(input,expect,385))

	def test86(self):
		input = """var declaration <- foo(123) 

        """
		expect = """Program([VarDecl(Id(declaration), None, var, CallExpr(Id(foo), [NumLit(123.0)]))])"""
		self.assertTrue(TestAST.test(input,expect,386))

	def test87(self):
		input = """func main() begin
            for i until i >= 2 by 1 
            begin
                for j until j >= 3 by 1 
                begin
                    begin
                        return 0
                    end
                end
            end
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(>=, Id(i), NumLit(2.0)), NumLit(1.0), Block([For(Id(j), BinaryOp(>=, Id(j), NumLit(3.0)), NumLit(1.0), Block([Block([Return(NumLit(0.0))])]))]))]))])"""
		self.assertTrue(TestAST.test(input,expect,387))

	def test88(self):
		input = """func main() begin
            var a <- [1,2,3]
            for a until len_a >= 10 by 0 begin
                arr[0] <- x
            end
            arr[a[1]] <- x
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, var, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0))), For(Id(a), BinaryOp(>=, Id(len_a), NumLit(10.0)), NumLit(0.0), Block([AssignStmt(ArrayCell(Id(arr), [NumLit(0.0)]), Id(x))])), AssignStmt(ArrayCell(Id(arr), [ArrayCell(Id(a), [NumLit(1.0)])]), Id(x))]))])"""
		self.assertTrue(TestAST.test(input,expect,388))

	def test89(self):
		input = """func main() 
        begin
            number x <- main()
            begin
                x <- main()
                begin
                    x <- main()
                end
                x <- main()
            end
            x <- main()
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(x), NumberType, None, CallExpr(Id(main), [])), Block([AssignStmt(Id(x), CallExpr(Id(main), [])), Block([AssignStmt(Id(x), CallExpr(Id(main), []))]), AssignStmt(Id(x), CallExpr(Id(main), []))]), AssignStmt(Id(x), CallExpr(Id(main), []))]))])"""
		self.assertTrue(TestAST.test(input,expect,389))

	def test90(self):
		input = """
func isPrime(number x)

func main()
begin
	number x <- readNumber()
	if (isPrime(x)) printString("Yes")
	else printString("No")
end

func isPrime(number x) begin
	if (x <= 1) return false
	var i <- 2
	for i until i > x / 2 by 1
	begin
		if (x % i = 0) return false
	end
	return true
end
        """
		expect = """Program([FuncDecl(Id(isPrime), [VarDecl(Id(x), NumberType, None, None)], None), FuncDecl(Id(main), [], Block([VarDecl(Id(x), NumberType, None, CallExpr(Id(readNumber), [])), If((CallExpr(Id(isPrime), [Id(x)]), CallStmt(Id(printString), [StringLit(Yes)])), [], CallStmt(Id(printString), [StringLit(No)]))])), FuncDecl(Id(isPrime), [VarDecl(Id(x), NumberType, None, None)], Block([If((BinaryOp(<=, Id(x), NumLit(1.0)), Return(BooleanLit(False))), [], None), VarDecl(Id(i), None, var, NumLit(2.0)), For(Id(i), BinaryOp(>, Id(i), BinaryOp(/, Id(x), NumLit(2.0))), NumLit(1.0), Block([If((BinaryOp(=, BinaryOp(%, Id(x), Id(i)), NumLit(0.0)), Return(BooleanLit(False))), [], None)])), Return(BooleanLit(True))]))])"""
		self.assertTrue(TestAST.test(input,expect,390))

	def test91(self):
		input = """
func areDivisors(number num1, number num2)
	return ((num1 % num2 = 0) or (num2 % num1 = 0))

func main() begin
	var num1 <- readNumber()
	var num2 <- readNumber()
	if (areDivisors(num1, num2)) printString("Yes")
	else printString("No")
end

        """
		expect = """Program([FuncDecl(Id(areDivisors), [VarDecl(Id(num1), NumberType, None, None), VarDecl(Id(num2), NumberType, None, None)], Return(BinaryOp(or, BinaryOp(=, BinaryOp(%, Id(num1), Id(num2)), NumLit(0.0)), BinaryOp(=, BinaryOp(%, Id(num2), Id(num1)), NumLit(0.0))))), FuncDecl(Id(main), [], Block([VarDecl(Id(num1), None, var, CallExpr(Id(readNumber), [])), VarDecl(Id(num2), None, var, CallExpr(Id(readNumber), [])), If((CallExpr(Id(areDivisors), [Id(num1), Id(num2)]), CallStmt(Id(printString), [StringLit(Yes)])), [], CallStmt(Id(printString), [StringLit(No)]))]))])"""
		self.assertTrue(TestAST.test(input,expect,391))

	def test92(self):
		input = """func main() 
        begin
            number a_1 <- funcfunc()
            for a_1 until exp = 1000 and not exp2 by a + arr[0] begin
                return 
            end
        end

        """
		expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a_1), NumberType, None, CallExpr(Id(funcfunc), [])), For(Id(a_1), BinaryOp(=, Id(exp), BinaryOp(and, NumLit(1000.0), UnaryOp(not, Id(exp2)))), BinaryOp(+, Id(a), ArrayCell(Id(arr), [NumLit(0.0)])), Block([Return()]))]))])"""
		self.assertTrue(TestAST.test(input,expect,492))

	def test93(self):
		input = """
        func main() begin
            number a <- foo(b1(1, 3), b2(5))
            bool b <- ((a or false) and true) or (not a)
            number c[4, 3] 
            c <- temp(a, b, (a - 2 * a - 3), foo((a * b), a + b))
            var d <- c[1,2] + c[2,3] - c[3,4]
            return d
        end

        """
		expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, CallExpr(Id(foo), [CallExpr(Id(b1), [NumLit(1.0), NumLit(3.0)]), CallExpr(Id(b2), [NumLit(5.0)])])), VarDecl(Id(b), BoolType, None, BinaryOp(or, BinaryOp(and, BinaryOp(or, Id(a), BooleanLit(False)), BooleanLit(True)), UnaryOp(not, Id(a)))), VarDecl(Id(c), ArrayType([4.0, 3.0], NumberType), None, None), AssignStmt(Id(c), CallExpr(Id(temp), [Id(a), Id(b), BinaryOp(-, BinaryOp(-, Id(a), BinaryOp(*, NumLit(2.0), Id(a))), NumLit(3.0)), CallExpr(Id(foo), [BinaryOp(*, Id(a), Id(b)), BinaryOp(+, Id(a), Id(b))])])), VarDecl(Id(d), None, var, BinaryOp(-, BinaryOp(+, ArrayCell(Id(c), [NumLit(1.0), NumLit(2.0)]), ArrayCell(Id(c), [NumLit(2.0), NumLit(3.0)])), ArrayCell(Id(c), [NumLit(3.0), NumLit(4.0)]))), Return(Id(d))]))])"""
		self.assertTrue(TestAST.test(input,expect,393))

	def test94(self):
		input = """func foo(number a[5.12, 3.22e-14], string b)
begin
	var i <- 0
	for i until i >= 5 by 1
	begin
		a[i] <- i * i + 5
	end
	return -1
end
"""
		expect = """Program([FuncDecl(Id(foo), [VarDecl(Id(a), ArrayType([5.12, 3.22e-14], NumberType), None, None), VarDecl(Id(b), StringType, None, None)], Block([VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), NumLit(5.0)), NumLit(1.0), Block([AssignStmt(ArrayCell(Id(a), [Id(i)]), BinaryOp(+, BinaryOp(*, Id(i), Id(i)), NumLit(5.0)))])), Return(UnaryOp(-, NumLit(1.0)))]))])"""
		self.assertTrue(TestAST.test(input,expect,394))

	def test95(self):
		input = """func main() 
        begin
            if (true) begin
                if (true) begin
                    x <- true
                end 
                else begin
                    x <- false
                end
            end 
            else begin
                x <- -false
            end
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([If((BooleanLit(True), Block([If((BooleanLit(True), Block([AssignStmt(Id(x), BooleanLit(True))])), [], Block([AssignStmt(Id(x), BooleanLit(False))]))])), [], Block([AssignStmt(Id(x), UnaryOp(-, BooleanLit(False)))]))]))])"""
		self.assertTrue(TestAST.test(input,expect,395))

	def test96(self):
		input = """func foo(number a[5.12, 3.22e-14], bool b)
begin
	var i <- 0
	for i until i >= 5 by 1
	begin
		a[i] <- i * i + 5
	end
	return -1
end
"""
		expect = """Program([FuncDecl(Id(foo), [VarDecl(Id(a), ArrayType([5.12, 3.22e-14], NumberType), None, None), VarDecl(Id(b), BoolType, None, None)], Block([VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), NumLit(5.0)), NumLit(1.0), Block([AssignStmt(ArrayCell(Id(a), [Id(i)]), BinaryOp(+, BinaryOp(*, Id(i), Id(i)), NumLit(5.0)))])), Return(UnaryOp(-, NumLit(1.0)))]))])"""
		self.assertTrue(TestAST.test(input,expect,396))

	def test97(self):
		input = """func main() begin
        a[3 + foo(2)] <- a[b[2, 3]] + 4
        string a[1,2,3] <- ["Hello", "World"]
        number b[1] <- a[1,2,3]
        bool c[1] <- [[true, false], [false, true], true]
    end


    """
		expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(a), [BinaryOp(+, NumLit(3.0), CallExpr(Id(foo), [NumLit(2.0)]))]), BinaryOp(+, ArrayCell(Id(a), [ArrayCell(Id(b), [NumLit(2.0), NumLit(3.0)])]), NumLit(4.0))), VarDecl(Id(a), ArrayType([1.0, 2.0, 3.0], StringType), None, ArrayLit(StringLit(Hello), StringLit(World))), VarDecl(Id(b), ArrayType([1.0], NumberType), None, ArrayCell(Id(a), [NumLit(1.0), NumLit(2.0), NumLit(3.0)])), VarDecl(Id(c), ArrayType([1.0], BoolType), None, ArrayLit(ArrayLit(BooleanLit(True), BooleanLit(False)), ArrayLit(BooleanLit(False), BooleanLit(True)), BooleanLit(True)))]))])"""
		self.assertTrue(TestAST.test(input,expect,397))

	def test98(self):
		input = """func main()
begin
	if (true) begin
		printLine()
		if (foo() = 2) printLine("True")
		else
		begin


			if (fee() = 1) printLine(1)
			elif (fee() = 2) printLine(2)
			elif (fee() = 3) begin
				if (foo() = 1)
				begin 
				end

				else 
				begin


					printLine(4)
				end
			end
		end
	end
end
"""
		expect = """Program([FuncDecl(Id(main), [], Block([If((BooleanLit(True), Block([CallStmt(Id(printLine), []), If((BinaryOp(=, CallExpr(Id(foo), []), NumLit(2.0)), CallStmt(Id(printLine), [StringLit(True)])), [], Block([If((BinaryOp(=, CallExpr(Id(fee), []), NumLit(1.0)), CallStmt(Id(printLine), [NumLit(1.0)])), [(BinaryOp(=, CallExpr(Id(fee), []), NumLit(2.0)), CallStmt(Id(printLine), [NumLit(2.0)])), (BinaryOp(=, CallExpr(Id(fee), []), NumLit(3.0)), Block([If((BinaryOp(=, CallExpr(Id(foo), []), NumLit(1.0)), Block([])), [], Block([CallStmt(Id(printLine), [NumLit(4.0)])]))]))], None)]))])), [], None)]))])"""
		self.assertTrue(TestAST.test(input,expect,398))

	def test99(self):
		input = """func main() 
        begin
            x <- 10
            i <- 0
            for i until i > x by x-2
                if (true) break
                elif (x <= 1) continue
                elif (a[10,2+3] < a(1,true)[1,2-2,3*4]) printLine("elif 2nd")
                else i <- printLine("Hi")
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(x), NumLit(10.0)), AssignStmt(Id(i), NumLit(0.0)), For(Id(i), BinaryOp(>, Id(i), Id(x)), BinaryOp(-, Id(x), NumLit(2.0)), If((BooleanLit(True), Break), [(BinaryOp(<=, Id(x), NumLit(1.0)), Continue), (BinaryOp(<, ArrayCell(Id(a), [NumLit(10.0), BinaryOp(+, NumLit(2.0), NumLit(3.0))]), ArrayCell(CallExpr(Id(a), [NumLit(1.0), BooleanLit(True)]), [NumLit(1.0), BinaryOp(-, NumLit(2.0), NumLit(2.0)), BinaryOp(*, NumLit(3.0), NumLit(4.0))])), CallStmt(Id(printLine), [StringLit(elif 2nd)]))], AssignStmt(Id(i), CallExpr(Id(printLine), [StringLit(Hi)]))))]))])"""
		self.assertTrue(TestAST.test(input,expect,399))

	def test100(self):
		input = """func main() begin
            begin
                begin
                    for i until i < 0 by true
                    begin
                    end
                end
                begin
                    for i until i > 0 by false
                    begin
                    end
                end
            end
        end
        """
		expect = """Program([FuncDecl(Id(main), [], Block([Block([Block([For(Id(i), BinaryOp(<, Id(i), NumLit(0.0)), BooleanLit(True), Block([]))]), Block([For(Id(i), BinaryOp(>, Id(i), NumLit(0.0)), BooleanLit(False), Block([]))])])]))])"""
		self.assertTrue(TestAST.test(input,expect,400))

