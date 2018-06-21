# import falcon

# from sudoku.model.sudoku import Sudoku

# methode Poste
class DataService:

    def on_post(self, req, resp):
        data = req.stream.read().decode('utf-8')
        # output the data, we could write it to persistent storage here
        resp.media = "<p>" +resolutionSudo + "</p>"
        print(data)



# s = Sudoku()

#formate les données en format JSON
# s.deserialisation(data)

# resoud le sudoku
# s.solve()

# renvoie les données formater sur la page HTML
#s.serialisation()

# resolutionSudo = s.serialisation()

resolutionSudo = 'test'

