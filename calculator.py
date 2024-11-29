import tkinter as tk

# Funções para realizar as operações
def add():
    result_var.set(float(entry1.get()) + float(entry2.get()))

def subtract():
    result_var.set(float(entry1.get()) - float(entry2.get()))

def multiply():
    result_var.set(float(entry1.get()) * float(entry2.get()))

def divide():
    try:
        result_var.set(float(entry1.get()) / float(entry2.get()))
    except ZeroDivisionError:
        result_var.set("Erro: Divisão por zero")

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora Simples")

# Criando os elementos da interface
label1 = tk.Label(root, text="Digite o primeiro número:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Digite o segundo número:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

# Variável para exibir o resultado
result_var = tk.StringVar()

# Exibindo o resultado
label_result = tk.Label(root, text="Resultado:")
label_result.pack()

result_label = tk.Label(root, textvariable=result_var)
result_label.pack()

# Botões para as operações
button_add = tk.Button(root, text="Soma", command=add)
button_add.pack()

button_subtract = tk.Button(root, text="Subtração", command=subtract)
button_subtract.pack()

button_multiply = tk.Button(root, text="Multiplicação", command=multiply)
button_multiply.pack()

button_divide = tk.Button(root, text="Divisão", command=divide)
button_divide.pack()

# Iniciando a interface gráfica
root.mainloop()

