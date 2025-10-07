from abc import ABC, abstractmethod

class Veiculo:
    _ligado = False

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"{self.marca} {self.modelo} Ligado: {self._ligado}"
    
    @abstractmethod
    def ligar(self):
        pass


class Carro(Veiculo):
    def __init__(self, marca, modelo, portas, cor):
        super().__init__(marca, modelo)
        self.portas = portas
        self.cor = cor

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.portas} Portas Ligado: {self._ligado}"
    
    def ligar(self):
        if self._ligado == False:
            self._ligado = True
            print("Ligando carro")
        else:
            print("Carro já está ligado")

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init(marca, modelo)
        self.tipo = tipo

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.tipo} Ligado: {self._ligado}"

def main():
    carro = Carro("Toyota", "Corolla", 4, "Prata")
    print(carro)
    carro.ligar()
    carro.ligar()

if __name__ == "__main__":
    main()