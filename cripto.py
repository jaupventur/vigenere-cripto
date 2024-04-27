import tkinter as tk
from tkinter import simpledialog, messagebox

def vigenere_criptografar(texto_plano, chave):
    texto_cifrado = ""
    tamanho_chave = len(chave)
    for i in range(len(texto_plano)):
        char = texto_plano[i]
        if char.isalpha():
            deslocamento = ord(chave[i % tamanho_chave].upper()) - ord('A')
            if char.isupper():
                texto_cifrado += chr((ord(char) + deslocamento - 65) % 26 + 65)
            else:
                texto_cifrado += chr((ord(char) + deslocamento - 97) % 26 + 97)
        else:
            texto_cifrado += char
    return texto_cifrado

def vigenere_descriptografar(texto_cifrado, chave):
    texto_plano = ""
    tamanho_chave = len(chave)
    for i in range(len(texto_cifrado)):
        char = texto_cifrado[i]
        if char.isalpha():
            deslocamento = ord(chave[i % tamanho_chave].upper()) - ord('A')
            if char.isupper():
                texto_plano += chr((ord(char) - deslocamento - 65) % 26 + 65)
            else:
                texto_plano += chr((ord(char) - deslocamento - 97) % 26 + 97)
        else:
            texto_plano += char
    return texto_plano

def principal():
    raiz = tk.Tk()
    raiz.withdraw()  # Esconde a janela principal

    acao = simpledialog.askstring("Entrada", "Escolha a ação (criptografar/descriptografar):")
    if acao not in ["criptografar", "descriptografar"]:
        messagebox.showerror("Erro", "Ação escolhida inválida!")
        return

    mensagem = simpledialog.askstring("Entrada", "Digite sua mensagem:")
    chave = simpledialog.askstring("Entrada", "Digite sua chave:")
    
    if not mensagem or not chave or not all(k.isalpha() for k in chave):
        messagebox.showerror("Erro", "Mensagem ou chave inválida!")
        return

    if acao == "criptografar":
        resultado = vigenere_criptografar(mensagem, chave)
    else:
        resultado = vigenere_descriptografar(mensagem, chave)

    messagebox.showinfo("Resultado", resultado)

if __name__ == "__main__":
    principal()