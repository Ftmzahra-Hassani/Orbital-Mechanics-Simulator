import unittest
import math

from src.physics import (
    G,
    AU,
    M_SUN,
    gravitational_acceleration,
    kinetic_energy,
    gravitational_potential_energy,
    circular_orbit_speed
)

from src.simulator import Body, OrbitalSimulator


class TestPhysics(unittest.TestCase):

    def test_gravitational_acceleration(self):

        ax, ay = gravitational_acceleration(
            AU,
            0,
            M_SUN
        )

        expected = -G * M_SUN / AU**2

        self.assertAlmostEqual(ax, expected)

        self.assertAlmostEqual(ay, 0)

    def test_kinetic_energy(self):

        energy = kinetic_energy(
            2,
            3,
            4
        )

        self.assertAlmostEqual(energy, 25)

    def test_potential_energy_is_negative(self):

        energy = gravitational_potential_energy(
            1,
            M_SUN,
            AU
        )

        self.assertLess(energy, 0)

    def test_circular_orbit_speed(self):

        speed = circular_orbit_speed(
            M_SUN,
            AU
        )

        expected = math.sqrt(
            G * M_SUN / AU
        )

        self.assertAlmostEqual(speed, expected)

    def test_simulation_produces_results(self):

        speed = circular_orbit_speed(
            M_SUN,
            AU
        )

        earth = Body(
            name="Earth",
            mass=5.972e24,
            x=AU,
            y=0,
            vx=0,
            vy=speed
        )

        simulator = OrbitalSimulator(
            body=earth,
            central_mass=M_SUN,
            dt=3600
        )

        results = simulator.simulate(7200)

        self.assertEqual(len(results), 3)

        self.assertGreater(
            results[-1]["radius"],
            0
        )


if __name__ == "__main__":

    unittest.main()