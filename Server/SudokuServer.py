import falcon
import os
from wsgiref import simple_server
from falcon_cors import CORS
import urllib.parse

# from Server.Routes import DataService

cors = CORS(allow_origins_list=['http://127.0.0.1:8000/demo'])

app = falcon.API(middleware=[cors.middleware])

public_cors = CORS(allow_all_origins=True)

class DataService:
    cors = public_cors

    def on_get(self, req, resp):
        data = req.stream.read().decode('utf-8')
        # output the data, we could write it to persistent storage here
        resp.media = resolutionSudo
        print('Resolution du Sudoku' + resolutionSudo)

    def on_post(self, req, resp):
        data = req.stream.read().decode('utf-8')
        # urllib.parse.unquote(data)
        resp.media = "Everone can post to this resource" + urllib.parse.unquote(data)
        print(urllib.parse.unquote(data))

resolutionSudo = 'test'

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


