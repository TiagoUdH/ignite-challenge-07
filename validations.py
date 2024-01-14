from email_validator import validate_email, EmailNotValidError
from phonenumbers import parse

def name_validation() -> str:
  name = input("Digite o nome do contato: ")
  
  while name == "":
    name = input("Nome inválido! Digite novamente o nome do contato: ")
  
  return name

def email_is_valid(email_str: str) -> str:
  try:
    email = validate_email(email_str).email
    
  except EmailNotValidError:
    return ""
    
  else:
    return email

def email_validation() -> str:
  email = input("Digite o e-mail do contato: ")
  
  while not email_is_valid(email):
    email = input("E-mail inválido! Digite novamente o e-mail do contato: ")
  
  return email

def phone_is_valid(phone: str) -> bool:
  try:
    number = parse(phone)
    
  except:
    return False
    
  else:
    return True


def phone_validation() -> str:
  phone = input("Digite o telefone do contato: ")
  
  while not phone_is_valid(phone):
    phone = input("Telefone inválido! Digite novamente o telefone do contato: ")
  
  return phone

def favorite_validation() -> str:
  char = input("Deseja favoritar o contato? [s/n] ")
  
  while char != "s" and char != "n":
    char = input("Preenchimento inválido! Deseja favoritar o contato? [s/n] ")
  
  return char