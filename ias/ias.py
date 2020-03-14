
from ias.arithmeticOperations.operations import Operations
from ias.instructions.arithmetic import Arithmetic
from ias.instructions.addressModification import AddressModification
from ias.instructions.conditionalDeviation import ConditionalDeviation
from ias.instructions.dataTransfer import DataTransfer
from ias.instructions.unconditionalDeviation import UnconditionalDeviation

# Inicialização da memória
memory = []
for i in range(1000):
    memory.append("0000000000000000000000000000000000000000")

# Carregando programa na memória
program = open("ias/programFiles/sumOnePlusOne.txt", "r")
x = 0   # Acesso à memória
for line in program:
    partsOfTheLine = line.split()
    memory[x] = partsOfTheLine[0]
    x += 1

# Definição dos registradores
mbr = ""    # Registrador de buffer de memória
mar = ""    # Registrador de endereço de memória
ir = ""     # Registrador de instrução
ibr = ""    # Registrador de buffer de instrução
pc = 0      # Contador de programa
ac = "0000000000000000000000000000000000000000"     # Acumulador
mq = ""     # Quociente multiplicador

# Inicialização de Instâncias necessárias
op = Operations()
arithmetic = Arithmetic()
addressModification = AddressModification()
conditionalDeviation = ConditionalDeviation()
dataTransfer = DataTransfer()
unconditionalDeviation = UnconditionalDeviation()

# Ciclo de execução
def execution(ir, mar, memory, ac, mq, ibr):
    """Reproduz o ciclo de execução. Retorna uma tupla com: (ac, mq, ibr)"""
    
    mar = op.convertBinaryToDecimalWithoutSignal(mar)     # Converte mar para decimal para acessar a posição de memória
    
    # Execução das instruções de transferência de dados
    if(ir == "00001010"):
        ac = dataTransfer.loadMq(mq, ac)
    elif(ir == "00001001"):
        mq = dataTransfer.loadMqMx(mar, mq, memory)
    elif(ir == "00100001"):
        dataTransfer.storMx(ac, mar, memory)
    elif(ir == "00000001"):
        ac = dataTransfer.loadMx(ac, mar, memory)
    elif(ir == "00000010"):
        ac = dataTransfer.loadMxNeg(ac, mar, memory)
    elif(ir == "00000011"):
        ac = dataTransfer.loadAbsMx(ac, mar, memory)
    elif(ir == "00000100"):
        ac = dataTransfer.loadAbsMxNeg(ac, mar, memory)
    
    # Execução das instruções de desvio incondicional
    elif(ir == "00001101"):
        ibr = unconditionalDeviation.jumpMxLeft(mar, memory)
    elif(ir == "00001110"):
        ibr = unconditionalDeviation.jumpMxRight(mar, memory)
    
    # Execução das instruções de desvio condicional
    elif(ir == "00001111"):
        ibr = conditionalDeviation.jumpMxLeft(ac, mar, memory)
    elif(ir == "00010000"):
        ibr = conditionalDeviation.jumpMxRight(ac, mar, memory)
    
    # Execução das instruções aritméticas
    elif(ir == "00000101"):
        ac = arithmetic.addMx(ac, mar, memory)
    elif(ir == "00000111"):
        ac = arithmetic.addAbsMx(ac, mar, memory)
    elif(ir == "00000110"):
        ac = arithmetic.subMx(ac, mar, memory)
    elif(ir == "00001000"):
        ac = arithmetic.subAbsMx(ac, mar, memory)
    elif(ir == "00001011"):
        ans = arithmetic.multMx(mq, mar, memory)
        ac = ans[0]
        mq = ans[1]
    elif(ir == "00001100"):
        ans = arithmetic.divMx(ac, mar, memory)
        ac = ans[0]
        mq = ans[1]
    elif(ir == "00010100"):
        ac = arithmetic.lsh(ac)
    elif(ir == "00010101"):
        ac = arithmetic.rsh(ac)
    
    # Execução das instruções de modificação de endereço
    elif(ir == "00010010"):
        addressModification.storLeft(ac, mar, memory)
    elif(ir == "00010011"):
        addressModification.storRight(ac, mar, memory)
        
    return ac, mq, ibr

# Ciclo de busca
for i in range(10):
    if(ibr != ""):
        ir = ibr[0:8]
        mar = ibr[8:20]
        ibr = ""
        pc += 1
        answer = execution(ir, mar, memory, ac, mq, ibr)
        ac = answer[0]
        mq = answer[1]
        ibr = answer[2]
    else:
        # mar = pc  # A principio não precisa
        mbr = memory[pc]
        
        if(mbr[0:20] == "00000000000000000000"):
            ir = mbr[20:28]
            mar = mbr[28:40]
            mbr = ""
            pc += 1
            answer = execution(ir, mar, memory, ac, mq, ibr)
            ac = answer[0]
            mq = answer[1]
            ibr = answer[2]
        else:
            ibr = mbr[20:40]
            ir = mbr[0:8]
            mar = mbr[8:20]
            mbr = ""
            answer = execution(ir, mar, memory, ac, mq, ibr)
            ac = answer[0]
            mq = answer[1]
            ibr = answer[2]
    
    if(ir == "00000000"):
        break
    print("ir: ", ir, "ac: ", ac, "mq: ", "mq: ", mq, "ibr: ", ibr, "mar: ", mar)
print('finish')