#Esse é o projeto de um jogo de texto que estou fazendo com pythom. Espere falhas e erros e não espere codigos complexos pois sou um iniciante. Qualquer coisa só mandar a dica na aba de comentario ;) 
#Teste o jogo apenas colocando em algum lugar que suporte pythom e apertando play.

import time

inventario = []

def historia():
    print("\nVocê apareceu em uma floresta, você olha para os lados e vê apenas árvores e matos. Você está completamente perdido. Mas na sua frente você observa 3 caminhos.")
    pergunta = input("Qual deles você deseja ir?\n1- Um caminho Escuro mas que parece ter uma abundância de suprimentos\n2- Um caminho claro e com vacas e animais herbívoros de sobra\n3- Uma caverna escura, onde você não consegue saber o que tem nela.\n")

    if pergunta not in ['1', '2', '3']:
        print("\nEscolha uma das opções!\n")
        return historia()

    if pergunta == '1':
        print("Você morre, pois em um lugar como esse está recheado de predadores e ao entrar um lobo feroz com sua matilha te pega encurralado.")
        perdeu()

    elif pergunta == '2':
        print("Você morre, pois era um servo zombie.")
        perdeu()

    elif pergunta == '3':
        perguntaC = input("Neste lugar você pode encontrar um tesouro ou a saída desse lugar. Realmente deseja ir? (Y/N): ").lower()
        
        if perguntaC == 'y':
            print("Você entra com muito medo.")
            caverna()
        else:
            print("Você decide não arriscar e volta pelo mesmo caminho.")
            historia()

def perdeu():
    perdeu = input("\nVOCÊ PERDEU! Deseja recomeçar? (Y/N): ").lower()
    if perdeu == 'y':
        historia()
    else:
        exit()

def caverna():
    resposta = input("\nVocê está em um breu total, vê sons de morcegos irradiando a sala e algo parece bater em você.\nAutomaticamente você cai no chão e parece apertar um botão e uma luz forte acende, é um chapéu de mineiro!\nPegar? (Y/N): ").lower()

    if resposta not in ["y", "n"]:
        print("\nEscolha uma das opções!\n")
        return caverna()

    if resposta == "n":
        print("\nPor um motivo suicida você ignora o chapéu e desliga ele, ao se levantar você não sente mais o seu corpo. Algo desconhecido te matou.")
        perdeu()

    if resposta == "y":
        inventario.append("chapéu do mineiro")
        print("\nChapéu do mineiro agora está em seu inventário! Caso queira ver escreva 'i' na próxima pergunta!")
        caminhos()

def caminhos():
    caminho = input("\nDepois de caminhar muito você encontra 3 passagens, São 3 passagens iguais então é tentativa ou erro. Sua barriga ronca e você opta por se decidir mais rápido possível. \n1- Primeira passagem \n2- Segunda passagem \n3- Terceira passagem \n4- Vasculhar o local\n").lower()

    if caminho not in ["1", "2", "3", "4", "i"]:
        print("\nEscolha uma das opções!")
        return caminhos()

    if caminho == "4":
        print("\nVocê escolheu vasculhar o local.\nNo local você encontra um desenho na parede, você descreve o desenho em sua cabeça por causa da loucura.\n")
        desenhoparede()
    elif caminho == "i":
        print("Seu inventário contém:", inventario)
        caminhos()
    elif caminho == "2":
        caminho2()

def caminho2():
    print("\nVocê entra no segundo caminho e assim que você entra você escuta um barulho gigantesco vindo atrás de você! Ou você corre ou morre!\nVocê começa a correr loucamente sem olhar para trás e vê 2 passagens, você tem 5 segundos para decidir!")
    resposta = input("\n1- Direita\n2- Esquerda\n").lower()
    if resposta not in ["1", "2"]:
        print("\nEscolha uma das opções!")
        return caminho2()
    if resposta == "1":
        print("Você se encontra em um lugar sem saída, você se encolhe em posição fetal para esperar sua morte.")
        perdeu()
    if resposta == "2":
        print("Você acerta o caminho! Sua barriga gela e você agradece a Deus por conseguir! Mais à frente você vê uma ponte suspensa, parece velha e tudo que você fizer vai cair... Mas tem um monstro atrás de você, é morrer ou morrer.")
        pontee()

def pontee():
    print("\nVocê não tem tempo para pensar, mas por algum milagre conseguiu pensar em 2 coisas:\n1- Andar vagarosamente na ponte.\n2- Correr da ponte e rezar a Deus.")
    ponte = input("\nEscolha 1 ou 2: ").lower()
    if ponte not in ["1", "2"]:
        print("\nEscolha uma das opções!")
        return pontee()
    if ponte == "1":
        print("\nVocê escolheu andar vagarosamente.\nVocê anda devagar, mas o monstro não. Ele corre tão rápido na sua direção que, ao pular, a ponte quebra e ele cai em cima de você.")
        perdeu()
    if ponte == "2":
        print("Com seus últimos esforços você resolve correr, mas corre como se sua vida dependesse disso... E foi exatamente isso... O monstro, ao tocar na ponte, ela quebra imediatamente, mas por sorte da gravidade e de Isaac Newton, você consegue chegar ao fim da ponte antes dela cair.")



def desenhoparede():
    print("\n01100101 01110010 01110010 01100001 01100100 01101111 -- 01100011 01100101 01110010 01110100 01101111 -- 01100101 01110010 01110010 01100001 01100100 01101111\n")
    pergunta = input("\nAcabou por aqui? (Y/N): ").lower()
    if pergunta not in ["y", "n"]:
        print("\nEscolha uma das opções!")
        return desenhoparede()
    if pergunta == "y":
        print("\nVocê escolheu voltar.\n")
        caminho2()
    if pergunta == "n":
        print("Problema seu.")
        caminhos()
    


historia()
