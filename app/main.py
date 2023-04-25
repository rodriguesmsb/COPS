from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
import app.model as app_functions
import pandas as pd
import sklearn
from sklearn.ensemble import RandomForestClassifier


app = Flask(__name__)


@app.route("/", methods = ['GET','POST'])
def make_pred():

    #get user response
    if request.method == "POST":


        result = request.form.to_dict(flat = False) #convert form to a dict

        #convert dict to a data frame
        result = pd.DataFrame.from_dict(result)
        for col in result.columns:
            result[col] = result[col].astype(float)
        
        
        result.rename(columns = {"age": "Idade", "ars":"saturacao_ar_ambiente_adm", 
                                 "Leukocyte":"leucograma_na_admissao", "urea":"ureia_na_admissao", 
                                 "lactate":"lactato", "creactive": "valor_do_pcr", 
                                 "ddimer": "resultado_d_dimero"}, inplace = True)
        result = result[['Idade','saturacao_ar_ambiente_adm', 'leucograma_na_admissao', 'ureia_na_admissao',
                         'valor_do_pcr', 'resultado_d_dimero','lactato']]


    


        prob = app_functions.prediction_prob(result)[0][0]
        labels = ["Non Death", "Death"]
        values = [prob,1-prob]
        

        
        # data = [
        #     ("Death", prob),
        #     ("Non Death", 1 - prob)
        # ]

        # #split data into two list
        # labels = [row[0] for row in data]
        # values = [row[1] for row in data]
        # print(data)
        print(values)
        print(labels)
      
        return render_template("graph.html", labels = labels, values = values)

    return render_template("index.html")
