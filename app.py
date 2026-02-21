from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

workouts = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Fitness Tracker</title>
    <style>
        body {
            font-family: Arial;
            background: linear-gradient(to right, #00c6ff, #0072ff);
            text-align: center;
        }
        .container {
            background: white;
            padding: 30px;
            margin: 40px auto;
            width: 500px;
            border-radius: 12px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        input {
            padding: 8px;
            margin: 5px;
            width: 80%;
        }
        button {
            padding: 10px;
            background: green;
            color: white;
            border: none;
            margin: 5px;
            cursor: pointer;
        }
        .workout {
            background: #f4f4f4;
            padding: 10px;
            margin: 5px;
            border-radius: 5px;
        }
        hr {
            margin: 20px 0;
        }
    </style>
</head>
<body>

<div class="container">
<h1>💪 Fitness Tracker App</h1>

<h3>Add Workout</h3>
<form method="POST" action="/add">
    <input type="text" name="name" placeholder="Workout Name" required><br>
    <input type="number" name="calories" placeholder="Calories Burned" required><br>
    <button type="submit">Add Workout</button>
</form>

<h3>Today's Workouts</h3>
{% for workout in workouts %}
<div class="workout">
    {{ workout.name }} - {{ workout.calories }} calories
</div>
{% endfor %}

<h3>Total Calories Burned: {{ total }} kcal</h3>

<hr>

<h3>BMI Calculator</h3>
<form method="POST" action="/bmi">
    <input type="number" step="0.1" name="height" placeholder="Height (cm)" required><br>
    <input type="number" step="0.1" name="weight" placeholder="Weight (kg)" required><br>
    <button type="submit">Calculate BMI</button>
</form>

{% if bmi %}
<h4>Your BMI: {{ bmi }}</h4>
{% endif %}

</div>

</body>
</html>
"""

@app.route("/")
def home():
    total = sum(w["calories"] for w in workouts)
    return render_template_string(HTML, workouts=workouts, total=total, bmi=None)

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    calories = int(request.form["calories"])
    workouts.append({"name": name, "calories": calories})
    return redirect("/")

@app.route("/bmi", methods=["POST"])
def bmi():
    height = float(request.form["height"]) / 100
    weight = float(request.form["weight"])
    bmi_value = round(weight / (height * height), 2)
    total = sum(w["calories"] for w in workouts)
    return render_template_string(HTML, workouts=workouts, total=total, bmi=bmi_value)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
