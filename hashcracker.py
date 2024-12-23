import hashlib

hash = input("Enter the hash: ")

dicfile = input("Enter the dictionary file: ")

with open(dicfile, 'r') as file:

    diccionario = [line.strip() for line in file]

    for password in diccionario:

        hash_calculado = hashlib.sha256(password.encode()).hexdigest()

        if hash_calculado == hash:
            print(f"Password found: " + password)
            break
        else:
            print(f"Password not found: ")