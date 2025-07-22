from datetime import date

print("Olá turma do Python!")
print("Tudo bem!")
print("Bem-vindos ao programa introdutório!")

nome: str = input("Qual é o seu nome? ")
nome = nome.upper()
print(f"Olá, {nome}!")

idade: int = input("Quantos anos tem? ")

cidade: str = print("Em que cidade é que mora? ")

profissao = input("Qual é a sua profissão de sonho? ")

print(f"O/A {nome} tem {idade} anos de idade, e vive na localidade de {cidade}!")
print(f"A profissão de sonho de {nome} é ser {profissao}!")