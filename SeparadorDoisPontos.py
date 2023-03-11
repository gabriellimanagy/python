# Abre o arquivo com dois pontos
arquivo = open("example.txt", "r", encoding="utf-8")

# Abre os arquivos de saída
arqParte1 = open("parte1.txt", "a",  encoding="utf-8")
arqParte2 = open("parte2.txt", "a",  encoding="utf-8")

# lê todas as linhas do arquivo
linhas = arquivo.readlines()

# percorre todas as linhas do arquivo
for linha in linhas:
    # separa a linha em partes usando ":"
    partes = linha.split(":")
    
    # verifica se a linha contém ":" e tem exatamente dois elementos na lista
    if len(partes) == 2:
        # escreve o primeiro elemento no arquivo parte1.txt
        arqParte1.write(partes[0])
        
        # escreve o primeiro elemento no arquivo parte2.txt
        arqParte2.write(partes[1].rstrip("\n"))

# fecha os arquivos
arqParte1.close()
arqParte2.close()
arquivo.close()
