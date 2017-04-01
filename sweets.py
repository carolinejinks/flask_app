from flask import Flask, render_template
from data import SWEETS
app = Flask(__name__)

def get_ids_and_sweets(source):
    ids_and_sweet = []
    for row in source:
        id = row["ID"]
        name = row["Name"]
        ids_and_sweet.append( [id, name] )
    return ids_and_sweet

def get_sweet(source, id):
    for row in source:
        if id == str( row["ID"] ):
            name = row["Name"]
            manufacturer = row["Manufacturer"]
            country = row["Country"]
            kind = row["Kind"]
            id = str(id)
            return id, name, manufacturer, country, kind

@app.route('/')
@app.route('/index.html')
def index():
    ids_and_sweet = get_ids_and_sweets(SWEETS)
    return render_template('index.html', pairs=ids_and_sweet)

@app.route('/sweet/<id>')
def sweet(id):
    id, name, manufacturer, country, kind = get_sweet(SWEETS, id)
    return render_template('sweet.html', id=id, name=name, manufacturer=manufacturer, country=country, kind=kind)

if __name__ == '__main__':
    app.run(debug=True)
