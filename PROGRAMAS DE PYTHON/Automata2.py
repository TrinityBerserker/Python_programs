automata = {
    'estados': {'q0', 'q1', 'q2', 'q3', 'q4'},
    'alfabeto': {'0', '1'},
    'estado_inicial': 'q0',
    'estados_aceptacion': {'q3', 'q4'},
    'transiciones': {
        ('q0', '0'): 'q1',
        ('q0', '1'): 'q2',
        ('q1', '0'): 'q3',
        ('q1', '1'): 'q2',
        ('q2', '0'): 'q2',
        ('q2', '1'): 'q4',
        ('q3', '0'): 'q3',
        ('q3', '1'): 'q4',
        ('q4', '0'): 'q4',
        ('q4', '1'): 'q4'
    }
}

def simular_automata(automata, cadena):
    estado_actual = automata['estado_inicial']
    for simbolo in cadena:
        if (estado_actual, simbolo) in automata['transiciones']:
            estado_actual = automata['transiciones'][(estado_actual, simbolo)]
        else:
            return False
    return estado_actual in automata['estados_aceptacion']

cadena = input("Ingrese una cadena: ")

if simular_automata(automata, cadena):
    print(f'La cadena "{cadena}" es aceptada por el autómata.')
else:
    print(f'La cadena "{cadena}" no es aceptada por el autómata.')

