import re
import subprocess
import matplotlib.pyplot as plt
from model import generate_random_problem, generate_problem, write_problem
import subprocess

domain_path = "/home/mp/Desktop/starwars_planning/AI_A3/pythonProject/Planning/test_domain.pddl"
problem_path = "/home/mp/Desktop/starwars_planning/AI_A3/pythonProject/Planning/problem.pddl"
output_path = "/home/mp/Desktop/starwars_planning/AI_A3/pythonProject/Planning/output.txt"
exec_path = "/home/mp/Documents/downward-main/fast-downward.py"

def solve_random(nr):
    pb = generate_random_problem(nr)

    write_problem(pb, "../Planning/problem.pddl")

    command = [
        exec_path,
        domain_path,
        problem_path,
        "--search", "astar(lmcut())"
    ]

    with open(output_path, "w") as output_file:
        subprocess.run(command, stdout=output_file)

    return parse_output()

def parse_output():
    # Read the content of the sas_plan file
    try:
        with open('sas_plan', 'r') as file:
            str_output = file.read()
    except FileNotFoundError:
        str_output = ""


    with open('../Planning/output.txt', 'r') as file:
        content = file.read()


    time_match = re.search(r'Total time:\s*([\d.]+)s', content)
    if time_match:
        total_time = float(time_match.group(1))
    else:
        total_time = None

    return str_output, total_time



def generate_graph():
    # Define the different problem sizes, algorithms
    problem_sizes = [3,4,5,6,7,8,9,10]  # These are the number of droids
    algorithms = [
        "astar(lmcut())",  # Optimal Search: astar(lmcut())
        "eager_greedy([ff()], preferred=[ff()])",  # Fast Non-Optimal Search: eager_greedy([ff()], preferred=[ff()])
        "lazy_greedy([ff()], preferred=[ff()])"  # Fastest Non-Optimal Search: lazy_greedy([ff()], preferred=[ff()])
    ]

    costs = {alg: {size: [] for size in problem_sizes} for alg in algorithms}

    # Loop through each combination of problem size and algorithm
    for nr in problem_sizes:
        for alg in algorithms:
            # Generate random problem for this size
            pb = generate_random_problem(nr)
            write_problem(pb, "../Planning/problem.pddl")

            # Construct the command for the current algorithm and heuristic
            command = [
                exec_path,  # Path to the planner executable
                domain_path,  # Path to the domain file
                problem_path,  # Path to the problem file
                "--search", f"{alg}"
            ]

            # Run the planner and capture the output
            with open(output_path, "w") as output_file:
                subprocess.run(command, stdout=output_file)

            # Parse the output and get the cost
            output_str, total_time = parse_output()

            # Extract cost from the output
            cost_match = re.search(r'cost = (\d+)', output_str)
            if cost_match:
                cost = int(cost_match.group(1))
            else:
                cost = 80

            costs[alg][nr].append(cost)

    plt.figure(figsize=(10, 6))

    for alg in algorithms:
        y_values = [costs[alg][size][0] if costs[alg][size] else None for size in problem_sizes]  # Get the first cost value for each size
        plt.plot(problem_sizes, y_values, label=f"{alg}")

    plt.title("Performance of Algorithms with Different Heuristics")
    plt.xlabel("Number of Droids")
    plt.ylabel("Cost")
    plt.legend(title="Algorithm")
    plt.grid(True)

    graph_path = "../Planning/performance_graph.png"
    plt.savefig(graph_path)

    return graph_path



generate_graph()