def get_size(shape):
    flag = True
    while flag is True:
        flag = False
        try:
            height = int(input(f"Enter the height of the {shape}: "))
            while height < 2:
                height = int(input('''Wrong size! the height of a tower must be at least 2!
try again: '''))
            width = int(input(f"Enter the width of the {shape}: "))
        except ValueError:
            print("Invalid value")
            flag = True
    return height, width


def rectangular():
    (height, width) = get_size("rectangular")
    if height == width or height - width > 5:
        area = height * width
        print(f"The area of the rectangular is: {area}")
        print('\n')
    else:
        rperimeter = (height * 2) + (width * 2)
        print(f"The perimeter of the rectangular is: {rperimeter}")
        print('\n')


def tperimeter(height, width):
    perimeter = width + (2 * (height - 2)) + 1
    print(f"The perimeter of the triangle is: {perimeter}")


def print_asterisk(space, width):
    for i in range(space):
        print(' ', end='')

    for i in range(width):
        print('*', end='')
    print("\n")


def print_triangle(height, width):
    if width % 2 == 0 or width >= height * 2:
        print('''Sorry there is no option to display this triangle because of one of the options:
* if the width is even or 
* if it is greater than twice the height''')
    else:

       rows_num = width // 2 - 1
       rows_mul = (height - 2) // rows_num
       rest_rows_mul = (height - 2) % rows_num
       space = (width - 1) // 2
       width = 1

       print_asterisk(space, width)
       space -= 1
       width += 2

       for i in range(rest_rows_mul):
           print_asterisk(space, width)

       height -= (rest_rows_mul + 2)

       while height > 0:
           for i in range(rows_mul):
               print_asterisk(space, width)
           space -= 1
           width += 2
           height -= rows_mul

       print_asterisk(space, width)


triangle_options = {'1': tperimeter, '2': print_triangle}


def triangle_switch(option, *params):
    return triangle_options.get(option, lambda *_: "Invalid option")(*params)


def triangle():
    (height, width) = get_size("triangle")
    option = input('''Enter the number of the option you would like:

option 1: The triangle perimeter
option 2: display the triangle to the screen

Your answer: ''')

    triangle_switch(option, height, width)


main_options = {'1': rectangular, '2': triangle, '3': lambda: print("Bye Bye :)")}


def main_switch(option):
    return main_options.get(option, lambda: print("Invalid option try again"))()


def main():

    while option != '3':
        option = input('''Enter which kind of tower you would like (enter the number of the option):

option 1: Rectangular tower
option 2: Triangle tower
option 3: Exit the program

Your answer: ''')
        main_switch(option)


if __name__ == '__main__':
    main()






