import connexion
from connexion.resolver import RestyResolver


app = connexion.App(__name__,
                    options={"swagger_ui": True})
app.add_api('swagger.yaml')
application = app.app

if __name__ == '__main__':
    # run our standalone gevent server
    app.run(port=9999, server='gevent')
