from itertools import permutations
from random import shuffle

# Hacemos esto por la versión de Python 
try:
    raw_input
except:
    raw_input = input
try:
    from itertools import izip
except:
    izip = zip
#--------------------------------------

digits = '123456789'
size = 4
 
def separacion_valores(puntuacion):
    puntuacion = puntuacion.strip().split(',')
    return tuple(int(s.strip()) for s in puntuacion)
 
def scorecalc(suposicion, eleccion):
    bulls = cows = 0
    for g,c in izip(suposicion, eleccion):
        if g == c:
            bulls += 1
        elif g in eleccion:
            cows += 1
    return bulls, cows
 
elecciones = list(permutations(digits, size))

#Primer numero al azar
shuffle(elecciones)
respuestas = []
puntajes  = []
 
print ("Jugando Bulls & Cows con %i digitos únicos\n" % size)
 
while True:
    ans = elecciones[0]
    respuestas.append(ans)
    print ("(Reducido a %i posibilidades)" % len(elecciones))
    puntuacion = raw_input("El intento %2i es %*s. Respuesta: (Bulls, cows)? "
                      % (len(respuestas), size, ''.join(ans)))
    puntuacion = separacion_valores(puntuacion)
    puntajes.append(puntuacion)
    print("Bulls: %i, Cows: %i" % puntuacion)
    found =  puntuacion == (size, 0)
    if found:
        print ("Vamos no Más, Felicitaciones!!!")
        break
    elecciones = [c for c in elecciones if scorecalc(c, ans) == puntuacion]
    if not elecciones:
        print ("¿Mal Puntaje? algo no encaja con el puntaje que me diste:")
        print ('  ' +
               '\n  '.join("%s -> %s" % (''.join(an),sc)
                           for an,sc in izip(respuestas, puntajes)))
        break