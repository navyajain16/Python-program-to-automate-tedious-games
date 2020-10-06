def swipeRow(row):
    prev = -1  # previous non-zero element
    i = 0
    temp = [0, 0, 0, 0]

    for element in row:

        if element != 0:  # we skip elements that are zero and useless.
            if prev == -1:  # we make prev the first non-zero element and also the first element of temp array.
                prev = element
                temp[i] = element
                i += 1
            elif prev == element:
                temp[i - 1] = 2 * prev  # we make (i-1)th element of the array as 2*prev.
                prev = -1  # make prev=-1 as it can no longer can be added to other element.
            else:
                prev = element
                temp[i] = element
                i += 1

    return temp  # we return the new row temp.