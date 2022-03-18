# Assuntos genéricos

"""
LOGGING:
"""
import logging

# Recuperamos o LOG - Entender pq pylog e não outro parametro
# Aparentemente podemos colocar qql coisa no lugar de pylog
logger = logging.getLogger("pylog")

# As vezes não precisamos usar o get Logger, usamos só o basicconfig
# Caso nossa aplicação cresca, criamos uma classe de logs
logging.basicConfig(level=logging.DEBUG)
logging.debug('Aqui o que esta bugado')

# Log de variáveis:
nome = 'John'
logging.error('{0} raised an error'.format(nome))

# Escolhemos o level que podemos, isso é bom para saber se estamos fazendo debugging ou só rodando o código normal
logger.setLevel(logging.DEBUG)
h1 = logging.FileHandler(filename="/tmp/records.log")
h1.setLevel(logging.INFO)

h2 = logging.StreamHandler(sys.stderr)
h2.setLevel(logging.ERROR)

logger.addHandler(h1)
logger.addHandler(h2)

logger.info("testing %d.. %d.. %d..", 1, 2, 3)

"""
Python Mock Objects
- Bom para testes... rever depois
"""

"""
Python PEP8

Para documentação, usar PEP257
"""

def funcao():
    """ Docstring sempre entra após a chamada da função """
    pass


def funcao_extendida():
    """Caso a docstring seja grande, deixar com várias linhas

    Sempre continuando na próxima linha respectiva

    Desta forma
    """

    pass


# Teste da docstring
funcao_extendida.__doc__

class ClasseSempreCamelCase():
    def first_method(self):
        return None

    # Dentro da mesma mesma classe, só 1 de espaço
    def seconde_method(self):
        return None

# Sempre 2 linhas entre funções e classes

"""
Métodos para classes
"""

class ClasseExemplo():

    @classmethod
    def metodo_da_classe(cls):
        """ Isso faz com que o método seja somente para a classe, e não para o objeto """
        pass


    @staticmethod
    def metodo_estatico():
        """ Faz com que o método não varie independente do objeto instanciado """
        pass

    def metodo_normal(self):
        """ Precisa de uma instancia de um objeto para funcionar """
        pass

obj_metodos_classe = ClasseExemplo()

# Aparentemente isso funciona do mesmo jeito
obj_metodos_classe.metodo_normal()
ClasseExemplo.metodo_normal(obj_metodos_classe)

# Acessando metodos da classe, sem instanciar o objeto
obj_metodos_classe.metodo_da_classe()

obj_metodos_classe.metodo_estatico()

# Usamos class metodos para instanciar classes automaticamente
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])

# Assim, se eu quiser uma pizza de margeritta, simplismente chamo
Pizza.margherita()

"""
Decorators

Utilizado para otimizar funções e classes, deixando o código menos repetitivo, adicionar High Ordered Functions, etc
"""

# Podemos ter funções dentro de função, algo parecido com javascript
def funcao_pai():
    print("Printing from the parent() function")

    def funcao_filha():
        print("Printing from the child() function")

    def funcao_tio():
        print("Printing from the uncle() function")

    funcao_filha()

    return funcao_tio

# Quando executamos, também executamos a função filha, mas ela vem depois da função pai
tio = funcao_pai()

# Quando colocamos o TIO, ele volta a chamada da função, mas não sua execução

# Decorators nada mais são, do que funções que fazem algo específico, e depois retornam normalmente sua função

# Recebem uma função como argumento
def my_decorator(func):

    # Chamamos um wrapper, que fica responsável por fazer algo antes ou depois que a função é chamada, além disso, ele tb executa a função
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    # Retornamos a chamada do wrapper, mas não sua execução
    return wrapper

def say_whee():
    print("Whee!")

# Assim, quando fazemos que say_whee é o decorador, encapsulamos a função dentro de outra
say_whee = my_decorator(say_whee)
say_whee()

# Usando o "pie" syntax, podemos reduzir nossa escrita de decorators
@my_decorator
def say_whee():
    print("Whee!")

say_whee()

# Juntando com argumentos da função:
# Para resolver isso, usamos *args e **kwargs para receber parametros variáveis dentro do decorator

# Recebemos a função do mesmo jeito
def do_twice(func):

    # Dentro do wrapper, recebemos parametros variáveis
    def wrapper_do_twice(*args, **kwargs):

        # Executamos a função com seus respectivos parametros variáveis
        func(*args, **kwargs)

        # Com o return, conseguimos fazer com que tenhamos o output da função tb
        return func(*args, **kwargs)
    # Retornamos a chamada da função normalmente
    return wrapper_do_twice

# Possibilidades para decorators
# Tempo que a função executou

# Debugging
import functools

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)

    def wrapper_debug(*args, **kwargs):
        # Pegamos todos os nomes dos argumentos da função
        args_repr = [repr(a) for a in args]
        print(args_repr)
        # Pegamos todos os valores enviados para a chamada da função
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        # Juntamos tudo na assinatura da chamada da função
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        # Chamamos a função
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        # Falamos o resultado da função
        print(f"{func.__name__!r} returned {value!r}")           # 4
        # E retornamos o valor da função
        return value

    return wrapper_debug

@debug
def teste_complexo(e, f, t=1, n=7):
    print('OI TESTANDO DECORATORS')

    return e + f

teste_complexo(1, 4, 3)

# Para diminuir execução do código e entender o que está acontecendo:
import time

def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(4)
        return func(*args, **kwargs)
    return wrapper_slow_down

@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)

countdown(3)

# Classes já tem property decorator
@property

# Para realizar a função diversas vezes
@repeat

# Ver decorators com:
# argumento
# para classes
# statefull
