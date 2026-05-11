import tkinter as tk
import customtkinter as ctk

from dominio.jogo import Jogo


# =========================
# CONFIGURAÇÕES INICIAIS
# =========================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# =========================
# JANELA
# =========================

janela = ctk.CTk()

janela.title("Geek Store")
janela.geometry("1200x750")
janela.resizable(False, False)


# =========================
# LISTA DOS JOGOS
# =========================

jogos = [

    Jogo("Minecraft", 120, 10),

    Jogo("Red Dead Redemption 2", 250, 0),

    Jogo("Pragmata", 350, 3),

    Jogo("Assassins Creed Black Flag", 90, 8),

    Jogo("Resident Evil Requiem", 280, 4)
]


# =========================
# CLIENTE VIP
# =========================

cliente_vip = True


# =========================
# CARRINHO
# =========================

itens_carrinho = []
total = 0


# =========================
# FUNÇÃO ATUALIZAR CARRINHO
# =========================

def atualizar_carrinho():

    texto = "====================\n"
    texto += "🎮 ITENS NO CARRINHO\n"
    texto += "====================\n\n"

    contador = {}

    for item in itens_carrinho:

        nome = item.nome

        if nome in contador:

            contador[nome]["quantidade"] += 1

        else:

            contador[nome] = {
                "quantidade": 1,
                "preco": item.preco
            }

    for nome, dados in contador.items():

        texto += (
            f"🎮 {nome}\n"
            f"Quantidade: x{dados['quantidade']}\n"
            f"Preço: R$ {dados['preco']}\n\n"
        )

    texto += "--------------------\n"

    subtotal = total
    desconto = 0
    total_final = subtotal

    if cliente_vip:

        desconto = subtotal * 0.10
        total_final = subtotal - desconto

        texto += f"⭐ DESCONTO VIP: -R$ {desconto:.2f}\n"

    texto += f"💰 TOTAL FINAL: R$ {total_final:.2f}"

    carrinho_texto.configure(text=texto)


# =========================
# FUNÇÃO ADICIONAR
# =========================

def adicionar_carrinho(jogo):

    global total

    if jogo.estoque <= 0:

        status.configure(
            text=f"❌ {jogo.nome} está indisponível!"
        )

        return

    jogo.estoque -= 1

    itens_carrinho.append(jogo)

    total += jogo.preco

    atualizar_carrinho()

    criar_cards()

    status.configure(
        text=f"✅ {jogo.nome} adicionado ao carrinho!"
    )


# =========================
# FUNÇÃO CRIAR CARDS
# =========================

def criar_cards():

    for widget in catalogo_scroll.winfo_children():

        widget.destroy()

    for jogo in jogos:

        status_jogo = "✅ Disponível"
        cor_status = "#2FA572"

        if jogo.estoque <= 0:

            status_jogo = "❌ Indisponível"
            cor_status = "#D9534F"

        card = ctk.CTkFrame(
            catalogo_scroll,
            fg_color="#2b2b2b",
            corner_radius=15
        )

        card.pack(
            fill="x",
            padx=10,
            pady=10
        )

        nome = ctk.CTkLabel(
            card,
            text=jogo.nome,
            font=("Arial", 22, "bold")
        )

        nome.pack(
            anchor="w",
            padx=20,
            pady=(15, 5)
        )

        preco = ctk.CTkLabel(
            card,
            text=f"💰 Preço: R$ {jogo.preco}",
            font=("Arial", 16)
        )

        preco.pack(
            anchor="w",
            padx=20
        )

        estoque = ctk.CTkLabel(
            card,
            text=f"📦 Estoque: {jogo.estoque}",
            font=("Arial", 16)
        )

        estoque.pack(
            anchor="w",
            padx=20
        )

        disponibilidade = ctk.CTkLabel(
            card,
            text=status_jogo,
            text_color=cor_status,
            font=("Arial", 16, "bold")
        )

        disponibilidade.pack(
            anchor="w",
            padx=20,
            pady=(0, 10)
        )

        botao_jogo = ctk.CTkButton(
            card,
            text="Adicionar ao Carrinho",
            height=42,
            corner_radius=10,
            fg_color="#5865F2",
            hover_color="#4752C4",
            font=("Arial", 15, "bold"),
            command=lambda j=jogo: adicionar_carrinho(j)
        )

        botao_jogo.pack(
            padx=20,
            pady=(0, 15),
            fill="x"
        )

        if jogo.estoque <= 0:

            botao_jogo.configure(state="disabled")


# =========================
# FUNÇÃO FINALIZAR COMPRA
# =========================

