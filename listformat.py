LISTS = [['Name', 'Item', 'Amount', 'Unit_Price', 'Total_Price'],
         ['Bettison, Elnora', 'Doxycycline Hyclate', 98, 23.43, 2296.14],
         ['McShee, Glenn', 'DROXIA', 27, 33.86, 914.22],
         ['Conyard, Phil', 'Nadolol', 44, 12.35, 543.4],
         ['Bettison, Elnora', 'Claravis', 91, 9.85, 896.35],
         ['Idalia, Craig', 'Nadolol', 83, 12.35, 1025.05],
         ['Woodison, Annie', 'Metolazone', 46, 43.06, 1980.76],
         ['Woodison, Annie', 'DROXIA', 50, 33.86, 1693.0],
         ['Skupinski, Wilbert', 'Nadolol', 60, 12.35, 741.0],
         ['Conyard, Phil', 'WRINKLESS PLUS', 49, 23.55, 1153.95],
         ['Bettison, Elnora', 'Doxycycline Hyclate', 59, 23.43, 1382.37],
         ['Skupinski, Wilbert', 'Metolazone', 51, 43.06, 2196.06],
         ['McShee, Glenn', 'Claravis', 1, 9.85, 9.85]]


def get_widths(big_list):
    widths = [0] * len(big_list[0])
    for row in big_list:
        i = 0
        for word in row:
            if len(str(word)) > widths[i]:
                widths[i] = len(str(word))
            i += 1
    return widths


def print_widths_table(widths, header=['COLUMN', 'WIDTH']):
    c1 = max(len(header[0]), len(str(len(widths))) + 4)
    c2 = max(len(header[1]), len(str(sorted(widths)[-1])))
    firstrow = "| {:^" + str(c1) + "} | {:^" + str(c2) + "} |"
    firstrow = firstrow.format(*header)
    print(widths)
    print(firstrow)

    for num, width in enumerate(widths):
        row = '| {0:^' + str(c1) + '} | {1:^' + str(c2) + '} |'

        row = row.format('COL ' + str(num), width)

        print(row)


widths = get_widths(LISTS)
print_widths_table(widths)
