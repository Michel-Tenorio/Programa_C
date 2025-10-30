class Paciente:
    def __init__(self, nome, idade, profissao, altura, estado_civil):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        self.altura = altura
        self.estado_civil = estado_civil

    def __str__(self):
        return f"Nome: {self.nome}; Idade: {self.idade}; Profissão: {self.profissao}; Altura: {self.altura}; Estado civil: {self.estado_civil}"


def menu():
    pacientes = []
    while True:
        print("Menu Paciente")
        print("1. Cadastro Paciente")
        print("2. Editar Nome")
        print("3. Consulta")
        print("4. Consultar Todos")
        print("X. Sair")
        op = input("Escolha a Opção: ")

        if op.upper() == "X":
            print("Encerrando...")
            break
        elif op == "1":
            nome = input("Nome: ")
            idade = input("Idade: ")
            profissao = input("Profissão: ")
            altura = input("Altura: ")
            estado_civil = input("Estado civil: ")
            pacientes.append(Paciente(nome, idade, profissao, altura, estado_civil)) 
            print("Paciente cadastrado!")
       
        elif op == "2":
            nome = input("Digite o nome do paciente para editar: ") 
            for p in pacientes: 
                if p.nome.lower() == nome.lower():
                    p.nome = input(f"Nome ({p.nome}): ") or p.nome
                    p.idade = input(f"Idade ({p.idade}): ") or p.idade
                    p.profissao = input(f"Profissão ({p.profissao}): ") or p.profissao  
                    p.altura = input(f"Altura ({p.altura}): ") or p.altura              
                    p.estado_civil = input(f"Estado Civil ({p.estado_civil}): ") or p.estado_civil
                    print("DADOS ATUALIZADOS!")
                    break 
            else: 
                print("Paciente não encontrado")
        
        elif op == "3":
            nome = input ("Digite o nome: ")
            for p in pacientes:
                if p.nome.lower() == nome.lower():
                    print(p)
                    break
                else: 
                    print ("Paciente não encontrado.")
        
        elif op == "4": 
            if not pacientes:
                print("Nenhum paciente cadastrado.")
            else:
                for p in pacientes:
                    print(p)


if __name__ == "__main__":
    menu()
