from website import create_app
from os import environ

app = create_app() # default config

if __name__ == "__main__":
    debug = environ.get("DEBUG").lower() == "true" if "DEBUG" in environ else True
    app.run(debug=debug)