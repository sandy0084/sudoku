import json
from case import Case

#classe sudoku
class Sudoku:

    #constructeur
    def __init__(self):
        #attribut
        #self.grille = [[0 for x in range(9)] for y in range(9)]
        self.jsonstr = ""
        grille = []
        for l in range(0, 8):
            ligne = []
            #print(l)
            for c in range(0, 9):
                ligne.append(Case(0))
                #print(c)
            grille.append(l)

        #print("Creation d'un sudoku ")
        #print(grille)

        #creation des a, b, c, d, e, f, g, h, i (liste avec les cases correspondantes (schema))

    #deserialisation (reception de la grille)
    def deserialisation(self, sudoku):
        #notre grille (self) va prendre les valeurs du sudoku recu
        #self = sudoku
        # res = []
        # sudoku = sudoku.split(",")
        # z = 0
        # for i in sudoku :
        #     z = z + 1
        #     if(z == 1) :
        #         tempo = i.split("{")
        #         res.append(tempo[2])
        #     else :
        #         res.append(i.split("{"))
        #
        # #for s in res :
        #     #s.match("^[-+]?[0-9]+$")

        self.jsonstr = json.loads(sudoku)

        return


    # solve (test de la grille)
    def solve(self, sudoku):
        #test du sudoku
        return

    # serialisation (renvoi de la grille)
    def serialisation(self):

        for i in range(0, 9):
            for j in range(0, 9):
                indice = str(i) + str(j)
                #print(self.jsonstr[indice])
                if(self.jsonstr["sudoku"][indice] == ''):
                    self.jsonstr["sudoku"][indice] = -1
        return str(self.jsonstr)

grille = Sudoku()
sudoku = '{"sudoku":{"10":"1","11":"","12":"8","13":"","14":"","15":"6","16":"","17":"","18":"","20":"","21":"4","22":"","23":"","24":"8","25":"","26":"","27":"","28":"","30":"","31":"1","32":"","33":"","34":"","35":"4","36":"3","37":"","38":"","40":"","41":"","42":"","43":"","44":"","45":"7","46":"","47":"1","48":"2","50":"","51":"2","52":"","53":"3","54":"","55":"8","56":"9","57":"","58":"","60":"8","61":"","62":"4","63":"","64":"6","65":"5","66":"","67":"","68":"1","70":"9","71":"","72":"","73":"","74":"7","75":"","76":"","77":"4","78":"3","80":"","81":"","82":"","83":"","84":"4","85":"","86":"5","87":"6","88":"","00":"3","01":"","02":"","03":"","04":"5","05":"","06":"","07":"2","08":""}}'
grille.deserialisation(sudoku)
res = grille.serialisation()

print(res)