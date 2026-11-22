import csv
from pathlib import Path


def export_to_csv(results, filename):

    if not results:
        raise ValueError("No results to export.")

    output_path = Path(filename)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    fieldnames = [
        "time",
        "x",
        "y",
        "vx",
        "vy",
        "speed",
        "radius",
        "kinetic_energy",
        "potential_energy",
        "total_energy"
    ]

    with open(
        output_path,
        mode="w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for row in results:

            writer.writerow({

                "time": row["time"],

                "x": row["x"],

                "y": row["y"],

                "vx": row["vx"],

                "vy": row["vy"],

                "speed": row["speed"],

                "radius": row["radius"],

                "kinetic_energy": (
                    0.5 * row["mass"] * row["speed"]**2
                ),

                "potential_energy": (
                    row["energy"]
                    - 0.5 * row["mass"] * row["speed"]**2
                ),

                "total_energy": row["energy"]
            })

    print(f"\nCSV file saved: {output_path}")