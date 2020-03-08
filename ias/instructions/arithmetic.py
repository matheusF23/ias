## Arithmetic instructions ##
#
#  Opcode  | Symbolic representation | Description
# 00000101 |         ADD M(X)        | Soma M(X) a AC; coloca o resultado em AC
# 00000111 |        ADD |M(X)|       | Soma |M(X)| a AC; coloca o resultado em AC
# 00000110 |         SUB M(X)        | Subtrai M(X) de AC; coloca o resultado em AC
# 00001000 |        SUB |M(X)|       | Subtrai |M(X)| de AC; coloca o resto em AC
# 00001011 |         MUL M(X)        | Multiplica M(X) por MQ; coloca os bits mais significativos 
#          |                         | do resultado em AC; coloca bits menos significativos em MQ
# 00001100 |         DIV M(X)        | Divide AC por M(X); coloca o quociente em MQ e o resto em AC
# 00010100 |           LSH           | Multiplica o AC por 2; ou seja, desloca à esquerda uma posição de bit
# 00010101 |           RSH           | Divide o AC por 2; ou seja, desloca uma posição à direita

from ias.arithmeticOperations.operations import Operations

class Arithmetic():
    def __init__(self):
        super().__init__()
        self.operations = Operations()
    
    def addMx(self,ac, x, memory):
        mx = memory[x]
        ac = self.operations.convertBinaryToDecimal(ac) + self.operations.convertBinaryToDecimal(mx)
        ac = self.operations.convertDecimalToBinary(ac)
        return ac

    def __str__(self):
        return "Objeto contendo instruções de Aritmética"
    