def finalizar_compra():

    if itens_carrinho:

        subtotal = total
        desconto = 0
        total_final = subtotal

        if cliente_vip:

            desconto = subtotal * 0.10
            total_final = subtotal - desconto

        popup = ctk.CTkToplevel(janela)

        popup.title("Compra Finalizada")
        popup.geometry("450x320")
        popup.resizable(False, False)

        popup.configure(fg_color="#1e1e1e")

        popup.grab_set()

        titulo_popup = ctk.CTkLabel(
            popup,
            text="🎉 COMPRA REALIZADA!",
            font=("Arial", 28, "bold"),
            text_color="#2FA572"
        )

        titulo_popup.pack(pady=(30, 10))

        texto_popup = ctk.CTkLabel(
            popup,
            text=(
                "Obrigado por comprar na\n"
                "Geek Store!\n\n"
                f"💰 Subtotal: R$ {subtotal:.2f}\n"
                f"⭐ Desconto VIP: R$ {desconto:.2f}\n"
                f"✅ Total Final: R$ {total_final:.2f}"
            ),
            font=("Arial", 17),
            justify="center"
        )

        texto_popup.pack(pady=10)

        botao_fechar = ctk.CTkButton(
            popup,
            text="FECHAR",
            width=200,
            height=45,
            corner_radius=12,
            fg_color="#5865F2",
            hover_color="#4752C4",
            font=("Arial", 16, "bold"),
            command=popup.destroy
        )

        botao_fechar.pack(pady=20)

    else:

        status.configure(
            text="⚠️ Carrinho vazio!"
        )


# =========================
# TÍTULO
# =========================

titulo = ctk.CTkLabel(
    janela,
    text="GEEK STORE",
    font=("Arial", 46, "bold"),
    text_color="#5865F2"
)

titulo.pack(pady=(25, 5))


subtitulo = ctk.CTkLabel(
    janela,
    text="Sua loja gamer digital",
    font=("Arial", 18),
    text_color="gray"
)

subtitulo.pack(pady=(0, 20))


# =========================
# FRAME PRINCIPAL
# =========================

frame_principal = ctk.CTkFrame(
    janela,
    fg_color="#1a1a1a",
    corner_radius=20
)

frame_principal.pack(
    padx=20,
    pady=20,
    fill="both",
    expand=True
)


# =========================
# FRAME ESQUERDO
# =========================

frame_esquerdo = ctk.CTkFrame(
    frame_principal,
    fg_color="#242424",
    corner_radius=15
)

frame_esquerdo.pack(
    side="left",
    padx=20,
    pady=20,
    fill="both",
    expand=True
)


# =========================
# TÍTULO CATÁLOGO
# =========================

catalogo = ctk.CTkLabel(
    frame_esquerdo,
    text="CATÁLOGO DE JOGOS",
    font=("Arial", 28, "bold")
)

catalogo.pack(pady=20)


# =========================
# ÁREA SCROLLÁVEL
# =========================

catalogo_scroll = ctk.CTkScrollableFrame(
    frame_esquerdo,
    width=650,
    height=450,
    fg_color="#242424"
)

catalogo_scroll.pack(
    padx=20,
    pady=10,
    fill="both",
    expand=True
)

criar_cards()


# =========================
# STATUS
# =========================

status = ctk.CTkLabel(
    frame_esquerdo,
    text="Selecione um jogo.",
    font=("Arial", 14),
    text_color="gray"
)

status.pack(pady=15)


# =========================
# FRAME DIREITO
# =========================

frame_direito = ctk.CTkFrame(
    frame_principal,
    fg_color="#242424",
    corner_radius=15,
    width=350
)

frame_direito.pack(
    side="right",
    padx=20,
    pady=20,
    fill="y"
)

frame_direito.pack_propagate(False)


# =========================
# TÍTULO CARRINHO
# =========================

titulo_carrinho = ctk.CTkLabel(
    frame_direito,
    text="🛒 CARRINHO",
    font=("Arial", 28, "bold")
)

titulo_carrinho.pack(pady=20)


# =========================
# TEXTO CARRINHO
# =========================

carrinho_texto = ctk.CTkLabel(
    frame_direito,
    text="Carrinho vazio",
    font=("Arial", 15),
    justify="left",
    anchor="nw"
)

carrinho_texto.pack(
    padx=20,
    pady=10,
    anchor="nw"
)


# =========================
# BOTÃO FINALIZAR
# =========================

finalizar = ctk.CTkButton(
    frame_direito,
    text="Finalizar Compra",
    font=("Arial", 17, "bold"),
    height=50,
    corner_radius=12,
    fg_color="#2FA572",
    hover_color="#23855B",
    command=finalizar_compra
)

finalizar.pack(
    side="bottom",
    pady=25,
    padx=20,
    fill="x"
)


# =========================
# EXECUÇÃO
# =========================

if __name__ == "__main__":

    janela.mainloop()