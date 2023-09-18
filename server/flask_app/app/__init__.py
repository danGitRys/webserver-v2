from flask import Flask,request,jsonify
from config import Config
from app.extensions import db
from flask_cors import CORS
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app)
    db.init_app(app)
    @app.route('/test',methods=['GET','POST'])
    def test_page():
        liste = [
    {"id": "A1", "name": "test1"},
    {"id": "A2", "name": "test2"},
    {"id": "A3", "name": "test3"},
    {"id": "A4", "name": "test4"},
    {"id": "A5", "name": "test5"},
    {"id": "A6", "name": "test6"},
    {"id": "A7", "name": "test7"},
    {"id": "A8", "name": "test8"},
    {"id": "A9", "name": "test9"},
    {"id": "A10", "name": "test10"},
    {"id": "A11", "name": "test11"},
    {"id": "A12", "name": "test12"},
    {"id": "A13", "name": "test13"},
    {"id": "A14", "name": "test14"},
    {"id": "A15", "name": "test15"},
    {"id": "A16", "name": "test16"},
    {"id": "A17", "name": "test17"},
    {"id": "A18", "name": "test18"},
    {"id": "A19", "name": "test19"},
    {"id": "A20", "name": "test20"},
    {"id": "A21", "name": "test21"},
    {"id": "A22", "name": "test22"},
    {"id": "A23", "name": "test23"},
    {"id": "A24", "name": "test24"},
    {"id": "A25", "name": "test25"},
    {"id": "A26", "name": "test26"},
    {"id": "A27", "name": "test27"},
    {"id": "A28", "name": "test28"},
    {"id": "A29", "name": "test29"},
    {"id": "A30", "name": "test30"},
    {"id": "A31", "name": "test31"},
    {"id": "A32", "name": "test32"},
    {"id": "A33", "name": "test33"},
    {"id": "A34", "name": "test34"},
    {"id": "A35", "name": "test35"},
    {"id": "A36", "name": "test36"},
    {"id": "A37", "name": "test37"},
    {"id": "A38", "name": "test38"},
    {"id": "A39", "name": "test39"},
    {"id": "A40", "name": "test40"},
    {"id": "A41", "name": "test41"},
    {"id": "A42", "name": "test42"},
    {"id": "A43", "name": "test43"},
    {"id": "A44", "name": "test44"},
    {"id": "A45", "name": "test45"},
    {"id": "A46", "name": "test46"},
    {"id": "A47", "name": "test47"},
    {"id": "A48", "name": "test48"},
    {"id": "A49", "name": "test49"},
    {"id": "A50", "name": "test50"}
]

        if request.method == 'GET':
            return jsonify(liste)
        elif request.method == 'POST':
        # Receive JSON data from the POST request
            data = request.get_json()
            print(data)
        
        # Append the received data to the 'liste' list
            liste.append(data)
            return jsonify(liste)
        return "Hello"
    
    return app
