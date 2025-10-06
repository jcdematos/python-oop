class Veiculo:
    _ligado = False

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"{self.marca} {self.modelo} Ligado: {self._ligado}"

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.portas} Portas Ligado: {self._ligado}"

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init(marca, modelo)
        self.tipo = tipo

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.tipo} Ligado: {self._ligado}"

def main():
    carro = Carro("Toyota", "Corolla", 4)
    print(carro)

if __name__ == "__main__":
    main()