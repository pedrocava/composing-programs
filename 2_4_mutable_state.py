# strings

from datetime import date

tues = date(2014, 5, 13)

tues.strftime('%A, %B %d')

'1234'.isnumeric()

'rOBERT dE nIRO'.swapcase()

'eyes'.upper().endswith('YES')

chinese = ['coin', 'string', 'myriad']
suits = chinese # dois nomes na mesma lista

suits.pop() # remove e retorna o último elemento
suits.append('cup') # efeito colateral, esta operação altera estado e é impura
suits.extend(['sword', 'club']) # adiciona uma lista inteira

suits[2] = 'spade' # replace no índice

suits

suits[0:2] = ['heart', 'diamond']

suits

# todos os métodos de lista são funções impuras

chinese # alteramos o objeto original também

suits.insert(2, 'joker') # insert admite índice

suits is [0, 2, 3]
suits is ['heart', 'diamond', 'joker', 'spade', 'cup', 'sword', 'club']
suits == ['heart', 'diamond', 'joker', 'spade', 'cup', 'sword', 'club']

# ao contrário de métodos slicing cria um objeto que não é ligado ao original

a = [11, 12, 13]
b = a[1:]
b[1] = 15
a
b

# tuplas

1, 2 + 3
'a', 'bc', 23
('a', 'bc', 23, (1, 2))

()
(10, )

codigo = ("cima", "cima", "baixo", "baixo") + ("esquerda", "direita") * 2
len(codigo)

codigo.count("baixo")

# Dicionários

romanos = {
    "I" : 1.0,
    "V" : 5.0,
    "X" : 10.0,
    "L" : 50.0,
    "C" : 100.0
}

romanos['M'] = 1000.0

romanos

sum(romanos.values())
romanos.get("I")

{x : x*x for x in range(3, 6)} # compreensão de dicionários

# estado local e global

def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw

# make_withdraw é uma fábrica de funções que cria o global `balance` ao gerar uma função

saque = make_withdraw(25)
saque(12)
saque(5)

# iteradores

def dupla_e_printa(x):
    print(x, ' -> ', 2*x)
    return 2*x


s = range(3, 7)
duplicado = map(dupla_e_printa, s) # preciso excluir a minha map
next(duplicado)

# geradores

def letters_generator():
    current = 'a'
    while current <= 'p': 
        yield current
        current = chr(ord(current) + 1)


for letter in letters_generator():
    print(letter)

gerador = letters_generator()

next(gerador)
next(gerador)
next(gerador)



