class Matrix:
    def __init__(self, rows, columns):
        self.newMatrix = []
        for row in range(rows):
            rowOfMatrix = []
            for column in range(columns):
                item = int(input(f"Enter the Matrix [{row+1}] (row) [{column+1}] (column) => "))
                rowOfMatrix.append(item)
            self.newMatrix.append(rowOfMatrix)
        
    def __add__(self, B):
        self.outputMatrix = []
        for i in range(len(self.newMatrix)): #! Number of rows
            row = []
            for j in range(len(self.newMatrix[0])): #! Number of columns
                row.append(self.newMatrix[i][j] + B.newMatrix[i][j])
            self.outputMatrix.append(row)
        return self.outputMatrix
    
    def __str__(self):
        return str(self.newMatrix)
    
    
if __name__ == "__main__":
    m = int(input("Enter the number of rows : "))
    n = int(input("Enter the number of columns : "))
    A = Matrix(m, n)
    print(A)
    B = Matrix(m, n)
    print(B)
    print(f"The Sum Result :\n{A+B}")