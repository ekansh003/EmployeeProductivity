from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('gwp_xg.pkl', 'rb'))


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/predict')
def show_predict_form():
    return render_template("predict.html")


@app.route("/pred", methods=['POST'])
def handle_prediction():
    data = [
        int(request.form['quarter']),
        int(request.form['department']),
        int(request.form['day']),
        int(request.form['team']),
        float(request.form['targeted_productivity']),
        float(request.form['smv']),
        int(request.form['over_time']),
        int(request.form['incentive']),
        float(request.form['idle_time']),
        int(request.form['idle_men']),
        int(request.form['no_of_style_change']),
        float(request.form['no_of_workers']),
        int(request.form['month'])
    ]

    prediction = model.predict([data])[0]
    if prediction <= 0.3:
        result = 'Based on the given input, The employee is averagely productive.'
    elif 0.3 < prediction <= 0.8:
        result = 'Based on the given input, The employee is medium productive.'
    else:
        result = 'Based on the given input, The employee is highly productive.'

    return render_template("submit.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)
