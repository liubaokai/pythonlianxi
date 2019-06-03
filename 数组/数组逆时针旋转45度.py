def rotate_array(array):
    lens = len(array)
    i = lens - 1
    while i > 0:
        row = 0
        col = i
        while col < lens:
            print( array[row][col])
            row += 1
            col += 1
        i -= 1
    i = 0
    while i < lens:
        row = i
        col = 0
        while row < lens:
            print(array[row][col])
            row += 1
            col += 1
        i += 1