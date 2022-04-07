import snoop

# Olhar snoop: https://github.com/alexmojaki/snoop

@snoop
def number_to_bits(number):
    if number:
        bits = []
        while number:
            number, remainder = divmod(number, 2)
            bits.insert(0, remainder)
        return bits
    else:
        return [0]


number_to_bits(6)

# ######################################################################
# ######################################################################

from icecream import ic

# Olhar icecream: https://github.com/gruns/icecream

def foo(i):
    return i + 333

ic(foo(123))

# ######################################################################
# ######################################################################

# Muito potencial esse PyTrace para identificar bugs nas simulações
# https://pytrace.com/

# ######################################################################
# ######################################################################

# Cyberbrain para ver grafo de execução
# https://github.com/laike9m/Cyberbrain

from cyberbrain import trace

# As of now, you can only have one @trace decorator in the whole program.
# We may change this in version 2.0, see https://github.com/laike9m/Cyberbrain/discussions/73

@trace  # Disable tracing with `@trace(disabled=True)`
def foo():
    ...
