# Orbital-Mechanics-Simulator
A Python-based orbital mechanics simulator using Newtonian gravity and numerical integration to analyze planetary motion, velocity, and energy conservation.

# Orbital Mechanics Simulator

A Python-based orbital mechanics simulator that models the motion of a celestial body under Newtonian gravitational forces.

## Overview

This project simulates the orbital motion of Earth around the Sun using the Velocity Verlet numerical integration method.

It calculates position, velocity, gravitational acceleration, kinetic energy, potential energy, and total mechanical energy over time.

## Features

- Newtonian gravitational acceleration
- Two-dimensional orbital simulation
- Velocity Verlet numerical integration
- Orbital radius and velocity analysis
- Mechanical energy conservation analysis
- CSV data export
- SVG orbital trajectory visualization
- Unit testing

## Physics Concepts

- Newton's Law of Universal Gravitation
- Newton's Second Law of Motion
- Orbital Mechanics
- Kinetic and Gravitational Potential Energy
- Conservation of Mechanical Energy
- Numerical Integration

## Technologies

- Python 3.10+
- math
- csv
- pathlib
- dataclasses
- unittest

No external Python packages are required.


## Installation

Clone the repository:

bash
git clone YOUR_REPOSITORY_URL

Navigate to the project directory:

bash
cd Orbital-Mechanics-Simulator

No additional package installation is needed.

## Usage

Run the simulator:

bash
python main.py

## Run Tests

bash
python -m unittest discover -s tests
`

## Output

The simulator generates:

- `orbital_data.csv` — Numerical simulation results.
- `orbit.svg` — Orbital trajectory visualization.

Both files are saved in the `results` directory.

## Simulation Assumptions

- The Sun is treated as a stationary central body.
- The simulated planet moves in two dimensions.
- Newtonian gravity is assumed.
- Relativistic effects and interactions with other planets are ignored.
- SI units are used throughout the simulation.

## Future Improvements

- Multi-body gravitational simulation
- Interactive orbital visualization
- Comparison of numerical integration methods
- Orbital period estimation
- Energy conservation error analysis
