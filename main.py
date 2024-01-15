from utils import recieve_index
from validations import name_validation, email_validation, phone_validation, favorite_validation

contacts = []

def has_contact():
  if not len(contacts):
    print("Não há nenhum contato salvo!")
    
    return False
  
  return True

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
  print("Lista de contatos:")
  
  for index, contact in enumerate(contacts):
    favorite = "★" if contact["favorite"] else "☆"
    
    print(f"{index + 1}. {contact["name"]} {favorite}")
    
  return

def edit_contact():
  view_contacts()
  
  print()
  
  index = recieve_index(contacts)
  contact = contacts[index]
  
  print(f"Nome atual do contato: {contact["name"]}")
  contact["name"] = name_validation()
  
  print(f"E-mail atual do contato: {contact["email"]}")
  contact["email"] = email_validation()
  
  print(f"Telefone atual do contato: {contact["phone"]}")
  contact["phone"] = phone_validation()
  
  favorite = "" if contact["favorite"] else "não"
  print(f"O contato {favorite}está entre os favoritos")
  contact["favorite"] = favorite_validation()
  
  contacts[index] = contact
  print("Contato editado com sucesso!")
  
  return
  
def update_favorite():
  view_contacts()
  
  print()
  
  index = recieve_index(contacts)
  contact = contacts[index]
  
  contact["favorite"] = not contact["favorite"]
  
  contacts[index] = contact
  print("Contato editado com sucesso!")
  
  return
  
def view_favorites_contacts():
  favorites_contacts = list(filter(lambda contact: contact["favorite"], contacts))
  
  if not favorites_contacts:
    print("Você não possui um contato favorito")
    
    return
  
  print("Lista de contatos favoritos:")
  
  for index, contact in enumerate(favorites_contacts):
    print(f"{index + 1}. {contact["name"]}")
    
  return

def delete_contact():
  view_contacts()
  
  print()
  
  index = recieve_index(contacts)
  contacts.remove(contacts[index])
  
  print("Contato apagado com sucesso!")
  
  return

while True:
  print("\nGerenciador de contatos:")
  print("1. Adicionar contato")
  print("2. Ver contatos")
  print("3. Editar contato")
  print("4. Marcar/Desmarcar contato como favorito")
  print("5. Listar contatos favoritos")
  print("6. Apagar contato")
  print("7. Sair\n")
  
  option = input("Digite a sua opção: ")
  
  print()
  
  if option == "1":
    append_contact()
    
  elif option == "2":
    if has_contact():
      view_contacts()
    
  elif option == "3":
    if has_contact():
      edit_contact()
      
  elif option == "4":
    if has_contact():
      update_favorite()
      
  elif option == "5":
    if has_contact():
      view_favorites_contacts()
      
  elif option == "6":
    if has_contact():
      delete_contact()
    
  elif option == "7":
    break
  
  else:
    print("Opção inválida!")