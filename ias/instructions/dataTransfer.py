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
        ac = mq
        return ac

    def loadMqMx(self, x, mq, memory):
        mq = memory[x]
        return mq
    
    def storMx(self, ac, x, memory):
        memory[x] = ac

    def loadMx(self, ac, x, memory):
        ac = memory[x]
        return ac
    def loadMxNeg(self, ac, x, memory):
        if(memory[x][0] == '1'):
            temp = '0' + memory[x][1:]
        else:
            temp = '1' + memory[x][1:]
        ac = temp
        return ac
