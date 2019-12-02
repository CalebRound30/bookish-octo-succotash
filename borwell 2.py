answers1 = []#4 blank lists to store answers
answers2 = []
answers3 = []
answers4 = []
def valid_walls():#validator to check wall dimensions
    while True:
        try:
            width = float(input('Please enter the width of the wall in cm: \n'))
        except ValueError:
            print('Please enter a number')
            continue#restarts the loop 
        else:
            break#ends the loop

    while True:
        try:
            height = float(input('Please enter the height of the wall in cm: \n'))
        except ValueError:
            print('Please enter a number')
            continue
        else:
            break

    wall_area = width * height
    answers1.append(wall_area)#appends the answers to blank lists
            
def valid_windows():
    while True:
        try:
            width = float(input('Please enter the width of the window in cm: \n'))
        except ValueError:
            print('Please enter a number')
            continue
        else:
            break

    while True:
        try:
            height = float(input('Please enter the height of the window in cm: \n'))
        except ValueError:
            print('Please enter a number')
            continue
        else:
            break

    window_area = width * height
    answers2.append(window_area)

def valid_recess():
    while True:
        try:
            width = float(input('Please enter the width of the recess in cm: \n'))
        except ValueError:
            print('Please enter a number')
            continue
        else:
            break

    while True:
        try:
            length = float(input('Please enter the length of the recess in cm: \n'))
        except ValueError:
            print('Please enter a number')
            continue
        else:
            break

    recess_area = width * length
    answers3.append(recess_area)
    
    
    

def area_of_the_walls():
    while True:
        try:
            walls = int(input('How many walls are there'))# User input to determine how many times to repeat
        except ValueError:
            print('Please enter a whole number')
            continue
        else:
            break

    for i in range (walls):#repeates function for validating the amount of times depending on how many walls there are
        valid_walls()

    while True:
        try:
            windows = int(input('How many windows are there'))
        except ValueError:
            print('Please enter a whole number')
            continue
        else:
            break


    for i in range (windows):
        valid_windows()

    wall_sum = sum(answers1)

    window_sum = sum(answers2)

    total_area = wall_sum - window_sum#sums up both lists and subtracts them from each other to find the total

    if total_area < 0:
        print('The area of the windows exceeded the area of the walls')
        while True:
            try:
                restart = int(input('[1] Restart this service,\n[2]Or restart the whole program,\nType the number corresponding to you choice...'))#restart sub program
            except ValueError:
                print('Please enter a number')
                continue
            else:
                if restart == 1:
                    area_of_the_walls()
                else:
                    main()

    while True:
        try:
            paint = float(input('With the paint you are using how many cm2 does one tin cover'))
        except ValueError:
            print('Please enter a number')
            continue
        else:
            break
        
    paint_coverage = total_area / paint# divides the area of the walls by the paint coverage

    int_paint = int(paint_coverage)
    str_paint = str(int_paint)

    print('The number of tins of paint to cover the walls is '+str_paint)#concatonates str and variable

    while True:
            try:
                restart = int(input('[1] Restart this service,\n[2]Or restart the whole program,\nType the number corresponding to you choice...'))
            except ValueError:
                print('Please enter a number')
                continue
            else:
                if restart == 1:
                    area_of_the_walls()
                else:
                    main()

def room_volume():
    while True:
        try:
            recess = int(input('How many recesses does the room have'))
        except ValueError:
            print('Please enter a number')
            continue
        else:
            break

    for i in range(recess):
        valid_recess()

    while True:
        try:
            main_width = float(input('Please enter the width of the room excluding the recess(es) in cm'))
        except ValueError:
            print('Please enter a number')
            continue
        else:
            break

    while True:
        try:
            main_length = float(input('Please enter the length of the room excluding the recess(es) in cm'))
        except ValueError:
            print('Please enter a number')
            continue
        else:
            break

    while True:
        try:
            room_height = float(input('Please enter the height of the room in cm'))
        except ValueError:
            print('Please enter a number')
            continue
        else:
            break

    main_area = main_width * main_length
    answers4.append (main_area)

    recess_sum = sum(answers3)
    main_sum = sum(answers4)

    total_floor_area = recess_sum + main_sum

    volume_of_the_room = total_floor_area * room_height

    str_volume = str(volume_of_the_room)

    print('The total volume of the room is '+str_volume+'cm3')

    while True:
            try:
                restart = int(input('[1] Restart this service,\n[2]Or restart the whole program,\nType the number corresponding to you choice...'))
            except ValueError:
                print('Please enter a number')
                continue
            else:
                if restart == 1:
                    room_volume()
                else:
                    main()
        

def floor_area():
    while True:
        try:
            recess = int(input('How many recesses does the room have'))
        except ValueError:
            print('Please enter a whole number')
            continue
        else:
            break

    for i in range(recess):
        valid_recess()

    while True:
        try:
            main_width = float(input('Please enter the width of the room excluding the recess(es) in cm'))
        except ValueError:
            print('Please enter a number')
            continue
        else:
            break

    while True:
        try:
            main_length = float(input('Please enter the length of the room excluding the recess(es) in cm'))
        except ValueError:
            print('Please enter a number')
            continue
        else:
            break

    main_area = main_width * main_length
    answers4.append (main_area)

    recess_sum = sum(answers3)
    main_sum = sum(answers4)

    total_floor_area = recess_sum + main_sum

    str_area = str(total_floor_area)

    print('The total area of the floor is '+str_area+'cm2')

    while True:
            try:
                restart = int(input('[1] Restart this service,\n[2]Or restart the whole program,\nType the number corresponding to you choice...'))
            except ValueError:
                print('Please enter a number')
                continue
            else:
                if restart == 1:
                    room_volume()
                else:
                    main()

def main():#main program to find out which service the user wants
    service = input('[1] How much paint is needed to cover the walls,\n[2] Volume of the room,\n[3] Area of the floor\nType the number corresponding to the service you require...')
    if service == '1':
        area_of_the_walls()
    elif service == '2':
        room_volume()
    elif service == '3':
        floor_area()
    else:
        main()
main()
