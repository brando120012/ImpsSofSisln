def fizzbuzz(max_num):
    three_mul = 'fizz'  # Corregido
    five_mul = 'buzz'
    num1 = 3
    num2 = 5 

    for i in range(1, max_num + 1):  # Añadido el ':' al final
        if i % num1 == 0 and i % num2 == 0:
            print(i, three_mul + five_mul)
        elif i % num1 == 0:
            print(i, three_mul)
        elif i % num2 == 0:
            print(i, five_mul)

#----START OF SCRIPT
if __name__ == '__main__':
    fizzbuzz(99)  # Cambiado a 99 para incluir números del 1 al 99

