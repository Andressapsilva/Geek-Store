import tkinter as tk
import customtkinter as ctk

from PIL import Image

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

    # =========================
    # INDIE
    # =========================

    {
        "obj": Jogo("Minecraft", 120, 10),
        "imagem": "imagens/minecraft.png"
    },

    {
        "obj": Jogo("Hollow Knight", 80, 12),
        "imagem": "imagens/hollow_knight.jpg"
    },

    # =========================
    # AAA
    # =========================

    {
        "obj": Jogo("Red Dead Redemption 2", 250, 5),
        "imagem": "imagens/rdr2.jpg"
    },

    {
        "obj": Jogo("Elden Ring", 299, 6),
        "imagem": "imagens/elden_ring.jpg"
    },

    {
        "obj": Jogo("GTA V", 140, 9),
        "imagem": "imagens/gtav.jpg"
    },

    {
        "obj": Jogo("Forza Horizon 6", 320, 4),
        "imagem": "imagens/forza.jpg"
    },

    # =========================
    # SCI-FI
    # =========================

    {
        "obj": Jogo("Pragmata", 350, 3),
        "imagem": "imagens/pragmata.jpg"
    },

    # =========================
    # AVENTURA
    # =========================

    {
        "obj": Jogo("Assassins Creed Black Flag", 90, 8),
        "imagem": "imagens/black_flag.png"
    },

    # =========================
    # TERROR
    # =========================

    {
        "obj": Jogo("Resident Evil Requiem", 280, 4),
        "imagem": "imagens/resident_evil.jpg"
    }
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

    carrinho_texto.configure(state="normal")

    carrinho_texto.delete("1.0", "end")

    if not itens_carrinho:

        carrinho_texto.insert(
            "1.0",
            "🛒 Seu carrinho está vazio"
        )

        carrinho_texto.configure(state="disabled")

        return

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

    quantidade_total = sum(
        dados["quantidade"]
        for dados in contador.values()
    )

    texto = ""

    # =========================
    # CABEÇALHO
    # =========================

    texto += "━━━━━━━━━━━━━━━━━━━━━━\n"
    texto += f"🛒 {quantidade_total} ITEM(NS)\n"
    texto += "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    # =========================
    # ITENS
    # =========================

    for nome, dados in contador.items():

        subtotal_item = (
            dados["quantidade"] *
            dados["preco"]
        )

        texto += (
            f"🎮 {nome}\n"
            f"📦 x{dados['quantidade']}  •  "
            f"💰 R$ {subtotal_item}\n\n"
            f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        )

    # =========================
    # RESUMO
    # =========================

    subtotal = total
    desconto = 0
    total_final = subtotal

    texto += "💳 RESUMO\n\n"

    texto += f"💰 Subtotal: R$ {subtotal:.2f}\n"

    if cliente_vip:

        desconto = subtotal * 0.10
        total_final = subtotal - desconto

        texto += (
            f"⭐ VIP: -R$ {desconto:.2f}\n"
        )

    texto += (
        f"\n💚 TOTAL FINAL\n"
        f"R$ {total_final:.2f}"
    )

    carrinho_texto.insert("1.0", texto)

    carrinho_texto.configure(state="disabled")


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

    # animação simples no status

    status.after(
        1500,
        lambda: status.configure(
            text="Selecione um jogo."
        )
    )


# =========================
# FUNÇÃO CRIAR CARDS
# =========================

