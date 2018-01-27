# -*- coding: utf-8 -*-
"""1-D linear_convection.py
u^n+1_i \frac{i}{n+1} = u^n_i - c \frac {dt}{dx} (u^n_i - u^n_i-1)
"""
import numpy as np
from matplotlib import pyplot as plt


def main():
    sample(41)
    sample(81)


def sample(num_of_x):
    dt, num_of_timestep = .025, 25
    c = 1  # wavespeed

    xs = np.linspace(0, 2, num_of_x)
    dx = 2 / (num_of_x - 1)

    u = calc1(num_of_x, dx)
    plt.plot(xs, u)

    u = calc2(u, c, num_of_x, dx, num_of_timestep, dt)
    plt.plot(xs, u)


def calc1(num_of_x, dx):
    """setting u = 2 between 0.5 and 1 as per our I.C.s"""
    u = np.ones(num_of_x)
    u[int(.5 / dx):int(1 / dx + 1)] = 2
    return u


def calc2(u, c, num_of_x, dx, num_of_timestep, dt):
    un = np.ones(num_of_x)
    for _ in range(num_of_timestep):
        un = u.copy()
        u[1:num_of_x] = un[1:num_of_x] - c * dt / dx * (un[1:num_of_x] - un[0:num_of_x - 1])
    return u


if __name__ == '__main__':
    main()
