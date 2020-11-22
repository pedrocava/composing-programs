
# range() não armazena a sequencia inteira, apenas os bounds
# e computa o indice on request
# range() é lazy

r = range(1000, 1000000000000)
r[12324534]
r

# um iterador tem dois componentes
# um mecanismo para recuperar o próximo elemento
# outro para sinalizar o fim da sequencia

primes = [2, 3, 5, 7]
type(primes)
iterator = iter(primes)

next(iterator)
next(iterator)
next(iterator)

# para gerenciar o erro usamos try

try:
    next(iterator)
except:
    print('No more values')

# qualquer valor que produza iteradores é um iterável

counts = [1, 2, 3]

items = iter(counts)

try:
    while True:
        item = next(items)
        print(item)
except StopIteration:
    pass

# streams
# streams são linked lists preguiçosas
# um stream armazena como computar os dados, ao invés dos dados em si

class Stream:
    
    class empty:
        def __repr__(self):
            return 'Stream.empty'
    empty = empty()

    def __init__(self, first, compute_rest = lambda: empty):
        assert callable(compute_rest), 'compute_rest must be callable'
        self.first = first
        self._compute_rest = compute_rest
    @property
    def rest(self):
        if self._compute_rest is not None:
            self._rest = self._compute_rest()
            self._compute_rest = None
        return self._rest
    def __repr__(self):
        return 'Stream({0}, <...>)'.format(repr(self.first))

exemplo = Stream(1, lambda: Stream(2 + 3, lambda: Stream(9)))

exemplo.rest.rest # chegamos em 9
exemplo.rest.first

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

class Sequence:
    def __init__(self, values):
        assert type(values) is list, 'values must be a list'
        self.values = values
        self.length = len(values) 
    def append(self, x):
        self.values = [self.values] + [x]
        return self

seq = Sequence([fibonacci(3), fibonacci(5)])
seq2 = seq.append(3)

seq.values
seq2.values

fluxo = Stream(seq, lambda seq : seq.append(2))
fluxo.first.values
fluxo.rest.values

# stream de inteiros

def integer_stream(n):
    def compute_rest():
        return integer_stream(n + 1)
    return Stream(n, compute_rest)


positivos = integer_stream(1)

positivos.rest.rest.rest.first 

