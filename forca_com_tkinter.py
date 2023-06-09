import tkinter as tk
import tkinter.messagebox as messagebox
import random
import time

def verificar_palpite(event=None):
    global entrada
    global chute
    global chances
    global charada
    global mensagem_label
    global mensagem_erro_label
    global janela

    mensagem_erro = ''  # Inicializa a variável mensagem_erro

    palpite = entrada.get().upper()

    # CONTROLE DE PALPITE
    if len(palpite) > 1:
        mensagem_label['text'] = 'Só é permitida uma letra por vez'
        return

    if palpite in charada:
        chute.append(palpite)
    else:
        chances -= 1
        mensagem_erro = f'Você errou... \nVocê ainda tem {chances} chance(s)'

    correto = ''
    for letra_secreta in charada:
        if letra_secreta in chute:
            correto += letra_secreta
        else:
            correto += '*'

    mensagem_label['text'] = f'A palavra é {correto}'

    if correto == charada:
        mensagem_label['text'] = f'Parabéns, a palavra era {correto}.\nPelo seu conhecimento, você deve ter só mais uns 4 anos de vida....'
        time.sleep(2)
        reiniciar_jogo()

    if chances == 0:
        mensagem_label['text'] = 'Nunca foi num bloquinho de carnaval?'
        mensagem_label['text'] += f' A palavra era {charada}....'
        time.sleep(2)
        reiniciar_jogo()

    entrada.delete(0, tk.END)  # Limpa a caixa de texto
    

    if mensagem_erro:
        mensagem_erro_label['text'] = mensagem_erro

def reiniciar_jogo():
    global janela

    resposta = messagebox.askquestion('Reiniciar', 'Deseja jogar novamente?')
    if resposta == 'yes':
        janela.destroy()  # Fecha a janela atual
        forca()  # Inicia um novo jogo

def forca():
    global entrada
    global chute
    global chances
    global charada
    global mensagem_label
    global mensagem_erro_label
    global janela

    bd = ['COROTE','LOKAL','BAVARIA','CHANCELER','CATUABA','SERRANA','CHEVETTE','BALALAIKA','ASKOV','GLACIAL','CONTI','PRESIDENTE','TEQUILOKA','NATASHA','ITAIPAVA']
    palavra = ''
    chute = []
    chances = 3
    charada = random.choice(bd)

    janela = tk.Tk()
    janela.title('FORCA DE BEBIDAS')

    mensagem_label = tk.Label(janela, text='FORCA DAS BEBIDAS QUE A CADA GOLE, \nDIMINUEM A EXPECTATIVA DE VIDA EM 10 ANOS!!')
    mensagem_label.pack()

    dica = '' #APRESENTA UMA DICA, BASEADO NA PALAVRA QUE O CÓDIGO ESCOLHER PARA O JOGO
    if charada in ('LOKAL','BAVARIA','SERRANA','GLACIAL','CONTI','ITAIPAVA'):
        dica = 'DICA: É CERVEJA!'
    else:
        dica = 'DICA: É DESTILADO!'

    dica_label = tk.Label(janela, text=dica)
    dica_label.pack()

    entrada = tk.Entry(janela)
    entrada.pack()
    entrada.bind('<Return>', verificar_palpite)  # Associar o evento de pressionar Enter à função verificar_palpite

    botao = tk.Button(janela, text='Palpite', command=verificar_palpite)
    botao.pack()

    mensagem_erro_label = tk.Label(janela, text='')
    mensagem_erro_label.pack()

    janela.mainloop()

forca()
