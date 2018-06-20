sudokuGrid = [
    [9, 8, 7, 1, 6, 4, 3, 2, 5],
    [1, 0, 5, 0, 9, 0, 2, 0, 1],
    [8, 0, 0, 0, 4, 0, 0, 0, 0],
    [7, 0, 0, 0, 8, 0, 0, 0, 0],
    [6, 0, 0, 7, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 2, 6, 0, 0, 9],
    [2, 0, 0, 3, 0, 0, 0, 0, 6],
    [0, 0, 0, 2, 0, 0, 9, 0, 0],
    [3, 0, 1, 9, 0, 4, 5, 7, 0]

]

def getCarre(grid, letter):
    carre = []
    if letter == 'A':
        carreRow = [0, 1, 2]
        carreCol = [0, 1, 2]

    if letter == 'B':
        carreRow = [0, 1, 2]
        carreCol = [3, 4, 5]

    if letter == 'C':
        carreRow = [0, 1, 2]
        carreCol = [6, 7, 8]

    if letter == 'D':
        carreRow = [3, 4, 5]
        carreCol = [0, 1, 2]

    if letter == 'E':
        carreRow = [3, 4, 5]
        carreCol = [3, 4, 5]

    if letter == 'F':
        carreRow = [3, 4, 5]
        carreCol = [6, 7, 8]

    if letter == 'G':
        carreRow = [6, 7, 8]
        carreCol = [0, 1, 2]

    if letter == 'H':
        carreRow = [6, 7, 8]
        carreCol = [3, 4, 5]

    if letter == 'I':
        carreRow = [6, 7, 8]
        carreCol = [6, 7, 8]

    for iRow in carreRow:
            for iCol in carreCol:
                carre.append(grid[iRow][iCol])
    print('carre')
    print(carre)
    return carre

def getNotInNumber(carre):
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for case in carre:
        if case in list:
            list.remove(case)
    return list

# def getZeroPos(carre):
    # for case in carre:
    #     if case == 0:


def propagate(grid):
    # Verif carre
    carre = getCarre(grid, 'A')
    notIn = getNotInNumber(carre)

    # if 1 case last in carre
    if len(notIn) == 1:
        for i, item in enumerate(carre):
            if item == 0:
                carre[i] = notIn[0]
    # else:

    return carre

print('default carre : ', carre)
grid = propagate(sudokuGrid)
# print('carre propagated : ', carre)
# print(sudokuGrid[0])