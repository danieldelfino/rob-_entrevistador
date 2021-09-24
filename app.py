import time

def Google():
    print('Olá, candidato(a), bem-vindo(a) a Google, analisamos seu curriculo e você foi selecionado(a) para a entrevista com IA.')
    print('Você deseja participar do processo seletivo?')
    resposta = str(input())
    if resposta in ('sim' or 's'):
       print('Aguarde, nosso entrevistador em breve entrará em contato...')
    time.sleep(3)
    print('Antes de você realizar a entrevista com nosso robô, precisamos de algumas informações....')
Google()    

def nome_candidato():
    candidato = 'Daniel'
    time.sleep(3)
    print('Aguarde um momento.. buscando informações do usuário...')
    time.sleep(8)
    print(f'Olá {candidato}, nos informe seu CPF...')
    cpf_do_candidato = int(input())
    print('Analisando os dados...')
    time.sleep(8)
    print('Um momento... o entrevistador está analisando o CPF para ver se está de acordo com o cadastro em nosso banco de dados....')
    time.sleep(8)
    print('Aguarde, nossa forma de entrevistar nossos candidatos são inovadoras e não vai demorar...')
    time.sleep(8)
    print(f' Olá, {candidato} analisamos seu CPF e ele está de acordo com o seu cadastro em nossa empresa, nosso robô de Inteligência Artificial irá entrar em contato, desejamos uma boa sorte.')
    time.sleep(8)
    print(f' Olá {candidato}, Podemos começar a nossa entrevista nesse exato momento?')
    resposta = input()
    if resposta in ('sim', 's'):
        print('Então vamos começar...')
        time.sleep(10)
nome_candidato()

def robo_de_inteligencia_artificial():
    candidato = 'Daniel'
    print(f' Olá {candidato}, Meu nome é Calvin e irei te avaliar de agora em diante ... ')
    time.sleep(4)
    print(f' {candidato} me informe suas habilidades que tem adquirido durante esse tempo de estudos...')
    conhecimento_adquirido = str(input())
    print(f'Entendi {candidato}, porque você escolheu essa área?')
    resposta = str(input())
    print('Entendi, qual seus objetivos profissionais?')
    objetivos_profissionais = str(input())
    print(f' Certo {candidato}, me fale um pouco sobre você, quem é o {candidato}? Quais são suas qualidades? ')
    resposta = str(input())
    print(f'{candidato} Entendi, estou guardando suas respostas em meu sistema operacional para poder te avaliar da melhor forma possível.')   
robo_de_inteligencia_artificial()