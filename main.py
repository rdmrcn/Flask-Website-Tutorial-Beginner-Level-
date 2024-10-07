from flask import Flask
from views import views
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(views, url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
#your_project/
# ├── main.py
# ├── models.py
# ├── views.py
# ├── templates/
# │   └── index.html
# ├── static/
# │   ├── styles.css
# │   └── logo.png
