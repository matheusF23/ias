
from iasLib.arithmeticOperations.operations import Operations
from iasLib.instructions.arithmetic import Arithmetic
from iasLib.instructions.addressModification import AddressModification
from iasLib.instructions.conditionalDeviation import ConditionalDeviation
from iasLib.instructions.dataTransfer import DataTransfer
from iasLib.instructions.unconditionalDeviation import UnconditionalDeviation
from iasLib.instructions.instructionsData import instructionData

# Inicialização da memória
memory = []
for i in range(1000):
    memory.append("0000000000000000000000000000000000000000")

# Carregando programa na memória
program = open("programFiles/sumOnePlusOne.txt", "r")
x = 0   # Acesso à memória
for line in program:
    partsOfTheLine = line.split()
    memory[x] = partsOfTheLine[0]
    x += 1
program.close()

showMemory = input("Gostaria de visualizar a memória? (y/n)")
if(showMemory == 'y' or showMemory == 'yes'):
    for i in range(x):  # Mostrar apenar a memória carregada
        print(i, memory[i])
print("\n### Executando programa ###\n")
    
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

ex = 1  # Número de execuções

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
for i in range(999):
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

    print("Execução", ex, "|", "ir: ", ir, "|", instructionData(ir))
    print("mar: ", mar, "ac: ", ac, "mq: ", mq, "ibr: ", ibr, "\n")
    
    if(ir == "00000000"):
        break

    ex += 1

showMemory2 = input("\nGostaria de visualizar a Memória Completa? (y/n)")
if(showMemory2 == 'y' or showMemory == 'yes'):
    count = 0
    while(count < 1000):
        if(count == 999):
            print(count, memory[count])
            break
        print(count, memory[count], count+1, memory[count+1], count+2, memory[count+2])
        count += 3
print("\n### Finish Program ###")

getout = input("\nPressione qualquer tecla para sair!")
