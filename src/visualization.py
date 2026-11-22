from pathlib import Path
from html import escape


def create_orbit_plot(results, filename):

    if not results:
        raise ValueError("No simulation results.")

    width = 800
    height = 800
    padding = 60

    max_radius = max(
        max(abs(row["x"]), abs(row["y"]))
        for row in results
    )

    scale = (width / 2 - padding) / max_radius

    center_x = width / 2
    center_y = height / 2

    points = []

    for row in results:

        px = center_x + row["x"] * scale

        py = center_y - row["y"] * scale

        points.append(f"{px:.2f},{py:.2f}")

    path_data = " ".join(points)

    svg = f"""
    <svg xmlns="http://www.w3.org/2000/svg"
         width="{width}"
         height="{height}"
         viewBox="0 0 {width} {height}">

        <rect width="100%" height="100%"
              fill="#101827"/>

        <circle cx="{center_x}"
                cy="{center_y}"
                r="8"
                fill="#FFD166"/>

        <text x="{center_x + 15}"
              y="{center_y - 15}"
              fill="white"
              font-size="14">
            Sun
        </text>

        <polyline
            points="{path_data}"
            fill="none"
            stroke="#4CC9F0"
            stroke-width="2"
        />

        <circle
            cx="{center_x + results[-1]['x'] * scale}"
            cy="{center_y - results[-1]['y'] * scale}"
            r="6"
            fill="#EF476F"
        />

        <text x="30" y="35"
              fill="white"
              font-size="20">
            Orbital Mechanics Simulator
        </text>

        <text x="30" y="60"
              fill="#AAB4C3"
              font-size="13">
            Earth orbital trajectory
        </text>

    </svg>
    """

    output_path = Path(filename)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    output_path.write_text(
        svg,
        encoding="utf-8"
    )

    print(f"SVG plot saved: {output_path}")