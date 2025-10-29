import tkinter as tk


root = tk.Tk()
root.title("Ejercicio 10: Scrollbar")
root.geometry("500x300")


texto = tk.Text(root, wrap="word", width=50, height=10)
texto.pack(side="left", fill="both", expand=True, padx=5, pady=5)


scroll = tk.Scrollbar(root, orient="vertical", command=texto.yview)
scroll.pack(side="right", fill="y")


texto.config(yscrollcommand=scroll.set)


parrafo = """\
Blue Lock es una serie de manga y anime japonesa que mezcla el fútbol con elementos psicológicos y competitivos de una forma nunca antes vista. 

La historia comienza después del fracaso de la selección japonesa en el Mundial, lo que lleva a la Federación de Fútbol de Japón a crear un proyecto radical llamado Blue Lock, diseñado para encontrar y entrenar al delantero más egoísta, ambicioso y decisivo del país.

A diferencia de las academias tradicionales, donde se promueve el trabajo en equipo, Blue Lock rompe con esa idea: busca crear un jugador que piense solo en marcar goles y ganar, incluso si eso significa traicionar a sus compañeros.

El protagonista, Yoichi Isagi, es un joven con talento, pero inseguro y acostumbrado a jugar para el equipo. 
Cuando entra en Blue Lock, se enfrenta a cientos de delanteros que comparten el mismo sueño que él: convertirse en el mejor goleador del mundo. 
A través de pruebas físicas, psicológicas y tácticas, los participantes son eliminados.
"""

texto.insert("1.0", parrafo)


root.mainloop()