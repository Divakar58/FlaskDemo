from App import app
from flask import request,jsonify
from App.database import *
from App.weather import GetWeather

@app.route('/insert',methods=['POST'])
def InsertintoDB():
    try:
        if(request.method=='POST'):
            post_data=request.get_data()
            name=post_data['name']
            price=post_data["price"]
            columns='("name","price")'
            values=tuple([name,price])
            response=InsertData(columns,values)
            data = response.get_json()
            if(data["result"]=='success'):
                return jsonify({"result":"success","message": data['rowcount']+" rows inserted successfully"})
            else:
                return jsonify({"result":"error","message":data["message"]})
    except Exception as e:
        return jsonify({"result":"failed","message":e}),500

@app.route('/update',methods=['POST'])
def UpdateDB():
    try:
        if(request.method=='POST'):
            post_data=request.get_data()
            id=post_data["id"]
            name=post_data['name']
            price=post_data["price"]
            values={"id":id,"name":name,"price":price}
            response=UpdateData(values)
            data = response.get_json()
            if(data["result"]=='success'):
                return jsonify({"result":"success","message":data['rowcount']+" rows updated successfully"})
            else:
                return jsonify({"result":"error","message":data["message"]})
    except Exception as e:
        return jsonify({"result":"failed","message":e}),500

@app.route('/view',methods=['GET'])
def viewEntry():
    try:
        id = request.args.get('id', type=str)
        df=ViewData(id)
        return df.to_json(orient='records')
    except Exception as e:
        return jsonify({"result":"failed","message":e}),500

@app.route('/delete',methods=['GET'])
def deleteEntry():
    try:
        id = request.args.get('id', type=str)
        response=DeleteData(id)
        data=response.get_json()
        if(data['message'] == 'success'):
            return jsonify({'result': 'success', 'message': data['rowcount']+' rows deleted successfully'}), 200
        else:
            return jsonify({'result': 'error', 'message': 'Error occurred while deleting'}), 500
    except Exception as e:
        return jsonify({"result":"error","message":e}),500


@app.route('/weather',methods=['GET'])
def getWeather():
    try:
        df=GetWeather()
        return df.to_json(orient='records')
    except Exception as e:
        return jsonify({"result":"error","message":e}),500