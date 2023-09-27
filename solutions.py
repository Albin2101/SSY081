# Question 1

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as ss

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
impulses = np.array([[0]*samples]*8)

for n in range(8):
    for index in firing_samples[n]:
        impulses[n][index] = 1

# Actual action trains
action_trains = np.array([[0]*samples_convolved]*8)

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

emg_signal = np.array([0]*samples_convolved)
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

filtered_impulses = np.array([[0]*hanning_convolved_samples]*8)

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

axis[0].plot(xvalues, impulses[0])
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

axis[0].plot(xvalues, impulses[7])
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