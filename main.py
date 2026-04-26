import sys    
        
def main():
    # Argc
    if len(sys.argv) != 4:
        print("Usage: python main.py <input_file> <Verbose||Brief||None> <parameter>")
        sys.exit(1)

    # assign inputs
    filename = sys.argv[1]
    output_mode = sys.argv[2]
    parameter = int(sys.argv[3])

    if output_mode not in ["Verbose", "Brief", "None"]:
        print("Error: Output mode must be Verbose, Brief, or None")
        sys.exit(1)

    # read file
    with open(filename, "r") as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]

    algorithm = lines[0]
    player = lines[1]
    board = [list(row) for row in lines[2:8]]

    if algorithm == "UR":
    # TODO implement uniform_random alg. params may change
        move = uniform_random(board, player)

        if output_mode != "None":
            print(f"FINAL Move selected: {move}")
    
    # TODO add elifs and call other algs

if __name__ == "__main__":
    main()
