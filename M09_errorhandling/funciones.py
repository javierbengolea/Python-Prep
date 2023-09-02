import warnings
class Funciones():
    def __init__(self, lista=[1]):
        super(Funciones, self).__init__()
        self.lista = lista
        if len(lista) == 0:
            raise ValueError("Lista vacia!!!")
        for i in lista:
            if type(i) != int:
                raise ValueError(f"Elemento no entero en la lista: {i}")


    def es_primo(self, n):
        prim = True
        for i in range(2,n):        
            if n % i == 0:
                return False
            prim = True
        return prim

    def moda(self, lista):
        salida = dict()
        
        for i in lista:
            if i not in salida:
                salida[i] = 1
            else:
                salida[i] += 1
                
        mayor = 0
        indice = 0
                
        for i in lista:
            if salida[i] > mayor:
                mayor = salida[i]
                indice = i

        return indice, salida[indice]
        

    def conversion(self,t,de="Celsius", a="Fahrenheit"):
        grados = ["Celsius", "Fahrenheit", "Kelvin"]
        
        if de not in grados:
            raise ValueError(f"Error, medida incorrecta!!! {de}, valores esperados: {grados}")
        
        if a not in grados:
            raise ValueError(f"Error, medida incorrecta!!! {a}, valores esperados: {grados}")
        
        if(de == a):
            warnings.warn(f"La medida de {de} es igual a la medida de {a}")
            return t
        
        if type(t) not in [int, float]:
            raise ValueError(f"Error, valor incorrecto!!! {t}")
        
        if de == "Celsius" and a == "Fahrenheit":
            return (t * 1.8) + 32
        elif de == "Celsius" and a == "Kelvin":
            return t + 273.15
        elif de == "Fahrenheit" and a == "Celsius":
            return (t - 32) / 1.8
        elif de == "Fahrenheit" and a == "Kelvin":
            return (t - 32) / 1.8 + 273.15
        elif de == "Kelvin" and a == "Celsius":
            return t - 273.15
        elif de == "Kelvin" and a == "Fahrenheit":
            return (t - 273.15) * 1.8 + 32
        
        return t    

    def factorial(self, n):
        if n < 0 or (float(n) - float(int(n))) > 0:
            raise Exception("n must be a positive integer")
            
        if n == 1:
            return 1
        return n * self.factorial(n-1)
    
    def aplicar_funciones(self):

        lista_primos = [(i, "Primo" if self.es_primo(i) else "No Primo") for i in self.lista]
        print(lista_primos)
        print("La tupla (moda, ocurrencias) es, ", self.moda(self.lista))
        lista_temperaturas = [(i, self.conversion(i, "Celsius", "Fahrenheit")) for i in self.lista]
        print("Celsius a Farenheit: ", lista_temperaturas)
        lista_factoriales = [(i, self.factorial(i)) for i in self.lista]
        print("Factoriales: ", lista_factoriales)
    