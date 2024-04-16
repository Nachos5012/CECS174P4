def main_menu():
        """ printing the main menu"""
        print("Welcome to Pattern Print Shop. Please select from the following menu:")
        print("A- To print a rectangle")
        print("B- To print Pyramid pattern")
        print("C- To print Diamond Pattern")
        print("Q- To quit")
        print("Please enter a valid symbol.")
        
def rectangle_menu():
        print("Please select the type of rectangle:")
        print("1- Hollow Rectangle")
        print("2- Solid Rectangle")
        print("0- Return to main menu")
        
def hollow_rectangle(symbol, height, width):
    for i in range(height):
        for j in range(width):
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                print(symbol, end="")
            else:
                print(" ", end="")
        print()

def solid_rectangle(symbol, height, width):
    for i in range(height):
        for j in range(width):
            print(symbol, end="")
        print()
        
def pyramid_menu():
    print("Please select the type of pyramid:")
    print("1- Half Pyramid")
    print("2- Full Pyramid")
    print("0- Return to main menu")

def half_pyramid(symbol, height):
    for i in range(1, height + 1):
        print(symbol * i)

def full_pyramid(symbol, height):
    for i in range(1, height + 1):
        print(" " * (height - i) + symbol * (2 * i - 1))

def solid_half_pyramid(symbol, height):
    for i in range(1, height + 1):
        print(symbol * i)

def hollow_half_pyramid(symbol, height):
    for i in range(1, height + 1):
        if i == 1 or i == height:
            print(symbol * i)
        else:
            print(symbol + " " * (i - 2) + symbol)

def solid_inverted_half_pyramid(symbol, height):
    for i in range(height, 0, -1):
        print(symbol * i)

def hollow_inverted_half_pyramid(symbol, height):
    for i in range(height, 0, -1):
        if i == height or i == 1:
            print(symbol * i)
        else:
            print(symbol + " " * (i - 2) + symbol)

def solid_full_pyramid(symbol, height):
    for i in range(1, height + 1):
        print(" " * (height - i) + symbol * (2 * i - 1))

def hollow_full_pyramid(symbol, height):
    for i in range(1, height + 1):
        if i == 1 or i == height:
            print(" " * (height - i) + symbol * (2 * i - 1))
        else:
            print(" " * (height - i) + symbol + " " * (2 * (i - 1)) + symbol)

def solid_inverted_full_pyramid(symbol, height):
    for i in range(height, 0, -1):
        print(" " * (height - i) + symbol * (2 * i - 1))

def hollow_inverted_full_pyramid(symbol, height):
    for i in range(height, 0, -1):
        if i == height or i == 1:
            print(" " * (height - i) + symbol * (2 * i - 1))
        else:
            print(" " * (height - i) + symbol + " " * (2 * (i - 1)) + symbol)

def pyramid_type_menu():
    print("Please select the type of half pyramid:")
    print("1- Half Pyramid")
    print("2- Inverted Half Pyramid")
    print("3- Hollow Half Pyramid")
    print("4- Hollow Inverted Half Pyramid")
    print("0- Return to main menu")
    
def pyramid_type_menu2():
    print("Please select the type of half pyramid:")
    print("1- full Pyramid")
    print("2- Inverted full Pyramid")
    print("3- Hollow full Pyramid")
    print("4- Hollow Inverted full Pyramid")

    print("0- Return to main menu")
    
def diamond_menu():
    print("Please select the type of diamond pattern:")
    print("1- Solid Diamond")
    print("2- Hollow Diamond")
    print("0- Return to main menu")

def solid_full_diamond(symbol, size):
    for i in range(1, size + 1):
        print(" " * (size - i) + symbol * (2 * i - 1))
    for i in range(size - 1, 0, -1):
        print(" " * (size - i) + symbol * (2 * i - 1))

def hollow_full_diamond(symbol, size):
    for i in range(1, size + 1):
        if i == 1 or i == size:
            print(" " * (size - i) + symbol * (2 * i - 1))
        else:
            print(" " * (size - i) + symbol + " " * (2 * (i - 1)) + symbol)

def solid_half_diamond(symbol, size):
    for i in range(1, size + 1):
        print(" " * (size - i) + symbol * i)

