import pywhatkit
from datetime import datetime
from time import sleep
from pynput.keyboard import Key, Controller


def fechar_guia():
    """Gera um comando de 'CTRL' + 'W' para fechar
    a guia do navegador
    """
    tecla = Controller()
    tecla.press(Key.ctrl)
    tecla.press('w')
    tecla.release(Key.ctrl)
    tecla.release('w')


def carregar_lista():
    """Carregar lista de contatos no array 'lista'
    """

    try:
        lista = list()
        with open('contatos.txt', 'r') as arq:
            for valor in arq:
                lista.append(valor.replace('\n', ''))
    except:
        print('Erro ao localizar o arquivo!')
    finally:
        arq.close()
    return lista


def enviar_mensagem(msg='Olá'):
    """Realiza o envio de mensagem para os contatos
    """
    carregar_lista()
    lista = carregar_lista()
    cont = 0
    listaSucesso = list()
    listaFalha = list()

    while cont < len(lista):

        try:
            print(f'Enviando para: {lista[cont]}')
            pywhatkit.sendwhatmsg(lista[cont], msg,
                                  datetime.today().hour, datetime.today().minute + 1, wait_time=5)
        except:
            print(f'Falha ao enviar para: {lista[cont]}')
            listaFalha.append(lista[cont])
            cont += 1
            continue
        else:
            listaSucesso.append(lista[cont])
            sleep(5)
            fechar_guia()

            # Caso seja o último item da lista
            # não precisará contar até 60s
            if cont == len(lista) - 1:
                break

            sleep(60)
            cont += 1

    print('\033[7m\n -> Mensagens enviadas!\033[m')
    print(f'\033[32mEnvios realizados com sucesso: {listaSucesso}\033[m')
    print(f'\033[31mFalha no envio: {listaFalha}\033[m')
