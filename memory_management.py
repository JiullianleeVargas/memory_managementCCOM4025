import random
import os
import time

#  Clase 
class Memory:


    matrix = [[]]
    memoryVector = []
    
    # direccion base para el comienzo del vector
    baseAddress = int(0)

    
    # Inicializando la matriz con valores random
    def __init__(self):
        
        #  inicializando las filas y columnas para una matriz 10*10
        rows, cols = (10, 10)
        
        #  Inicializando matriz con valores random
        self.matrix = [[random.randint(0, 100) for i in range(cols)] for j in range(rows)]
        
        # Inizializando vector con valores 0
        self.memoryVector = [0] * (rows * cols)
        
        # Rellena el vector con los valores de la matriz en forma "row major order"
        self.rowMajorOrder()
        
    
    #  Buscar indice en el vector de la celda proveida desde la matriz
    def getIndexVector(self, r, c):
        
        rows, cols = (10, 10)
        index = self.baseAddress + (r * cols + c)
        return index
    
   
    def rowMajorOrder(self):
        #  Mathematical ecuation matrix -> vector
        # Address(a[i][j]) = B. A. + (i * n + j) * size   
        
        rows, cols = (10, 10)
        #  Para cada fila y para columna, agarra el valor de la matriz y guardalo en el vector con el indice
        # calculado mediante row major order
        for row in range(rows):
            for col in range(cols):
                matrixCellValue = self.matrix[row][col]
                indexInVector = self.getIndexVector(row,col)
                self.memoryVector[indexInVector] = matrixCellValue
       
       
    #  Asigna un valor en la matriz y luego actualizalo en el vector
    def setValue(self, r, c, val):
        self.matrix[r][c] = val
        self.rowMajorOrder()

    # Imprime la matriz
    def printMatrix(self):
        print("Matrix")
        self.rowMajorOrder()
        for row in self.matrix:
            print(" ".join(["%4d" % val for val in row]))
        print("\n")
         
    # Imprimir  vector
    def printVector(self):
        print("Vector - Memory representation of the Matrix")
        self.rowMajorOrder()
        for val in self.memoryVector:
            print("{:4d}".format(val),  end=" ")  # Using a fixed width of 4 characters
        print("\n")
      
        
        
    
    
#  MAIN

# Instancia de la clase de memoria
memory = Memory()
os.system('cls')


# menu principal
while True:
    
   
#    imprimir siempre el menu
    print("Kotlin Memory Management Simulation")
    print("Jiullian-Lee Vargas Ruiz\n")
    print  ("1. Initialize matrix with random numbers")
    print  ("2. Print the matrix and vector")
    print  ("3. Get 'memory address' of cell in matrix" )
    print  ("4. Set a value in the matrix")
    print("0. Exit")
    
    choice = input("Enter your choice: ")

    # Inicializa la matriz y actualiza el vector
    if choice == '1':
        os.system('cls')
        memory.__init__()
        memory.printMatrix()
        memory.printVector()
        
        
       
        
    # Imprimir vector y matriz
    elif choice == '2':
        os.system('cls')
        memory.printMatrix()
        memory.printVector()
        
    
    # Dada una fila y una columna de la matriz, devuelve el indice en el vector de esa celda
    # Debe ser un entero, si no, da un error
    elif choice == '3':
        rows, cols = (10, 10)
        r_input = input("Enter the row: ")
        c_input = input("Enter the column: ")

        #  asegurando que el input no tenga espacios y es un digito
        if r_input.strip().isdigit() and c_input.strip().isdigit():
            
            #  si es digito, convierte a numero
            r = int(r_input)
            c = int(c_input)
            
            #  verificando si esta dentro del rango 
            if 0 <= r < rows and 0 <= c < cols:
                os.system('cls')
                memory.printMatrix()
                memory.printVector()
                print(f'The element in row {r} and column {c}, with a value of {memory.matrix[r][c]} of the matrix is in the address {memory.getIndexVector(r,c)} of the vector\n')
            else:
                os.system('cls')
                print("Invalid input. Row or column out of range.\n")
                memory.printMatrix()
                memory.printVector()
        else:
            os.system('cls')
            print("Invalid input. Row and column should be integers.\n")
            memory.printMatrix()
            memory.printVector()
    
  
  #  Cambiar un valor de la matriz
    elif choice == '4':
        rows, cols = (10, 10)
        r_input = input("Enter the row: ")
        c_input = input("Enter the column: ")
        v_input = input("Enter the new value: ")

         #  asegurando que el input no tenga espacios y es un digito
        if r_input.strip().isdigit() and c_input.strip().isdigit() and v_input.strip().isdigit():
            r = int(r_input)
            c = int(c_input)
            val = int(v_input)

            # Verificar si esta en rango
            if 0 <= r < rows and 0 <= c < cols:
                memory.setValue(r, c, val)
                os.system('cls')
                memory.printMatrix()
                memory.printVector()
            else:
                os.system('cls')
                print("Invalid input. Row or column out of range.\n")
                memory.printMatrix()
                memory.printVector()
        else:
            os.system('cls')
            print("Invalid input. Row, column, or value should be integers.\n")
            memory.printMatrix()
            memory.printVector()

        
    elif choice == '0':
        print("You have exited the program\n")
        break
    
    #  Cualquier otro input va dar un error
    else:
        os.system('cls')
        print("Please enter one of the menu options\n")
       
        
    
 