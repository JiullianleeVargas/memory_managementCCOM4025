import random
import os

# Class Memory - functionalities of the kotlin memory management simulation
class Memory:


    matrix = [[]]
    memoryVector = []
    
    # base address for vector (simulation)
    baseAddress = int(0)

    
    # Initializing the matrix with random values
    def __init__(self):
        print( "Initializing")
        #  initializing rows and columns for a 10x10 matrix
        rows, cols = (10, 10)
        
        #  Initializing the matrix with random integers
        self.matrix = [[random.randint(0, 100) for i in range(cols)] for j in range(rows)]
        
        # Initializing the vector (memory) with 0s
        self.memoryVector = [0] * (rows * cols)
        
        # Filling the vector in row major order with the values of the matrix
        self.rowMajorOrder()
        
    
    #  Get the index in the vector  of the provided cell from the matrix
    def getIndexVector(self, r, c):
        
        rows, cols = (10, 10)
        index = self.baseAddress + (r * cols + c)
        return index
    
   
    def rowMajorOrder(self):
        #  Mathematical ecuation matrix -> vector
        # Address(a[i][j]) = B. A. + (i * n + j) * size   
        
        rows, cols = (10, 10)
        #  For each row and each column, grab the value in the matrix and store it in the vector with its 
        # calculated index based on row major order
        for row in range(rows):
            for col in range(cols):
                matrixCellValue = self.matrix[row][col]
                indexInVector = self.getIndexVector(row,col)
                self.memoryVector[indexInVector] = matrixCellValue
       
       
    #  Set a value in the matrix and then update the vector
    def setValue(self, r, c, val):
        self.matrix[r][c] = val
        self.rowMajorOrder()

    # Print matrix
    def printMatrix(self):
        print("Matrix")
        self.rowMajorOrder()
        for row in self.matrix:
            print(" ".join(["%4d" % val for val in row]))
        print("\n")
         
    # Print vector   
    def printVector(self):
        print("Vector - Memory representation of the Matrix")
        self.rowMajorOrder()
        for val in self.memoryVector:
            print("{:4d}".format(val),  end=" ")  # Using a fixed width of 4 characters
        print("\n")
      
        
        
    
    
#  MAIN

# Instance of the class
memory = Memory()

# Clear the screen 
os.system('cls')


# Main menu loop
while True:
    
   
#    Always printing the menu
    print  ("1. Initialize matrix with random numbers")
    print  ("2. Print the matrix and vector")
    print  ("3. Get 'memory address' of cell in matrix" )
    print  ("4. Set a value in the matrix")
    print("0. Exit")
    
    choice = input("Enter your choice: ")
  

    # Initialize the matrix by adding random ints and updating the vector
    if choice == '1':
        print("Initialized the matrix\n")
        memory.__init__()
        os.system('cls')
        memory.printMatrix()
        memory.printVector()
        
    # Just printing the matrix and vector
    elif choice == '2':
        os.system('cls')
        memory.printMatrix()
        memory.printVector()
        
    # Given a row and column from the matrix, return the index in the vector of that cell
    # Row and column must be integers and within range, if not return an error
    elif choice == '3':
        rows, cols = (10, 10)
        r_input = input("Enter the row: ")
        c_input = input("Enter the column: ")

        #  Stripping the input of spaces and making sure is a digit
        if r_input.strip().isdigit() and c_input.strip().isdigit():
            
            #  if digit then convert to int
            r = int(r_input)
            c = int(c_input)
            
            #  Verifying if its within range of columns and rows
            if 0 <= r < rows and 0 <= c < cols:
                os.system('cls')
                memory.printMatrix()
                memory.printVector()
                print(f'The element in row {r} and column {c}, with a value of {memory.matrix[r][c]} of the matrix is in the address {memory.getIndexVector(r,c)} of the vector\n')
            else:
                os.system('cls')
                print("Invalid input. Row or column out of range.\n")
        else:
            os.system('cls')
            print("Invalid input. Row and column should be integers.\n")
    
    # Given a row, column and value, replace that value in the matrix, update vector and print them
    # Row, column and value must be integers and within range, if not return an error
   # Given a row, column and value, replace that value in the matrix, update vector and print them
# Row, column and value must be integers and within range, if not return an error
    elif choice == '4':
        rows, cols = (10, 10)
        r_input = input("Enter the row: ")
        c_input = input("Enter the column: ")
        v_input = input("Enter the new value: ")

        # Stripping the input of spaces and making sure it's a digit
        if r_input.strip().isdigit() and c_input.strip().isdigit() and v_input.strip().isdigit():
            r = int(r_input)
            c = int(c_input)
            val = int(v_input)

            # Verifying if it's within the range of columns and rows
            if 0 <= r < rows and 0 <= c < cols:
                memory.setValue(r, c, val)
                os.system('cls')
                memory.printMatrix()
                memory.printVector()
            else:
                os.system('cls')
                print("Invalid input. Row or column out of range.\n")
        else:
            os.system('cls')
            print("Invalid input. Row, column, or value should be integers.\n")

        
    
        
    elif choice == '0':
        print("You have exited the program\n")
        break
    
    #  Any other input will cause and error and the clear the screen
    else:
        os.system('cls')
        print("Please enter one of the menu options\n")
        
    
 