from domínio.cliente import Cliente
from domínio.jogo import Jogo
from domínio.item_pedido import ItemPedido
from domínio.pedido import Pedido


jogos = [

    Jogo("Minecraft", 120, 10),

    Jogo("Red Dead Redemption 2", 250, 5),

    Jogo("Pragmata", 350, 3),

    Jogo("Assassins Creed Black Flag", 90, 8),

    Jogo("Resident Evil Requiem", 280, 4)
]


print("====== CATÁLOGO GEEK STORE =====")


cliente = Cliente("Andressa", True)

pedido = Pedido(cliente)


while True:

    print("\n===== GEEK STORE =====")

    for indice, jogo in enumerate(jogos):

        print(f"{indice + 1} - {jogo.nome} | R${jogo.preco}")

    print("0 - Finalizar compra")


    opcao = int(input("Escolha um jogo: "))


    if opcao == 0:
        break


    jogo_escolhido = jogos[opcao - 1]


    quantidade = int(input("Quantidade: "))


    item = ItemPedido(jogo_escolhido, quantidade)

    pedido.adicionar_item(item)


print("\n===== COMPRA FINALIZADA =====")

print("Total do pedido R$: ", pedido.calcular_total())