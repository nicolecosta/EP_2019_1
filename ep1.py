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
                "Térreo":"Ir para o térreo",
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
                "elevador":"Chamar o elevador"
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
                "chocolate":"Ir até a máquina comprar um M&M",
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
    