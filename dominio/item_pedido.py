class ItemPedido:
    def __init__(self, jogo, quantidade):
        self.jogo = jogo
        self.quantidade = quantidade

    def subtotal(self):
        return self.jogo.preco * self.quantidade