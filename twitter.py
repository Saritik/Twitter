# This function gets the height and width of a shape from the user
# It ensures the values are valid integers and handles exceptions
def get_size(shape):
    # Initialize flag to True to enter the loop
    flag = True
    while flag is True:
        # Reset flag to False at the beginning of each loop iteration
        flag = False
        try:
            # Get the height of the shape from the user
            height = int(input(f"Enter the height of the {shape}: "))
            # Validate the height input, must be at least 2
            while height < 2:
                height = int(input('''Wrong size! the height of a tower must be at least 2!
try again: '''))
            # Get the width of the shape from the user
            width = int(input(f"Enter the width of the {shape}: "))
        except ValueError:
            # Handle the case where a non-integer value is entered
            print("Invalid value")
            # Set flag to True to repeat the loop
            flag = True
    return height, width


# This function calculates and prints the area or perimeter of a rectangular shape
def rectangular():
    # Get the height and width of the rectangular shape from the user
    (height, width) = get_size("rectangular")
    # Check if the shape is closer to a square or a rectangle
    if height == width or height - width > 5:
        # Calculate and print the area of the rectangular if it's closer to a square
        area = height * width
        print(f"The area of the rectangular is: {area}")
        print('\n')
    else:
        # Calculate and print the perimeter of the rectangular if it's closer to a rectangle
        rperimeter = (height * 2) + (width * 2)
        print(f"The perimeter of the rectangular is: {rperimeter}")
        print('\n')


# This function calculates and prints the perimeter of a triangle
def tperimeter(height, width):
    perimeter = width + (2 * (height - 2)) + 1
    print(f"The perimeter of the triangle is: {perimeter}")


# This function prints a row of asterisks with a specified number of spaces
def print_asterisk(space, width):
    # Print leading spaces before the asterisks
    for i in range(space):
        print(' ', end='')

    # Print the asterisks for the specified width
    for i in range(width):
        print('*', end='')

    # Move to the next line after printing the asterisks
    print("\n")


# This function prints a triangle pattern with the specified height and width
def print_triangle(height, width):
    # Check if the width is even or greater than or equal to twice the height
    if width % 2 == 0 or width >= height * 2:
        print('''Sorry there is no option to display this triangle because of one of the options:
* if the width is even or 
* if it is greater than twice the height''')
    else:
        # Calculate the number of * in each row of the triangle
        rows_num = width // 2 - 1
        # Calculate how many times each row should be repeated
        rows_mul = (height - 2) // rows_num
        # Calculate the number of * int the rest rows
        rest_rows_mul = (height - 2) % rows_num
        # Calculate the initial number of spaces before the first asterisk in the first row
        space = (width - 1) // 2
        width = 1

        # Print the first row of the triangle
        print_asterisk(space, width)
        space -= 1
        width += 2

        # Print the rest rows in the triangle
        for i in range(rest_rows_mul):
            print_asterisk(space, width)

        # Adjust the height to account for the rows already printed
        height -= (rest_rows_mul + 2)

        # Print the remaining rows
        while height > 0:
            for i in range(rows_mul):
                print_asterisk(space, width)
            space -= 1
            width += 2
            height -= rows_mul

        # Print the last row of the triangle
        print_asterisk(space, width)


# Dictionary mapping options to functions for the triangle
triangle_options = {'1': tperimeter, '2': print_triangle}


# This function selects the correct function based on the option provided
def triangle_switch(option, *params):
    return triangle_options.get(option, lambda *_: "Invalid option")(*params)


# This function handles the triangle menu and processing
def triangle():
    (height, width) = get_size("triangle")
    option = input('''Enter the number of the option you would like:

option 1: The triangle perimeter
option 2: display the triangle to the screen

Your answer: ''')

    triangle_switch(option, height, width)


# Dictionary mapping options to functions for the main menu
main_options = {'1': rectangular, '2': triangle, '3': lambda: print("Bye Bye :)")}


# This function selects the correct function based on the option provided
def main_switch(option):
    return main_options.get(option, lambda: print("Invalid option try again"))()


# This is the main function of the program
# It displays the main menu and handles user input
def main():
    while option != '3':
        option = input('''Enter which kind of tower you would like (enter the number of the option):

option 1: Rectangular tower
option 2: Triangle tower
option 3: Exit the program

Your answer: ''')
        main_switch(option)


# The program entry point
if __name__ == '__main__':
    main()
