import time
start_time = time.time()

import numpy as np
from scipy.io import wavfile
from scipy import signal
import matplotlib.pyplot as plt
import librosa


# fs = 10e3
# N = 1e5
# amp = 2 * np.sqrt(2)
# noise_power = 0.01 * fs / 2
# time = np.arange(N) / float(fs)
# mod = 500*np.cos(2*np.pi*0.25*time)
# carrier = amp * np.sin(2*np.pi*3e3*time + mod)
# noise = np.random.normal(scale=np.sqrt(noise_power), size=time.shape)
# noise *= np.exp(-time/5)
# x = carrier + noise
#
# print ('x: ', np.min(x), np.max(x)) # audio generated by code
# print (x)


# fs, audio = wavfile.read('02_wind_and_cars_org.wav') # audio from scipy audio io
# print ('audio: ', np.min(audio), np.max(audio))
# print (audio)


y, sr = librosa.load('_samples/01_counting.m4a') # audio from librosa
print ('y: ', np.min(y), np.max(y))
print (y)

# y_t, sr_te = librosa.load('Kevin_MacLeod_-_Vibe_Ace.mp3') # audio from librosa sample file
# print ('y_t: ', np.min(y_t), np.max(y_t))
# print (y_t)

# print (np.max(librosa.feature.spectral_centroid(y=y, sr=sr)))
# print (np.max(librosa.feature.spectral_centroid(y=audio, sr=fs)))

plt.figure(1)
stft = librosa.stft(y, hop_length=64)
stft = librosa.amplitude_to_db(stft)
plt.pcolormesh(stft)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Samples')
plt.title('Spectragram of the raw audio recording,\nwhich was used as the dataset for this research')
plt.savefig('_plots/pcolormesh.png', dpi=300)

plt.figure(2)
rows, columns = stft.shape
X = np.zeros((columns*rows,3))

i = 0
for r in range(0, rows):
    for c in range(0,columns):
        X[i,:]=(c,r,stft[r,c])
        i = i + 1

# np.savetxt("scatter.csv", X, delimiter=",")

# print ()
# print ()
# print ()
print ('X: ', X.shape)
# print (X)

# , cmap="YlGnBu"
plt.scatter(X[:,0], X[:,1], c=X[:,2], s=1)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Samples')
# plt.xticks(fontsize=8)
# plt.yticks(fontsize=8)
plt.title('Scatter plot of the spectragram of the raw audio recording,\nwhich was used as the dataset for this research\nEach data point was used as a single sample')
# plt.yticks(fontsize=8)
plt.savefig('_plots/scatter.png', dpi=300)

# plt.show()
end_time = time.time()
print ('\n~~~\n🕑  script run time (seconds)= ', end_time-start_time, '\n')
print ('🌳  yas!\n~~~\n')