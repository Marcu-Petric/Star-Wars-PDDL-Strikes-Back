import random
from os import write
from Src.config import all_planets, all_droids


def generate_random_problem(nr_of_droids):
    # Randomly select the ship location from the list of planets
    ship_location = random.choice(all_planets)

    droids_info = []

    selected_droids = random.sample(all_droids, nr_of_droids)
    for droid in selected_droids:
        droid_location = random.choice(all_planets)
        while droid_location == ship_location:
            droid_location = random.choice(all_planets)
        droid_home = random.choice(all_planets)
        while droid_home == droid_location:
            droid_home = random.choice(all_planets)

        droids_info.append((droid, droid_location, droid_home))

    return generate_problem(ship_location, droids_info)


def generate_problem(ship_location, droids_info):
    """
    Function to generate a PDDL problem file based on the input parameters.

    :param ship_location: The starting location of the spaceship.
    :param droids_info: A list of tuples where each tuple contains:
        - droid_name (str): Name of the droid (e.g., "r2d2")
        - droid_location (str): Current location of the droid (e.g., "tatooine")
        - droid_home (str): Target location for the droid (e.g., "dagobah")
    :param problem_file_path: Path to save the generated problem.pddl (default: "Planning/problem.pddl").
    """

    # Define constants (planets and droids)
    planets = set()
    droids = set()

    for droid_name, droid_location, droid_home in droids_info:
        planets.add(droid_location)
        planets.add(droid_home)
        droids.add(droid_name)

    planets.add(ship_location)  # Add the spaceship's location to the planets set

    problem_str = f"(define (problem starwars-delivery)\n"
    problem_str += f"   (:domain starwars-transport)\n"

    # Define the objects (planets and droids)
    problem_str += "   (:objects\n       "
    for planet in planets:
        problem_str += f"{planet} "
    for droid in droids:
        problem_str += f"{droid} "
    problem_str += ")\n"

    # Define the initial conditions
    problem_str += "   (:init\n"
    for planet in planets:
        problem_str += f"      (planet {planet})\n"
    for droid in droids:
        problem_str += f"      (droid {droid})\n"
    problem_str += f"      (ship-at {ship_location})\n"
    problem_str += f"      (ship-free)\n"
    for droid_name, droid_location, _ in droids_info:
        problem_str += f"      (droid-at {droid_name} {droid_location})\n"
    problem_str += "   )\n"

    # Define the goal conditions
    problem_str += "   (:goal\n"
    problem_str += "      (and\n"
    for droid_name, _, droid_home in droids_info:
        problem_str += f"         (droid-at {droid_name} {droid_home})\n"
    problem_str += "      )\n"
    problem_str += "   )\n"

    problem_str += ")\n"

    return problem_str

def write_problem(problem, path):
    # Write to problem file
    with open(path, "w") as problem_file:
        problem_file.write(problem)

# Example usage:
droids_i = [
    ("r2d2", "tatooine", "dagobah"),
    ("c3po", "hoth", "dagobah")
]
pb = generate_random_problem(12)
write_problem(pb, "../Planning/problem.pddl")