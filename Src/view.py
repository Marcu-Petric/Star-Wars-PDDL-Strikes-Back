import tkinter as tk
from tkinter import messagebox
from controller import solve_random, generate_graph, solve_problem

# Function to generate random problem

def display_prob(problem, str_output, total_time):
    # Create a new window to display the result
    result_window = tk.Toplevel()  # This creates a new top-level window
    result_window.title("Random Problem Output")

    # Create a label for the string output
    output_label = tk.Label(result_window, text=problem + "\n\n\n\n" + str_output, font=("Arial", 12), justify="left")
    output_label.pack(padx=20, pady=10)

    # Create a label for the total time (larger font)
    time_label = tk.Label(result_window, text=f"Total Time: {total_time} seconds", font=("Arial", 18, "bold"), fg="red")
    time_label.pack(padx=20, pady=10)

    # Start the Tkinter event loop
    result_window.mainloop()

def generate_random():
    nr_of_droids = int(droid_count_entry.get())

    prob, stri, out = solve_random(nr_of_droids)
    display_prob(prob, stri, out)


def create_problem():
    # Get the number of droids
    nr_of_droids = int(droid_count_entry.get())

    # Create a new window for input
    problem_window = tk.Toplevel()
    problem_window.title("Create Problem")

    # Create labels and input fields for each droid
    labels = []
    name_entries = []
    loc_entries = []
    home_entries = []

    for i in range(nr_of_droids):
        # Droid name, location, and home
        label = tk.Label(problem_window, text=f"Droid {i+1}:")
        label.grid(row=i, column=0, padx=5, pady=5)
        labels.append(label)

        name_entry = tk.Entry(problem_window)
        name_entry.grid(row=i, column=1, padx=5, pady=5)
        name_entries.append(name_entry)

        loc_entry = tk.Entry(problem_window)
        loc_entry.grid(row=i, column=2, padx=5, pady=5)
        loc_entries.append(loc_entry)

        home_entry = tk.Entry(problem_window)
        home_entry.grid(row=i, column=3, padx=5, pady=5)
        home_entries.append(home_entry)

    # Create an entry for the planet location
    planet_label = tk.Label(problem_window, text="Planet Location:")
    planet_label.grid(row=nr_of_droids, column=0, padx=5, pady=5)
    planet_entry = tk.Entry(problem_window)
    planet_entry.grid(row=nr_of_droids, column=1, padx=5, pady=5)

    # Define the solve function to process the problem
    def solve():
        # Create a dictionary with the droid information
        droids_info = []
        for i in range(nr_of_droids):
            droid_name = name_entries[i].get()
            droid_loc = loc_entries[i].get()
            droid_home = home_entries[i].get()
            droids_info.append((droid_name, droid_loc, droid_home))

        # Get the planet location
        planet_loc = planet_entry.get()

        # Call the solve_problem function with the ship and droids
        prob, stri, out = solve_problem(planet_loc, droids)
        display_prob(prob, stri, out)

        # Close the problem window after solving
        problem_window.destroy()

    # Add a "Solve" button
    solve_button = tk.Button(problem_window, text="Solve", command=solve)
    solve_button.grid(row=nr_of_droids + 1, column=0, columnspan=4, pady=10)

    # Start the problem window loop
    problem_window.mainloop()

# Function to create the graph (Placeholder)
def create_graph():
    generate_graph()

# Function to create the entire view
def create_view():
    # Initialize the main window
    root = tk.Tk()
    root.title("Star Wars Planning")

    root.config(bg="black")

    # Create a large title for the window
    title_label = tk.Label(root, text="STAR WARS", font=("Helvetica", 48, "bold"), fg="gold", bg="black")
    title_label.pack(pady=20)  # Add some space above the title

    # Label and entry for the number of droids
    droid_count_label = tk.Label(root, text="Enter number of droids (1-50):")
    droid_count_label.pack()

    global droid_count_entry
    droid_count_entry = tk.Entry(root)
    droid_count_entry.pack()

    # Button to generate random problem
    generate_button = tk.Button(root, text="Generate Random", command=generate_random)
    generate_button.pack()

    # Button to create problem (go to another page)
    create_problem_button = tk.Button(root, text="Create Problem", command=create_problem)
    create_problem_button.pack()

    # Button to create graph
    create_graph_button = tk.Button(root, text="Create Graph", command=create_graph)
    create_graph_button.pack()

    # Start the GUI event loop
    root.mainloop()

# Call the function to display the view
if __name__ == "__main__":
    create_view()
