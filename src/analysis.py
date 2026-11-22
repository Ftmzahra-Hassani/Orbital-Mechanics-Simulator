def analyze_simulation(results):

    if not results:
        raise ValueError("Simulation results are empty.")

    radii = [row["radius"] for row in results]

    speeds = [row["speed"] for row in results]

    energies = [row["energy"] for row in results]

    initial_energy = energies[0]

    final_energy = energies[-1]

    if initial_energy == 0:
        energy_error = None
    else:
        energy_error = (
            abs(final_energy - initial_energy)
            / abs(initial_energy)
        ) * 100

    summary = {

        "total_steps": len(results) - 1,

        "initial_radius": radii[0],

        "minimum_radius": min(radii),

        "maximum_radius": max(radii),

        "maximum_speed": max(speeds),

        "initial_energy": initial_energy,

        "final_energy": final_energy,

        "energy_error_percent": energy_error
    }

    return summary


def print_analysis(summary):

    print("\n" + "=" * 45)

    print("       ORBITAL SIMULATION ANALYSIS")

    print("=" * 45)

    print(f"Total Steps: {summary['total_steps']}")

    print(
        f"Initial Radius: "
        f"{summary['initial_radius']:.3e} m"
    )

    print(
        f"Minimum Radius: "
        f"{summary['minimum_radius']:.3e} m"
    )

    print(
        f"Maximum Radius: "
        f"{summary['maximum_radius']:.3e} m"
    )

    print(
        f"Maximum Speed: "
        f"{summary['maximum_speed']:.3f} m/s"
    )

    print(
        f"Initial Energy: "
        f"{summary['initial_energy']:.3e} J"
    )

    print(
        f"Final Energy: "
        f"{summary['final_energy']:.3e} J"
    )

    if summary["energy_error_percent"] is not None:

        print(
            f"Energy Error: "
            f"{summary['energy_error_percent']:.8f}%"
        )

    print("=" * 45)