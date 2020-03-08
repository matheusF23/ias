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

class Arithmetic():
    def __init__(self):
        super().__init__()

    def convertDecimalToBinary(self, n):
        binary = ""
        nabs = abs(n)
        while(True):
            binary = binary + str(nabs%2)
            nabs = nabs//2
            if nabs == 0:
                break
        binary = binary[::-1]
        if(n >= 0):
            binary = '0' + binary
        else:
            binary = '1' + binary
        return binary   # Retorna uma string
    
    def convertBinaryToDecimal(self, n):
        signal = n[0]   # bit de sinal
        decimal = 0
        n = n[:0:-1]
        tam = len(n)
        for i in range(tam):
            if n[i] == "1":
                decimal = decimal + 2**i
        if(signal == '0'):  # Número positivo
            return decimal
        else:
            return decimal * (-1)   # Retorna um inteiro
    
    # def addMx(self,ac, x, memory):
    #     mx = 
    #     return ac
    