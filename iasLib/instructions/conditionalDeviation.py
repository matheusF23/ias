## Conditional Deviation instructions ##
#
#  Opcode  | Symbolic representation | Description
# 00001111 |     JUMP+ M(X,0:19)     | Se o número no AC for não negativo, apanha a próxima instrução da 
#          |                         | metade esquerda de M(X)
# 00010000 |     JUMP+ M(X,20:39)    | Se o número no AC for não negativo, apanha a próxima instrução da 
#          |                         | metade direita de M(X)

class ConditionalDeviation():
    def __init__(self):
        super().__init__()
    
    def jumpMxLeft(self, ac, x, memory):
        """00001111 -  Se o número no AC for não negativo, apanha a próxima instrução da metade 
        esquerda de M(X)
        """
        if(ac[0] == '0'):
            return memory[x][0:20]
        return ''
    
    def jumpMxRight(self, ac, x, memory):
        """00010000 -  Se o número no AC for não negativo, apanha a próxima instrução da metade 
        direita de M(X)
        """
        if(ac[0] == '0'):
            return memory[x][20:40]
        return ''
