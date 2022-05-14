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
    if escolha == 1:
        opção1()
    elif escolha == 2:
        opção2()
    elif escolha == 3:
        print("\033[32mVolte sempre!\033[m")
        break
    else:
        print("\033[31mopção invalida tente novamente!\033[m")
        sleep(2)
