# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Beatriz Lourenço, beatrizcpl@al.insper.edu.br
# - aluno B: Nicole Costa, nicolesac@al.insper.edu.br

import random
t="t"
p="p"
def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Entrada do Insper",
            "descricao": "Voce esta na entrada do Insper",
            "opcoes": {
                "predio novo":"Ir para o prédio novo",
                "seguir professor":"Seguir o professor até a sala",
            }
        },
        "seguir professor": {
            "titulo": "Momento do Desespero",
            "descricao": "Você chegou à sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguão de entrada",
                "professor": "Falar com o professor"
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao":"Você foi pedir para o professor adiar o EP."
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {
                "fim":"E agora?"
            }
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Você está na biblioteca", 
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
        "escadas":{
            "titulo":"UHUUUUU acho que nunca andei de escada antes",
            "descricao":"Não sei se faria isso se não tivesse tomado café",
            "opcoes":{
                "6":"Você chegou ao sexto andar"
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
            "descricao":"Você entrou no elevador",
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
                "comprar cookie":"Comprar um cookie",
                "aquario": "Tentar missão impossível de achar um aquário vazio em horário de pico!"
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
        "investigar":{
            "titulo":"BU!!",
            "descricao":"O Raul não está aqui, ao menos você se divertiu descendo o escorregador até o térreo!",
            "opcoes":{
                "elevador":"Chamar o elevador"
            }
        },
        "help desk":{
            "titulo":"O help desk está fechado...",
            "descricao":"Volte mais tarde",
            "opcoes":{
                "fablab":"Talvez eu consiga fazer um clone do Raul...Isso facilitaria a minha busca",
                "elevador":"Chamar o elevador"
            }
        },
        "pergunta":{
            "titulo":"Você pergunta ao zelador se ele viu o Raul",
            "descricao":"Acontece que não tem zelador, você deve estar delirando"
            "Esse EP deve estar mexendo com a sua mente...",
            "opcoes":{
                "chocolate":"Ir até a máquina comprar um M&M (+2 energia)",
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
                "chá":"Assustei depois dessa, preciso de um chazinho",
                "elevador":"Sair desse andar"
            }
        },
        "chá":{
            "titulo":"Tomando cháziho da tarde",
            "descricao":"Até parece a Rainha Elizabeth",
            "opcoes":{
            "sacada":"ir para a sacada",
            "elevador":"chamar o elevador"
            }
        },
        "sacada":{
            "titulo":"UAU QUE LINDO, talvez o Raul curta essa vista também",
            "descricao":"Porém o Raul também não está na sacada :)",
            "opcoes":{
                "elevador":"Entrar e chamar o elevador"
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
        "fugir":{
            "titulo":"Está fugindo do monstro como está fugindo do EP não é mesmo??",
            "descricao":"Mas fugir nem sempre funciona...",
            "opcoes":{
                "pergunta":"perguntar para a primeira pessoa que passar se ela viu o Raul",
                "elevador":"Chamar o elevador"
            }
        },
        "aquario": {
            "titulo": "Único aquário vazio",
            "descricao": "Você resolveu entrar no aquario mas acabou sendo teletransportado para um universo paralelo"
        },
        "fablab":{
            "titulo":"O famoso FABLAB",
            'descricao': "A segunda casa dos bixos de engenharia",
            "opcoes": {
                "papelao":"colar algumas coisas com super cola", 
                "3D":"tentar usar a impressora 3D"              
            }
        },
        "3D":{
            "titulo":"Você acabou de entrar na faculdade e ainda não sabe mexer muito bem na impressora 3D",
            "descricao":"Cuidado para os técnicos não te expulsarem de lá",
            "opcoes":{
                "chave":"Imprimir chave na impressora 3D",
                "3":"Retornar ao terceiro andar"
            }
        },
        "predio novo":{
            "titulo":"Prédio do Tobogã",
            "descricao":"UHUUUUUU",
            "opcoes":{
                "elevador":"subir de elevador",
                "escadas": "ser fitness e subir de escada",
                "biblioteca": "Ir para a biblioteca"
            }
        },
        "realidade virtual":{
            "titulo":"Lucy in the Sky with Diamonds",
            "descricao":"Voce entrou no mundo do Mario Kart!",
            "opcoes":{
                "unicornio":"Dar uma volta de unicórnio pelos ladrilhos de arco-íris",
                "lua":"Passear pelas crateras lunares"
            }
        },
        "lua":{
            "titulo":"Lua de chocolate",
            "descricao":"Voce encontrou uma lua de chocolate! Pena que vce descobriu que é intolerante à lactose :(",
            "opcoes":{
                "5":"Voltar para o quinto andar"
            }
        },
        "unicornio":{
            "titulo":"Unicornio de glitter",
            "descricao":"Voce encontrou um unicornio e resolveu viajar pelo arco-iris com ele!",
            "opcoes":{
                "5":"Pena que voce tem que oltar para o quinto andar e adiar o EP"
            }
        },
        "fim":{
            "titulo":"Parece que chegamos ao fim não é mesmo",
            "descricao":"E agora? Acho que ninguém sabe ainda..."
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

#itens do inventário
inventario={}
mickey="calça do mickey"
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
            
        if nivel_de_energia <= 2:
            print("{0}, sua energia está se esgotando".format(nickname))
            
        if nivel_de_energia==0:
            game_over=True
        
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
            
        elif opcoes == "elevador":
            ran=random.choice([t,t,t,t,t,t,t,t,p])
            if ran==p:
                print("VOCÊ ESTÁ PRESO!! O ELEVADOR QUEBROU")
                game_over=True
            else:
                print ("PORTA ABRINDO!!!")
                for k, v in cenarios["elevador"]["opcoes"].items():
                    print ("{0}: {1}".format(k,v))
                    
        elif escolha=="café":
            if nivel_de_energia<10:
                nivel_de_energia+=1
                
        elif escolha=="fablab":
            if "mickey" not in inventario:
                print("{0} ache a calca do mickey para poder entrar no fab lab".format(nickname))
                nome_cenario_atual="elevador"
            else:
                nome_cenario_atual="fablab"
                
        elif escolha=="3d":
            inventario['chave']="chave"
            nome_cenario_atual="elevador"
            
        elif escolha=="papelao":
            inventario["carrinho de papelao"]="carrinho de papelao que nao serve para nada"
            nome_cenario_atual="fablab"
            
        elif escolha=="aquario":
            print ("Você resolveu entrar no aquário mas acabou sendo teletransportado para uma realidade virtual")
            nome_cenario_atual="realidade virtual"
            
        #Pedra, papel, tesoura com o monstro
        elif escolha=="lutar":
            jogador=input("pedra, papel ou tesoura: ")
            mmonster=random.choice(['pedra','papel','tesoura'])
            if jogador=='pedra' and mmonster=='tesoura':
                print("Você consegui combater o monstro do M&M!!")
                nivel_de_energia+=2
            elif jogador=='pedra' and mmonster=='papel':
                print("O monstro comeu você e o M&M")
                nivel_de_energia-=2
            elif jogador=='papel' and mmonster=='tesoura':
                print("O monstro comeu você e o M&M")
                nivel_de_energia-=2
            elif jogador=='papel' and mmonster=='pedra':
                print("Você consegui combater o monstro do M&M!!")
                nivel_de_energia+=2
            elif jogador=='tesoura' and mmonster=='papel':
                print("Você consegui combater o monstro do M&M!!")
                nivel_de_energia+=2
            elif jogador=='tesoura' and mmonster=='pedra':
                print("O monstro comeu você e o M&M")
                nivel_de_energia-=2
            elif jogador==mmonster:
                print('EMPATE! Divida o M&M com o monstro, ele tem fome também')
                nivel_de_energia+=2
            nome_cenario_atual="4"    
            
            
        elif escolha=="professor":
            if "chave" not in inventario:
                print ("Faça uma chave para entrar na sala do professor")
                nome_cenario_atual="inicio"
            else:
                nome_cenario_atual="professor"
                print("Voce foi pedir para o professor adiar o EP. ")
                print("{0}: Raul, pode adiar o Ep por favooooooorrrrr???".format(nickname))
                print("Raul: não.",)
                game_over=True
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
            else:
                nome_cenario_atual="cookies"
                
        elif escolha=="realidade virtual":
            with open('lsd.txt','r') as arquivo:
                conteudo=arquivo.read()
                print (conteudo)
                
        elif escolha in opcoes:
            nome_cenario_atual = escolha
            
        elif escolha=="fim":
            game_over=True
            
        else:
            print("Sua indecisão foi sua ruína!")
            game_over = True
            

             
        
    #texto do fim do jogo
    print("G A M E    O V E R \n Raul: MUAH HA HA HA HA\n Parece que agora não vai ter como fugir do EP!!")



# Programa principal.
if __name__ == "__main__":
    print("Acha bonito né, {0}".format(nickname))
    main()
