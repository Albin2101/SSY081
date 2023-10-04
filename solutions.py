# Question 1

import math as m
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as ss
import scipy.fft as sf

f = 10_000 # Hz
t = 20 # s

# total amount of samples
samples = f * t

samples_convolved = samples + 99

# time for each sample
xvalues=[(t/samples)*n for n in range(samples)]

# time for each convolved sample
# we have to take n-99//2 since the convolution "adds" samples to each side
# so the original timeframe is in the middle, that is 99//2 samples in.
xvalues_convolved=[(t/samples)*(n-(99//2)) for n in range(samples_convolved)]

action_potentials = np.load("./data_files/action_potentials.npy", allow_pickle=True)
# Not sure why [0] is needed, but this works
firing_samples = np.load("./data_files/firing_samples.npy", allow_pickle=True)[0]

# Signal which is 1 when there is a sample
impulses = np.array([[0]*samples]*8, dtype='float')

for n in range(8):
    for index in firing_samples[n]:
        impulses[n][index] = 1

# Actual action trains
action_trains = np.array([[0]*samples_convolved]*8, dtype='float')

# 1a)

# Calculated through convolution
#   impulses is a sum of impulses at each instance where there is a action potential
#   so we can use the convolution which will "paste" the action potential at each impulse
for n in range(8):
    action_trains[n] = ss.fftconvolve(impulses[n], action_potentials[n], mode='full')


#setting up the plots to check correctness

figure, axis = plt.subplots(8,3)
for n in range(8):
  axis[n,0].plot(xvalues_convolved, action_trains[n])
  axis[n,1].plot(xvalues, impulses[n])
  axis[n,2].plot(action_potentials[n])

  axis[n,0].axis([0,0.2,-100,100])
  axis[n,1].axis([0,0.2,-2,2])

plt.show()


# 1c)
plt.plot(xvalues_convolved, action_trains[0])
plt.title("Action train 1 (index 0)")
plt.xlabel("seconds")
plt.ylabel("A.U")
plt.show()

plt.plot(xvalues_convolved, action_trains[0])
plt.title("Action train 1 (index 0)")
plt.xlabel("seconds")
plt.ylabel("A.U")
plt.axis([10,10.5,-100,100])
plt.show()

# 1e)

emg_signal = np.array([0]*samples_convolved, dtype='float')
for n in range(8):
    emg_signal += action_trains[n]


plt.plot(xvalues_convolved, emg_signal)
plt.title("EMG Signal")
plt.xlabel("seconds")
plt.ylabel("A.U")
plt.axis([10,10.5,-200,200])
plt.show()

# 2a)

hanning_samples = f # amount of samples in one second

hanning = np.hanning(hanning_samples)

hanning_convolved_samples = samples + hanning_samples - 1

xvalues_hanning_convolved=[(t/samples)*(n-(hanning_samples//2)) for n in range(hanning_convolved_samples)]

filtered_impulses = np.array([[0]*hanning_convolved_samples]*8, dtype='float')

for n in range(8):
    filtered_impulses[n] = ss.fftconvolve(impulses[n], hanning, mode='full')

# 2b)
figure, axis = plt.subplots(8)

#plotting the filtered impulse
for n in range(8):
  axis[n].plot(xvalues_hanning_convolved, filtered_impulses[n])
  axis[n].axis([-2,22,0,10])
  axis[n].set_title(f"filtered impulse #{n+1}")
  axis[n].set_xlabel("seconds")
  axis[n].set_ylabel("A.U")
plt.show()

# 2c)

# comparing with and without filtering

figure, axis = plt.subplots(2)

axis[0].plot(xvalues, impulses[3])
axis[0].axis([-2,22,0,1.5])
axis[0].set_title("unfiltered impulse #1")
axis[0].set_xlabel("seconds")
axis[0].set_ylabel("A.U")

axis[1].plot(xvalues_hanning_convolved, filtered_impulses[0])
axis[1].axis([-2,22,0,10])
axis[1].set_title("filtered impulse #1")
axis[1].set_xlabel("seconds")
axis[1].set_ylabel("A.U")
plt.show()

# 2d)

figure, axis = plt.subplots(2)

axis[0].plot(xvalues, impulses[6])
axis[0].axis([-2,22,0,1.5])
axis[0].set_title("unfiltered impulse #8")
axis[0].set_xlabel("seconds")
axis[0].set_ylabel("A.U")

axis[1].plot(xvalues_hanning_convolved, filtered_impulses[7])
axis[1].axis([-2,22,0,10])
axis[1].set_title("filtered impulse #8")
axis[1].set_xlabel("seconds")
axis[1].set_ylabel("A.U")

plt.show()

# 3a)

f = 1024 # Hz
t = 1 # s
interference_frequency = 50 # Hz
samples = f * t # amount of samples

xvalues = [n*(t/samples) for n in range(samples)]

surface_emg = np.load("./data_files/f.npy", allow_pickle=True)[0]

# sinus is very pretty :D <3
interference = np.array([0.2*m.sin(2*m.pi*interference_frequency*t) for t in xvalues], dtype='float')

result_emg = np.add(surface_emg, interference)

surface_emg_freq_domain = sf.fft(surface_emg)
surface_emg_freq_domain = np.abs(surface_emg_freq_domain[:len(surface_emg_freq_domain)//2])
result_emg_freq_domain = sf.fft(result_emg)
result_emg_freq_domain = np.abs(result_emg_freq_domain[:len(result_emg_freq_domain)//2])

# xvalues range from 0Hz to 512Hz (our sampling frequency / 2, shoutouts nyquist)
xvalues_freq_domain = [(f*n)/samples for n in range(samples // 2)]

plt.plot(xvalues_freq_domain, result_emg_freq_domain, color='red', label='With Interference')
plt.plot(xvalues_freq_domain, surface_emg_freq_domain, color='blue', label='No Interference')
plt.title("Frequency domain plots")
plt.xlabel("Hz")
plt.ylabel("A.U")
plt.legend()

plt.show()