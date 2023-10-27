import tkinter as tk
import numpy as np
  
def comprobar():
    filasA = int(filasA_entry.get())
    columnasA = int(columnasA_entry.get())
    filasB = int(filasB_entry.get())
    columnasB = int(columnasB_entry.get())

    if columnasA != filasB:
        resultado_label.config(text="La operación no se puede realizar porque las filas y las columnas de las matrices no son iguales")
    else:
        crear_entradas_matriz(filasA, columnasA, filasB, columnasB)

def crear_entradas_matriz(filasA, columnasA, filasB, columnasB):
    global matriz_a_entries  
    global matriz_b_entries 

    matriz_a_entries = []
    matriz_b_entries = []

    for i in range(filasA):
        row_entries = []
        for j in range(columnasA):
            entry = tk.Entry(frame2)
            entry.grid(row=i + 1, column=j)
            row_entries.append(entry)
        matriz_a_entries.append(row_entries)

    for i in range(filasB):
        row_entries = []
        for j in range(columnasB):
            entry = tk.Entry(frame2)
            entry.grid(row=i + 1, column=j + columnasA + 1)
            row_entries.append(entry)
        matriz_b_entries.append(row_entries)

    calcular_button = tk.Button(frame2, text="Calcular", bg="blue", font=("Helvetica", 12, "bold"), command=calcular_matrices)
    calcular_button.grid(row=max(filasA, filasB) + 2, columnspan=2, pady=10)

def obtener_valores_matriz(entries):
    return [[float(entry.get()) for entry in row] for row in entries]

def calcular_matrices():
    matriz_A = obtener_valores_matriz(matriz_a_entries)
    matriz_B = obtener_valores_matriz(matriz_b_entries)

    resultado_multiplicacion = np.dot(matriz_A, matriz_B)

    # Convertir el resultado en una cadena para mostrarlo en la etiqueta
    resultado_multiplicacion_str = "\n".join(["\t".join(map(str, row)) for row in resultado_multiplicacion])

    resultado_label.config(text=resultado_multiplicacion_str, bg="royalblue")
    resultado_label.grid(row=5, columnspan=2, pady=10)

    matC_label = tk.Label(frame2, text="Matriz C", bg="royalblue", font=("Helvetica", 12, "bold"))
    matC_label.grid(row=4, columnspan=2, pady=10)

root = tk.Tk()
root.title("Multiplicación de Matrices")
root.geometry("800x500")
root.config(bg="royalblue")

frame1 = tk.Frame(root, bg="navy")
frame1.pack()

# Widget para ingresar los datos de las matrices
titulo_label = tk.Label(frame1, text="Calculadora de Multiplicación de Matrices", bg="navy", font=("Helvetica", 25, "bold"))
titulo_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky='n')

filas_A = tk.Label(frame1, bg="navy", text="Número de filas de la Matriz A:", fg="white", font=("Helvetica", 12, "bold"))
filas_A.grid(row=1, column=0)
filasA_entry = tk.Entry(frame1)
filasA_entry.grid(row=1, column=1)

columnasA = tk.Label(frame1, bg="navy", text="Número de columnas de la Matriz A:", fg="white", font=("Helvetica", 12, "bold"))
columnasA.grid(row=2, column=0)
columnasA_entry = tk.Entry(frame1)
columnasA_entry.grid(row=2, column=1)

filasB = tk.Label(frame1, bg="navy", text="Número de filas de la Matriz B:", fg="white", font=("Helvetica", 12, "bold"))
filasB.grid(row=3, column=0)
filasB_entry = tk.Entry(frame1)
filasB_entry.grid(row=3, column=1)

columnasB = tk.Label(frame1, bg="navy", text="Número de columnas de la Matriz B:", fg="white", font=("Helvetica", 12, "bold"))
columnasB.grid(row=4, column=0)
columnasB_entry = tk.Entry(frame1)
columnasB_entry.grid(row=4, column=1)

comprobar_button = tk.Button(frame1, bg="blue", text="INGRESAR MATRICES", command=comprobar, font=("Helvetica", 12, "bold"))
comprobar_button.grid(row=5, columnspan=2, pady=10)

frame2 = tk.Frame(root, bg="navy")
frame2.pack()

# Labels que muestran las matrices en la interfaz
label_matA = tk.Label(frame2, bg="navy", text="Matriz A:", fg="white", font=("Helvetica", 12, "bold"))
label_matA.grid(row=0, column=1, pady=10)
label_matB = tk.Label(frame2, bg="navy", text="Matriz B:", fg="white", font=("Helvetica", 12, "bold"))
label_matB.grid(row=0, column=2, pady=10)

resultado_label = tk.Label(frame2, text="", bg="navy")
resultado_label.grid(row=1, columnspan=2)

root.mainloop()
