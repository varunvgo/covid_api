from flask_restful import Resource
from models.company import CompanyModel


class Company(Resource):
    # def __init__(self, name):
    #     self.name = name
        
    def get(self, name):
        company = CompanyModel.find_by_name(name)
        if company:
            return company.json()
        return {'message': 'Company not found'}, 404

    def post(self, name):
        if CompanyModel.find_by_name(name):
            return {'message': "A company with name '{}' already exists.".format(name)}, 400

        company = CompanyModel(name)
        try:
            company.save_to_db()
        except:
            return {"message": "An error occurred creating the company."}, 500

        return company.json(), 201

    def delete(self, name):
        company = CompanyModel.find_by_name(name)
        if company:
            company.delete_from_db()

        return {'message': 'Company deleted'}


class CompanyList(Resource):
    def get(self):
        return {'companys': list(map(lambda x: x.json(), CompanyModel.query.all()))}
