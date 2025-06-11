import tkinter as tk
from tkinter import messagebox
import threading
import time
import pygame
import sys
import os

# === Caminho seguro para tick.wav (funciona mesmo empacotado) ===
def resource_path(relative_path):
    """Retorna o caminho absoluto para o arquivo, funcionando com PyInstaller"""
    try:
        base_path = sys._MEIPASS  # PyInstaller usa isso ao empacotar
    except AttributeError:
        base_path = os.path.abspath(".")  # Caminho padrão ao rodar como .py
    return os.path.join(base_path, relative_path)

# === Inicializa o pygame e carrega o som ===
pygame.mixer.init()
tick_sound = pygame.mixer.Sound(resource_path("tick.wav"))

# === Variável de controle do loop ===
rodando = False

def iniciar_metronomo(bpm):
    global rodando
    rodando = True
    intervalo = 60 / bpm

    def loop():
        while rodando:
            tick_sound.play()
            time.sleep(intervalo)

    threading.Thread(target=loop, daemon=True).start()

def parar_metronomo():
    global rodando
    rodando = False
    tick_sound.stop()

def on_iniciar_click():
    try:
        bpm = int(entry_bpm.get())
        if bpm <= 0:
            raise ValueError
        iniciar_metronomo(bpm)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido de BPM.")

def on_parar_click():
    parar_metronomo()

# === Interface Gráfica (Tkinter) ===
janela = tk.Tk()
janela.title("Basic Metrônomo")
janela.geometry("300x150")
janela.resizable(False, False)

label = tk.Label(janela, text="BPM:")
label.pack(pady=10)

entry_bpm = tk.Entry(janela, justify="center", font=("Arial", 14))
entry_bpm.insert(0, "60")
entry_bpm.pack()

btn_iniciar = tk.Button(janela, text="Iniciar", command=on_iniciar_click, bg="green", fg="white", width=10)
btn_iniciar.pack(pady=5)

btn_parar = tk.Button(janela, text="Parar", command=on_parar_click, bg="red", fg="white", width=10)
btn_parar.pack()

janela.mainloop()