def hollow_half_diamond(symbol, size):
    for i in range(1, size + 1):
        if i == 1 or i == size:
            print(" " * (size - i) + symbol * i)
        else:
            print(" " * (size - i) + symbol + " " * (i - 2) + symbol)

def main():
    while True:
        main_menu()
        choice = input("Your choice: ").upper()
        if choice == "A":
            rectangle_menu()
            rect_choice = input("Your choice: ")
            if rect_choice == "1":
                height = int(input("Enter the height of the rectangle: "))
                width = int(input("Enter the width of the rectangle: "))
                symbol = input("Enter the symbol to use (!, @, #, $, %, ^, &, *): ")
                hollow_rectangle(symbol, height, width)
            elif rect_choice == "2":
                height = int(input("Enter the height of the rectangle: "))
                width = int(input("Enter the width of the rectangle: "))
                symbol = input("Enter the symbol to use (!, @, #, $, %, ^, &, *): ")
                solid_rectangle(symbol, height, width)
            elif rect_choice == "0":
                continue
            else:
                print("Invalid choice")
        elif choice == "B":
            pyramid_menu()
            pyramid_choice = input("Your choice: ")
            if pyramid_choice == "1":
                pyramid_type_menu()
                pyramid_type_choice = input("Your choice: ")
                if pyramid_type_choice == "1":
                    height = int(input("Enter the height of the pyramid: "))
                    symbol = input("Enter the symbol to use (!, @, #, $, %, ^, &, *): ")
                    solid_half_diamond(symbol, height)
                elif pyramid_type_choice == "2":
                    height = int(input("Enter the height of the pyramid: "))
                    symbol = input("Enter the symbol to use (!, @, #, $, %, ^, &, *): ")
                    solid_inverted_half_pyramid(symbol, height)
                elif pyramid_type_choice == "3":
                    height = int(input("Enter the height of the pyramid: "))
                    symbol = input("Enter the symbol to use (!, @, #, $, %, ^, &, *): ")
                    hollow_half_pyramid(symbol, height)
                elif pyramid_type_choice == "4":
                    height = int(input("Enter the height of the pyramid: "))
                    symbol = input("Enter the symbol to use (!, @, #, $, %, ^, &, *): ")
                    hollow_inverted_half_pyramid(symbol, height)
                elif pyramid_type_choice == "0":
                    continue
                else:
                    print("Invalid choice")
            elif pyramid_choice == "2":
                pyramid_type_menu2()
                pyramid_type_choice = input("Your choice: ")
                if pyramid_type_choice == "1":
                    height = int(input("Enter the height of the pyramid: "))
                    symbol = input("Enter the symbol to use (!, @, #, $, %, ^, &, *): ")
                    solid_full_pyramid(symbol, height)
                elif pyramid_type_choice == "2":
                    height = int(input("Enter the height of the pyramid: "))
                    symbol = input("Enter the symbol to use (!, @, #, $, %, ^, &, *): ")
                    solid_inverted_full_pyramid(symbol, height)
                elif pyramid_type_choice == "3":
                    height = int(input("Enter the height of the pyramid: "))
                    symbol = input("Enter the symbol to use (!, @, #, $, %, ^, &, *): ")
                    hollow_full_pyramid(symbol, height)
                elif pyramid_type_choice == "4":
                    height = int(input("Enter the height of the pyramid: "))
                    symbol = input("Enter the symbol to use (!, @, #, $, %, ^, &, *): ")
                    hollow_inverted_full_pyramid(symbol, height)
                elif pyramid_type_choice == "0":
                    continue
                else:
                    print("Invalid choice")
            elif pyramid_choice == "0":
                continue
            else:
                print("Invalid choice")
        elif choice == "C":
            diamond_menu()
            diamond_choice = input("Your choice: ")
            if diamond_choice == "1":
                size = int(input("Enter the size of the diamond: "))
                symbol = input("Enter the symbol to use (!, @, #, $, %, ^, &, *): ")
                solid_full_diamond(symbol, size)
            elif diamond_choice == "2":
                size = int(input("Enter the size of the diamond: "))
                symbol = input("Enter the symbol to use (!, @, #, $, %, ^, &, *): ")
                hollow_full_diamond(symbol, size)
            elif diamond_choice == "0":
                continue
            else:
                print("Invalid choice")
        elif choice == "Q":
            print("Thank you for your Business")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

