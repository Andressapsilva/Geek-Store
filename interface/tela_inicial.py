import tkinter as tk
import customtkinter as ctk


# =========================
# CONFIGURAÇÕES INICIAIS
# =========================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


janela = ctk.CTk()

janela.title("Geek Store")
janela.geometry("1000x650")
janela.resizable(False, False)


# =========================
# LISTA DOS JOGOS
# =========================

jogos = [

    {"nome": "Minecraft", "preco": 120},

    {"nome": "Red Dead Redemption 2", "preco": 250},

    {"nome": "Pragmata", "preco": 350},

    {"nome": "Assassins Creed Black Flag", "preco": 90},

    {"nome": "Resident Evil Requiem", "preco": 280}
]


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

        nome = item["nome"]

        if nome in contador:

            contador[nome]["quantidade"] += 1

        else:

            contador[nome] = {
                "quantidade": 1,
                "preco": item["preco"]
            }

    for nome, dados in contador.items():

        texto += (
            f"🎮 {nome}\n"
            f"Quantidade: x{dados['quantidade']}\n"
            f"Preço: R$ {dados['preco']}\n\n"
        )

    texto += "--------------------\n"
    texto += f"💰 TOTAL: R$ {total}"

    carrinho_texto.configure(text=texto)


# =========================
# FUNÇÃO ADICIONAR
# =========================

def adicionar_carrinho():

    global total

    indice = lista_jogos.curselection()

    if indice:

        jogo = jogos[indice[0]]

        itens_carrinho.append(jogo)

        total += jogo["preco"]

        atualizar_carrinho()

        status.configure(
            text=f"✅ {jogo['nome']} adicionado ao carrinho!"
        )


# =========================
# FUNÇÃO FINALIZAR COMPRA
# =========================

def finalizar_compra():

    if itens_carrinho:

        popup = ctk.CTkToplevel(janela)

        popup.title("Compra Finalizada")
        popup.geometry("450x300")
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
                f"💰 Total pago: R$ {total}"
            ),
            font=("Arial", 18),
            justify="center"
        )

        texto_popup.pack(pady=10)

        linha = ctk.CTkFrame(
            popup,
            height=2,
            fg_color="#5865F2"
        )

        linha.pack(fill="x", padx=40, pady=15)

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

        botao_fechar.pack(pady=15)

        carrinho_texto.configure(
            text="✅ Compra finalizada!"
        )

        status.configure(
            text="Obrigado por comprar na Geek Store!"
        )

    else:

        popup = ctk.CTkToplevel(janela)

        popup.title("Aviso")
        popup.geometry("400x250")
        popup.resizable(False, False)

        popup.configure(fg_color="#1e1e1e")

        popup.grab_set()

        aviso = ctk.CTkLabel(
            popup,
            text="⚠️ CARRINHO VAZIO",
            font=("Arial", 26, "bold"),
            text_color="#FFCC00"
        )

        aviso.pack(pady=(35, 15))

        texto = ctk.CTkLabel(
            popup,
            text=(
                "Adicione um jogo antes\n"
                "de finalizar a compra."
            ),
            font=("Arial", 16),
            justify="center"
        )

        texto.pack(pady=10)

        botao_ok = ctk.CTkButton(
            popup,
            text="OK",
            width=160,
            height=40,
            corner_radius=12,
            fg_color="#5865F2",
            hover_color="#4752C4",
            font=("Arial", 15, "bold"),
            command=popup.destroy
        )

        botao_ok.pack(pady=20)


# =========================
# TÍTULO
# =========================

titulo = ctk.CTkLabel(
    janela,
    text="GEEK STORE",
    font=("Arial", 42, "bold"),
    text_color="#5865F2"
)

titulo.pack(pady=(25, 5))


subtitulo = ctk.CTkLabel(
    janela,
    text="Sua loja gamer digital",
    font=("Arial", 16),
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
# TEXTO CATÁLOGO
# =========================

catalogo = ctk.CTkLabel(
    frame_esquerdo,
    text="CATÁLOGO DE JOGOS",
    font=("Arial", 24, "bold")
)

catalogo.pack(pady=20)


# =========================
# LISTA DE JOGOS
# =========================

lista_jogos = tk.Listbox(
    frame_esquerdo,
    width=42,
    height=15,
    bg="#2b2b2b",
    fg="white",
    font=("Arial", 14),
    selectbackground="#5865F2",
    selectforeground="white",
    bd=0,
    highlightthickness=0
)

lista_jogos.pack(padx=20, pady=10)


for jogo in jogos:

    lista_jogos.insert(
        tk.END,
        f"{jogo['nome']} - R${jogo['preco']}"
    )


# =========================
# BOTÃO ADICIONAR
# =========================

botao = ctk.CTkButton(
    frame_esquerdo,
    text="Adicionar ao Carrinho",
    font=("Arial", 16, "bold"),
    height=50,
    corner_radius=12,
    fg_color="#5865F2",
    hover_color="#4752C4",
    command=adicionar_carrinho
)

botao.pack(pady=20)


# =========================
# STATUS
# =========================

status = ctk.CTkLabel(
    frame_esquerdo,
    text="Selecione um jogo para adicionar.",
    font=("Arial", 13),
    text_color="gray"
)

status.pack(pady=(0, 15))


# =========================
# FRAME DIREITO
# =========================

frame_direito = ctk.CTkFrame(
    frame_principal,
    fg_color="#242424",
    corner_radius=15,
    width=340
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
    font=("Arial", 24, "bold")
)

titulo_carrinho.pack(pady=20)


# =========================
# TEXTO CARRINHO
# =========================

carrinho_texto = ctk.CTkLabel(
    frame_direito,
    text="Carrinho vazio",
    font=("Arial", 14),
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
    font=("Arial", 16, "bold"),
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
# RODAR JANELA
# =========================

janela.mainloop()