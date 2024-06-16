lista_de_medicos = []
lista_de_pacientes = []
lista_de_convenios = []
lista_de_consultas = []
lista_de_compromissos = []

def cadastrarMedicos():
    CadastrarMedica_nome = input('Nome do médico:')
    CadastrarMedica_CPF = input('Digite o CPF:')
    CadastrarMedica_RG = input('Digite o RG:')
    CadastrarMedica_CRM = input('Digite o CRM:')
    CadastrarMedica_telefone = input('Telefone do médico:')
    CadastrarMedica_endereco = input('Endereço do médico:')
    CadastrarMedica_Sexo = input('Sexo(M/F):')
    CadastrarMedica_Senha = input('Digite a senha de acesso:')
    lista_de_medicos.append({
        'nome': CadastrarMedica_nome,
        'CPF': CadastrarMedica_CPF,
        'RG': CadastrarMedica_RG,
        'CRM': CadastrarMedica_CRM,
        'telefone': CadastrarMedica_telefone,
        'endereco': CadastrarMedica_endereco,
        'sexo': CadastrarMedica_Sexo,
        'senha': CadastrarMedica_Senha
    })
    print('Médico Cadastrado')

def cadastrarPacientes():
    CadastrarPaciente_nome = input('Nome do Paciente:')
    CadastrarPaciente_CPF = input('Digite o CPF:')
    CadastrarPaciente_RG = input('Digite o RG:')
    CadastrarPaciente_CRM = input('Digite o CRM:')
    CadastrarPaciente_telefone = input('Telefone do Paciente:')
    CadastrarPaciente_endereco = input('Endereço do Paciente:')
    CadastrarPaciente_Sexo = input('Sexo(M/F):')
    CadastrarPaciente_Senha = input('Digite a senha de acesso:')
    lista_de_pacientes.append({
        'nome': CadastrarPaciente_nome,
        'CPF': CadastrarPaciente_CPF,
        'RG': CadastrarPaciente_RG,
        'CRM': CadastrarPaciente_CRM,
        'telefone': CadastrarPaciente_telefone,
        'endereco': CadastrarPaciente_endereco,
        'sexo': CadastrarPaciente_Sexo,
        'senha': CadastrarPaciente_Senha
    })
    print('Paciente Cadastrado')

def cadastrarConvenios():
    cadastrarConvenios_nome = input('Nome do Convênio:')
    cadastrarConvenios_CPF = input('Digite o CPF:')
    cadastrarConvenios_RG = input('Digite o RG:')
    cadastrarConvenios_CRM = input('Digite o CRM:')
    cadastrarConvenios_telefone = input('Telefone do Convênio:')
    cadastrarConvenios_endereco = input('Endereço do Convênio:')
    cadastrarConvenios_Sexo = input('Sexo(M/F):')
    cadastrarConvenios_Senha = input('Digite a senha de acesso:')
    lista_de_convenios.append({
        'nome': cadastrarConvenios_nome,
        'CPF': cadastrarConvenios_CPF,
        'RG': cadastrarConvenios_RG,
        'CRM': cadastrarConvenios_CRM,
        'telefone': cadastrarConvenios_telefone,
        'endereco': cadastrarConvenios_endereco,
        'sexo': cadastrarConvenios_Sexo,
        'senha': cadastrarConvenios_Senha
    })
    print('Convênio Cadastrado')

def marcarCompromisso():
    print("Marcar Compromisso")
    medico = buscarMedicos()
    if not medico:
        print("Médico não encontrado.")
        return
    
    paciente = buscarPacientes()
    if not paciente:
        print("Paciente não encontrado.")
        return
    
    data = input("Data do compromisso (Dia/Mês): ")
    horario = input("Horário do compromisso (Horário): ")
    
    lista_de_compromissos.append({
        'medico': medico['nome'],
        'paciente': paciente['nome'],
        'data': data,
        'horario': horario
    })
    print("Compromisso marcado com sucesso.")



def buscarMedicos():
    busca = input("Procurar médico (nome/CPF): ")
    
    if busca == "nome":
       
        nome = input("Digite o nome do médico: ")
        
        for medico in lista_de_medicos:
            
            if medico['nome'] == nome:
                print(medico)
                
                return medico
       
        print("Médico não encontrado.")
   
    elif busca == "cpf":
        
        cpf = input("Digite o CPF do médico: ")
        
        for medico in lista_de_medicos:
           
            if medico['CPF'] == cpf:
                
                print(medico)
               
                return medico
        print("Médico não encontrado.")
    else:
        print("Busca inválido.")

def buscarPacientes():
    busca = input("Procurar paciente (nome/CPF): ")
    if busca == "nome":
        
        nome = input("Digite o nome do paciente: ")
        
        for paciente in lista_de_pacientes:
            if paciente['nome'] == nome:
               
                print(paciente)
                
                return paciente
        print("Paciente não encontrado.")
    
    elif busca == "cpf":
       
        cpf = input("Digite o CPF do paciente: ")
        
        for paciente in lista_de_pacientes:
           
            if paciente['CPF'] == cpf:
                print(paciente)
               
                return paciente
        print("Paciente não encontrado.")
    else:
        print("Busca inválido.")

