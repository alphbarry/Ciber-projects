import  string
import random

longitud = int(input("Introduce la longitud de la contraseña: "))

caracteres = string.ascii_letters + string.digits + string.punctuation

contraseña = ''.join(random.choice(caracteres) for i in range(longitud))

print("la contrasena generadad es: " + contraseña)