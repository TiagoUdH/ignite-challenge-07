def recieve_index(contacts: dict) -> int:
  index = int(input("Digite o número do contato que deseja efetuar a ação: ")) - 1
  
  while not (index >= 0 and index < len(contacts)): 
    index = int(input("Identificação inválida! Digite o número do contato que deseja efetuar a ação: ")) - 1
  
  return index