from flask import Flask
from flask import render_template
from flask import request
from src.pipeline.prediction_pipeline import custom_data,prediction_pipeline
app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def prediction():
    if request.method == 'GET':
        return render_template("home.html")
    else:
        data = custom_data(
            gender = request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))
        )
        df = data.raw_data_to_dataframe()
        predict_pipeline = prediction_pipeline()
        results = predict_pipeline.predict(df)
        return render_template("home.html", prediction_result=results[0])


if __name__ == '__main__' :
    app.run(debug=True)