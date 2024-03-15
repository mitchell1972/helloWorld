import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'site.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disables modification tracking
db = SQLAlchemy(app)

class HelloWorld(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"HelloWorld('{self.content}')"

@app.route('/')
def hello():
    hello_message = HelloWorld.query.first()  # Fetches the first "Hello World" message from the database
    if hello_message:
        return hello_message.content
    else:
        return 'Hello, World!'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Creates the database file and tables
        # Checks if the HelloWorld table is empty and inserts the default message if it is
        if not HelloWorld.query.first():
            hello_row = HelloWorld(content='Hello, World!')
            db.session.add(hello_row)
            db.session.commit()
    # Takes the port from the environment variable or defaults to 5001 if not available
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port, debug=True)

