import librosa
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
import numpy as np 
import soundfile as sf         

# Load the audio file
audio_data, sample_rate = librosa.load("test_audio.mp3")
print(sample_rate)
# NEW — design and apply the filter
cutoff = 3000
nyquist = sample_rate / 2
normal_cutoff = cutoff / nyquist
b, a = butter(4, normal_cutoff, btype='low', analog=False)
filtered_data = filtfilt(b, a, audio_data)

sf.write("filtered_audio.wav", filtered_data, sample_rate) 

# NEW — Compute frequency spectrum

fft_original = np.fft.fft(audio_data)
fft_filtered = np.fft.fft(filtered_data)
frequencies = np.fft.fftfreq(len(audio_data), 1/sample_rate)
half = len(frequencies) // 2


# Plot the waveform
# Plot original vs filtered
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))

ax1.plot(audio_data)
ax1.set_title("Original")
ax1.set_ylabel("Amplitude")
ax1.set_xlabel("Sample")

ax2.plot(filtered_data)
ax2.set_title("Filtered (low-pass, 3000 Hz cutoff)")
ax2.set_xlabel("Sample")
ax2.set_ylabel("Amplitude")

plt.tight_layout()
plt.savefig("waveform_comparison.png") 
plt.show()

# NEW — Plot frequency spectrum
plt.figure(figsize=(10, 4))
plt.plot(frequencies[:half], np.abs(fft_original[:half]), label="Original")
plt.plot(frequencies[:half], np.abs(fft_filtered[:half]), label="Filtered")
plt.title("Frequency Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.legend()
plt.savefig("frequency_spectrum.png")


plt.show()