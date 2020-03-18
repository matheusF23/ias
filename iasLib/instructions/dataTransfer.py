## Data transfer instructions ##
#
#  Opcode  | Symbolic representation | Description
# 00001010 |         LOAD MQ         | Transfere o conteúdo de MQ para AC
# 00001001 |       LOAD MQ,M(X)      | Transfere o conteúdo do local de memória X para MQ
# 00100001 |         STOR M(X)       | Transfere o conteúdo de AC para o local de memória X
# 00000001 |         LOAD M(X)       | Transfere M(X) para o AC
# 00000010 |        LOAD –M(X)       | Transfere – M(X) para o AC
# 00000011 |        LOAD |M(X)|      | Transfere o valor absoluto de M(X) para o AC
# 00000100 |        LOAD –|M(X)|     | Transfere -|M(X)| para o acumulador

class DataTransfer():
    def __init__(self):
        super().__init__()
    
    def loadMq(self, mq, ac):
        """00001010 - Transfere o conteúdo de MQ para AC"""
        ac = mq
        return ac

    def loadMqMx(self, x, mq, memory):
        """00001001 - Transfere o conteúdo do local de memória X para MQ"""
        mq = memory[x]
        return mq
    
    def storMx(self, ac, x, memory):
        """00100001 - Transfere o conteúdo de AC para o local de memória X"""
        memory[x] = ac

    def loadMx(self, ac, x, memory):
        """00000001 - Transfere M(X) para o AC"""
        ac = memory[x]
        return ac
    
    def loadMxNeg(self, ac, x, memory):
        """00000010 - Transfere – M(X) para o AC"""
        if(memory[x][0] == '1'):
            temp = '0' + memory[x][1:]
        else:
            temp = '1' + memory[x][1:]
        ac = temp
        return ac
    
    def loadAbsMx(self, ac, x, memory):
        """00000011 - Transfere o valor absoluto de M(X) para o AC"""
        absMx = '0' + memory[x][1:]
        ac = absMx
        return ac
    
    def loadAbsMxNeg(self, ac, x, memory):
        """00000100 - Transfere -|M(X)| para o acumulador"""
        absMxNeg = '1' + memory[x][1:]
        ac = absMxNeg
        return ac
