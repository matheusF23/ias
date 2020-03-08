# Operations é uma classe para realizar determinadas operações com os números vindos da classe de intruções
# atitméticas como conversóes binário/decimal.

class Operations():
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

    def __str__(self):
        return "Classe para operações com números aritméticos"