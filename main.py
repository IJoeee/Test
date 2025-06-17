## main.py
from Functions.module1.module1 import print_from_module1
from Functions.module2.module2 import print_from_module2

def main():
    print_from_module1()
    print_from_module2()

if __name__ == "__main__":
    main()
