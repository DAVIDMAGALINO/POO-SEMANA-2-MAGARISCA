import threading
import time

# Definimos una función para la tarea del primer hilo
def tarea1():
    for i in range(5):
        print(f"Hilo 1: Contador {i}")
        time.sleep(1)  # Simula una tarea que toma tiempo

# Definimos una función para la tarea del segundo hilo
def tarea2():
    for i in range(5):
        print(f"Hilo 2: Contador {i}")
        time.sleep(1.5)  # Simula una tarea que toma más tiempo

# Definimos una función para la tarea del tercer hilo
def tarea3():
    for i in range(5):
        print(f"Hilo 3: Contador {i}")
        time.sleep(2)  # Simula una tarea que toma tiempo

# Creamos los hilos
hilo1 = threading.Thread(target=tarea1)
hilo2 = threading.Thread(target=tarea2)
hilo3 = threading.Thread(target=tarea3)

# Iniciamos los hilos
hilo1.start()
hilo2.start()
hilo3.start()

# Esperamos a que todos los hilos terminen
hilo1.join()
hilo2.join()
hilo3.join()

print("Todas las tareas han finalizado.")
