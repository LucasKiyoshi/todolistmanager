def adicionar_tafefa(tarefas, nome_tarefa):
    tarefa = {
        "tarefa": nome_tarefa,
        "completada": False
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{nome_tarefa}' adicionada com sucesso!")
    return

def ver_tarefas(tarefas):
    print("\nLista de Tarefas:")
    for indice, tarefa in enumerate(tarefas, start = 1):
        status = "✔" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa} ")
    return

def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa ):
    indice_tarefa_ajustado = int(indice_tarefa) -1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas): 
        tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
        print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}!")
    else:
        print("Índice inválido. Tarefa não encontrada.")
    return

def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    tarefas[indice_tarefa_ajustado]["completada"] = True
    print(f"\n Tarefa {indice_tarefa} marcada como completada!")
    return

def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas: 
        if tarefa["completada"]==True:
            tarefas.remove(tarefa)
    print("\n Deletando tarefas completadas...")
    return
    
tarefas = []

while True:
    print ("\n Menu do Gerenciador de Lista de Tarefas:")
    print ("1. Adicionar Tarefa")
    print ("2. Ver Tarefas")
    print ("3. Atualizar Tarefa")
    print ("4. Completar Tarefa")
    print ("5. Deletar Tarefas Completadas")
    print ("6. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa: ")
        adicionar_tafefa(tarefas, nome_tarefa)
    elif escolha == "2":
        ver_tarefas(tarefas)
    elif escolha == "3":
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite o número da tarefa que deseja atualizar: ")
        novo_nome = input("Digite o novo nome da tarefa: ")
        atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)
    elif escolha == "4":
        ver_tarefas(tarefas)
        indice_tarefa= input("Digite o número da tarefa que deseja completar: ")
        completar_tarefa(tarefas, indice_tarefa)
    elif escolha == "5":
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)
    elif escolha == "6":
        break

    print("Programa finalizado")
