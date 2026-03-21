
# grid_tasks.py

def generate_chess_grid(n):
    """
    TaskPY200_T5: Chessboard with Numbers
    Rules: 
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