def buscarConvenios():
    busca = input("Buscar convênio por (nome/CPF): ")
    
    if busca == "nome":
        nome = input("Digite o nome do convênio: ")
       
        for convenio in lista_de_convenios:
           
            if convenio['nome'] == nome:
                print(convenio)
                return convenio
        
        print("Convênio não encontrado.")
    
    elif busca == "cpf":
        cpf = input("Digite o CPF do convênio: ")
        
        for convenio in lista_de_convenios:
            if convenio['CPF'] == cpf:
                print(convenio)
                return convenio
        print("Convênio não encontrado.")
    else:
        print("Critério inválido.")

def alterarMedicos():
    medico = buscarMedicos()
   
    if medico:
        print("Alterar os dados do médicos:")
        nome = input(f"Nome {medico['nome']}: ")
        CPF = input(f"CPF ({medico['CPF']}): ")
        RG = input(f"RG ({medico['RG']}): ")
        CRM = input(f"CRM ({medico['CRM']}): ")
        telefone = input(f"Telefone ({medico['telefone']}): ")
        endereco = input(f"Endereço ({medico['endereco']}): ")
        sexo = input(f"Sexo ({medico['sexo']}): ")
        senha = input(f"Senha ({medico['senha']}): ")

        medico.mudar({
            'nome': nome,
            'CPF': CPF,
            'RG': RG,
            'CRM': CRM,
            'telefone': telefone,
            'endereco': endereco,
            'sexo': sexo,
            'senha': senha
        })
        print("Dados do médico alterados com sucesso.")

def alterarPacientes():
    paciente = buscarPacientes()
    if paciente:
        print("Altere os dados do paciente. Deixe em branco para manter o valor atual.")
        nome = input(f"Nome ({paciente['nome']}): ") or paciente['nome']
        CPF = input(f"CPF ({paciente['CPF']}): ") or paciente['CPF']
        RG = input(f"RG ({paciente['RG']}): ") or paciente['RG']
        CRM = input(f"CRM ({paciente['CRM']}): ") or paciente['CRM']
        telefone = input(f"Telefone ({paciente['telefone']}): ") or paciente['telefone']
        endereco = input(f"Endereço ({paciente['endereco']}): ") or paciente['endereco']
        sexo = input(f"Sexo ({paciente['sexo']}): ") or paciente['sexo']
        senha = input(f"Senha ({paciente['senha']}): ") or paciente['senha']

        paciente.mudar({
            'nome': nome,
            'CPF': CPF,
            'RG': RG,
            'CRM': CRM,
            'telefone': telefone,
            'endereco': endereco,
            'sexo': sexo,
            'senha': senha
        })
        print("Dados do paciente alterados com sucesso.")

def marcarConsulta():
    
    print("Marcar Consulta")
    medico = buscarMedicos()
    if not medico:
        print("Médico não encontrado.")
        return
    
    paciente = buscarPacientes()
    if not paciente:
        print("Paciente não encontrado.")
        return
    
    data = input("Data da consulta (Dia/Mes:) ")
    horario = input("Horário da consulta (Horário): ")
    
    lista_de_consultas.append({
        'medico': medico['nome'],
        'paciente': paciente['nome'],
        'data': data,
        'horario': horario
    })
    print("Consulta marcada com sucesso.")



def emitirRelatorio():
   
    print("Relatório de Consultas")
    if not lista_de_consultas:
        print("Não há consultas marcadas.")
        return
    
    for consulta in lista_de_consultas:
        print(f"Médico: {consulta['medico']}, Paciente: {consulta['paciente']}, Data: {consulta['data']}, Horário: {consulta['horario']}")



def main():
    while True:
        lang = input("1 - Cadastrar Médico\n"
                     "2 - Cadastrar Pacientes\n"
                     "3 - Cadastrar Convênios\n"
                     "4 - Buscar Médicos\n"
                     "5 - Buscar Pacientes\n"
                     "6 - Buscar Convênios\n"
                     "7 - Alterar Médicos\n"
                     "8 - Alterar Pacientes\n"
                     "9 - Marcar Consulta\n"
                     "10 - Emitir Relatório\n"
                     "11 - Marcar compromisso\n"
                     "12 - Encerrar Programa\n"
                     "O que você deseja fazer? ")

        match lang:
            case "1":
                cadastrarMedicos()
            case "2":
                cadastrarPacientes()
            case "3":
                cadastrarConvenios()
            case "4":
                buscarMedicos()
            case "5":
                buscarPacientes()
            case "6":
                buscarConvenios()
            case "7":
                alterarMedicos()
            case "8":
                alterarPacientes()
            case "9":
                marcarConsulta()
            case "10":
                emitirRelatorio()
            case "12":
                print("Programa encerrado.")
            case "11":
                marcarCompromisso()
                break
            case _:
                print("Escolha uma opção válida")

        mais = input('Deseja fazer mais alguma coisa? (s/n): ')
        if mais != 's':
            print("Programa encerrado.")
            break

if __name__ == "__main__":
    main()
