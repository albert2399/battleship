import os
import time


class Tablero:
    
    def __init__(self, mar):
        self.mar = mar

    def coordenadas():
        coordenadas = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
        return coordenadas

    def mapa(self):
        print("  A B C D E F G H")
        print("  _ _ _ _ _ _ _ _")
        numero_fila = 1
        for fila in self.mar:
          print("%d|%s|" % (numero_fila, "|".join(fila)))
          numero_fila += 1

class Barcos:
    
    barcos = {'Acorazado': 4, 'Submarino': 3, 'Destructor': 2, 'Barco': 1}
    
    def __init__(self, name, vertical):
        self.coordenadas = []
        self.hundido = False
        self.vertical = vertical
        self.name = name
        self.lenght = self.barcos[name]
        
    
class Jugador:
    
    def __init__(self, mar):
        self.mar = mar
        
    def posiciones(self):
        try:
      
            columna_y = input('\nIntroduce la columna en la que crees que está el barco: ').upper()
            while columna_y not in "ABCDEFGH":
          
                print('\nCaracter no válido. Introduce una letra de la A a la H')
                columna_y = input('\nIntroduce la columna en la que deseas colocar el barco: ').upper()
          
            fila_x = input('\nIntroduce la fila en la que deseas colocar el barco: ')
      
            while fila_x not in '12345678':
                print('\nCaracter no válido. Introduce un número del 1 al 8.')
                fila_x = input('\nIntroduce la fila en la que deseas colocar el baro: ')    
    
            return int(fila_x) - 1, Tablero.coordenadas()[columna_y]
            
            
    
        except ValueError and KeyError:
            print("Caracter no válido.")
      
            return self.posiciones()
        
            
    def ataque(self):
        try:
      
            columna_y = input('\nIntroduce la columna en la que crees que está el barco: ').upper()
            while columna_y not in "ABCDEFGH":
          
                print('\nCaracter no válido. Introduce una letra de la A a la H')
                columna_y = input('\nIntroduce la columna en la que deseas colocar el barco: ').upper()
          
            fila_x = input('\nIntroduce la fila en la que deseas colocar el barco: ')
      
            while fila_x not in '12345678':
                print('\nCaracter no válido. Introduce un número del 1 al 8.')
                fila_x = input('\nIntroduce la fila en la que deseas colocar el baro: ')
          
            return int(fila_x) - 1, Tablero.coordenadas()[columna_y]
    
        except ValueError and KeyError:
            print("Caracter no válido.")
      
            return self.ataque()
            

    
    
def run():
    tablero1 = Tablero([[" "] * 8 for i in range(8)])
    tablero2 = Tablero([[" "] * 8 for i in range(8)])
    ataque1 = Tablero([[" "] * 8 for i in range(8)])
    ataque2 = Tablero([[" "] * 8 for i in range(8)])
    barcos1 = 8
    barcos2 = 8
    turn = 0
    player1 = 0
    player2 = 0

    
    while barcos1 != 0:
        print('Jugador 1, es tu turno de colocar los barcos\n' + str(barcos1) + ' barcos restantes\n')
        Tablero.mapa(tablero1)
        jugador1_x, jugador1_y = Jugador.posiciones(object)
        if tablero1.mar[jugador1_x][jugador1_y] == "O":
          print("\nYa introduciste esta posición antes")
          barcos1 += 1
        
        tablero1.mar[jugador1_x][jugador1_y] = 'O'
        barcos1 -= 1
    
    os.system('clear')
          
    while barcos2 != 0:
        print('Jugador 2, es tu turno de colocar los barcos\n' + str(barcos2) + ' barcos restantes\n')
        Tablero.mapa(tablero2)
        jugador2_x, jugador2_y = Jugador.posiciones(object)
        if tablero2.mar[jugador2_x][jugador2_y] == "O":
            print("\nYa introduciste esta posición antes")
            barcos2 += 1
        tablero2.mar[jugador2_x][jugador2_y] = 'O'
        barcos2 -= 1
    
    os.system('clear')
        
    while True:
    
        if turn % 2 == 0:
            print('\nJugador 1, es tu turno de atacar\n')
            Tablero.mapa(ataque1)
            ataque1_x, ataque1_y = Jugador.ataque(object)
            while ataque1.mar[ataque1_x][ataque1_y] == '-' or ataque1.mar[ataque1_x][ataque1_y] == 'X':
                print('\nYa introduciste esta posición antes')
                ataque1_x, ataque1_y = Jugador.ataque(object)
        
            if tablero2.mar[ataque1_x][ataque1_y] == "O":
                print('\n¡Tocado y hundido!')
                ataque1.mar[ataque1_x][ataque1_y] = "X"
                player1 += 1
            else:
                print("\nAgua")
                ataque1.mar[ataque1_x][ataque1_y] = "-"   
            turn += 1    
            time.sleep(2)
            os.system('clear')
        
        elif turn % 2 != 0:
            print('\nJugador 2, es tu turno de atacar\n')
            Tablero.mapa(ataque2)
            ataque2_x, ataque2_y = Jugador.ataque(object)
            while ataque2.mar[ataque2_x][ataque2_y] == '-' or ataque2.mar[ataque2_x][ataque2_y] == 'X':
                print('\nYa introduciste esta posición antes')
                ataque2_x, ataque2_y = Jugador.ataque(object)
            
            if tablero1.mar[ataque2_x][ataque2_y] == "O":
                print('\n¡Tocado y hundido!')
                ataque2.mar[ataque2_x][ataque2_y] = "X"
                player2 += 1
            else:
                print("\nAgua")
                ataque2.mar[ataque2_x][ataque2_y] = "-" 
                
            turn += 1
            time.sleep(2)
            os.system('clear')
        
        if player1 == 8:
            print('\nEl jugador 1 ha ganado ¡Enhorabuena!')
            return False
        
        elif player2 == 8:
            print('\nEl jugador 2 ha ganado ¡Enhorabuena!')
            return False    
        
        
        
        
if __name__ == '__main__':
    run()
        
        
    
    

        
    
    