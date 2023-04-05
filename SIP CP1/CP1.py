import matplotlib.pyplot as plt
import scipy
from scipy import fftpack
import numpy as np
from scipy.io.wavfile import write
import scipy.signal as signal
from scipy.io.wavfile import read
import winsound

#Prefix o denotes original signal

oFreqSampling, oAudioData = read("Recording.wav")
OSingleChannelData=[]
for i in oAudioData:
    OSingleChannelData.append(i[0])
    
b = 150528 / oFreqSampling #Length of Data/ fs
oTime = np.arange(0, b, 1 / oFreqSampling)

plt.title("Original Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.plot(oTime, OSingleChannelData)
plt.show()

oFFT = np.fft.fft(OSingleChannelData)
oLenData = len(OSingleChannelData)
x = np.arange(oLenData)
oFreqency = x*(oFreqSampling/oLenData)
oMagnitude = abs(oFFT)

plt.title("DFT of Original Signal")
plt.xlim(0,2000)
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.plot(oFreqency, oMagnitude)
plt.show()


#Prefix n denotes noisy

nFreqSampling, nAudioData  = read("noisySYC04new.wav") 
a = len(nAudioData) / nFreqSampling
nTime = np.arange(0, a, 1 / nFreqSampling)

plt.title("Noisy Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.plot(nTime, nAudioData)
plt.show()

nFFT = fftpack.fft(nAudioData)
nLenData = len(nAudioData)
x = np.arange(nLenData)
nFrequency = x*(nFreqSampling/nLenData)
nMagnitude = abs(nFFT)

plt.title("DFT of Noisy Signal")
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.plot(nFrequency,nMagnitude)
plt.show()



nFreqSampling=44100
nNyquistRate =nFreqSampling/2
N1 = 9501
N2 = 5001

nBandSTOPCoef = signal.firwin(N1, cutoff = (80/nNyquistRate,110/nNyquistRate, 180/nNyquistRate,210/nNyquistRate, 280/nNyquistRate,310/nNyquistRate, 380/nNyquistRate,410/nNyquistRate, 480/nNyquistRate,510/nNyquistRate, 580/nNyquistRate,610/nNyquistRate,650/nNyquistRate,), window = "blackmanharris", pass_zero="bandstop")
nBandPASSCoef = signal.firwin(N2, cutoff = (1/nNyquistRate,850/nNyquistRate), window = "blackmanharris", pass_zero="bandpass")

nFilteredBSTOP = signal.lfilter(nBandPASSCoef, 1.0, nAudioData)
nFilteredBPASS= signal.lfilter(nBandSTOPCoef, 1.0, nFilteredBSTOP)

Temp1= fftpack.fft(nFilteredBSTOP)
Temp2= fftpack.fft(nFilteredBPASS)

nMagFFTBSTOP = abs(Temp1)
nMagFFTBPASS = abs(Temp2)

plt.figure()
plt.xlim(0, 1200)
plt.title("Bandstop FFT")
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.plot(nFrequency,nMagFFTBSTOP)
plt.show()

plt.figure()
plt.xlim(0, 1200)
plt.title("Bandpass FFT")
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.plot(nFrequency,nMagFFTBPASS)
plt.show()

x2 = 2*nFilteredBPASS
write("Filtered_Shaunak.wav", nFreqSampling, np.int16(x2))
winsound.PlaySound('Filtered_Shaunak.wav', winsound.SND_FILENAME)



a = len(nFilteredBPASS) / nFreqSampling
nTime = np.arange(0, a, 1 / nFreqSampling)

plt.title("Filtered Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.plot(nTime, nFilteredBPASS)
plt.show()

#f prefix denotes filtered signal

fFFT = np.fft.fft(nFilteredBPASS)
fLenData = len(nFilteredBPASS)
x = np.arange(fLenData)
fFrequency = x*(nFreqSampling/fLenData)
fMagnitude = abs(fFFT)

plt.title("DFT of Filtered Signal")
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.plot(fFrequency,fMagnitude)
plt.show()


