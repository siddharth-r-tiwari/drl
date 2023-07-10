
import torch
import math
import numpy as np
import pandas as pd
import json


def run_sim(trial_params, model_params):
    result = {'x': [float(v) + 1 for v in trial_params], 'y': [float(v) + 4 for v in trial_params]}
    return json.dumps(result)