def count(s, value):
    total, index = 0, 0
    while index < len(s):
        if s[index] == value:
            total = total + 1
        index = index + 1
    return total


count([1,1,1,2,3,2,1], 2)

###


def count_equal_pair(seq):
    count = 0
    for x, y in seq:
        if x == y:
            count = count + 1
    return count

pares = [[1,2], [2,2], [4, 2], [1, 1]]

count_equal_pair(pares)

area = list(range(1,10))

## range util para repetir for

for _ in range(3):
    print('Printa essa porra de novo')


## compreensão de listas

[x for x in range(10)]
[x + 1 for x in range(10)]

# filtrar com compreensão

sequencia = list(range(27, 49))

[x for x in sequencia if x % 2 == 0] 

def divisors(n):
    return [x for x in range(1, n) if n % x == 0]

divisors(49)
divisors(33*42)

def perfect(n):
    if n == sum(divisors(n)):
        return True
    else:
        return False
    

def nperfects(n):
    return [x for x in range(1, n) if perfect(x) == True]

nperfects(1000)

## implementando as map, filter e reduce

def map(fn, seq):
    return [fn(x) for x in seq]

def filter(pred, seq):
    return [x for x in seq if pred(x)]

def reduce(agg, seq, init = None):
    if init is None:
        for x in seq:
            reduzido = agg(reduzido, x)
        return reduzido
    else:
        reduzido = list(None)
        for x in seq:
            reduzido = agg(reduzido, x)
        return reduzido

map(divisors, list(range(1, 10)))
filter(lambda x : x % 2 == 0, list(range(1, 10)))
reduce(sum, list(range(1, 10)))

# membresia

1 in range(0, 10)
15 not in range(0, 14)

# fatias

digitos = [1, 8, 2, 8]

digitos[0:2]
digitos[2:]
digitos[:3]

# strings

'eu sou uma string'

cidade = 'Rio de Janeiro'
len(cidade)
cidade[4:]

cidade_pior = 'São Paulo'

cidade + ' e essa tal de ' + cidade_pior

cidade in cidade_pior

'Rio' in cidade

str(divisores(6)) + ' são divisores de 6'

# árvores

def tree(root, branches = []):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

not [] # retorna true, lol

def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])


branches(fib_tree(3))


def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(tree)]
        return sum(branch_counts)

count_leaves(fib_tree(8))

## árvore de partição

def partition_tree(n, m):
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(True)
    else:
        left = partition_tree(n - m, m)
        right = partition_tree(n, m - 1)
        return tree(m, [left, right])


def print_parts(tree, partition = []):
    if is_leaf(tree):
        if label(tree):
            print(' + '.join(partition))
    else:
        left, right = branches(tree)
        m = str(label(tree))
        print_parts(left, partition + [m])
        print_parts(right, partition)


print_parts(partition_tree(12, 2))

partition_tree(6, 2)
count_leaves(partition_tree(6, 2))


