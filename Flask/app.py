from flask import Flask, render_template, request
import pickle
import xgboost as xgb

app = Flask(__name__)

# ==========================================
# LOAD MODEL + ENCODERS
# ==========================================

model = xgb.XGBRegressor()
model.load_model("productivity_model.json")

with open("productivity_encoders.pkl", "rb") as file:
    encoders = pickle.load(file)


# ==========================================
# ROUTES
# ==========================================

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/predict")
def show_predict_form():
    return render_template("predict.html")


# ==========================================
# PREDICTION
# ==========================================

@app.route("/pred", methods=["POST"])
def handle_prediction():

    # Encode categorical inputs
    quarter = encoders["quarter"].transform(
        [request.form["quarter"]]
    )[0]

    department = encoders["department"].transform(
        [request.form["department"]]
    )[0]

    day = encoders["day"].transform(
        [request.form["day"]]
    )[0]

    # Build model input in exact feature order
    data = [[
        quarter,
        department,
        day,
        int(request.form["team"]),
        float(request.form["targeted_productivity"]),
        float(request.form["smv"]),
        int(request.form["over_time"]),
        int(request.form["incentive"]),
        float(request.form["idle_time"]),
        int(request.form["idle_men"]),
        int(request.form["no_of_style_change"]),
        float(request.form["no_of_workers"]),
        int(request.form["month"])
    ]]

    # Generate prediction
    prediction = float(model.predict(data)[0])

    # Classify productivity
    if prediction <= 0.3:
        level = "Averagely Productive"
    elif prediction <= 0.8:
        level = "Medium Productive"
    else:
        level = "Highly Productive"

    return render_template(
        "submit.html",
        prediction=prediction,
        level=level
    )


# ==========================================
# RUN
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)