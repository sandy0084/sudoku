from case import Case

#classe sudoku
class Sudoku:

    #constructeur
    def __init__(self):
        #attribut
        #self.grille = [[0 for x in range(9)] for y in range(9)]
        grille = []
        for l in range(0, 8):
            ligne = []
            print(l)
            for c in range(0, 9):
                ligne.append(Case(0))
                print(c)
            grille.append(l)

        case = grille[3][4]
        print("Creation d'un sudoku ")
        print(grille)

        #creation des a, b, c, d, e, f, g, h, i (liste avec les cases correspondantes (schema))

    #deserialisation (reception de la grille)
    def deserialisation(self, sudoku):
        #notre grille (self) va prendre les valeurs du sudoku recu
        #self = sudoku
        return


    # solve (test de la grille)
    def solve(self, sudoku):
        #test du sudoku
        return

    # serialisation (renvoi de la grille)
    def serialisation(self):
        res =  "{ sudoku : { '00' : '1', '01' : '2', '02' : '3', '03' : '4', '04' : '5', '05' : '6',  '06' : '7',  '07' : '8',  '08' : '9', '10' : '1',  '11' : '2', '12' : '3', '13' : '4', '14' : '5', '15' : '6', '16' : '7',  '17' : '8',  '18' : '9', '20' : '1', '21' : '2',  '22' : '3', '23' : '4',  '24' : '5',  '25' : '6', '26' : '7',  '27' : '8',  '28' : '9', '30' : '1',  '31' : '2',  '32' : '3', '33' : '4',  '34' : '5',  '35' : '6', '36' : '7',  '37' : '8', '38' : '9',  '40' : '1',  '41' : '2',  '42' : '3',  '43' : '4',  '44' : '5',  '45' : '6',  '46' : '7',  '47' : '8', '48' : '9', '50' : '1', '51' : '2',  '52' : '3', '53' : '4', '54' : '5',  '55' : '6',  '56' : '7',  '57' : '8',  '58' : '9',  '60' : '1', '61' : '2',  '62' : '3', '63' : '4', '64' : '5', '65' : '6',  '66' : '7', '67' : '8', '68' : '9',  '70' : '1', '71' : '2', '72' : '3', '73' : '4', '74' : '5', '75' : '6', '76' : '7', '77' : '8', '78' : '9', '80' : '1',  '81' : '2',  '82' : '3', '83' : '4', '84' : '5', '85' : '6', '86' : '7', '87' : '8', '88' : '9' } }"
        return res

s = Sudoku()