from dataclasses import dataclass

from src.physics import (gravitational_acceleration,total_energy,distance)


@dataclass
class Body:
    name: str
    mass: float
    x: float
    y: float
    vx: float
    vy: float


class OrbitalSimulator:

    def __init__(self, body, central_mass, dt):

        if dt <= 0:
            raise ValueError("Time step must be positive.")

        if body.mass <= 0 or central_mass <= 0:
            raise ValueError("Masses must be positive.")

        self.body = body
        self.central_mass = central_mass
        self.dt = dt

    def simulate(self, duration):

        if duration <= 0:
            raise ValueError("Duration must be positive.")

        steps = int(duration / self.dt)

        if steps < 1:
            raise ValueError("Duration must be at least one time step.")

        dt = self.dt
        body = self.body

        x = body.x
        y = body.y

        vx = body.vx
        vy = body.vy

        results = []

        for step in range(steps + 1):

            current_time = step * dt

            radius = distance(x, y)

            speed = (vx**2 + vy**2) ** 0.5

            energy = total_energy(
                body.mass,
                self.central_mass,
                x, y, vx, vy
            )

            results.append({"time": current_time,"x": x,"y": y,"vx": vx,"vy": vy,"speed": speed,"radius": radius,"energy": energy, "mass": body.mass})

            if step == steps:
                break

            # Initial acceleration
            ax, ay = gravitational_acceleration(
                x, y, self.central_mass
            )

            # Update position
            new_x = x + vx * dt + 0.5 * ax * dt**2
            new_y = y + vy * dt + 0.5 * ay * dt**2

            # New acceleration
            new_ax, new_ay = gravitational_acceleration(
                new_x, new_y, self.central_mass
            )

            # Update velocity
            new_vx = vx + 0.5 * (ax + new_ax) * dt
            new_vy = vy + 0.5 * (ay + new_ay) * dt

            x = new_x
            y = new_y

            vx = new_vx
            vy = new_vy

        return results