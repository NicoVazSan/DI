import tkinter as tk
from tkinter import messagebox
import random


root = tk.Tk()
root.title("Piedra-Papel-Tijera")


player_score = tk.IntVar(value=0)
cpu_score = tk.IntVar(value=0)


def nuevo_juego():
    player_score.set(0)
    cpu_score.set(0)
    resultado_label.config(text="")
    eleccion_cpu_label.config(text="")
    eleccion_jugador_label.config(text="")
    habilitar_botones(True)


def habilitar_botones(valor):
    piedra_btn.config(state=tk.NORMAL if valor else tk.DISABLED)
    papel_btn.config(state=tk.NORMAL if valor else tk.DISABLED)
    tijera_btn.config(state=tk.NORMAL if valor else tk.DISABLED)


def jugar(jugada_jugador):
    opciones = ["Piedra", "Papel", "Tijera"]
    jugada_cpu = random.choice(opciones)

    eleccion_jugador_label.config(text=f"Tú elegiste: {jugada_jugador}")
    eleccion_cpu_label.config(text=f"CPU eligió: {jugada_cpu}")

    if jugada_jugador == jugada_cpu:
        resultado_label.config(text="Empate")
        return
    elif (jugada_jugador == "Piedra" and jugada_cpu == "Tijera") or \
            (jugada_jugador == "Papel" and jugada_cpu == "Piedra") or \
            (jugada_jugador == "Tijera" and jugada_cpu == "Papel"):
        player_score.set(player_score.get() + 1)
        resultado_label.config(text="¡Ganaste esta ronda!")
    else:
        cpu_score.set(cpu_score.get() + 1)
        resultado_label.config(text="CPU gana esta ronda")


    if player_score.get() == 3:
        messagebox.showinfo("Fin de partida", "¡Felicidades, ganaste la partida!")
        habilitar_botones(False)
    elif cpu_score.get() == 3:
        messagebox.showinfo("Fin de partida", "Lo siento, la CPU ganó la partida")
        habilitar_botones(False)



tk.Label(root, text="Jugador:").grid(row=0, column=0)
tk.Label(root, textvariable=player_score).grid(row=0, column=1)
tk.Label(root, text="CPU:").grid(row=0, column=2)
tk.Label(root, textvariable=cpu_score).grid(row=0, column=3)


eleccion_jugador_label = tk.Label(root, text="", font=("Arial", 12))
eleccion_jugador_label.grid(row=1, column=0, columnspan=2)
eleccion_cpu_label = tk.Label(root, text="", font=("Arial", 12))
eleccion_cpu_label.grid(row=1, column=2, columnspan=2)


resultado_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
resultado_label.grid(row=2, column=0, columnspan=4, pady=10)


piedra_btn = tk.Button(root, text="Piedra", width=10, command=lambda: jugar("Piedra"))
piedra_btn.grid(row=3, column=0, pady=5)
papel_btn = tk.Button(root, text="Papel", width=10, command=lambda: jugar("Papel"))
papel_btn.grid(row=3, column=1, pady=5)
tijera_btn = tk.Button(root, text="Tijera", width=10, command=lambda: jugar("Tijera"))
tijera_btn.grid(row=3, column=2, pady=5)


nuevo_btn = tk.Button(root, text="Nuevo Juego", command=nuevo_juego)
nuevo_btn.grid(row=4, column=0, columnspan=2, pady=10)
salir_btn = tk.Button(root, text="Salir", command=root.quit)
salir_btn.grid(row=4, column=2, columnspan=2, pady=10)

root.mainloop()