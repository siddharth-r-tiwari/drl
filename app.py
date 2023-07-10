from flask import Flask, render_template, request, session, jsonify
import classical, distributional

app = Flask(__name__)
app.secret_key = 'SLDKFKJLSKFJDLSDKFJLSDKFKJlj'

params = {
    'classical_rl': {
        'trial_params': [
            'Number of Trials',
            'Number of Trial Types',
            'Trial Switch Probabilities',
            'Length of Trial',
            'Timestep Size (dt)',
            'Time of Stimulus',
            'Time of Reward',
            'Size of Reward'
        ],
        'model_params': [
            'Gamma',
            'Alpha',
            'Lambda'
        ]
    },
    'distributional_rl': {
        'trial_params': [
            'Number of Trials',
            'Number of Trial Types',
            'Trial Switch Probabilities',
            'Number of Value Predictors',
            'Length of Trial',
            'Timestep Size (dt)',
            'Time of Stimulus',
            'Time of Reward',
            'Size of Reward'
        ],
        'model_params': [
            'Gamma',
            'Alpha',
            'Lambda'
        ]
    }
}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            session['learning_type'] = request.form['learning_type']
            return render_template('params.html', learning_type=session['learning_type'], params=params[session['learning_type']])
        except:
            return render_template("invalid.html")
    else:
        return render_template('index.html')


@app.route('/process_params', methods=['POST'])
def process_params():
    trial_params = request.form.getlist('trial_params')
    model_params = request.form.getlist('model_params')
    learning_type = session.get('learning_type')
    if any(val == '' for val in trial_params) or any(val == '' for val in model_params):
        return render_template('invalid.html')

    if learning_type == "classical_rl":
        vals = classical.run_sim(trial_params, model_params)
    elif learning_type == "distributional_rl":
        vals = distributional.run_sim(trial_params, model_params)
    else:
        return "No learning type selected."

    return render_template('visualizations.html', vals=vals)


if __name__ == '__main__':
    app.run(debug=True)
