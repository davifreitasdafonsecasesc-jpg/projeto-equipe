# ================================================================
#  💬 QUADRO DE COMUNICAÇÃO
#  Um app pra quem tem dificuldade de falar (por exemplo, por autismo,
#  depois de um AVC, ou um paciente conversando com quem cuida dele).
#  A pessoa clica num botão e a frase aparece GIGANTE pra outra ler.
#
#  Esse código é SEU: cria suas frases, muda as cores, inventa moda.
#  Procura os comentários "👉 TROQUE AQUI" pra saber por onde começar.
# ================================================================

import customtkinter

# Tema do app: "dark" é o modo escuro e "light" é o claro
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Criando a janela, que é a "estante" onde as caixas vão ficar
janela = customtkinter.CTk()
janela.title("Quadro de Comunicação")
janela.geometry("800x650")

# Tamanho da letra do visor
tamanho_letra = 50  # 👉 TROQUE AQUI se quiser começar maior ou menor


# ================================================================
#  FUNÇÕES DAS FRASES
#  Cada botão tem a sua função. Repara que todas seguem o MESMO
#  padrão: só muda a frase. Quer uma frase nova? Copia uma, cola
#  embaixo, troca o nome e a frase. Fácil demais!
# ================================================================

def falar_fome():
    visor.configure(text="Estou com fome")


def falar_sede():
    visor.configure(text="Estou com sede")


def falar_banheiro():
    visor.configure(text="Preciso ir ao banheiro")


def falar_sim():
    visor.configure(text="SIM")


def falar_nao():
    visor.configure(text="NÃO")


def falar_ajuda():
    visor.configure(text="Preciso de ajuda!")


def mostrar_frase():
    # Pega a frase que a pessoa digitou
    frase = entrada.get()

    # Se não digitou nada, a gente avisa de boa
    if frase == "":
        visor.configure(text="Digite uma frase primeiro!")
    else:
        visor.configure(text=frase)
        entrada.delete(0, "end")  # Limpa a entrada pra próxima frase


# ================================================================
#  FUNÇÕES DE ACESSIBILIDADE (as mesmas da Lupa de Texto!)
# ================================================================

def aumentar():
    # "global" avisa o Python que é pra mexer na variável lá de cima
    global tamanho_letra

    if tamanho_letra < 120:
        tamanho_letra = tamanho_letra + 10
        visor.configure(font=("Arial", tamanho_letra))
        info_tamanho.configure(text="Letra: " + str(tamanho_letra))


def diminuir():
    global tamanho_letra

    if tamanho_letra > 20:
        tamanho_letra = tamanho_letra - 10
        visor.configure(font=("Arial", tamanho_letra))
        info_tamanho.configure(text="Letra: " + str(tamanho_letra))


def trocar_tema():
    tema_atual = customtkinter.get_appearance_mode()

    if tema_atual == "Dark":
        customtkinter.set_appearance_mode("light")
        btn_tema.configure(text="Modo escuro")
    else:
        customtkinter.set_appearance_mode("dark")
        btn_tema.configure(text="Modo claro")


# ================================================================
#  📦 CAIXA 1: BARRA DE ACESSIBILIDADE (lá no topo)
#  Igualzinha à da Lupa de Texto. Reaproveitar código é coisa de dev!
# ================================================================

frame_barra = customtkinter.CTkFrame(master=janela)
frame_barra.pack(padx=10, pady=10, fill="x")

btn_diminuir = customtkinter.CTkButton(master=frame_barra, text="A-", width=60, height=50,
                                       font=("Arial", 22), command=diminuir)
btn_diminuir.pack(side="left", padx=5, pady=10)

btn_aumentar = customtkinter.CTkButton(master=frame_barra, text="A+", width=60, height=50,
                                       font=("Arial", 22), command=aumentar)
btn_aumentar.pack(side="left", padx=5, pady=10)

info_tamanho = customtkinter.CTkLabel(master=frame_barra, text="Letra: 50", font=("Arial", 20))
info_tamanho.pack(side="left", padx=15)

btn_tema = customtkinter.CTkButton(master=frame_barra, text="Modo claro", height=50,
                                   font=("Arial", 20), command=trocar_tema)
btn_tema.pack(side="right", padx=10, pady=10)


# ================================================================
#  📦 CAIXA 2: VISOR (onde a frase aparece grandona)
#  Lembra do segredo das cores? (cor do modo claro, cor do modo escuro)
# ================================================================

frame_visor = customtkinter.CTkFrame(master=janela,
                                     fg_color=("white", "black"))  # 👉 TROQUE AQUI as duas cores
