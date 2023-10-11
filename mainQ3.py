import math as m
import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as sf

# 3a)

f = 1024 # Hz
t = 1 # s
interference_frequency = 50 # Hz
samples = f * t # amount of samples

xvalues = [n*(t/samples) for n in range(samples)]

surface_emg = np.load("./data_files/f.npy", allow_pickle=True)[0]

# a clear sinus wave, used for interference
interference = np.array([0.2*m.sin(2*m.pi*interference_frequency*t) for t in xvalues], dtype='float')

result_emg = np.add(surface_emg, interference)

# switching to frequency domain, keeping half
surface_emg_freq_domain = sf.fft(surface_emg)
surface_emg_freq_domain = np.abs(surface_emg_freq_domain[:len(surface_emg_freq_domain)//2])
result_emg_freq_domain = sf.fft(result_emg)
result_emg_freq_domain = np.abs(result_emg_freq_domain[:len(result_emg_freq_domain)//2])

# xvalues range from 0Hz to 512Hz (our sampling frequency / 2, shoutouts nyquist)
xvalues_freq_domain = [(f*n)/samples for n in range(samples // 2)]

plt.plot(xvalues_freq_domain, result_emg_freq_domain, color='red', label='With Interference')
plt.plot(xvalues_freq_domain, surface_emg_freq_domain, color='blue', label='No Interference')
plt.title("Frequency domain plots")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude [A.U]")
plt.legend()

plt.show()
