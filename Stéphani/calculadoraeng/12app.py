import math
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import numpy as np
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Interface gráfica (utilizando tkinter como exemplo)
def interface():
    # Criar a janela principal
    janela = Tk()
    janela.title("Calculadora Científica Avançada - Engenharia Civil e Básica")

    # Abas para separação das funcionalidades
    abas = ttk.Notebook(janela)
    aba_basica = ttk.Frame(abas)
    aba_avancada = ttk.Frame(abas)
    aba_engenharia_civil = ttk.Frame(abas)
    abas.add(aba_basica, text="Básica")
    abas.add(aba_avancada, text="Avançada")
    abas.add(aba_engenharia_civil, text="Eng. Civil")
    abas.pack(expand=True, fill="both")

    # Funcionalidades básicas (utilizar widgets do tkinter)
    # ... (implementar campos de entrada, botões, labels para as operações básicas)

    # Funcionalidades avançadas (integração, derivada, transformada de Fourier)
    def integracao_numerica():
        funcao_str = entrada_funcao.get()
        a = float(entrada_limite_a.get())
        b = float(entrada_limite_b.get())
        n = int(entrada_pontos.get())
        resultado = integral_numerica(funcao_str, a, b, n)
        if resultado is not None:
            label_resultado_integracao.config(text=f"Resultado: {resultado:.4f}")

    label_funcao_integracao = Label(aba_avancada, text="Função:")
    label_funcao_integracao.pack()
    entrada_funcao = Entry(aba_avancada)
    entrada_funcao.pack()

    label_limite_a = Label(aba_avancada, text="Limite inferior (a):")
    label_limite_a.pack()
    entrada_limite_a = Entry(aba_avancada)
    entrada_limite_a.pack()

    label_limite_b = Label(aba_avancada, text="Limite superior (b):")
    label_limite_b.pack()
    entrada_limite_b = Entry(aba_avancada)
    entrada_limite_b.pack()

    label_pontos = Label(aba_avancada, text="Número de pontos (n):")
    label_pontos.pack()
    entrada_pontos = Entry(aba_avancada)
    entrada_pontos.pack()

    botao_integrar = Button(aba_avancada, text="Integrar", command=integracao_numerica)
    botao_integrar.pack()

    label_resultado_integracao = Label(aba_avancada, text="Resultado:")
    label_resultado_integracao.pack()

    def derivada_numerica():
        funcao_str = entrada_funcao_derivada.get()
        x = float(entrada_valor_x.get())
        h = float(entrada_passo.get())
        resultado = derivada_numerica(funcao_str, x, h)
        if resultado is not None:
            label_resultado_derivada.config(text=f"Derivada: {resultado:.4f}")

    label_funcao_derivada = Label(aba_avancada, text="Função:")
    label_funcao_derivada.pack()
    entrada_funcao_derivada = Entry(aba_avancada)
    entrada_funcao_derivada.pack()

    label_valor_x = Label(aba_avancada, text="Valor de x:")
    label_valor_x.pack()
    entrada_valor_x = Entry(aba_avancada)
    entrada_valor_x.pack()

    label_passo = Label(aba_avancada, text="Passo (h):")
    label_passo.pack()
    entrada_passo = Entry(aba_avancada)
    entrada_passo.pack()

    botao_derivar = Button(aba_avancada, text="Derivar", command=derivada_numerica)
    botao_derivar.pack()

    label_resultado_derivada = Label(aba_avancada, text="Resultado:")
    label_resultado_derivada.pack()

    def transformada_fourier_plot():
        sinal_str = entrada_sinal.get()
        try:
            sinal = eval(sinal_str)
            fourier = transformada_fourier(sinal)
            plt.plot(np.abs(fourier))
            plt.title("Transformada de Fourier")
            plt.xlabel("Frequência")
            plt.ylabel("Magnitude")
            plt.show()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao processar o sinal: {e}")

    label_sinal = Label(aba_avancada, text="Sinal:")
    label_sinal.pack()
    entrada_sinal = Entry(aba_avancada)
    entrada_sinal.pack()

    botao_fourier = Button(aba_avancada, text="Calcular Fourier", command=transformada_fourier_plot)
    botao_fourier.pack()

    # Funções de Engenharia Civil (implementar botões para acionar funções específicas)
    # ... (implementar botões para momento fletor, cortante
	# ... (código anterior para integração, derivada e transformada de Fourier)

    # Funções de Engenharia Civil (implementar botões para acionar funções específicas)
    # ... (implementar botões para momento fletor, cortante
	# ... (código anterior para integração, derivada e transformada de Fourier)


# Interface gráfica principal
app = tk.Tk()
app.title("Calculadora Avançada")

# Criando abas para diferentes funcionalidades
aba_basica = tk.Frame(app)
aba_avancada = tk.Frame(app)
aba_memoria = tk.Frame(app)
aba_engenharia_civil = tk.Frame(app)

aba_basica.pack(side="top", fill="both", expand=True)
aba_avancada.pack(side="top", fill="both", expand=True)
aba_memoria.pack(side="top", fill="both", expand=True)
aba_engenharia_civil.pack(side="top", fill="both", expand=True)

# Funções básicas (soma, subtração, multiplicação, divisão)
label_titulo_basica = tk.Label(aba_basica, text="Funções Básicas")
label_titulo_basica.pack()

label_a_soma = tk.Label(aba_basica, text="Valor de a:")
label_a_soma.pack()
entrada_a_soma = tk.Entry(aba_basica)
entrada_a_soma.pack()

label_b_soma = tk.Label(aba_basica, text="Valor de b:")
label_b_soma.pack()
entrada_b_soma = tk.Entry(aba_basica)
entrada_b_soma.pack()

botao_somar = tk.Button(aba_basica, text="Somar", command=lambda: soma_interface(entrada_a_soma, entrada_b_soma))
botao_somar.pack()

label_resultado_soma = tk.Label(aba_basica, text="Resultado:")
label_resultado_soma.pack()

# ... (interfaces para as outras funções básicas: subtração, multiplicação, divisão)

# Funções avançadas (integração, derivada, transformada de Fourier)
label_titulo_avancada = tk.Label(aba_avancada, text="Funções Avançadas")
label_titulo_avancada.pack()

# ... (implementar interfaces para integração, derivada e transformada de Fourier)

# Funções de memória (adicionar, remover, consultar, limpar)
label_titulo_memoria = tk.Label(aba_memoria, text="Memória")
label_titulo_memoria.pack()

# ... (implementar interfaces para as funções de memória)

# Funções de Engenharia Civil (momento fletor, cortante, etc.)
label_titulo_engenharia_civil = tk.Label(aba_engenharia_civil, text="Engenharia Civil")    