frame_visor.pack(padx=10, pady=10, fill="both", expand=True)

visor = customtkinter.CTkLabel(master=frame_visor, text="Clique em um botão",
                               font=("Arial", tamanho_letra), wraplength=700,
                               text_color=("black", "yellow"))  # 👉 TROQUE AQUI as duas cores
visor.pack(padx=20, pady=20, fill="both", expand=True)


# ================================================================
#  📦 CAIXA 3: LINHA DAS NECESSIDADES (botões azuis)
#  side="left" deixa os botões lado a lado.
#  expand=True e fill="x" fazem eles dividirem o espaço certinho.
# ================================================================

frame_necessidades = customtkinter.CTkFrame(master=janela, fg_color="transparent")
frame_necessidades.pack(padx=10, pady=5, fill="x")

btn_fome = customtkinter.CTkButton(master=frame_necessidades, text="Fome", height=70,
                                   font=("Arial", 24), command=falar_fome)
btn_fome.pack(side="left", padx=5, pady=5, expand=True, fill="x")

btn_sede = customtkinter.CTkButton(master=frame_necessidades, text="Sede", height=70,
                                   font=("Arial", 24), command=falar_sede)
btn_sede.pack(side="left", padx=5, pady=5, expand=True, fill="x")

btn_banheiro = customtkinter.CTkButton(master=frame_necessidades, text="Banheiro", height=70,
                                       font=("Arial", 24), command=falar_banheiro)
btn_banheiro.pack(side="left", padx=5, pady=5, expand=True, fill="x")


# ================================================================
#  📦 CAIXA 4: LINHA DAS RESPOSTAS (Sim, Não e Ajuda)
#  Aqui cada botão tem uma cor, pra pessoa achar rapidinho.
#  Botão pode usar uma cor só, porque o texto branco aparece bem
#  nos dois temas.
# ================================================================

frame_respostas = customtkinter.CTkFrame(master=janela, fg_color="transparent")
frame_respostas.pack(padx=10, pady=5, fill="x")

btn_sim = customtkinter.CTkButton(master=frame_respostas, text="Sim", height=70,
                                  font=("Arial", 24), fg_color="#2E7D32",  # verde 👉 TROQUE AQUI
                                  command=falar_sim)
btn_sim.pack(side="left", padx=5, pady=5, expand=True, fill="x")

btn_nao = customtkinter.CTkButton(master=frame_respostas, text="Não", height=70,
                                  font=("Arial", 24), fg_color="#C62828",  # vermelho 👉 TROQUE AQUI
                                  command=falar_nao)
btn_nao.pack(side="left", padx=5, pady=5, expand=True, fill="x")

btn_ajuda = customtkinter.CTkButton(master=frame_respostas, text="Ajuda!", height=70,
                                    font=("Arial", 24), fg_color="#E65100",  # laranja 👉 TROQUE AQUI
                                    command=falar_ajuda)
btn_ajuda.pack(side="left", padx=5, pady=5, expand=True, fill="x")


# ================================================================
#  📦 CAIXA 5: MINHA FRASE (lá embaixo)
#  Pra quando a frase que a pessoa quer não tem botão
# ================================================================

frame_frase = customtkinter.CTkFrame(master=janela)
frame_frase.pack(padx=10, pady=10, fill="x")

entrada = customtkinter.CTkEntry(master=frame_frase, height=50, font=("Arial", 24),
                                 placeholder_text="Escreva sua frase...")
entrada.pack(side="left", padx=10, pady=10, fill="x", expand=True)

btn_mostrar = customtkinter.CTkButton(master=frame_frase, text="Mostrar", height=50,
                                      font=("Arial", 22), command=mostrar_frase)
btn_mostrar.pack(side="right", padx=10, pady=10)


# ================================================================
#  💡 IDEIAS PRA VOCÊ TURBINAR O SEU APP
#  1. Troca as frases pelas que fazem sentido pra você ou pra alguém
#     que você conhece (ex.: "Estou com frio", "Quero dormir")
#  2. Cria uma CAIXA 6 com uma linha nova de botões (ex.: sentimentos:
#     Feliz, Triste, Cansado). É só copiar a caixa 3 e mudar os nomes!
#  3. Faz o botão Ajuda deixar o texto vermelho:
#     visor.configure(text_color="red")
#     (Mas atenção: aí os outros botões precisam voltar a cor normal com
#     visor.configure(text_color=("black", "yellow")), senão fica tudo vermelho!)
#  4. Coloca um botão "Limpar" que volta o visor pra "Clique em um botão"
# ================================================================

# Essa linha mantém a janela aberta. Ela sempre fica por último!
janela.mainloop()
