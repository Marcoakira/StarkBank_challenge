from flask import Flask,request,json, Response


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Webhooks with Python'

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/webhook',methods=['GET'])
def resposta():

    print(request.json)
    return Response(status=200)