def fizzbuzz():
    three_mul = 'fizz'
    five_mul = 'buzz'

    try:
        with open('myfile.txt', 'r') as f:
            print('Archivo abierto exitosamente.')
            num1 = int(f.readline())  # Lee el primer número (múltiplo de 3)
            num2 = int(f.readline())  # Lee el segundo número (múltiplo de 5)
            max_num = int(f.readline())  # Lee el número máximo a procesar

        for i in range(1, max_num + 1):
            if i % num1 == 0 and i % num2 == 0:
                print(i, three_mul + five_mul)
            elif i % num1 == 0:
                print(i, three_mul)
            elif i % num2 == 0:
                print(i, five_mul)
    except FileNotFoundError:
        print('Error: El archivo "mifile.txt" no se encuentra.')
    except ValueError:
        print('Error: Asegúrate de que el archivo contiene únicamente números enteros.')

#----START OF SCRIPT
if __name__ == '__main__':
    fizzbuzz()

