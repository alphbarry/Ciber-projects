import hashlib
import time

def get_hash_function(algo):
    """Obtiene la función de hash según el algoritmo especificado."""
    try:
        return getattr(hashlib, algo)
    except AttributeError:
        raise ValueError(f"Hash algorithm '{algo}' is not supported.")

def crack_password(hash_to_crack, dicfile, hash_func):
    """Intenta encontrar el password en el archivo de diccionario."""
    try:
        with open(dicfile, 'r') as file:
            for line in file:
                password = line.strip()
                if hash_func(password.encode()).hexdigest() == hash_to_crack:
                    return password
        return None
    except FileNotFoundError:
        print(f"Error: File '{dicfile}' not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def main():
    """Función principal para ejecutar el programa."""
    try:
        # Solicitar datos al usuario
        hash_algo = input("Enter hash algorithm (e.g., sha256, md5): ").strip()
        hash_to_crack = input("Enter the hash to crack: ").strip()
        dicfile = input("Enter the dictionary file path: ").strip()

        # Obtener la función de hash
        hash_func = get_hash_function(hash_algo)

        # Medir el tiempo de ejecución
        start_time = time.time()

        # Intentar encontrar el password
        result = crack_password(hash_to_crack, dicfile, hash_func)

        end_time = time.time()

        # Mostrar resultados
        if result:
            print(f"Password found: {result}")
        else:
            print("Password not found in the dictionary.")

        print(f"Execution time: {end_time - start_time:.2f} seconds")

    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    main()
