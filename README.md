# Orbital Mechanics Simulator

A Python-based orbital mechanics simulator that models planetary motion using Newtonian gravity and numerical integration.

# Project Overview

This project simulates the orbital motion of a celestial body around a stationary central mass using the Velocity Verlet integration method.

It calculates position, velocity, gravitational acceleration, kinetic energy, potential energy, and total mechanical energy over time.

The project combines classical mechanics, computational physics, and Python programming.

# Simulation Preview

"Orbital Mechanics Simulation" (results/orbit.svg)

Figure 1. Simulated orbital trajectory of Earth around the Sun.

# Features

- Newtonian gravitational acceleration
- Two-dimensional orbital simulation
- Velocity Verlet numerical integration
- Orbital radius and velocity analysis
- Mechanical energy conservation analysis
- CSV data export
- SVG orbital trajectory visualization
- Unit testing

# Physics Concepts

- Newton's Law of Universal Gravitation
- Newton's Second Law of Motion
- Orbital Mechanics
- Kinetic Energy
- Gravitational Potential Energy
- Conservation of Mechanical Energy
- Numerical Integration

# Technologies

- Python 3.10+
- math
- csv
- pathlib
- dataclasses
- unittest

No external Python packages are required.

# Simulation Configuration and Workflow

The orbital mechanics simulator models the motion of Earth under the gravitational influence of the Sun.

Initial Conditions

The simulation uses the following initial parameters:

- Central Body: Sun
- Orbiting Body: Earth
- Initial Position: 1 AU from the Sun along the x-axis
- Initial Velocity: 98% of the theoretical circular orbital speed
- Time Step: 3600 seconds (1 hour)
- Simulation Duration: 1 year

The initial orbital velocity is calculated using the "circular_orbit_speed()" function, with a scaling factor of 0.98.

Simulation Process

The simulation follows these main steps:

1. Define the initial position and velocity of Earth.
2. Create an Earth object using its physical properties.
3. Initialize the orbital simulator with the Sun's mass and the selected time step.
4. Run the simulation for one year.
5. Analyze the simulation results.
6. Export the numerical data and generate an orbital trajectory plot.

Generated Outputs

The simulator automatically generates the following files in the "results" directory:

- "orbital_data.csv" – Contains the exported simulation data.
- "orbit.svg" – Contains the visualization of the orbital trajectory.

This workflow provides a structured way to simulate planetary motion, analyze the resulting data, and visualize orbital behavior.

# Project Structure

Orbital-Mechanics-Simulator/
│
├── main.py
│
├── src/
│   ├── init.py
│   ├── physics.py
│   ├── simulator.py
│   ├── analysis.py
│   ├── exporter.py
│   └── visualization.py
│
├── tests/
│   ├── init.py
│   └── test_physics.py
│
├── results/
│   └── orbit.svg
│
├── README.md
├── LICENSE
└── .gitignore

# Installation

Clone the repository:

```bash
git clone https://github.com/Ftmzahra-Hassani/Orbital-Mechanics-Simulator.git


Navigate to the project directory:

cd Orbital-Mechanics-Simulator

No additional package installation is required.

# Usage

```markdown
## Usage

Run the simulator:

```bash
python main.py

# Run Tests

```markdown
## Run Tests

Run the test suite using:

```bash
python -m unittest discover -s tests

# Output

The simulator generates:

- "orbital_data.csv" — Numerical simulation data.
- "orbit.svg" — Orbital trajectory visualization.

Both files are saved in the "results" directory.

# Simulation Assumptions

- The Sun is treated as a stationary central body.
- The simulated planet moves in two dimensions.
- Newtonian gravity is assumed.
- Gravitational interactions with other planets are ignored.
- Relativistic effects are not included.
- SI units are used throughout the simulation.

## Energy Conservation Analysis

Energy conservation is an important indicator
of numerical accuracy in orbital mechanics.

The total mechanical energy of an orbiting
system consists of kinetic and gravitational
potential energy.

For a system of two bodies:

- Kinetic Energy:
  E_k = 1/2 * m * v^2

- Gravitational Potential Energy:
  E_p = -G * m1 * m2 / r

- Total Mechanical Energy:
  E_total = E_k + E_p

In an ideal isolated system, total mechanical
energy remains constant over time.

Monitoring energy variations helps evaluate
the accuracy and stability of numerical
integration methods.

# Future Improvements

- Multi-body gravitational simulation (N-Body)
- Interactive orbital visualization
- Comparison of numerical integration methods
- Orbital period estimation
- Improved energy conservation analysis

# License

This project is licensed under the MIT License.
