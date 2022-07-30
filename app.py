import sys,os
from turtle import left
from flask import Flask
from housing.logger import logging
from housing.exception import HousingException
from flask import Flask, request
from housing.entity.retension_predict import RetensionPredictor, RetensionData
from flask import send_file, abort, render_template
from flask import Response



ROOT_DIR = os.getcwd()
SAVED_MODELS_DIR_NAME = "saved_models"
MODEL_DIR = os.path.join(ROOT_DIR, SAVED_MODELS_DIR_NAME)


HOUSING_DATA_KEY = "retension_data"
LEFT_KEY = "left"




app=Flask(__name__)



# @app.route("/",methods=["GET","POST"])
# def index():
#     try:
#         raise Exception("we are testing exception")
#     except Exception as e:
#         housing = HousingException(e,sys)
#         logging.info(housing.error_message)
#         logging.info("we are logging")
#     return "CI-CD Pipeline"


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    context = {
        HOUSING_DATA_KEY: None,
        LEFT_KEY: None
    }

    if request.method == 'POST':
        satisfaction_level = float(request.form['satisfaction_level'])
        last_evaluation = float(request.form['last_evaluation'])
        number_project = int(request.form['number_project'])
        average_montly_hours = int(request.form['average_montly_hours'])
        time_spend_company = int(request.form['time_spend_company'])
        Work_accident = int(request.form['Work_accident'])
        promotion_last_5years = int(request.form['promotion_last_5years'])
        sales = request.form['sales']
        salary = request.form['salary']

        retension_data = RetensionData(satisfaction_level=satisfaction_level,
                                   last_evaluation=last_evaluation,
                                   number_project=number_project,
                                   average_montly_hours=average_montly_hours,
                                   time_spend_company=time_spend_company,
                                   Work_accident=Work_accident,
                                   promotion_last_5years=promotion_last_5years,
                                   sales=sales,
                                   salary=salary,
                                   )
        housing_df = retension_data.get_housing_input_data_frame()
        housing_predictor = RetensionPredictor(model_dir=MODEL_DIR)
        left = housing_predictor.predict(X=housing_df)
        print('output : '+str(left))
        context = {
            HOUSING_DATA_KEY: retension_data.get_housing_data_as_dict(),
            LEFT_KEY: left,
        }
        return render_template('index.html', context=context)
    
    return render_template("index.html", context=context)





if __name__=="__main__":
    app.run(debug=True)