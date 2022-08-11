
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello World from Flask!!!'
 

@app.route('/yaso')
def yaso():
    return 'basardim'

@app.route('/kendi_denemem')
def kendi():
    return 'olacak ins'

@app.route('/forth/<string:id>')
def forth(id):
    return f'Id number of this page is {id}'
    

if __name__ == '__main__':
    app.run(debug=True, port=2000)
