Orbital Mechanics Simulator

A Python-based orbital mechanics simulator that models planetary motion using Newtonian gravity and numerical integration.

Project Overview

This project simulates the orbital motion of a celestial body around a stationary central mass using the Velocity Verlet integration method.

It calculates position, velocity, gravitational acceleration, kinetic energy, potential energy, and total mechanical energy over time.

The project combines classical mechanics, computational physics, and Python programming.

Simulation Preview

"Orbital Mechanics Simulation" (results/orbit.svg)

Figure 1. Simulated orbital trajectory of Earth around the Sun.

Features

- Newtonian gravitational acceleration
- Two-dimensional orbital simulation
- Velocity Verlet numerical integration
- Orbital radius and velocity analysis
- Mechanical energy conservation analysis
- CSV data export
- SVG orbital trajectory visualization
- Unit testing

Physics Concepts

- Newton's Law of Universal Gravitation
- Newton's Second Law of Motion
- Orbital Mechanics
- Kinetic Energy
- Gravitational Potential Energy
- Conservation of Mechanical Energy
- Numerical Integration

Technologies

- Python 3.10+
- math
- csv
- pathlib
- dataclasses
- unittest

No external Python packages are required.

Project Structure

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

Installation

Clone the repository:

git clone https://github.com/Ftmzahra-Hassani/Orbital-Mechanics-Simulator.git

Navigate to the project directory:

cd Orbital-Mechanics-Simulator

No additional package installation is required.

Usage

Run the simulator:

python main.py

Run Tests

Execute the unit tests:

python -m unittest discover -s tests -t .

Output

The simulator generates:

- "orbital_data.csv" — Numerical simulation data.
- "orbit.svg" — Orbital trajectory visualization.

Both files are saved in the "results" directory.

Simulation Assumptions

- The Sun is treated as a stationary central body.
- The simulated planet moves in two dimensions.
- Newtonian gravity is assumed.
- Gravitational interactions with other planets are ignored.
- Relativistic effects are not included.
- SI units are used throughout the simulation.

Future Improvements

- Multi-body gravitational simulation (N-Body)
- Interactive orbital visualization
- Comparison of numerical integration methods
- Orbital period estimation
- Improved energy conservation analysis

License

This project is licensed under the MIT License.
