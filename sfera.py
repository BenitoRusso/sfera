import math

def volume(r):
   Volume = 4.*(r**3*math.pi)/3.
   return Volume

r = int( input ("inserisci il raggio"))
Palla = volume (r) 
print (Palla)