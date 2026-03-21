from grid_tasks import generate_chess_grid

def main():
    val = input("Enter N for the grid size: ")
    n = int(val)

    if n < 0:
         print("Enter a positive integer!")
         return
    result = generate_chess_grid(n)
    print(result)

if __name__ == "__main__":
    main()
