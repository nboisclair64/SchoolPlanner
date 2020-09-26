from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # 3 slashes is a relative path
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    className = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0) # Ignore this column, it is never used
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

# db.create_all() create database (first time only)

if __name__ == "__main__":
    app.run(debug=True)