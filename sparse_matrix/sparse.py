# importing the operating system module
import os


class SparseMatrix:
    """
    A class that represents sparse matrices

    Attributes
    ----------
    num_rows: int
        The number of rows sparse matrices take up in a matrix file
    num_cols: int
        The number of columns sparse matrices take up in a matrix file
    matrix: dict
        The dictionary storing the row and column of sparse matrix non zero value

    Methods
    -------
    load(file)
        Extracts the sparse matrices and stores them in a dictionary
    add(matrixA, matrixB)
        Adds the sparse matrices from two files
    subtract(matrixA, matrixB)
        Subtracts the sparse matrices from two files
    multiply(matrixA, matrixB)
        Multiplies the sparse matrices from two files
    save_to_file()
        Stores the results to a file
    """

    def __init__(self):
        """
        Initializes a SparseMatrix instance
        """
        self.matrix = {}
        self.num_rows = 0
        self.num_cols = 0

    def load_matrix(self, file):
        """
        Loads the matrix file into a dictionary

        Parameter
        ---------
        file:
            Path to the file containing the matrix
        """
        # open file in read mode
        with open(file, "r") as f:
            # put all lines into a list
            content = f.readlines()
        # extract number of rows and columns
        try:
            self.num_rows = int(content[0].strip().split("=")[1])
            self.num_cols = int(content[1].strip().split("=")[1])
        except (ValueError, IndexError):
            print("Input file has wrong format!int")
            return
        # formating extracted data
        for line in content[2:]:
            # removing trailing spaces
            line = line.replace("(", "").replace(")", "").strip()
            # getting row, column and non zero value
            parts = line[0:].split(",")
            # checking if parts has 3 values for row, column and value
            if len(parts) != 3:
                print("Input file has wrong format!")
                return
            # checking if value is a float
            if "." in parts[2]:
                raise ValueError("Invalid value")
            # storing the extracted data into the matrix dictionary
            try:
                row, col, value = int(parts[0]), int(parts[1]), int(parts[2])
                self.matrix[(row, col)] = value
            # returning when there is a value error
            except ValueError:
                print("Input file has wrong format!")
                return

    def add(self, matrixB):
        """
        Adds the current matrix with matrixB
        Parameter
        ---------
        matrixB
                another matrix dictionary to add to the current one
        """
        # Checking if dimensions match
        if self.num_rows != matrixB.num_rows or self.num_cols != matrixB.num_cols:
            # checking if the user wants to proceed or not
            ans = input(
                "Matrices' dimensions don't match. Do you wish to continue?(y/n): ").strip().lower()
            while ans not in ["y", "n"]:
                ans = input(
                    "Please choose a valid answer (y/n): ").strip().lower()
            if ans == "n":
                print("Operation cancelled!")
                return
        # instatiating an instance
        result = SparseMatrix()
        result.num_cols = max(self.num_cols, matrixB.num_cols)
        result.num_rows = max(self.num_rows, matrixB.num_rows)

        keys = set(self.matrix.keys()) | set(matrixB.matrix.keys())

        # adding the two matrices
        for key in keys:
            result.matrix[key] = self.matrix.get(
                key, 0) + matrixB.matrix.get(key, 0)
        return result

    def subtract(self, matrixB):
        """
        Subtracts the current matrix with matrixB
        Parameter
        ---------
        matrixB
               another matrix dictionary to add to the current one
        """
        # Checking if dimensions match
        if self.num_rows != matrixB.num_rows or self.num_cols != matrixB.num_cols:
            # checking if the user wants to proceed or not
            ans = input(
                "Matrices' dimensions don't match. Do you wish to continue?(y/n): ").strip().lower()
            while ans not in ["y", "n"]:
                ans = input(
                    "Please choose a valid answer (y/n): ").strip().lower()
            if ans == "n":
                print("Operation cancelled!")
                return
        # instatiating an instance
        result = SparseMatrix()
        # assigning number of columns and rows
        result.num_cols = max(self.num_cols, matrixB.num_cols)
        result.num_rows = max(self.num_rows, matrixB.num_rows)

        keys = set(self.matrix.keys()) | set(matrixB.matrix.keys())

        # subtracting the two matrices
        for key in keys:
            result.matrix[key] = self.matrix.get(
                key, 0) - matrixB.matrix.get(key, 0)
        return result

    def multiply(self, matrixB):
        """
        Multiplies the current matrix with matrixB
        Parameter
        ---------
        matrixB
               another matrix dictionary to add to the current one
        """
        # Checking if dimensions match
        if self.num_cols != matrixB.num_rows:
            # checking if the user wants to proceed or not
            print("Multiplication is impossible with different dimensions!")
            print("Operation cancelled!")
            return
        # instatiating an instance
        result = SparseMatrix()
        # setting number of rows and columns
        result.num_cols = matrixB.num_cols
        result.num_rows = self.num_rows

        b_dict = {}
        # iterating over the current matrix
        for (rowb, colb), valueb in matrixB.matrix.items():
            if rowb not in b_dict:
                b_dict[rowb] = {}
            b_dict[rowb][colb] = valueb
        # iterating over self matrix and performs multiplication
        for (row_a, col_a), val_a in self.matrix.items():
            # check if column_a in b_dict
            if col_a in b_dict:
                for col_b, val_b in b_dict[col_a].items():
                    result.matrix[(row_a, col_b)] = result.matrix.get(
                        (row_a, col_b), 0) + val_a * val_b

        return result

    def save_to_file(self):
        """
        Saves the results to a variation of results0.txt
        """
        # checking if the file already exists
        i = 0
        while True:
            file = f"results{i}.txt"
            if not os.path.exists(file):
                break
            i += 1
        # adding the results to the file
        with open(file, "w") as f:
            f.write(f"rows={self.num_rows}\n")
            f.write(f"cols={self.num_cols}\n")
            for (row, col), value in sorted(self.matrix.items()):
                f.write(f"({row}, {col}, {value})\n")
        print(f"Results saved to {file}")


