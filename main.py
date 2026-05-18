from domínio.cliente import Cliente
from domínio.jogo import Jogo
from domínio.item_pedido import ItemPedido
from domínio.pedido import Pedido


# =========================
# CATÁLOGO DE JOGOS
# =========================

jogos = [

    # =========================
    # SANDBOX / INDIE
    # =========================

    Jogo("Minecraft", 120, 10),

    Jogo("Hollow Knight", 80, 12),

    # =========================
    # AAA
    # =========================

    Jogo("Red Dead Redemption 2", 250, 5),

    Jogo("Elden Ring", 299, 6),

    Jogo("GTA V", 140, 9),

    Jogo("Forza Horizon 6", 320, 4),

    # =========================
    # SCI-FI
    # =========================

    Jogo("Pragmata", 350, 3),

    # =========================
    # AÇÃO / AVENTURA
    # =========================

    Jogo("Assassins Creed Black Flag", 90, 8),

    # =========================
    # TERROR
    # =========================

    Jogo("Resident Evil Requiem", 280, 4)
]


# =========================
# INÍCIO DO SISTEMA
# =========================

print("===================================")
print("🎮     CATÁLOGO GEEK STORE     🎮")
print("===================================")


# =========================
# CLIENTE
# =========================

cliente = Cliente("Andressa", True)

pedido = Pedido(cliente)


# =========================
# LOOP PRINCIPAL
# =========================

while True:

    print("\n===================================")
    print("🛒          GEEK STORE")
    print("===================================")

    categoria_atual = ""

    for indice, jogo in enumerate(jogos):

        # =========================
        # DEFINIÇÃO DAS CATEGORIAS
        # =========================

        if jogo.nome in [
            "Red Dead Redemption 2",
            "Elden Ring",
            "GTA V",
            "Forza Horizon 6"
        ]:

            categoria = "🔥 AAA"

        elif jogo.nome in [
            "Minecraft",
            "Hollow Knight"
        ]:

            categoria = "🎮 INDIE / SANDBOX"

        elif jogo.nome in [
            "Resident Evil Requiem"
        ]:

            categoria = "👻 TERROR"

        elif jogo.nome in [
            "Assassins Creed Black Flag"
        ]:

            categoria = "⚔️ AÇÃO / AVENTURA"

        else:

            categoria = "🚀 SCI-FI"

        # =========================
        # EXIBIR CATEGORIA
        # =========================

        if categoria != categoria_atual:

            categoria_atual = categoria

            print("\n-----------------------------------")
            print(categoria)
            print("-----------------------------------")

        # =========================
        # STATUS ESTOQUE
        # =========================

        if jogo.estoque > 0:

            status = "✅ Disponível"

        else:

            status = "❌ Indisponível"

        # =========================
        # EXIBIR JOGO
        # =========================

        print(
            f"{indice + 1} - "
            f"{jogo.nome} | "
            f"R${jogo.preco} | "
            f"Estoque: {jogo.estoque} | "
            f"{status}"
        )

    print("\n0 - Finalizar compra")

    # =========================
    # ESCOLHA DO USUÁRIO
    # =========================

    opcao = int(input("\nEscolha um jogo: "))

    if opcao == 0:

        break

    # =========================
    # VALIDAR OPÇÃO
    # =========================

    if opcao < 1 or opcao > len(jogos):

        print("\n❌ Opção inválida!")

        continue

    jogo_escolhido = jogos[opcao - 1]

    # =========================
    # VERIFICAR ESTOQUE
    # =========================

    if jogo_escolhido.estoque <= 0:

        print("\n❌ Esse jogo está sem estoque!")

        continue

    quantidade = int(input("Quantidade: "))

    # =========================
    # VALIDAR QUANTIDADE
    # =========================

    if quantidade > jogo_escolhido.estoque:

        print("\n❌ Quantidade indisponível em estoque!")

        continue

    # =========================
    # ADICIONAR ITEM
    # =========================

    item = ItemPedido(
        jogo_escolhido,
        quantidade
    )

    pedido.adicionar_item(item)

    print(
        f"\n✅ {quantidade}x "
        f"{jogo_escolhido.nome} "
        f"adicionado ao carrinho!"
    )


# =========================
# FINALIZAÇÃO
# =========================

print("\n===================================")
print("✅      COMPRA FINALIZADA")
print("===================================")

total = pedido.calcular_total()

# =========================
# DESCONTO VIP
# =========================

if cliente.vip:

    desconto = total * 0.10

    total_final = total - desconto

    print(f"\n⭐ Cliente VIP detectado!")
    print(f"💸 Desconto aplicado: R$ {desconto:.2f}")

else:

    total_final = total

# =========================
# TOTAL
# =========================

print(f"\n💰 Total final: R$ {total_final:.2f}")

print("\n🎮 Obrigado por comprar na Geek Store!")