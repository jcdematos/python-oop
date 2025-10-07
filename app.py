from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante = Restaurante("Praça", "Gourmet")
prato = Prato("Arroz e Bife", 30.0, "Arroz branco com bife acebolado")
bebida = Bebida("Coca-Cola", 5.0, "350ml")

restaurante.adicionar_no_cardapio(bebida)
restaurante.adicionar_no_cardapio(prato)

def main():
    restaurante.exibir_cardapio

if __name__ == "__main__":
    main()