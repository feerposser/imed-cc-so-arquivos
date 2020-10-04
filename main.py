import os, sys


def func1():
    with open("E:\imed-cc-so-arquivos\Pasta2\\arq6.txt", 'r') as file:
        print("caminho: ", file.name)
        print(file.read())


print(os.getcwd())

opcao = int(input("opcao: "))

if opcao == 1:
    func1()