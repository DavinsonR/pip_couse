import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,4,5]

@app.get('/contact')
def get_json():
    return {'name': 'Payout-them'}

@app.get('/items/', response_class = HTMLResponse)
async def read_items():
    return """
    <html>
        <head>this is the title in page
        </head>
            <body>
            <h1> this is the title inside<h1/>
            <p>lorem impsum, look at this mom</p>
            </body>
    </html>
    """


def run():
    store.get_categories()
    

if __name__ == '__main__':
    run()
    