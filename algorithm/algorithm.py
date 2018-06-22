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


def getCarre(grid, iRow, iCol):
    carre = []
    if iRow in range(0, 2):
        if iCol in range(0, 2):
            carreRow = [0, 1, 2]
            carreCol = [0, 1, 2]

        elif iCol in range(3, 5):
            carreRow = [0, 1, 2]
            carreCol = [3, 4, 5]

        elif iCol in range(6, 8):
            carreRow = [0, 1, 2]
            carreCol = [6, 7, 8]

    if iRow in range(3, 5):
        if iCol in range(0, 2):
            carreRow = [3, 4, 5]
            carreCol = [0, 1, 2]

        elif iCol in range(3, 5):
            carreRow = [3, 4, 5]
            carreCol = [3, 4, 5]

        elif iCol in range(3, 5):
            carreRow = [3, 4, 5]
            carreCol = [6, 7, 8]

    if iRow in range(6, 8):
        if iCol in range(0, 2):
            carreRow = [6, 7, 8]
            carreCol = [0, 1, 2]

        elif iCol in range(3, 5):
            carreRow = [6, 7, 8]
            carreCol = [3, 4, 5]

        elif iCol in range(3, 5):
            carreRow = [6, 7, 8]
            carreCol = [6, 7, 8]

    for iRow in carreRow:
            for iCol in carreCol:
                carre.append(grid[iRow][iCol])
    return carre


def getNotInNumber(carre):
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for case in carre:
        if case in list:
            list.remove(case)
    return list


def propagate(grid):
    for iRow in range(0, 9):
        for iCol in range(0, 9):
            cellVal = grid[iRow][iCol]
            if cellVal == 0:
                possibility = verifRow(iRow)
                if len(possibility) > 1:
                    verifCol(iCol, possibility)
                    if len(possibility) > 1:
                        verifCarre(grid, iRow, iCol)

    return grid

def verifRow(iRow):
    listCell = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for cell in sudokuGrid[iRow]:
        if cell in listCell:
            listCell.remove(cell)
    return listCell

def verifCol(iCol, possibility):
    for cell in sudokuGrid[iCol]:
        if cell in possibility:
            possibility.remove(cell)
    return possibility

def verifCarre(grid, iRow, iCol):
    # Verif carre
    carre = getCarre(grid, iRow, iCol)
    notIn = getNotInNumber(carre)

    # if 1 case last in carre
    if len(notIn) == 1:
        for i, item in enumerate(carre):
            if item == 0:
                carre[i] = notIn[0]
propagate(sudokuGrid)
# print('carre propagated : ', carre)
# print(sudokuGrid[0])