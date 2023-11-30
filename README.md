# Kotlin Memory Management Simulation

## Description
This program simulates the behavior of a computer's memory to store a matrix in Kotlin. The matrix is stored in memory using Row Major Order (RMO), meaning that the elements of the first row are stored contiguously in memory, followed by the elements of the second row, and so on.

The program features a class named `Memory` that represents the computer's memory. This class has two main attributes:
- `matrix`: a two-dimensional array representing the matrix stored in memory.
- `memoryVector`: a one-dimensional array representing the computer's memory.

The `Memory` class also includes various methods that allow the user to initialize the matrix, print both the matrix and the vector, obtain the memory address of a cell in the matrix, and set a value in the matrix.

## Usage
The main program creates an instance of the `Memory` class and enters into an infinite loop. In each iteration of the loop, the program prints a menu with the following options:
1. Initialize the matrix with random numbers.
2. Print the matrix and the vector.
3. Get the memory address of a cell in the matrix.
4. Set a value in the matrix.
0. Exit the program.

The user selects an option from the menu, and the program performs the corresponding action. If the user chooses option 1, the program initializes the matrix with random numbers. If the user selects option 2, the program prints the matrix and the vector. If the user chooses option 3, the program prompts the user for the row and column of a cell in the matrix and then prints the memory address of that cell. If the user selects option 4, the program prompts the user for the row, column, and the value to be set in the matrix, and then it sets the corresponding value in the matrix. If the user chooses option 5, the program exits the infinite loop and terminates.

### Note: For this program to look good, it needs to be executed in an external terminal (shell, bash, cmd, etc)
