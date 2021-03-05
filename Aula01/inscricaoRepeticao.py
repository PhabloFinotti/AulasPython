contador = 0
idade = 0
nome = ""
cargo = ""

contador = int(input("\nQuantas pessoas voce deseja cadastrar?\n"))

file = open("pessoas.txt", "w")

for i in range(contador):
    nome = str(input("Digite o nome da pessoa:\n")) + "\n"
    idade = str(input("Digite a idade da pessoa:\n")) + "\n"
    cargo = str(input("Digite o cargo da pessoa:\n")) + "\n"
    print("\n")
    todos = [nome, idade, cargo]
    
    file.writelines(todos)


file.close()


leitura = open("pessoas.txt", "r")

for x in range(contador):
    nomeRes = leitura.readline()
    idadeRes = leitura.readline()
    cargoRes = leitura.readline()
   
    print("\nPessoa", x + 1)
    print("Nome: " + nomeRes  + "Idade: " + idadeRes + "Cargo: " + cargoRes)

leitura.close()