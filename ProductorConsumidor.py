import time, random
import keyboard
from os import system

semaforo_prod = False
ocupado = False
semaforo_consu = False

lleno = False
vacio = False

productor_posicion= 0
Consumidor_posicion = 0
contador = 0

buffer = [" "] * 22 #creamos el Buffer con el tamaño de los datos

def Productor():
    global productor_posicion, contador, buffer, semaforo_prod, semaforo_consu, ocupado
    RemainingTime = random.randrange(2,8)
    while True:
        if RemainingTime == 0: break
        if ocupado == True and semaforo_consu == True: 
            print("El productor dormirá hasta que este disponible o se termine su tiempo")
        else: 
            ocupado = True
            semaforo_prod = True
            if (productor_posicion >= 22):
                productor_posicion = 0
            if buffer[productor_posicion] == 'X':
                if(RemainingTime > 2):
                    print("Aún hay valores el productor dormirá un momento")
                    time.sleep(RemainingTime)
                    break  
            else:                                   
                buffer[productor_posicion] = 'X'
            print("{} Productor Agrego elementos".format(buffer))            
            if (productor_posicion < 22):
                productor_posicion += 1            
            else: 
                productor_posicion = 0
           
            RemainingTime = RemainingTime - 1
        time.sleep(0.25)
    ocupado = False
    semaforo_prod = False

def Consumidor():
    global Consumidor_posicion, contador, buffer, semaforo_prod, semaforo_consu, ocupado
    RemainingTime = random.randrange(2,5)
    while True:     
        if RemainingTime == 0: break   
        if ocupado == True and semaforo_prod == True: 
            print("El consumidor dormirá hasta que este disponible o se termine su tiempo")
        else: 
            ocupado = True
            semaforo_consu = True
            if (Consumidor_posicion >= 22 ):
                Consumidor_posicion = 0
            if buffer[Consumidor_posicion] == ' ':
                print("no hay para consumir es esa posición")
                time.sleep(RemainingTime)
                break
            else: buffer[Consumidor_posicion] = ' '
            print("{} Consumidor quitó elementos".format(buffer))         
            if (Consumidor_posicion < 22):
                Consumidor_posicion += 1            
            else: 
                Consumidor_posicion = 0
            RemainingTime = RemainingTime - 1
        time.sleep(0.25)  
    ocupado = False
    semaforo_consu = False

def main():
    while True:        
        time.sleep(0.25)    
        if keyboard.is_pressed('esc'):
            print('proceso terminado')
            break        
        else:     
            Productor()
            Consumidor() 
        


main()