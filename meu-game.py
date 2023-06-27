def somar(num1: int, num2: int) -> str:
    """Função que soma dois números aleatórios."""
    global score, rodadas
    result = int(input(f'{num1} + {num2} = '))
    rodadas += 1
    if result == (num1+num2):
        score += 1
        return f'Resposta correta!   Score: {score}'
    return f'Resposta incorreta, a resposta esperada era {num1 + num2}!'


def subtrair(num1: int, num2: int) -> str:
    """Função que subtrai dois números aleatórios."""
    global score, rodadas
    result = int(input(f'{num1} - {num2} = '))
    rodadas += 1
    if result == (num1 - num2):
        score += 1
        return f'Resposta correta!   Score: {score}'
    return f'Resposta incorreta, a resposta esperada era {num1 - num2}!'


def multiplicar(num1: int, num2: int) -> str:
    """Função que multiplica dois números aleatórios."""
    global score, rodadas
    result = int(input(f'{num1} * {num2} = '))
    rodadas += 1
    if result == (num1 * num2):
        score += 1
        return f'Resposta correta!   Score: {score}'
    return f'Resposta incorreta, a resposta esperada era {num1 * num2}!'


def dividir(num1: int, num2: int) -> str:
    """Função que divide dois números aleatórios."""
    global score, rodadas
    result = int(input(f'{num1*num2} / {num2} = '))
    rodadas += 1
    if result == num1:
        score += 1
        return f'Resposta correta!   Score: {score}'
    return f'Resposta incorreta, a resposta esperada era {num1}!'


def continuar():
    """Função que continua ou para o jogo."""
    continuar = input('Deseja continuar? [s/n] ')
    if continuar == 'n':
        print(f'Você terminou o jogo com um score de {score} resposta(s) correta(s) em {rodadas} pergunta(s)!')
        with open('histórico_de_score', 'r') as arquivo:
            arquivo.seek(0)
            maior_pontuacao = int(arquivo.read())
            if score > maior_pontuacao:
                with open('histórico_de_score', 'w') as arquivo2:
                    arquivo2.write(f'{score}')
            arquivo.seek(0)
            print(f'A sua maior pontuação no jogo foi de: {arquivo.read()} ponto(s)')
        exit(1)


def dif1(min, max):
    """função para o jogo de dificuldade nível 1."""
    print(somar(randint(min, max), randint(min, max)))
    continuar()


def dif2(min, max):
    """função para o jogo de dificuldade nível 2."""
    operacao: int = randint(1, 2)
    if operacao == 1:
        dif1(1, 50)
        print(subtrair(randint(min, max), randint(min, max)))
        continuar()
    else:
        print(subtrair(randint(min, max), randint(min, max)))
        continuar()
        dif1(1, 50)

def dif3():
    """função para o jogo de dificuldade nível 3."""
    operacao: int = randint(1, 2)
    if operacao == 1:
        dif2(1, 40)
        print(multiplicar(randint(2, 15), randint(2, 15)))
        continuar()
    else:
        print(multiplicar(randint(2, 15), randint(2, 15)))
        continuar()
        dif2(1, 40)


def dif4():
    """função para o jogo de dificuldade nível 4."""
    operacao: int = randint(1, 2)
    if operacao == 1:
        dif3()
        print(dividir(randint(2, 6), randint(6, 15)))
        continuar()
    else:
        print(dividir(randint(2, 6), randint(6, 15)))
        continuar()
        dif3()


from random import randint

while True:
    try:
        dificuldade = int(input('Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: '))
    except ValueError:
        print('Tente novamente!')
    else:
        break

score = 0
rodadas = 0
if dificuldade == 1:
    while True:
        print('Digite o resultado da seguinte operação: ')
        dif1(1, 20)
elif dificuldade == 2:
    while True:
        print('Digite o resultado da seguinte operação: ')
        dif2(1, 20)
elif dificuldade == 3:
    while True:
        print('Digite o resultado da seguinte operação: ')
        dif3()
elif dificuldade == 4:
    while True:
        print('Digite o resultado da seguinte operação: ')
        dif4()
