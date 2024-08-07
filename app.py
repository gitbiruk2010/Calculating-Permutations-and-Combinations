import math
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for flashing messages

def calculate_permutations(n, r):
    try:
        return math.factorial(n) // math.factorial(n - r)
    except ValueError as e:
        raise ValueError("Invalid calculation for permutations.") from e

def calculate_combinations(n, r):
    try:
        return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
    except ValueError as e:
        raise ValueError("Invalid calculation for combinations.") from e

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        n = int(request.form['n'])
        r = int(request.form['r'])

        if n < 0 or r < 0:
            flash("Error: n and r should be non-negative integers.")
            return redirect(url_for('index'))
        elif r > n:
            flash("Error: r cannot be greater than n.")
            return redirect(url_for('index'))
        
        permutations = calculate_permutations(n, r)
        combinations = calculate_combinations(n, r)
        
        flash(f"Permutations P({n}, {r}) = {permutations}")
        flash(f"Combinations C({n}, {r}) = {combinations}")
        return redirect(url_for('index'))

    except ValueError:
        flash("Error: Please enter valid integers for n and r.")
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
