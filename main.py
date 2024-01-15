from validations import name_validation, email_validation, phone_validation, favorite_validation

contacts = []

def append_contact():
  contact = {}
  
  contact["name"] = name_validation()
  contact["email"] = email_validation()
  contact["phone"] = phone_validation()
  contact["favorite"] = favorite_validation()
  
  contacts.append(contact)
  print("Contato adicionado com sucesso!")
  
  return
  
def view_contacts():
  if not len(contacts):
    print("Não há nenhum contato salvo!")
    
    return
    
  print("Lista de contatos:")
  
  for index, contact in enumerate(contacts):
    favorite = "★" if contact["favorite"] else "☆"
    
    print(f"{index + 1}. {contact["email"]} {favorite}")
    
  return

while True:
  print("\nGerenciador de contatos:")
  print("1. Adicionar contato")
  print("2. Ver contatos")
  print("3. Ediar contato")
  print("4. Marcar/Desmarcar contato como favorito")
  print("5. Listar contatos favoritos")
  print("6. Apagar contato")
  print("7. Sair\n")
  
  option = input("Digite a sua opção: ")
  
  print()
  
  if option == "1":
    append_contact()
    
  elif option == "2":
    view_contacts()
    
  elif option == "7":
    break
  
  else:
    print("Opção inválida!")