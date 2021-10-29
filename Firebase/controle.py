import os
import stat
from datetime import datetime
from appFire import *


def control(user):
    # Verifica se o arquivo existe
    if os.path.isfile("controle.txt"):
        # Modifica a permissão do arquivo para leitura, escrita e execução
        os.chmod("controle.txt", stat.S_IRWXU)

    # Abre o arquivo para escrita
    arquivo = open("controle.txt", 'a')
    data = datetime.now()
    # Escreve no arquivo
    arquivo.write(f'Login: {user} , {data} \n')
    #arquivo.write("\n")
    # Fecha o arquivo
    arquivo.close()

    # Modifica o arquivo apenas para leitura
    os.chmod("controle.txt", stat.S_IRUSR)

