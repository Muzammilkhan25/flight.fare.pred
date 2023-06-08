from flask import Flask, request,url_for, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))



@app.route("/")

def hello_world():
    return render_template("pricing.html")




@app.route("/predict", methods = ["GET","POST"])
   
def predict():
       airline=request.form["airline"]
       source_city=request.form["source_city"]
       departure_time = request.form["departure_time"]
       stops=request.form["stops"]
       arrival_time=request.form["arrival_time"]
       destination_city=request.form["destination_city"]
       grade = request.form["grade"]
       days_left=request.form["days_left"]
       hours=request.form["hours"]
       mins=request.form["mins"]
       
       #features
       # features = [np.aaray([airline,source_city,departure_time,stops,arrival_time,destination_city,grade,days_left,hours,mins])]
       # prediction=moel.predict(features)  
       charge_per_source=0
       if(source_city==0):
            charge_per_source=21469.4605750946
       elif(source_city==1):
            charge_per_source=21995.33987080103
       elif(source_city==2):
            charge_per_source=18951.326638736286
       elif(source_city==3):
            charge_per_source=20155.623878841347
       elif(source_city==4):
            charge_per_source=21746.235678684705
       elif(source_city==5):
            charge_per_source=21483.818838675776
       else:
            charge_per_source=22000.000000000000  
       charge_per_destination=0
       if(destination_city==0):
            charge_per_destination=21593.95578444427
       elif(destination_city==1):
            charge_per_destination=21953.323969480778
       elif(destination_city==2):
            charge_per_destination=18436.767869595536
       elif(destination_city==3):
            charge_per_destination=20427.661283527596
       elif(destination_city==4):
            charge_per_destination=21959.55755642589
       elif(destination_city==5):
            charge_per_destination=21372.52946850094
       else:
            charge_per_destination=22000.000000000000     
       
       charge_per_stops=0
       if(stops==0):
            charge_per_stops=22900.9924819523
       elif(stops==1):
            charge_per_stops=14113.450775252146
       elif(stops==2):
            charge_per_stops=9375.938534607265
       else:
            charge_per_stops=23000.000000000000
       
       features = [np.array([airline,source_city,departure_time,stops,arrival_time,destination_city,grade,days_left,charge_per_source,charge_per_destination,charge_per_stops,hours,mins])]
       prediction=model.predict(features)  
       output = round(prediction[0], 2)  
       return render_template('pricing.html',prediction_text="Your Flight price is Rs. {}".format(output))
        

if __name__ == "__main__":
     app.run(debug=True)

        