
# from ias.arithmeticOperations.operations import Operations
# from ias.instructions.arithmetic import Arithmetic
# from ias.instructions.addressModification import AddressModification
# from ias.instructions.conditionalDeviation import ConditionalDeviation
# from ias.instructions.dataTransfer import DataTransfer
# from ias.instructions.unconditionalDeviation import UnconditionalDeviation

# Inicialização da memória
memory = []
for i in range(1000):
    memory.append("0000000000000000000000000000000000000000")

# Definição dos registradores
mbr = ""    # Registrador de buffer de memória
mar = ""    # Registrador de endereço de memória
ir = ""     # Registrador de instrução
ibr = ""    # Registrador de buffer de instrução
pc = 0      # Contador de programa
ac = ""     # Acumulador
mq = ""     # Quociente multiplicador

# # Inicialização de Instâncias necessárias
# op = Operations()
# arithmetic = Arithmetic()
# addressModification = AddressModification()
# conditionalDeviation = ConditionalDeviation()
# dataTransfer = dataTransfer()
# unconditionalDeviation = UnconditionalDeviation()

while(True):
    if(ibr != ''):
        ir = ibr[0:8]
        mar = ibr[8:20]
        pc += 1
        # execution(ir, mar, memory, ac, mq)
    else:
        # mar = pc  # A principio não precisa
        mbr = memory[pc]
        
        if(mbr[0:20] == "00000000000000000000"):
            ir = mbr[20:28]
            mar = mbr[28:40]
            pc += 1
            # execution(ir, mar, memory, ac, mq)
        else:
            ibr = mbr[20:40]
            ir = mbr[0:8]
            mar = mbr[8:20]
            # execution(ir, mar, memory, ac, mq)

    if(ir[0:8] == "00000000"):
        break
