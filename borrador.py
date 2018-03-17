"""Nombre: Karla Fragoso Cerecedo	
   Grupo: TIC 21
   Matricula: 1717110248	
   Fecha: 16/03/2018	
   Descripcion: 0.- Repetir indefinidamente:
   Imprimir el mapa en dos dimensiones 
   Preguntar hacia donde se quiere mover
   Mover derecha
   Mover izquierda 
   Mover arriba 
   Mover abajo 
   Empujar una caja 
   Activar/Desactivar habilidad especial 
"""


print "        Juego SokoBan"
print " Alumna: Karla Fragoso Cerecedo"
print " "
print " "
mapa=[[3,3,3,3,3,3,3,3,3,3],
      [3,4,0,4,4,4,4,4,4,3],
      [3,4,4,4,4,1,4,4,4,3],
      [3,4,1,1,4,4,4,4,4,3],
      [3,4,1,1,4,4,4,4,4,3],
      [3,4,4,4,4,4,4,4,4,3],
      [3,4,4,4,4,4,4,4,4,3],
      [3,3,3,3,3,3,3,3,3,3]]

fila=1
columna=2

while True:
    for x in (mapa):
        for y in x:
            print y,
        print
    print " "
    print "A= Izquierda y D= Derecha" 
    print "W= Arriba    y S= Abajo"
    print "   F= Super Fuerza"
    print " "
    movimiento=str(raw_input("Mueve al Sokobanito: "))
    if movimiento=="f":
            if mapa[fila][columna + 1]==1:
                 if mapa [fila][columna +2]==1:
                      if  mapa [fila][columna + 3]==4:
                                 mapa [fila][columna]=4
                                 mapa [fila][columna + 1]=0
                                 mapa [fila][columna + 2]=1
                                 mapa [fila][columna + 3]= 1
                                 columna= columna + 1
    if movimiento=="f":
            if mapa[fila][columna - 1]==1:
                 if mapa [fila][columna - 2]==1:
                      if  mapa [fila][columna - 3]==4:
                                 mapa [fila][columna]=4
                                 mapa [fila][columna - 1]=0
                                 mapa [fila][columna - 2]=1
                                 mapa [fila][columna - 3]= 1
                                 columna= columna - 1
    if movimiento=="f":
            if mapa[fila - 1][columna]==1:
                  if mapa [fila - 2][columna]==1:
                       if  mapa [fila - 3][columna]==4:
                                 mapa [fila][columna]=4
                                 mapa [fila - 1][columna]=0
                                 mapa [fila - 2][columna]=1
                                 mapa [fila - 3][columna]= 1
                                 fila=fila - 1
    if movimiento=="f":
            if mapa[fila + 1][columna]==1:
                  if mapa [fila + 2][columna]==1:
                       if  mapa [fila + 3][columna]==4:
                                 mapa [fila][columna]=4
                                 mapa [fila + 1][columna]=0
                                 mapa [fila + 2][columna]=1
                                 mapa [fila + 3][columna]= 1
                                 fila=fila + 1


    if movimiento== "d":
         if mapa [fila][columna + 1]==4:
              columna = columna + 1
              mapa [fila][columna]=0
              mapa [fila][columna - 1]=4 
         elif mapa[fila][columna + 1]==1:
              if mapa[fila][columna + 2]==4:
                        mapa[fila][columna]=4
                        mapa[fila][columna+ 1]=0
                        mapa[fila][columna + 2]= 1
                        columna= columna + 1
         
    if movimiento== "a":
         if mapa [fila][columna - 1]==4:
              columna = columna - 1
              mapa [fila][columna]=0
              mapa [fila][columna + 1]=4 
         elif mapa[fila][columna - 1]==1:
              if mapa[fila][columna - 2]==4:
                        mapa[fila][columna]=4
                        mapa[fila][columna- 1]=0
                        mapa[fila][columna - 2]= 1
                        columna= columna - 1
    if movimiento == "w":
        if mapa [fila - 1][columna]==4:
            fila= fila - 1
            mapa [fila][columna]=0
            mapa [fila + 1][columna]=4
        elif mapa[fila - 1][columna]==1:
              if mapa[fila- 2][columna]==4:
                        mapa[fila][columna]=4
                        mapa[fila - 1][columna]=0
                        mapa[fila - 2][columna]= 1
                        fila= fila -1

    if movimiento == "s":
         if mapa [fila + 1][columna]==4:
            fila= fila + 1
            mapa [fila][columna]=0
            mapa [fila - 1][columna]=4
         elif mapa[fila + 1][columna]==1:
              if mapa[fila + 2][columna]==4:
                        mapa[fila][columna]=4
                        mapa[fila + 1][columna]=0
                        mapa[fila + 2][columna]= 1
                        fila= fila + 1
        