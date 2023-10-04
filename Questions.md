# Questions

## Problem 1

### a)

For a specific unit we take the firing times of that unit and create a signal which is always 0, except for the time-points where there is a firing, where the signal is one. This is a sum of discrete impulses (dirac delta). In order to have a action train at each impulse we may simply convolve the sum of impulses with the action train. Since a shifted impulse convoluted with a signal simply shifts the other signal, and the convolution distributes over addition, the result is that we get a sum of our action trains shifted to each firing point.

### b)

200_099 since the amount of samples is 200_000, and the action train is 100 samples and the discrete convolution on inputs of size N, M produces an output of size N+M-1, which is a well known property of the discrete convolution.

### d)

When calculating the time of the original samples we said that sample n occurs at time (time/#samples)\*n, that is (20/200000)\*n, but for the convoluted signal there are 99 more samples, which are added to each side. Therefore the time of sample n is now (time/#samples)\*(n-99/2), as time 0 is after the first 99/2 samples which end up on the left side of the original signal.

## Problem 2

### d)

Unit 7 fires faster, we can see that the amplitude of the graph for unit 7 has an amplitude around 7.5, while unit 4 has an amplitude hovering around 5. The amplitude being higher implies a higher frequency, as the impulses being tightly together means more windows in the convolution will "overlap" and add up at that point.

## Problem 3

### b)

There is a huge peak in the signal with interference at f=50Hz, which is to be expected since we added a pure 50Hz sine wave as interference. :P
