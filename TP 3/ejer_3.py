# Ejercicio 3 - TP3 - Automata: (a|b)*(a|b|e)

aut = input("Enter the string: ")
aut.re

dfa = {0:{'a':1, 'b':2},
       1:{'a':1, 'b':3}, 
       2:{'a':3, 'b':2},
       3:{'a':3, 'b':3}}

# accepting = "2"
initial = 0

def accepts(transitions,initial,accepting,s):
    state = initial
    for c in s:
        state = transitions[state][c]
    return state in accepting

print(accepts(dfa,initial,{1,2,3},aut))
