import torch
import math
import numpy as np
import pandas as pd

def run_sim(trial_params, model_params):
    dt = np.arange(float(trial_params[0]), 10, 0.25).tolist()
    result = {'x': dt, 'y': [v * float(trial_params[2]) for v in range(len(dt))]}
    return json.dumps(result)