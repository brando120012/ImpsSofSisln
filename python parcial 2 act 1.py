def fizzbuzz(max_num):
    """Este método implementa FizzBuzz"""
    
    tres_mul = 'fizz'
    cinco_mul = 'buzz'
    num1 = 3
    num2 = 5 

    for i in range(1, max_num + 1):  # Asegurar que 99 esté incluido
        if i % num1 == 0 and i % num2 == 0:
            print(i, tres_mul + cinco_mul)
        elif i % num1 == 0:
            print(i, tres_mul)
        elif i % num2 == 0:
            print(i, cinco_mul)
        else:
            print(i)  # Agregar esta línea para imprimir números que no sean múltiplos de 3 ni 5

#----Iniciar el script
if __name__ == '__main__':
    fizzbuzz(99)  # Llamar correctamente la función
