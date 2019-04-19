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
                "andar professor": "Tomar o elevador para o andar do professor",
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
                "inicio": "Voltar para o saguao de entrada"
            }
        },
        "elevador": {
            "titulo": "Elevador da Sorte",
            "descricao":"Voce entrou no elevador",
            "opcoes":{}
        },
        "saiu do elevador":{
            "titulo": "Caminho",
            "descricao": "Para onde voce que ir agora?",
            "opcoes": {
                "aquario": "Pegar missao impossivel de achar um aquario vazio!",
                "fablab": "tentar colar papelao no fablab"
            }
        },
        "aquario": {
            "titulo": "Unico aquario vazio",
            "descricao": "Voce resolveu entrar no aquario mas acabou sendo teletransportado para o fumodromo",
            "opcoes":{
                "Ir para o fumodromo"
            }
        },
        "fumodromo":{
            "titulo": "",
            "descricao":"Voce foi jogado no fumodromo",
            "opcoes":{
                "ficar ai mesmo",
                "Voltar para o saguao de entrada"
            }
        },
        "fablab":{
            "titulo":"", #calca do mickey (inventario), no fablab voce pode fazer uma chave?
            'descricao': "",
            "opcoes": {
                ""
                ""              
            }
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual
'''
import random
r=random.randint(1,2)
subiu="PORTA ABRINDO!!!"
preso="Voce esta preso no elevador"
if r==1:
    print (subiu)
    #colocar um if para ir para o aquario ou para outro lugar
else:
    print (preso)

'''

def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa ideia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

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
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            for k,v in opcoes.items():
                print ("{0}: {1}".format(k,v))
            escolha = input("Para onde quer ir? ")

            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()