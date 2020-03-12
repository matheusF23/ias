
from ias.arithmeticOperations.operations import Operations
from ias.instructions.arithmetic import Arithmetic
from ias.instructions.addressModification import AddressModification
from ias.instructions.conditionalDeviation import ConditionalDeviation
from ias.instructions.dataTransfer import DataTransfer
from ias.instructions.unconditionalDeviation import UnconditionalDeviation

# Inicialização da memória
memory = []
for i in range(1000):
    memory.append('0000000000000000000000000000000000000000')

# Definição dos registradores
mbr = ''    # Registrador de buffer de memória
mar = ''    # Registrador de endereço de memória
ir = ''     # Registrador de instrução
ibr = ''    # Registrador de buffer de instrução
pc = ''     # Contador de programa
ac = ''     # Acumulador
mq = ''     # Quociente multiplicador

# Inicialização de Instâncias necessárias
op = Operations()
arithmetic = Arithmetic()
addressModification = AddressModification()
conditionalDeviation = ConditionalDeviation()
dataTransfer = dataTransfer()
unconditionalDeviation = UnconditionalDeviation()
