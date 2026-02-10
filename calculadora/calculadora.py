class Calculadora:
    def sumar(self, NUM1, NUM2):
        if (type(NUM1) == str or type(NUM2) == str):
            print("Los numeros deben ser enteros")
            return
        return NUM1 + NUM2    

    def restar(self, NUM1, NUM2):
        if (type(NUM1) == str or type(NUM2) == str):
            print("Los numeros deben ser enteros")
            return
        return NUM1 - NUM2    

    def multiplicar(self, NUM1, NUM2):
        if (type(NUM1) == str or type(NUM2) == str):
            print("Los numeros deben ser enteros")
            return
        return NUM1 * NUM2    

    def dividir(self, NUM1, NUM2):
        if (type(NUM1) == str or type(NUM2) == str):
            print("Los numeros deben ser enteros")
            return
        if NUM2 == 0:
            print("No se puede dividir entre cero")
            return
        return NUM1 / NUM2  

    def raiz(self,NUM1, NUM2):
        if (type(NUM1) == str or type(NUM2) == str):
            print("Los numeros deben ser enteros")
            return
        return NUM1 ** (1/NUM2)  
    
    def potencia(self,NUM1, NUM2):
        if (type(NUM1) == str or type(NUM2) == str):
            print("Los numeros deben ser enteros")
            return
        return NUM1 ** NUM2  
