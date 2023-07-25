from flask import Flask,request
app = Flask(__name__)

@app.route("/")
def main():
    return {"payload":"welcome to my project2"}

@app.route("/read")
def read():
    content=request.args.get("content")
    if content=="foo":
        return  {"payload": content}
    else: 
        return "usuario no encontrado"

@app.route("/create", methods=["POST"])
def create():
    content=request.args.get("content")
    if content=="bar":
        return  {"payload": content}
    else: 
        return "usuario no encontrado"

@app.route("/delete", methods=["DELETE"])
def delete():
    content=request.args.get("content")
    if content=="qux":
        return  {"payload": content}
    else: 
        return "usuario no encontrado"
    
@app.route("/put", methods=["PUT"])
def put():
    content=request.args.get("content")
    if content=="echo":
        return  {"payload": content}
    else: 
        return "usuario no encontrado"
    
@app.route("/init", methods=["GET"])
def init():
    content=request.args.get("content")
    if content=="alfa":
        return  {"payload": content}
    else: 
        return "usuario no encontrado"



if __name__== "__main__":
    app.run(debug=True)
