from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import classical, distributional
import threading

app = Flask(__name__)
app.secret_key = 'SLDKFKJLSKFJDLSDKFJLSDKFKJlj'
#app.config['SERVER_NAME'] = '127.0.0.1:5000'

params = {
    'classical_rl': {
        'trial_params' : [
        'Number of Trials',
        'Number of Trial Types',
        'Trial Switch Probabilities',
        'Length of Trial',
        'Timestep Size (dt)',
        'Time of Stimulus',
        'Time of Reward',
        'Size of Reward'
        ],
        'model_params' : [
            'Gamma',
            'Alpha',
            'Lambda'
        ]
    },
    'distributional_rl': {
        'trial_params' : [
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
        'model_params' : [
            'Gamma',
            'Alpha',
            'Lambda'
        ]
    }
}

#def run_simulation(trial_params, model_params, learning_type):
 #   with app.app_context():
        
            # Process the simulation results as needed

        # Store the results in a file or perform any other necessary actions

        # Redirect to the visualizations page once the simulation is completed
#        return redirect(url_for('visualizations'))

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

     # Start a new thread to run the simulation
     #thread = threading.Thread(target=run_simulation, args=(trial_params, model_params, learning_type))
     #thread.start()

     #return render_template('loading.html')
    if learning_type == "classical_rl":
        vals = classical.run_sim(trial_params, model_params)
             # Process the simulation results as needed

    elif learning_type == "distributional_rl":
        vals = distributional.run_sim(trial_params, model_params)

    return render_template('visualizations.html')

if __name__ == '__main__':
    app.run(debug=True)