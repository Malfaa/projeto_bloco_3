prescricoes=[]

"""_summary_
metadados explicados:
    ID da tarefa -> ID da Prescrição
    descrição -> Resumo da Prescrição
    data de criação -> Data de Emissão
    status -> Status da Prescrição
    prazo final -> Data de Validade da Receita
    prioridadeprescricao_prioridadeência -> Prioridade / Tipo de Uso
    entre outros atributos... -> {
        registro_profissional,
        assinatura_digital
    }
"""

def adicionar_prescricao():
  """ Função que cria uma nova prescrição e adiciona a lista de prescrições"""
  print("=== Adicionar Tarefa ===\n")

  prescricao_id = input("ID da Prescrição (Ex:1): ")
  prescricao_desc = input("Descrição (Ex: 'Amoxicilina para João'): ")
  prescricao_emissao = input("Data de Emissão (dd/mm/aaaa): ")
  prescricao_validade = input("Data de Validade (dd/mm/aaaa): ")
  prescricao_prioridade = input("Prioridade (Ex: 'Uso Contínuo', 'Padrão'): ")
  prescritor = input("Nome do Prescritor: ")
  registro_profissional = input("Registro do prescritor (Ex: CRF-SP: 00001): ")

  for p in prescricoes:
      if p['id'] == prescricao_id:
          print("\nERRO: Já existe uma prescrição com este ID. Tente novamente.")
          return

  nova_prescricao = {
    'id': prescricao_id,
    'descricao': prescricao_desc,
    'emissao': prescricao_emissao,
    'status': "PENDENTE",
    'validade': prescricao_validade,
    'prioridade': prescricao_prioridade,
    'prescritor': prescritor,
    'registro': registro_profissional
  }
  prescricoes.append(nova_prescricao)
  print("\nPrescrição adicionada com sucesso!")

def listar_prescricoes():
  """Funçao que faz a listagem de todas as prescrições disponíveis"""
  print("=== Listar Prescrições ===\n")

  if len(prescricoes) == 0:
    print("Não há prescrições disponíveis.\n")
  else:
    for p in prescricoes:
      print(f"ID: {p['id']} | Descrição: {p['descricao']} | Status: {p['status']}")
      print(f"Data de Emissao: {p['emissao']} | Data de Validade: {p['validade']} | Prioridade: {p['prioridade']}")
      print(f"Prescritor: {p['prescritor']} | Registro do Prescritor: {p['registro']}")
      print("===========---============")

def selecionar_prescricao():
    """Função que possibilita escolher entre ações em uma prescrição específica (Marcar/Remover)."""
    print("\n=== Selecionar Prescrição ===")
    id = input("Digite o ID da prescrição desejada: ")

    prescricao_existe = any(p['id'] == id for p in prescricoes)

    if not prescricao_existe:
        print(f"\nERRO: Prescrição com ID {id} não encontrada.")
        return

    while True:
        print("\nEscolha uma ação para a prescrição ID", id)
        print("1. Marcar como Dispensada")
        print("2. Remover Prescrição")
        print("3. Voltar ao menu principal")

        opcao = input("Digite sua escolha: ")

        if opcao == '1':
            marcar_dispensado(id)
            break
        elif opcao == '2':
            remover_prescricao(id)
            break
        elif opcao == '3':
            break
        else:
            print("Opção inválida, tente novamente.")


def marcar_dispensado(id):
  """Busca uma prescrição pelo ID e atualiza seu status para DISPENSADA."""
  print("=== Marcar Tarefa como Concluída ===\n")
  for p in prescricoes:
    if p['id'] == id:
        p['status'] = "DISPENSADA"
        print(f"Sucesso: Prescrição ID {id} marcada como DISPENSADA.\n")
        return

  print(f"\nERRO: Prescrição com ID {id} não encontrada.")

def remover_prescricao(id):
  """Busca uma prescrição pelo ID e a remove da lista."""
  print("=== Remover Tarefa ===\n")
  prescricao_encontrada = None
  for p in prescricoes:
        if p['id'] == id:
            prescricao_encontrada = p
            break

  if prescricao_encontrada:
      prescricoes.remove(prescricao_encontrada)
      print(f"Sucesso: Prescrição ID {id} foi removida.\n")
  else:
      print(f"ERRO: Prescrição com ID {id} não encontrada.\n")


while True:
    """_Main Loop_ loop gera o menu no terminal, assim podendo escolher qual opção"""
    print("=== Gestão de Prescrições === \n\nEscolha sua opção:")
    print("1. Listar Prescrições")
    print("2. Adicionar Prescrição")
    print("3. Selecionar uma Prescrição (Marcar/Remover)")
    print("0. Sair do programa")

    escolha = input("Digite um número: ")
    match escolha:
        case 1:
            listar_prescricoes()
        case 2:
            adicionar_prescricao()
        case 3:
            selecionar_prescricao()
        case 0:
            break
        case _:
            print("\nComando inválido, tente novamente!")