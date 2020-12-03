import random

WORDS = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
TEXT = 'Vvedite bukvu\n'


def check(char):

    '''Проверяем является ли ввод буквой'''

    if (type(char) == str) and (len(char) == 1):
        return True
    else:
        return False

def get_input(text):

    '''Возвращаем пользовательский ввод'''

    return input(text)

def vvod_bukv():

    '''Возвращает введеную букву'''

    char = get_input(TEXT)
    while not check(char):
        char = get_input(TEXT)
    return char
    
def attempt(char, word):

    '''Проверяем есть ли буква в загаданном слове. Если да, то возвращаем номера позиций буквы в слове'''

    pos = [ pos for pos, c in enumerate(word) if char == c ]
    if len(pos) == 0:
        return False
    else:
        return pos

def fail(fouls):

    '''Увеличиваем число штрафный очков'''

    fouls += 1
    print('Wrong bukv')
    return fouls

def succes(pos, lines, char):

    '''Возвращаем загаданное слово с угаданными буквами'''

    for i in pos:
                lines[i] = char
    return lines

def game(word):

    '''В методе реализована логика игры'''

    lines = []
    fouls = 0
    for i in range(len(word)):
        lines.append('_')
    print(" ".join(lines), '\n')
    while fouls < 4 and ('_' in lines):
        char = vvod_bukv()
        pos = attempt(char, word)
        if pos:
            lines = succes(pos, lines, char)
        else:
            fouls = fail(fouls)
        print(" ".join(lines), '\n')
        if fouls > 0:
            print('You have {} fouls from 4'.format(fouls))
    if fouls == 4:
        return 1
    else:
        return 0
    
def main():
    word = random.choice(WORDS)
    result = game(word)
    if result == 0:
        print('You win!')
        return
    else:
        print('Game over')
        return


if __name__ == '__main__':
    main()