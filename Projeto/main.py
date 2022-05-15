from Interface import *
from time import sleep

while True:
    MenuPrincipal()
    while True:
        try:
            escolha = int(input("\033[33mSua opção: \033[m"))
        except:
            print('\033[31mOcorreu um erro tente novamente\033[m')
        else:
            break
    
    # filtrando Escolhas
    if escolha == 1:
        opção1()

        # Tratamento de erro
        try:
            # Leitura de Dados
            with open('BD.txt','r') as file:
                print(file.read())

        except FileNotFoundError:
            print('Sem Cadastros'.center(40))
            sleep(1.5)
        except:
            print('\033[31mErro!! Tente novamente\033[m')
        else:
            sleep(2.5)

    elif escolha == 2:
        opção2()
        # Tratamento de erro
        while True:
            try:
                nome = str(input("Digite o nome da pessoa: "))
            except:
                print('\033[31mOcorreu um erro tente novamente\033[m')
            else:
                break

        while True:
            try:
                idade = int(input("Digite a idade da pessoa:"))
            except:
                print('\033[31mOcorreu um erro tente novamente\033[m')
            else:
                print("\033[32mCadastro feito com sucesso!!!\033[m")
                sleep(1)
                break

        # Armazenado Dados
        with open('BD.txt','a') as file:
            file.write(f'{nome}\t\t\t{idade} Anos' + '\n')

    elif escolha == 3:
        print("\033[32mVolte sempre!\033[m")
        break
    else:
        print("\033[31mOpção invalida tente novamente!\033[m")
        sleep(1)

