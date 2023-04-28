import tkinter as tk
from tkinter import ttk
import datetime as dt
import mysql.connector

lista_tipos = ["Caixa", "Saco", "Unidade"]
lista_codigos = []

janela = tk.Tk()

#conexao com o banco
conexao = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= 'root',
    database= 'AtividadeExtra'
)


# CREATE
def command(conexao=conexao):
    cursor = conexao.cursor()
    nome_material = entry_descricao.get()
    tipo_unidade = combobox_selecionar_tipo.get()
    quantidade = entry_quant.get()
    comando = f'INSERT INTO materiais (nome_material, tipo_unidade, quantidade_unidade) VALUES ("{nome_material}", "{tipo_unidade}", {quantidade})'

    cursor.execute(comando)
    conexao.commit()  # CONEXAO PARA EDITAR O BANCO DE DADOS
    cursor.close()


# Título da Janela

janela.title('Ferramenta de cadastro de materiais')

label_descricao = tk.Label(text="Descrição do Material")
label_descricao.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

entry_descricao = tk.Entry()
entry_descricao.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

label_tipo_unidade = tk.Label(text="Tipo da unidade do Material")
label_tipo_unidade.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

combobox_selecionar_tipo = ttk.Combobox(values=lista_tipos)
combobox_selecionar_tipo.grid(row=3, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

label_quant = tk.Label(text="Quantidade na unidade de material")
label_quant.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

entry_quant = tk.Entry()
entry_quant.grid(row=4, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

botao = tk.Button(text="Criar código", command=command)
botao.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

janela.mainloop()