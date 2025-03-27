class Fizz_Buzz:
    def fizzbuzz(self, max_num):  # Agregar 'self' como primer argumento
        three_mul = 'fizz'
        five_mul = 'buzz'
        num1 = 3
        num2 = 5 

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
    fizzbuzz_obj = Fizz_Buzz()  # Inicializa correctamente el objeto
    fizzbuzz_obj.fizzbuzz(99)  # Llama al método con la instancia


