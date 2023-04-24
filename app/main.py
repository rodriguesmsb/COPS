from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
import app.model as app_functions
import pandas as pd


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
        
        
        result.rename(columns = {"age": "idade", "ars":"saturacao_ar_ambiente_adm", 
                                 "Leukocyte":"leucograma_na_admissao", "urea":"ureia_na_admissao", 
                                 "lactate":"lactato", "creactive": "valor_do_pcr", 
                                 "ddimer": "resultado_d_dimero"}, inplace = True)
        print(result)


        # ##add new features
        # result = app_functions.create_feature(result)
    
        # #remove other dishx
        # result.drop(["other_dishx"], axis = 1, inplace = True)

        # #reorder columns
        # result = result[['age', 'race', 'sex', 'education', 'prior_tb', 'hiv', 'diabetes',
        #                  'ilicit_drug', 'alcohol', 'tobacco', 'cash_transfer', 'liberty_dep',
        #                  'exp_homelessness', 'n_of_morb']]

        


        # prob = app_functions.prediction_prob(result)[0]

        
        # data = [
        #     ("Desfavorável", prob),
        #     ("Favorável", 1 - prob)
        # ]

        # #split data into two list
        # labels = [row[0] for row in data]
        # values = [row[1] for row in data]
      
        return render_template("graph.html")#, labels = labels, values = values)

    return render_template("index.html")