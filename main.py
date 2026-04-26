import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <input_file> <Verbose||Brief||None> <parameter>")
        sys.exit(1)

    filename = sys.argv[1]
    output_mode = sys.argv[2]
    parameter = int(sys.argv[3])

    if output_mode not in ["Verbose", "Brief", "None"]:
        print("Error: Output mode must be Verbose, Brief, or None")
        sys.exit(1)

