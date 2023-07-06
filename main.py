import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import simulations

# Function to handle button click event
def plot_graph():
    try:
        drl = drl_var.get()
        n_trials = int(entries['n_trials'].get())
        t_int = float(entries['t_int'].get())
        dt = float(entries['dt'].get())
        t_stim = float(entries['t_stim'].get())
        t_rew = float(entries['t_rew'].get())
        s_rew = float(entries['s_rew'].get())
        gamma = float(entries['gamma'].get())
        alpha = float(entries['alpha'].get())
        lmbda = float(entries['lmbda'].get())
        viz_type = entries['viz_type'].get()

        # Call the simulation function from the separate file and get the generated data
        data = simulations.run_simulation(drl, n_trials, t_int, dt, t_stim, t_rew, s_rew, gamma, alpha, lmbda)

        # Generate the graph using the returned data
        plot_data(data, viz_type)

    except ValueError:
        messagebox.showerror("Error", "Invalid input!")

# Function to plot the graph using matplotlib
def plot_data(data, viz_type):
    x = data['x']
    y = data['y']

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the data
    ax.plot(x, y)

    # Customize the plot
    ax.set_xlabel('Trials')
    ax.set_ylabel('Data')
    ax.set_title('Interactive Graph')

    # Display the graph
    if viz_type == 'Tkinter':
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    else:
        plt.show()

# Create the GUI window
root = tk.Tk()
root.title("Interactive Graph")

# Create labels and entry fields for parameters
labels = ['drl', 'n_trials', 't_int', 'dt', 't_stim', 't_rew', 's_rew', 'gamma', 'alpha', 'lmbda', 'viz_type']
entries = {}
drl_var = tk.IntVar()

for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5)
    if label == 'drl':
        checkbox = tk.Checkbutton(root, variable=drl_var)
        checkbox.grid(row=i, column=1, padx=10, pady=5)
        entries[label] = checkbox
    else:
        entry = tk.Entry(root)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[label] = entry

# Create a button to plot the graph
button = tk.Button(root, text="Plot", command=plot_graph)
button.grid(row=len(labels), columnspan=2, padx=10, pady=5)

# Start the Tkinter event loop
root.mainloop()
