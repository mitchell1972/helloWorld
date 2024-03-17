import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'site.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class HelloWorld(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<HelloWorld {self.content}>"


@app.before_request
def initialize_database():
    db.create_all()
    if not HelloWorld.query.first():
        hello_row = HelloWorld(content='Hello, World!')
        db.session.add(hello_row)
        db.session.commit()


@app.route('/')
def hello():
    hello_message = HelloWorld.query.first()
    if hello_message:
        return hello_message.content
    else:
        return 'Hello, World!'


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)
