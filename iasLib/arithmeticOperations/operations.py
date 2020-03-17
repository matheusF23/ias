# Operations é uma classe para realizar determinadas operações com os números vindos da classe de intruções
# atitméticas como conversóes binário/decimal.

class Operations():
    def __init__(self):
        super().__init__()
    def convertDecimalToBinary(self, n):
        """Converte um número Decimal em Binário, retornando um número binário de 40 bits, sendo o primeiro
        um bit de sinal"""
        binary = ""
        nabs = abs(n)

        # Fazendo a conversão
        while(True):
            binary = binary + str(nabs%2)
            nabs = nabs//2
            if nabs == 0:
                break

        binary = binary[::-1]

        # Adicionar zeros à esquerda para termos os 40 bits com o de sinal
        while(len(binary) < 39):
            binary = '0' + binary

        # Adicinoando o bit de sinal
        if(n >= 0):
            binary = '0' + binary
        else:
            binary = '1' + binary
        return binary   # Retorna uma string
    
    def convertBinaryToDecimal(self, n):
        """Converte um número Binário em Decimal"""
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
    
    def convertBinaryToDecimalWithoutSignal(self, n):
        """Converte um número Binário em Decimal"""
        decimal = 0
        n = n[::-1]
        tam = len(n)
        for i in range(tam):
            if n[i] == "1":
                decimal = decimal + 2**i
        return decimal
