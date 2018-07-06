# import falcon
# import sys
# sys.path.append('D:\Documents\Master Digital Campus\Master 1\Big Data\Python\App_Sudoku\sudoku\model')
#
# from sudoku import Sudoku

# methode Poste
class DataService:

    def on_get(self, req, resp):
        data = req.stream.read().decode('utf-8')
        # output the data, we could write it to persistent storage here
        resp.media = resolutionSudo
        print('Resolution du Sudoku' + resolutionSudo)



# s = Sudoku()

#formate les données en format JSON
# s.deserialisation(data)

# resoud le sudoku
# s.solve()

# renvoie les données formater sur la page HTML
#s.serialisation()

# resolutionSudo = s.serialisation()


resolutionSudo = 'test'

