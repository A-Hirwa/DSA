# Sparse Matrix Operator

A command-line Python tool for performing **addition, subtraction, and multiplication** on sparse matrices stored in structured text files. Sparse matrices are efficiently stored as dictionaries, containing only their non-zero values.

---

## Matrix File Format

Each matrix is stored in a `.txt` file using this format:

```
rows=3
cols=3
(0, 1, 5)
(1, 2, -3)
(2, 2, 7)
```

### Format Explanation:

- The first line defines the number of rows: `rows=<int>`
- The second line defines the number of columns: `cols=<int>`
- Each following line contains one non-zero value in the format `(row, col, value)`
- Brackets **must be round `()`**, not square `[]` or curly `{}`.

---

## Features

- Load sparse matrices from properly formatted files.
- Add or subtract matrices with matching dimensions.
- Multiply matrices if dimensions are compatible.
- Automatically skips zero values in results to keep matrices sparse.
- Saves output to uniquely named result files like `results0.txt`, `results1.txt`, etc.

---

## How to Run the Program

### Prerequisites

- Python 3.x installed
- No external libraries are required
- Matrix files must be prepared and saved in the correct format

---

### Steps to Run

0. Clone the repository or download the source code **git clone https://github.com/A-Hirwa/DSA**
1. **Open a terminal or command prompt**.
2. **Navigate to the folder** where `sparse_matrix.py` is located:
   ```bash
   cd path/to/your/project
   ```

3. **Run the script** using Python:
   ```bash
   python sparse_matrix.py
   ```

4. **Follow the on-screen prompts**:
   - Choose **first file name/ path**: 
   - Choose **second file name/ path**: 
   - Choose an operation:
     - `+` for addition
     - `-` for subtraction
     - `*` for multiplication

5. **Check the terminal** for status messages.

6. If the operation succeeds, the result is saved in a file like:
   ```
   results0.txt
   ```

---

## Output File Format

The output file will be structured similarly to the input files, containing only the non-zero results:

```
rows=3
cols=3
(0, 1, 10)
(1, 2, -6)
```

---

## Notes

- **Addition and subtraction** require both matrices to have the same dimensions. If they don't, you'll be prompted to confirm whether to continue.
- **Multiplication** requires the number of columns in matrix A to equal the number of rows in matrix B.
- Invalid or malformed matrix files will result in an error and early termination.

---

## Example

### Input: `matrixA.txt`
```
rows=2
cols=3
(0, 1, 4)
(1, 0, 2)
```

### Input: `matrixB.txt`
```
rows=2
cols=3
(0, 1, 1)
(1, 0, -2)
```

### User chooses operation: `+`

### Output: `results0.txt`
```
rows=2
cols=3
(0, 1, 5)
```

---

## Author

Hirwa Ariane  
