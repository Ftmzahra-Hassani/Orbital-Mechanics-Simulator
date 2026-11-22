from pathlib import Path

from src.physics import (
    G,
    M_SUN,
    M_EARTH,
    AU,
    YEAR,
    circular_orbit_speed
)

from src.simulator import Body, OrbitalSimulator

from src.analysis import (
    analyze_simulation,
    print_analysis
)

from src.exporter import export_to_csv

from src.visualization import create_orbit_plot


def main():

    print("=" * 45)

    print("       ORBITAL MECHANICS SIMULATOR")

    print("=" * 45)

    # Initial conditions

    initial_x = AU
    initial_y = 0.0

    circular_speed = circular_orbit_speed(
        M_SUN,
        AU
    )

    initial_vx = 0.0

    initial_vy = circular_speed * 0.98

    # Create Earth

    earth = Body(

        name="Earth",

        mass=M_EARTH,

        x=initial_x,

        y=initial_y,

        vx=initial_vx,

        vy=initial_vy
    )

    # Create simulator

    time_step = 3600

    simulator = OrbitalSimulator(

        body=earth,

        central_mass=M_SUN,

        dt=time_step
    )

    print("\nStarting simulation...")

    # Run simulation

    results = simulator.simulate(YEAR)

    print("Simulation completed.")

    # Analyze results

    summary = analyze_simulation(results)

    print_analysis(summary)

    # Output directory

    project_path = Path(__file__).resolve().parent

    results_path = project_path / "results"

    # Export CSV

    export_to_csv(
        results,
        results_path / "orbital_data.csv"
    )

    # Generate SVG

    create_orbit_plot(
        results,
        results_path / "orbit.svg"
    )

    print("\nAll operations completed successfully.")


if __name__ == "__main__":

    main()