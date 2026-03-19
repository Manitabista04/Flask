from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer , primary_key= True)
    title = db.Column(db.String(200), nullable= False)
    desc = db.Column(db.String(500), nullable= False)
    date_created = db.Column(db.DateTime)

    def __repr__(self):
        return f"{self.sno} - {self.title}"
    
@app.route("/")
def hello_world():
    todo = Todo(title = "First Todo" , desc = "Learn advance python")
    db.session.add(todo)
    db.session.commit()
    return render_template('index.html')
    

@app.route('/products')
def products():
    return 'this is a products page'

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, port=5001)
