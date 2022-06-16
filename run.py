from distutils.log import debug
from nortsev_flask_blog import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
