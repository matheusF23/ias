
def instructionData(opcode):
    if opcode == "00000000":
        return "Fim da execução"
    elif opcode == "00001010":
        return "LOAD MQ: Transfere o conteúdo de MQ para AC"
    elif opcode == "00001001":
        return "LOAD MQ,M(X): Transfere o conteúdo do local de memória X para MQ"
    elif opcode == "00100001":
        return "STOR M(X): Transfere o conteúdo de AC para o local de memória X"
    elif opcode == "00000001":
        return "LOAD M(X): Transfere M(X) para o AC"
    elif opcode == "00000010":
        return "LOAD –M(X): Transfere – M(X) para o AC"
    elif opcode == "00000011":
        return "LOAD |M(X)|: Transfere o valor absoluto de M(X) para o AC"
    elif opcode == "00000100":
        return "LOAD –|M(X)|: Transfere -|M(X)| para o acumulador"
    elif opcode == "00001111":
        return "JUMP+ M(X,0:19): Se o número no AC for não negativo, apanha a próxima instrução da metade esquerda de M(X)"
    elif opcode == "00010000":
        return "JUMP+ M(X,20:39): Se o número no AC for não negativo, apanha a próxima instrução da metade direita de M(X)"
    elif opcode == "00001101":
        return "JUMP M(X,0:19): Apanha a próxima instrução da metade esquerda de M(X)"
    elif opcode == "00001110":
        return "JUMP M(X,20:39): Apanha a próxima instrução da metade direita de M(X)"
    elif opcode == "00000101":
        return "ADD M(X): Soma M(X) a AC; coloca o resultado em AC"
    elif opcode == "00000111":
        return "ADD |M(X)|: Soma |M(X)| a AC; coloca o resultado em AC"
    elif opcode == "00000110":
        return "SUB M(X): Subtrai M(X) de AC; coloca o resultado em AC"
    elif opcode == "00001000":
        return "SUB |M(X)|: Subtrai |M(X)| de AC; coloca o resto em AC"
    elif opcode == "00001011":
        return "MUL M(X): Multiplica M(X) por MQ; coloca os bits mais significativos do resultado em AC; coloca bits menos significativos em MQ"
    elif opcode == "00001100":
        return "DIV M(X): Divide AC por M(X); coloca o quociente em MQ e o resto em AC"
    elif opcode == "00010100":
        return "LSH: Multiplica o AC por 2; ou seja, desloca à esquerda uma posição de bit"
    elif opcode == "00010101":
        return "RSH: Divide o AC por 2; ou seja, desloca uma posição à direita"
    elif opcode == "00010010":
        return "STOR M(X,8:19): Substitui campo de endereço da esquerda em M(X) por 12 bits mais à direita de AC"
    elif opcode == "00010011":
        return "STOR M(X,28:39): Substitui campo de endereço da direita em M(X) por 12 bits mais à direita de AC"
    else:
        return "Aguardando instrução."