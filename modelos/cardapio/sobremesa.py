from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, tipo, tamanho, descricao):
        # Uses constructor from base class
        super().__init__(nome, preco)
        # New attribute specific to Prato
        self.tipo = tipo
        self.tamanho = tamanho
        self.descricao = descricao

    def __str__(self):
        return f"{self._nome, self._preco, self.tipo, self.tamanho, self.descricao}"
    
    def aplicar_desconto(self):
        self._preco -= self._preco * 0.20