def criar_cards():

    for widget in catalogo_scroll.winfo_children():

        widget.destroy()

    categoria_atual = ""

    for item in jogos:

        jogo = item["obj"]

        # =========================
        # CATEGORIAS
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

            categoria = "🎮 INDIE"

        elif jogo.nome == "Resident Evil Requiem":

            categoria = "👻 TERROR"

        elif jogo.nome == "Assassins Creed Black Flag":

            categoria = "⚔️ AVENTURA"

        else:

            categoria = "🚀 SCI-FI"

        # =========================
        # MOSTRAR CATEGORIA
        # =========================

        if categoria != categoria_atual:

            categoria_atual = categoria

            titulo_categoria = ctk.CTkLabel(
                catalogo_scroll,
                text=f"━━━━━━━━━━━━━━━━━━\n{categoria}\n━━━━━━━━━━━━━━━━━━",
                font=("Arial", 28, "bold"),
                text_color="#5865F2",
                justify="left"
            )

            titulo_categoria.pack(
                anchor="w",
                padx=15,
                pady=(30, 10)
            )

        # =========================
        # STATUS
        # =========================

        status_jogo = "🟢 Disponível"
        cor_status = "#2FA572"

        if jogo.estoque <= 0:

            status_jogo = "🔴 Indisponível"
            cor_status = "#D9534F"

        # =========================
        # CARD
        # =========================

        card = ctk.CTkFrame(
            catalogo_scroll,
            fg_color="#262626",
            corner_radius=18,
            border_width=1,
            border_color="#3a3a3a"
        )

        card.pack(
            fill="x",
            padx=15,
            pady=22
        )

        # =========================
        # IMAGEM
        # =========================

        img = Image.open(item["imagem"])

        img.thumbnail((650, 300))

        imagem = ctk.CTkImage(
            light_image=img,
            dark_image=img,
            size=img.size
        )

        frame_imagem = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )

        frame_imagem.pack(
            pady=(15, 10),
            padx=15
        )

        label_imagem = ctk.CTkLabel(
            frame_imagem,
            text="",
            image=imagem,
            corner_radius=12
        )

        label_imagem.pack()

        # =========================
        # NOME
        # =========================

        nome = ctk.CTkLabel(
            card,
            text=f"🎮 {jogo.nome}",
            font=("Arial", 24, "bold")
        )

        nome.pack(
            anchor="w",
            padx=20,
            pady=(5, 5)
        )

        # =========================
        # PREÇO
        # =========================

        preco = ctk.CTkLabel(
            card,
            text=f"💰 Preço: R$ {jogo.preco}",
            font=("Arial", 17)
        )

        preco.pack(
            anchor="w",
            padx=20
        )

        # =========================
        # ESTOQUE
        # =========================

        estoque = ctk.CTkLabel(
            card,
            text=f"📦 Estoque: {jogo.estoque}",
            font=("Arial", 17)
        )

        estoque.pack(
            anchor="w",
            padx=20
        )

        # =========================
        # DISPONIBILIDADE
        # =========================

        disponibilidade = ctk.CTkLabel(
            card,
            text=status_jogo,
            text_color=cor_status,
            font=("Arial", 17, "bold")
        )

        disponibilidade.pack(
            anchor="w",
            padx=20,
            pady=(0, 15)
        )

        # =========================
        # BOTÃO
        # =========================

        botao_jogo = ctk.CTkButton(
            card,
            text="Adicionar ao Carrinho",
            height=45,
            corner_radius=12,
            fg_color="#5865F2",
            hover_color="#4752C4",
            font=("Arial", 16, "bold"),
            command=lambda j=jogo: adicionar_carrinho(j)
        )

        botao_jogo.pack(
            padx=20,
            pady=(0, 20),
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

subtitulo.pack(pady=(0, 5))


# =========================
# BADGE VIP
# =========================

vip_label = ctk.CTkLabel(
    janela,
    text="⭐ CLIENTE VIP",
    font=("Arial", 15, "bold"),
    text_color="#FFD700"
)

vip_label.pack(pady=(0, 15))


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
    font=("Arial", 30, "bold")
)

catalogo.pack(pady=20)


# =========================
# ÁREA SCROLL
# =========================

catalogo_scroll = ctk.CTkScrollableFrame(
    frame_esquerdo,
    width=720,
    height=500,
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
# CARRINHO SCROLL
# =========================

carrinho_texto = ctk.CTkTextbox(
    frame_direito,
    width=300,
    height=360,
    font=("Arial", 16),
    corner_radius=10,
    fg_color="#1f1f1f",
    border_width=1,
    border_color="#333333",
    text_color="white"
)

carrinho_texto.pack(
    padx=20,
    pady=(10, 15),
    fill="x"
)

carrinho_texto.insert(
    "1.0",
    "🛒 Seu carrinho está vazio"
)

carrinho_texto.configure(state="disabled")


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
    pady=20,
    padx=20,
    fill="x"
)


# =========================
# EXECUÇÃO
# =========================

if __name__ == "__main__":

    janela.mainloop()