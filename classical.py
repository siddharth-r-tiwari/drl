
import torch
import math
import numpy as np
import pandas as pd
import json

def run_sim(trial_params, model_params):
    def step(t):
        return round(t / dt)

    n_trials = int(trial_params[0])
    trial_types = int(trial_params[1])
    ps = float(trial_params[2])
    t_int = float(trial_params[3])
    dt = float(trial_params[4])
    t_stim = float(trial_params[5])
    t_rew = float(trial_params[6])
    s_rew = float(trial_params[7])

    gamma = float(model_params[0])
    alpha = float(model_params[1])
    lmbda = float(model_params[2])


    # steps
    steps = step(t_int) + 1
    T = np.arange(0, t_int + dt, dt)

    # stimulus
    x = np.zeros((steps, steps))
    x[step(t_stim)-1:, step(t_stim)-1:] = np.eye(steps - step(t_stim) + 1) 

    # reward function (np.zeros(steps))
    r = np.zeros(steps)
    r[step(t_rew)-1] = s_rew

    # weights
    w = np.zeros(steps)

    # Value function
    V = []
    # v = np.zeros(steps)
    # for t in range(steps):
    #     v[t] = np.dot(w, x[:, t])
    # V.append(v.tolist())

    #deltas
    delta_list = []

    for n in range(n_trials):

        # Value function
        v = np.zeros(steps)
        for t in range(steps):
            v[t] = np.dot(w, x[:, t])
        V.append(v.tolist())
        el = np.zeros(steps)

        delta = np.zeros(steps - 1)

        for t in range(steps - 1):
            d = r[t] + gamma * v[t + 1] - v[t]  # calculate delta
            el = lmbda * el + x[:, t]           # eligibility trace
            dw = alpha * d * el
            w = w + dw

            delta[t] = d

        delta_list.append(delta)

    return json.dumps({"t" : T.tolist(), "V": V, "r" : r.tolist()})

