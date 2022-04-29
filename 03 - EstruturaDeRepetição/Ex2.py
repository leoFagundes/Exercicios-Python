"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações."""

nome_usuario = 'admin'
senha = 'admin'

while nome_usuario == senha:
    nome_usuario = str(input("Nome de usuário: "))
    senha = str(input("Senha: "))
    if nome_usuario == senha:
        print("ERROR.the username is the same as the password.\n")

