import numpy as np
from scipy.fft import fft
import math
import matplotlib.pyplot as plt


def cart2pol(x, y):
    # converts cartesian coordinates to polar coordinates
    theta = np.arctan2(y, x)
    rho = np.sqrt(x**2 + y**2)
    return [theta, rho]


def main():
    # textbook implementation
    # from your textbook Bandwidth = 100/pi = 31.8310 Hz
    T = 0.015625    # 1 / 64
    T0 = 4
    N0 = T0 / T     # 256

    t = np.arange(0, T * (N0 - 1) + T, step=T)
    f = T * np.exp(-2*t)

    F = fft(f)
    [Fp, Fm] = cart2pol(F.real, F.imag)
    k = np.arange(0, N0, step=1)
    w = 2 * math.pi * k / T0

    fig, axs = plt.subplots(2)
    axs[0].plot(w[0:int(N0/2)], Fm[0:int(N0/2)], linewidth=0.5)
    axs[0].set_ylabel('|F| [a.u.]')
    axs[0].set_xlabel('Angular frequency [rad/s]')
    axs[0].set_xlim(0, 200)
    axs[1].plot(w[0:int(N0/2)], np.rad2deg(Fp[0:int(N0/2)]), linewidth=0.5)
    axs[1].set_xlabel('Angular frequency [rad/s]')
    axs[1].set_ylabel('∠ F [rad]')
    axs[1].set_xlim(0, 200)
    plt.tight_layout()

    fig, axs = plt.subplots(2)
    axs[0].plot(w[0:int(N0 / 2)], Fm[0:int(N0 / 2)], linewidth=0.5)
    axs[0].plot(w[0:int(N0 / 2)], Fm[0:int(N0 / 2)], 'ro', linewidth=0.5)
    axs[0].set_xlabel('Angular frequency [rad/s]')
    axs[0].set_ylabel('|F| [a.u.]')
    axs[0].set_xlim(0, 40)
    axs[1].plot(w[0:int(N0 / 2)], np.rad2deg(Fp[0:int(N0 / 2)]), linewidth=0.5)
    axs[1].plot(w[0:int(N0 / 2)], np.rad2deg(Fp[0:int(N0 / 2)]), 'ro', linewidth=0.5)
    axs[1].set_xlabel('Angular frequency [rad/s]')
    axs[1].set_ylabel('∠ F [rad]')
    axs[1].set_xlim(0, 40)
    plt.tight_layout()

    # Silvia's implementation
    # from your textbook Bandwidth = 100 / pi = 31.8310 Hz
    fsamp = 64
    N0 = 256

    T0 = 4
    t2 = np.arange(0, T0, step=1/fsamp)
    f2 = 1/fsamp*np.exp(-2*t2)

    F2 = fft(f2)
    amplitude = abs(F2)
    phase = np.arctan2(F2.imag, F2.real)

    k = np.arange(0, N0, step=1)
    f_axis = k / T0     # in this way you get the axis in Hz
    w_axis = 2 * math.pi * k / T0   # in this way you get the axis in rad/s as in your textbook

    fig, axs = plt.subplots(2)
    # axs[0].plot(f_axis, amplitude, linewidth=0.5)
    axs[0].plot(f_axis[0:int(N0/2)], amplitude[0:int(N0/2)], linewidth=0.5)
    axs[0].set_xlabel('Frequency [Hz]')
    axs[0].set_ylabel('|F| [a.u.]')
    axs[0].set_xlim(0, 35)

    # axs[1].plot(f_axis, phase, linewidth=0.5)
    axs[1].plot(f_axis[0:int(N0/2)], phase[0:int(N0/2)], linewidth=0.5)
    axs[1].set_xlabel('Frequency [Hz]')
    axs[1].set_ylabel('∠ F [rad]')
    axs[1].set_xlim(0, 35)
    plt.tight_layout()

    fig, axs = plt.subplots(2)
    axs[0].plot(w_axis[0:int(N0/2)], amplitude[0:int(N0/2)], linewidth=0.5)
    axs[0].set_xlabel('Angular frequency [rad/s]')
    axs[0].set_ylabel('|F| [a.u.]')
    axs[0].set_xlim(0, 40)

    axs[1].plot(w_axis[0:int(N0/2)], phase[0:int(N0/2)], linewidth=0.5)
    axs[1].set_xlabel('Angular frequency [rad/s]')
    axs[1].set_ylabel('∠ F [rad]')
    axs[1].set_xlim(0, 40)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
