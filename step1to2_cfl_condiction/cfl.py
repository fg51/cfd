# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt


def main():
    linear_conv(41)
    linear_conv(61)
    linear_conv(71)
    linear_conv(85)


def linear_conv(nx: int):
    dx = 2 / (nx - 1)
    nt = 20    # nt is the number of timesteps we want to calculate
    dt = .025  # dt is the amount of time each timestep covers (delta t)
    c = 1

    u = np.ones(nx)  # defining a numpy array which is nx elements long with every value equal to 1.
    u[int(.5 / dx):int(1 / dx + 1)] = 2  # setting u = 2 between 0.5 and 1 as per our I.C.s

    un = np.ones(nx)

    for _ in range(nt):  # iterate through time
        un = u.copy()
        for i in range(1, nx):
            u[i] = un[i] - c * dt / dx * (un[i] - un[i - 1])
    return u

    plt.plot(np.linspace(0, 2, nx), u)
    plt.show()
    plt.close()


def linearconv2(nx):
    dx = 2 / (nx - 1)
    nt = 20
    c = 1
    sigma = .5

    dt = sigma * dx

    u = np.ones(nx)
    u[int(.5 / dx):int(1 / dx + 1)] = 2

    un = np.ones(nx)

    for _ in range(nt):  # iterate through time
        un = u.copy()  # copy the existing values of u into un
        for i in range(1, nx):
            u[i] = un[i] - c * dt / dx * (un[i] - un[i - 1])

    plt.plot(np.linspace(0, 2, nx), u)


if __name__ == '__main__':
    main()
