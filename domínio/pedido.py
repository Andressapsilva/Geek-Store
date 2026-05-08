class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []

    def adicionar_item(self, item):

        if item.quantidade <= item.jogo.estoque:
            self.itens.append(item)
            item.jogo.estoque -= item.quantidade

        else:
            print("Estoque insuficiente")

    def calcular_total(self):

        total = 0

        for item in self.itens:
            total += item.subtotal()

        if self.cliente.vip:
            total *= 0.9

        return total