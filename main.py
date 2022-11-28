from flask import Flask,jsonify,request,render_template, redirect, url_for
from project_app.util import IrisData

import config

app =Flask(__name__)
@app.route("/")   # Home API
def hello_flask():
    print("Welcome to flask")
    #return "Hello Python"
    return render_template("guess.html")
    
@app.route('/result')
def result():
    return "Successful try"    


@app.route("/specices")
def myfun():
    SepalLengthCm=25
    SepalWidthCm =40
    PetalLengthCm =24
    PetalWidthCm=22

    specices_ans=IrisData(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm)
    spvalue=specices_ans.get_species()
    return jsonify({"Return" : f"Predicted specices are :{spvalue}"})
@app.route("/guess_specices",methods=["POST","GET"])
def def_specices():
    if request.method == 'POST':

        data = request.form 
        SepalLengthCm = data["sepalLengthcm"]
        SepalWidthCm = data["sepalwidthcm"]
        PetalLengthCm = data["petalLengthcm"]
        PetalWidthCm = data["petalwidthcm"]
        #print("Id ::",Id)
        specices_ans=IrisData(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm)
        spvalue=specices_ans.get_species()
        print(spvalue)
        #return redirect(url_for('result',spvalue = spvalue))
        if (spvalue<=0):
            spvalue="setosa"
        else: 
            if (spvalue<=1 and spvalue>0):
                spvalue="versicolor"
            else :
                
                 spvalue="virginica"

        return render_template('res.html',sp=spvalue)
        

if __name__=="__main__":
    app.run(debug="true")
        
