import falcon
import os
from wsgiref import simple_server

from sudoku.Server.Routes import DataService

app = falcon.API()

# Recupere le chemin du dossier courant
dir_path = os.path.dirname(os.path.realpath(__file__))

# Ajoute dans l'applicationw
ressource = os.path.dirname(dir_path) + '/sudokuUI/'
app.add_static_route('/application', ressource)

# Envoie les données Post
app.add_route('/demo', DataService())


#  main for debug only (not in production)
if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1',8000, app)
    httpd.serve_forever()


