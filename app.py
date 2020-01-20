import os
from flask import Flask, render_template, jsonify, request
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS
from models import db

from family import Family

'''for find the place of the file that we are executing '''
BASE_DIR = os.path.abspath(os.path.dirname(__file__)) 
app = Flask(__name__)
''' for the case that i forget de slash on the endpoint '''
app.url_map.strict_slashes = False 
''' for the show or not the errors '''
app.config['DEBUG'] = True
''' for configuration of the environment '''
app.config['ENV'] = 'development'
'''for define my database route and configuration'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'dev.db')
'''is required when i use SQLALCHEMY and for delete not important changes '''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
''' for configuration of command to migrate '''
db.init_app(app)
migrate = Migrate(app, db)
''' for start de liveServer '''
manager = Manager(app)
''' run for console the migrate command '''
manager.add_command('db',MigrateCommand)
''' for use the development environment '''
CORS(app)

fam = Family()

''' for define the route for default '''
@app.route('/')
def home():
    return render_template('index.htm', name='home')
''' for consulting my API '''

@app.route('/family', methods=['GET', 'POST'])
@app.route('/family/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def members(id = None): # Name not affect functionality
    if request.method == 'GET':
        if id is not None:
            member = fam.get_member(id)
            return jsonify(member), 200
        else:
            #members = Member.query.all() //# only when we work with server(insomnia)
            members = fam.get_all_members()
            #members = list(map(lambda member: member.serialize(), members)) //# only when we work with server(insomnia)
            return jsonify(members), 200


    if request.method == 'POST': #creating new member
        if not request.json.get('name'):
            return jsonify({"name": "Is requierd"}), 422
        if not request.json.get('lastname'):
            return jsonify({"lastname": "Is requierd"}), 422
        if not request.json.get('age'):
            return jsonify({"age": "Is requierd"}), 422

        fam._name = request.json.get('name')
        fam._age = request.json.get('age')
        fam._last_name = request.json.get('lastname')
        
        #we need to generate id
        member = fam.add_member(fam)
        return jsonify(member), 200

    if request.method == 'PUT':#creating new member
        if not request.json.get('name'):
            return jsonify({"name": "Is requierd"}), 422
        if not request.json.get('lastname'):
            return jsonify({"lastname": "Is requierd"}), 422
        if not request.json.get('age'):
            return jsonify({"age": "Is requierd"}), 422

        update = {
            "name": request.json.get("name"),
            "age": request.json.get("age"),
            "lastname": request.json.get("lastname")
        }
        #we need to generate id
        member = fam.update_member(id, update)
        return jsonify(member), 200

    if request.method == 'DELETE':
        if id is not None:
            member = fam.delete_member(id)
            return jsonify({"name": "Deleted succsesfully"}), 200
        else:
            #members = Member.query.all() //# only when we work with server(insomnia)
            members = fam.get_all_members()
            #members = list(map(lambda member: member.serialize(), members)) //# only when we work with server(insomnia)
            return jsonify(members), 200




''' for start my app'''
if __name__=='__main__':
    manager.run()