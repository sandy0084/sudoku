import falcon
class DataPost(object):
    def on_get(self, req, resp, filename):
        # do some sanity check on the filename
        resp.status = falcon.HTTP_200
        resp.content_type = 'appropriate/content-type'


