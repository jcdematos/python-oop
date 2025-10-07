from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        # Uses constructor from base class
        super().__init__(nome, preco)
        # New attribute specific to Prato
        self.descricao = descricao
    
    def aplicar_desconto(self):
        self._preco -= self._preco * 0.08