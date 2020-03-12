
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
