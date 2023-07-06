def run_simulation(drl, n_trials, t_int, dt, t_stim, t_rew, s_rew, gamma, alpha, lmbda):
        # Generate the graph data based on the provided parameters\
    if drl:
        x = [i for i in range(n_trials)]
        y = [i * t_int for i in x]
    else:
        x = [i for i in range(n_trials)]
        y = [i * dt for i in x]
        
    data = {'x' : x, 'y' : y}
    
    return data
        