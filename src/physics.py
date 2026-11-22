import math

# Physical constants
G = 6.67430e-11

M_SUN = 1.989e30
M_EARTH = 5.972e24

AU = 1.496e11
DAY = 86400
YEAR = 365.25 * DAY


def distance(x, y):
    """
    Calculate distance from the origin.
    """
    return math.sqrt(x**2 + y**2)


def gravitational_acceleration(x, y, central_mass):
    """
    Calculate gravitational acceleration.
    """

    r = distance(x, y)

    if r == 0:
        raise ValueError("Distance cannot be zero.")

    factor = -G * central_mass / r**3

    ax = factor * x
    ay = factor * y

    return ax, ay


def gravitational_force(mass, acceleration):
    """
    Calculate gravitational force.
    """

    ax, ay = acceleration

    fx = mass * ax
    fy = mass * ay

    return fx, fy


def kinetic_energy(mass, vx, vy):
    """
    Calculate kinetic energy.
    """

    speed_squared = vx**2 + vy**2

    return 0.5 * mass * speed_squared


def gravitational_potential_energy(mass, central_mass, r):
    """
    Calculate gravitational potential energy.
    """

    if r == 0:
        raise ValueError("Distance cannot be zero.")

    return -G * mass * central_mass / r


def total_energy(mass, central_mass, x, y, vx, vy):

    r = distance(x, y)

    kinetic = kinetic_energy(mass, vx, vy)

    potential = gravitational_potential_energy(
        mass, central_mass, r
    )

    return kinetic + potential


def circular_orbit_speed(central_mass, radius):

    if radius <= 0:
        raise ValueError("Radius must be positive.")

    return math.sqrt(G * central_mass / radius)