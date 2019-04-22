#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 12:54:13 2019

@author: beatriz
"""
# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Beatriz Lourenço, beatrizcpl@al.insper.edu.br
# - aluno B: Nicole Costa, nicolesac@al.insper.edu.br

import random

def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Entrada do Insper",
            "descricao": "Voce esta na entrada do Insper",
            "opcoes": {
                "predio novo":"Ir para o predio novo",
                "seguir professor":"Seguir o professor até a sala",
            }
        },
        "seguir professor": {
            "titulo": "Momento do Desespero",
            "descricao": "Você chegou à sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor"
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca", 
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                "ler":  "Ler Introdução à Programação com Python"
            }
        },
        "ler":{
            "titulo":"Eu Devia Ter Lido Esse Livro",
            "descricao":"Bom Agora Nem Adianta",
            "opcoes":{
                "inicio":"Voltar para o saguão da entrada",
                "cochilo":"Esse sofá seria ideal para um cochilo..."
            }
        },
        "cochilo":{
            "titulo":"O sono dos universitários",
            "descricao":"O MONSTRO DO SONO PROFUNDO TE PEGOU!!!",
            "opcoes":{
                "café":"Tomar café para atacar o monstro",
                "amigos":"Tomar café com o monstro"
            }
        },
        "café":{
            "titulo":"Em busca de café",
            "descricao":"O café te deixou hiperativo",
            "opcoes":{
                "escadas":"Subir correndo até o sexto andar de escada",
                "inicio":"Voltar para o saguão e correr em círculos"
            }
        },
        "amigos":{
            "titulo":"Sempre Quis Ter um Amigo Monstro",
            "descricao":"O monstro te abandonou e foi atrás dos estudantes de administração",
            "opcoes":{
                "inicio":"Voltar para o saguão",
                "elevador":"Chamar o elevador"
            }
        },
        "elevador": {
            "titulo": "Elevador da Sorte",
            "descricao":"Voce entrou no elevador",
            "opcoes":{
                "inicio":"Ir para o térreo",
                "1":"Ir para o primeiro andar",
                "2":"Ir para o segundo andar",
                "3":"Ir para o terceiro andar",
                "4":"Ir para o quarto andar",
                "5":"Ir para o quinto andar",
                "6":"Ir para o sexto andar"
            }
        },
        "1":{
            "titulo":"Porta Abrindo",
            "descricao":"Primeiro Andar",
            "opcoes":{
                "elevador":"Chamar o elevador",
                "comprar cookie":"Comprar um cookie"
            }
        },
        "2":{
            "titulo":"Segundo Andar",
            "descricao":"O Andar do Escorregador",
            "opcoes":{
                "inicio":"Descer de escorregador até o saguão",
                "investigar":"Ver se o Raul está escondido dentro do escorregador",
                "elevador":"Chamar o elevador"
            }
        },
        "3":{
            "titulo":"Terceiro Andar",
            "descricao":"Porta Abrindo",
            "opcoes":{
                "help desk":"Perdir help pra desk",
                "fablab":"Talvez eu consiga fazer um clone do Raul...Isso facilitaria a minha busca",
                "elevador":"Chame o elevador"
            }
        },
        "4":{
            "titulo":"Make 4 andar Great Again",
            "descricao":"Quarto Andar. Porta Abrindo",
            "opcoes":{
                "pergunta":"perguntar para a primeira pessoa que passar se ela viu o Raul",
                "chocolate":"Ir até a máquina comprar um M&M (+1 energia)",
                "elevador":"Chamar o elevador"
            }
        },
        "5":{
            "titulo":"Quinto Andar",
            "descricao":"Labs, labs, labs",
            "opcoes":{
                "realidade virtual":"Ir para o laboratório de realidade virtual",
                "supercomputação":"Ir para o laboratório de supercomputação",
                "elevador":"chamar o elevador"
            }
        },
        "6":{
            "titulo":"Cobertura",
            "descricao":"Espero que o Raul esteja aqui..."
                        "Quero curtir minha Pascoa e deixar o EP só pro mês que vem.",
            "opcoes":{
                "sacada":"Ir para a sacada",
                "geladeira":"Ver se tem alguma comida na geladeira",
                "elevador":"Chamar o elevador"
            }
        },
        "geladeira":{
            "titulo":"COOKIE MONSTER",
            "descricao":"HA HA HA vou te prender na geladeira!!!",
            "opcoes":{
                "arrego":"pedir socorro para os bombeiros",
                "cookies":"alimentar o cookie monster até que ele exploda"
            }
        },
        "arrego":{
            "titulo":"NINGUÉM ESTÁ A SALVO",
            "descricao":"O cookie monster capturou o bombeiro também",
            "opcoes":{
                "cookies":"alimentar o cookie monster até explodir"
            }
        },
        "cookies":{
            "titulo":"Você está dando toda a comida da geladeira para o cookie monster, ele está inflando",
            "decsricao":"BOOM!!! O cookie monster explodiu",
            "opcoes":{
                "sacada":"Ir para a sacada",
                "Chá":"Assustei depois dessa, preciso de um chazinho",
                "elevador":"Sair desse andar"
            }
        },
        "sacada":{
            "titulo":"UAU QUE LINDO",
            "descricao":"Talvez o Raul curta essa vista também",
            "opcoes":{
                ""
            }
        },
        "chocolate":{
            "titulo":"123 kcal",
            "descricao":"HGSHGRH QUEM OUSA ROUBAR MEU M&M??",
            "opcoes":{
                "lutar":"lutar pelo seu chocolate",
                "fugir":"Trocar M&M por sanduíche vegano"
            }
        },
        "saida do elevador":{
            "titulo": "Caminho",
            "descricao": "",
            "opcoes": {
                "aquario": "Pegar missao impossivel de achar um aquario vazio!",
                "fablab": "tentar colar papelao no fablab"
            }
        },
        "aquario": {
            "titulo": "Unico aquario vazio",
            "descricao": "Voce resolveu entrar no aquario mas acabou sendo teletransportado para a realidade virtual",
            "opcoes":{}
        },
        "fablab":{
            "titulo":"", #calca do mickey (inventario), no fablab voce pode fazer uma chave?
            'descricao': "",
            "opcoes": {
                "papelao":"colar algumas coisas com super cola", #add inventario carrro de papelao
                "3d":"tentar usar a impressora 3D"  #chave            
            }
        },
        "predio novo":{
            "titulo":"Prédio do Tobogã",
            "descricao":"UHUUUUUU",
            "opcoes":{
                "elevador":"subir de elevador",
                "escada": "ser fitness e subir de escada",
                "biblioteca": "Ir para a biblioteca"
            }
        },
        "escada":{
            "titulo":"",
            "descricao":"",
            "opcoes": {
                "aquario": "Pegar missão mpossíel de achar um aquário vazio!",
                "fablab": "fazer carrinho de papelão no fablab"
            }
        },
        "realidade virtual":{
            "titulo":"Lucy in the Sky with Diamonds",
            "descricao":"Voce entrou no mundo do Mario Kart!",
            "opcoes":{
                "unicornio":"Dar uma volta de unicórnio pelos ladrilhos de arco-íris",
                "lua":"Passear pelas crateras lunares"
            }
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

inventario={}
mickey="calca do mickey"
chave="chave"
carriho_de_papelao="papelao"
cookie="cookie"

nickname=input('nickname: ')    


def main():
    print("Na hora do sufoco!")
    print("------------------\n")
    print("Parecia uma boa ideia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...\n")
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)\n")

    cenarios, nome_cenario_atual = carregar_cenarios()
    nivel_de_energia=10
    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]

        print(nome_cenario_atual)
        print('-'*len(nome_cenario_atual))
        print("Nível de Energia: {0}".format(nivel_de_energia))
        if nivel_de_energia<=2:
        print("Acha bonito né, {0}".format(nickname))
        if nivel_de_energia <= 2:
            print("{0}, sua energia está se esgotando".format(nickname))
        
        for tipo,v in cenario_atual.items():
            if tipo!="opcoes":
                print (v)
                print()
        opcoes = cenario_atual['opcoes']
        for k,v in opcoes.items():
            print ("{0}: {1}".format(k,v))
        escolha = input("Qual é a sua escolha? ")
            

        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        elif opcoes == "elevador":
            ran=random.randit(1,30)
            if ran>22:
                print("VOCÊ ESTÁ PRESO!! O ELEVADOR QUEBROU")
                escolha = input("Qual é a sua escolha? ")
            else:
                print ("PORTA ABRINDO!!!")
                for k, v in cenarios["elevador"]["opcoes"].items():
                    print ("{0}: {1}".format(k,v))
                    nome_cenario_atual="saida do elevador"
        elif escolha=="café":
            if nivel_de_energia<10:
                nivel_de_energia+=1
        elif escolha=="fablab":
            if "mickey" not in inventario:
                print("{0} ache a calca do mickey para poder entrar no fab lab".format(nickname))
                nome_cenario_atual="saida do elevador"
        elif escolha=="3d":
            inventario['chave']="chave"
            nome_cenario_atual="saida do elevador"
        elif escolha=="papelao":
            inventario["carrinho de papelao"]="carrinho de papelao que nao serve para nada"
            nome_cenario_atual="fablab"
        elif escolha=="aquario":
            print ("Você resolveu entrar no aquário mas acabou sendo teletransportado para uma realidade virtual")
            nome_cenario_atual="realidade virtual"
        elif escolha=="lutar":
            jogador=input("pedra, papel ou tesoura: ")
            mmonster=random.choice(['pedra','papel','tesoura'])
            if jogador=='pedra' and mmonster=='tesoura':
                print("Você consegui combater o monstro do M&M!!")
            elif jogador=='pedra' and mmonster=='papel':
                print("O monstro comeu você e o M&M")
            elif jogador=='papel' and mmonster=='tesoura':
                print("O monstro comeu você e o M&M")
            elif jogador=='papel' and mmonster=='pedra':
                print("Você consegui combater o monstro do M&M!!")
            elif jogador=='tesoura' and mmonster=='papel':
                print("Você consegui combater o monstro do M&M!!")
            elif jogador=='tesoura' and mmonster=='pedra':
                print("O monstro comeu você e o M&M")
            elif jogador==mmonster:
                print('EMPATE! Divida o M&M com o monstro, ele tem fome também')
            nome_cenario_atual="4"    
        elif escolha=="professor":
            if "chave" not in inventario:
                print ("Ache a chave para entrar na sala do professor")
                nome_cenario_atual="andar do professor"
        elif escolha=="comprar cookie":
            inventario['cookie']="cookie"
            with open('cookiebia.txt','r') as arquivo:
                conteudo=arquivo.read()
                print (conteudo)
            nome_cenario_atual="1"
        elif escolha=="cookies":
            if 'cookie' not in inventario:
                print("Você não tem um cookie para dar ao cookie monster, que pena!")
                nivel_de_energia-=3
                nome_cenario_atual="6"
        elif escolha=="realidade virtual":
            print ("")
        elif escolha in opcoes:
            nome_cenario_atual = escolha
        else:
            print("Sua indecisão foi sua ruína!")
            game_over = True
            

             
        

    print("Você morreu!")



# Programa principal.
if __name__ == "__main__":
    print("Acha bonito né, {0}".format(nickname))
    main()
            
