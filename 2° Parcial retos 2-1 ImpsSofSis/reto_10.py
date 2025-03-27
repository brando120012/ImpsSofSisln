def fizzbuzz(max_num):
    three_mul = 'fizz'
    five_mul = 'buzz'
    num1 = 3  # Múltiplo base para fizz
    num2 = 5  # Múltiplo base para buzz

    for i in range(1, max_num + 1):  # Incluye el número máximo
        if i % num1 == 0 and i % num2 == 0:
            print(i, three_mul + five_mul)
        elif i % num1 == 0:
            print(i, three_mul)
        elif i % num2 == 0:
            print(i, five_mul)

#----START OF SCRIPT
if __name__ == '__main__':
    print("Iniciando FizzBuzz...")
    fizzbuzz(99)  # Llama a la función pasando el rango deseado
