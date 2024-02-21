
import argparse

# I put default values up here in all caps
PROGRAM_NAME = "argparse-example"
__version__ = 1.0

parser = argparse.ArgumentParser(description="This is an example program to showcase argparse and serve as a future guide")
parser.add_argument("-v", "--version", action="store_true", default=False, help="Returns the version of the program and exit")
parser.add_argument("-q", action="version")
parser.add_argument("-f", "--frame", type=int, metavar='', help="The frame number to be proccessed")
parser.add_argument("-m", "--mode", type=str, metavar='', help="Changes the value calculations for each section exw:Extremity Width, ks:Kuiper")


def main():
    print("Up here in main")

if __name__ == "__main__":


    args = parser.parse_args()


    #if args.version:
    #    print(f"version = {VERSION}")
    #    exit(0)
    main()