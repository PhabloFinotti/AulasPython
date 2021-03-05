file = open("teste.txt", "w")
file.write("Phablin")
file.close()

file = open("teste.txt", "r")
dados = file.read()
file.close()

print(dados)
