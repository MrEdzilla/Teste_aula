from datetime import date

print("Olá turma do Python!")
print("Tudo bem!")
print("Bem-vindos ao programa introdutório!")

nome: str = input("Qual é o seu nome? ")
nome = nome.upper()
print(f"Olá, {nome}!")

idade: int = input("Quantos anos tem? ")

ano_atual = date.today().year
ano_nascimento = ano_atual - idade

cidade: str = print("Em que cidade é que mora? ")

profissao = input("Qual é a sua profissão ")

print(f"O/A {nome} e vive na localidade de {cidade}!")
print(f"Nasceu no ano de {ano_nascimento} e, como tal, tem {idade} anos de idade!")
print(f"A profissão de {nome} é {profissao}!")

print(f"\nResumo:")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Cidade: {cidade}")
print(f"Profissão: {profissao}")