import sys

def run_matplotlib_test():
    print("Running matplotlib test...")



def run_turtlesim_test():
    print("Running turtlesim test...")



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py [matplotlib|turtlesim]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "matplotlib":
        run_matplotlib_test()
    elif command == "turtlesim":
        run_turtlesim_test()
    else:
        print(f"Unknown command: {command}")
        print("Available commands: matplotlib, turtlesim")
        sys.exit(1)