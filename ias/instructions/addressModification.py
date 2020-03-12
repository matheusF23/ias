## Address Modification instructions ##
#
#  Opcode  | Symbolic representation | Description
# 00010010 |      STOR M(X,8:19)     | Substitui campo de endereço da esquerda em M(X) por 12 bits mais 
#          |                         | à direita de AC
# 00010011 |      STOR M(X,28:39)    | Substitui campo de endereço da direita em M(X) por 12 bits mais  
#          |                         | à direita de AC

class AddressModification():
    def __init__(self):
        super().__init__()
    
    def storLeft(self, ac, x, memory):
        """00010010 - Substitui campo de endereço da esquerda em M(X) por 12 bits mais à direita de AC
        Retorna mx atualizado"""
        mx = memory[x][0:8] + ac[28:40] + memory[x][20:40]

        return mx
