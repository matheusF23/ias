## Unconditional Deviation instructions ##
#
#  Opcode  | Symbolic representation | Description
# 00001101 |      JUMP M(X,0:19)     | Apanha a próxima instrução da metade esquerda de M(X)
# 00001110 |      JUMP M(X,20:39)    | Apanha a próxima instrução da metade direita de M(X)

class UnconditionalDeviation():
    def __init__(self):
        super().__init__()

    def jumpMxLeft(self, x, memory):
        """00001101 -  Apanha a próxima instrução da metade esquerda de M(X)"""
        return memory[x][0:20]

    def jumpMxRight(self, x, memory):
        """00001110 - Apanha a próxima instrução da metade direita de M(X)"""
        return memory[x][20:40]
