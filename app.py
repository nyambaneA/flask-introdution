
from os import abort
from flask import (Flask, render_template, url_for, abort, jsonify, request, redirect)
#from flask_sqlalchemy import SQLAlchemy
#from datetime import datetime
from model import db, save_data


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

#db = SQLAlchemy(app)

#class Todo(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    content = db.Column(db.String(200), nullable=False)
#    dateCreated = db.Column(db.DateTime, default=datetime.utcnow)
    
 #   def __repr__(self):
 #       return '<Task %I>' % self.id
@app.route('/')
def welcome(): 
    return render_template('welcome.html', cards = db)
@app.route('/card/<int:index>')
def card_view(index):
    try:
        card = db[index]
        return render_template("card.html", card=card, index = index , max_index = len(db)-1)
    except IndexError:
        abort(404)

@app.route('/add_card', methods=['GET', 'POST'])
def add_card():
    if request.method == 'POST':
        card ={
            "question": request.form["question"],
            "answer": request.form["answer"]
        }
        db.append(card)
        save_data()
        return redirect(url_for('card_view', index=len(db)-1))
    else:
        return render_template('add_card.html')



@app.route('/api/card/')
def api_card_list():
    return jsonify(db)
    
@app.route('/api/card/<int:index>')
def card_view_detail(index):
    try:
       return db[index]
    except IndexError:
        abort(404)

@app.route('/remove_card/<int:index>', methods=["GET", 'POST'])
def remove_card(index):
    try:
        if request.method == "POST":
            del db[index]
            save_data()
            return redirect(url_for('welcome'))

        else:
            return render_template("remove_card.html", card=db[index])
    except IndexError:
        abort(404)
def alfred_dance():
    return "alfred"
#@app.context_processor
#def context_processor():
#    return dict(key ='value', alfred= alfred_dance)


if __name__ == '__main__':

    app.run(debug=True)