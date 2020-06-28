from flask import Flask
from flask_restful import Api
from flask_jwt import JWT


from resources.company import Company, CompanyList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123-asdf@localhost/expenses'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'expenses'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


# jwt = JWT()  # /auth

api.add_resource(Company, '/company/<string:name>')
api.add_resource(CompanyList, '/company')

# api.add_resource(, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