if __name__ == "__main__":
    print("-"*6, "Welcome to the sparse matrix operator", "-"*6, "\n")
    print("*"*2, "Input file names from the sample_inputs folder", "*"*2, "\n")
    mat1 = input("Choose first file: ")
    # build full path to the file
    path1 = os.path.abspath(os.path.join("sample_inputs", mat1))
    # check if file exists
    while True:
        if os.path.exists(path1):
            break
        else:
            mat1 = input("Please input a valid file name: ")
            path1 = os.path.abspath(os.path.join("sample_inputs", mat1))
    mat2 = input("Choose your second file: ")
    # build full path to the file
    path2 = os.path.abspath(os.path.join("sample_inputs", mat2))    
    # check if file exists
    while True:
        if os.path.exists(path2):
            break
        else:
            mat2 = input("Please input a valid file path: ")
            path2 = os.path.abspath(os.path.join("sample_inputs", mat2))
    print()
    operation = input(
        "choose an operation:\n * for multiplication\n - for subtraction\n + for addition\n\n > ").strip()
    # checks if the operation is among the provided options
    while operation not in ["*", "-", "+"]:
        operation = input(
            "Please choose:\n * for multiplication\n - for subtraction\n + for addition\n\n > ")
    print()

    print("loading...\n")
    # instatiate a and b
    a = SparseMatrix()
    b = SparseMatrix()
    # load mat1 and mat2
    a.load_matrix(path1)
    b.load_matrix(path2)
    # call method according to operation chosen
    if operation == "*":
        result = a.multiply(b)
    elif operation == "-":
        result = a.subtract(b)
    elif operation == "+":
        result = a.add(b)
    # store results to file if the results aren't empty
    if result:
        result.save_to_file()
    else:
        print("Can't create a file for empty results!")
