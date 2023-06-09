import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
def get_list():
    return [1, 2, 3]


@app.get("/contact", response_class=HTMLResponse)
def get_contact():
    return """
    <html>
        <head>
            <title>Holi probando ando</title>
        </head>
        <body>
            <h1>Soy un párrafo</h1>
            <p>Probando ando xx</p>
        </body>
    </html>
    """


def run():
    store.get_categories()


if __name__ == '__main__':
    run()
