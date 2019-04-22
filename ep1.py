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

def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "predio novo":"ir para o predio novo",
                "biblioteca": "Ir para a biblioteca"
            }
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
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
            "descricao": "Voce esta na biblioteca", #inventario multimetro
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                "ler":  "Ler Introdução à Programação com Python"
            }
        },
        "elevador": {
            "titulo": "Elevador da Sorte",
            "descricao":"Voce entrou no elevador",
            "opcoes":{}
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
            "descricao": "Voce resolveu entrar no aquario mas acabou sendo teletransportado para o fumodromo",
            "opcoes":{}
        },
        "fumodromo":{
            "titulo": "",
            "descricao":"Voce foi jogado no fumodromo",
            "opcoes":{
                "fumar":"ficar ai mesmo",
                "inicio":"Voltar para o saguao de entrada"
            }
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
            "titulo":"predio do toboga",
            "descricao":"",
            "opcoes":{
                "elevador":"subir de elevador",
                "escada": "ser fitness e subir de escada"
            }
        },
        "escada":{
            "titulo":"",
            "descricao":"",
            "opcoes": {
                "aquario": "Pegar missao impossivel de achar um aquario vazio!",
                "fablab": "tentar colar papelao no fablab"
            }
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

inventario={}
m="mickey"
c="chave"
p="papelao"

import random
def sorte_elevador():
    r=random.randint(1,3)
    subiu="PORTA ABRINDO!!!"
    preso="Voce esta preso no elevador"
    if r==1 or r==3:
        print (subiu)
        #colocar um if para ir para o aquario ou para outro lugar
    else:
        print (preso)

def main():
    print("Na hora do sufoco!")
    print("------------------\n")
    print("Parecia uma boa ideia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...\n")
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)\n")

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]

        print (nome_cenario_atual)
        print('-'*len(nome_cenario_atual))
        for tipo,v in cenario_atual.items():
            if tipo!="opcoes":
                print (v)
                print()
        opcoes = cenario_atual['opcoes']
            r=random.randint(1,2)
            subiu="PORTA ABRINDO!!!"
            preso="Voce esta preso no elevador"
            if r==1:
                print (subiu)
                cenario_atual=="saida do elevador"
            else:
                print (preso)
        '''
            nome_cenario_atual="saida do elevador"
        elif escolha=="fablab":
            if m not in inventario:
                print("ache a calca do mickey para poder entrar no fab lab")
                nome_cenario_atual="saida do elevador"
        elif escolha=="aquario":
            print ("Voce resolveu entrar no aquario mas acabou sendo teletransportado para o fumodromo")
            nome_cenario_atual="fumodromo"
        elif escolha in opcoes:
            nome_cenario_atual = escolha
        else:
            print("Sua indecisão foi sua ruína!")
            game_over = True

    print("Você morreu!")



# Programa principal.
if __name__ == "__main__":
    main()
    