def generate_chess_grid(n):
    """
    - If row == col -> 'X'
    - Else if (row + col) is even -> '1'
    - Else -> '0'
    """
    grid = []
    for r in range(n):
        row_data = []
        for c in range(n):
            if r == c:
                row_data.append("X")
            elif (r + c) % 2 == 0:
                row_data.append("1")
            else:
                row_data.append("0")
        grid.append(" ".join(row_data))
    return "\n".join(grid)

val = input("Enter N for the grid size: ")
n = int(val)

if n < 0:
   print("Enter a positive integer!")
result = generate_chess_grid(n)
print(result)
