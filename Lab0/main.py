from CompoundStm import CompoundStm
from AssignStm import AssignStm
from OpExp import OpExp
from NumExp import NumExp
from Binop import Binop
from CompoundStm import CompoundStm
from EseqExp import EseqExp
from PrintStm import PrintStm
from PairExpList import PairExpList
from IdExp import IdExp
from LastExpList import LastExpList

if __name__ == "__main__": # a := 5+3; b := (print(a, a-1), 10*a); print(b)
    print("Inicio")
    op1 = OpExp(NumExp(5), Binop.plus, NumExp(3))
    ida = AssignStm("a", op1)

    op2 = OpExp(IdExp("a"), Binop.minus, NumExp(1))
    print_stm = PrintStm(PairExpList(IdExp("a"), LastExpList(op2) ))
    eseq = EseqExp(print_stm , OpExp(NumExp(10), Binop.times, IdExp("a")))
    idb = AssignStm("b", eseq)

    print_stm_b = PrintStm(LastExpList(IdExp("b")))
    prog = CompoundStm(ida, CompoundStm(idb, print_stm_b ) )
    print(prog)
    print("FIM")
