table = [
    ["Employee ID", "Name", "Age", "Job"],
    ["101", "Jessica", "26", "Perfume expert"],
    ["102", "Milan", "30", "Tree dealer"],
    ["103", "Radim", "21", "Charlatan"]
]
options = """
What do we want to do? Enter the number
    1-Create table | 2-Insert new row | 3-Insert new column |
    4-Update a cell | 5-Column Total | 6-Row Total |
    7-Print Table | 8-Export do List of Dicts | 9-Quit program
"""

delimiter = "=" * 60
is_on = True
while is_on:
    print(delimiter)
    print(options)
    prompt = int(input("Option: "))
    print(delimiter)

    if prompt < 1 or prompt > 9:
        input("Option out of range, press ENTER to continue.")

    elif prompt == 1:
        table = []
        new_table = input(
            "Enter header names separated by a comma for example: Name,Age,Email ")
        table.append(new_table.split(","))
        print(f"Here is your new table: {table}")

    elif prompt == 2:
        which_row = int(input("Row number: "))
        new_row = input(
            "Enter data separated by a comma for example: Name,Age,Email ").split(",")

        if 0 < which_row < len(table):
            table.insert(which_row, new_row)
        else:
            table.append(new_row)

    elif prompt == 3:
        col_name = input('COLUMN NAME: ')
        table[0].append(col_name)

        for index, row in enumerate(table[1:]):
            val = input('ENTER VALUE: ' + '|'.join(row) + '|')
            table[index+1].append(val)

    elif prompt == 4:
        which_row = int(input("Row number: "))
        which_column = int(input("Column number: "))
        if which_row in range(len(table)) and which_column in range(len(table[0])):
            val = input('VALUE (current value: ' +
                        table[which_row][which_column] + '):')
            table[which_row][which_column] = val
        else:
            print("No such row or column!")

    elif prompt == 5:
        print("|".join(table[0]))
        which_column = input("Column name: ")
        total = 0
        if which_column in table[0]:
            col_index = table[0].index(which_column)

            for row in table[1:]:
                if row[col_index].isnumeric():
                    total += int(row[col_index])
            print("Total in column " + which_column + ": " + str(total))

        else:
            print("No column named " + which_column)

    elif prompt == 6:
        total = 0
        which_row = int(input("Row number: "))
        if which_row in range(len(table)):
            for cell in table[which_row]:
                if cell.isnumeric():
                    total += int(cell)
            print(f"Total for {table[which_row]} is {total}")
        else:
            print("Row index out of range")

    elif prompt == 7:
        user_option = int(input(
            "Would you like to print selected rows [1] or would you like to print the whole table? [2] "))
        if user_option == 1:
            start = int(input('FROM ROW: '))

            end = int(input('TILL ROW: '))

            skip = 1

            if input('Skip rows? [y/n]: ') == 'y':

                skip = int(input('How many? (2 for every second etc.): '))

            start = 0 if start not in range(len(table)) else start

            end = len(table) if end > len(table) else end

            print(delimiter)

            for num in range(start, end, skip):
                row = table[num]
                print(' | '.join(row))

        elif user_option == 2:
            print(table)

        else:
            print("Program did not recognize your input, please try again.")

    elif prompt == 8:
        data = []
        for row in table[1:]:
            dictionary = {}
            for index, header in enumerate(table[0]):
                dictionary[header] = row[index]
            data.append(dictionary)

        print(data)

    elif prompt == 9:
        print("Quitting!")
        break

    repeat = input('Press enter to repeat or q to quit: ').lower()
    if repeat == "q":
        print("Quitting! Goodbye.")
        is_on = False
