# Funções para operações com memória
memoria = {}

def adicionar_memoria(nome, valor):
    memoria[nome] = valor

def remover_memoria(nome):
    if nome in memoria:
        del memoria[nome]
    else:
        messagebox.showinfo("Informação", f"Nome '{nome}' não encontrado na memória.")

def consultar_memoria(nome):
    if nome in memoria:
        return memoria[nome]
    else:
        messagebox.showinfo("Informação", f"Nome '{nome}' não encontrado na memória.")

def limpar_memoria():
    memoria.clear()
    messagebox.showinfo("Informação", "Memória limpa.")

# Funções de memória
def adicionar_memoria(nome, valor):
    # ... (implementar a lógica para adicionar o valor à memória)

def remover_memoria(nome):
    # ... (implementar a lógica para remover o valor da memória)

def consultar_memoria(nome):
    # ... (implementar a lógica para consultar o valor na memória)

def limpar_memoria():
    # ... (implementar a lógica para limpar a memória)    