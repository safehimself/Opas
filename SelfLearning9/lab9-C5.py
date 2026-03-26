import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
y, sr = librosa.load("489578__leonseptavaux__dogs_moan_sound_1.wav", sr=None)
D = librosa.stft(y)
S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
plt.figure(figsize=(10, 4))
librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='hz')
plt.colorbar(label='dB')
plt.title('Spectrogram')
plt.tight_layout()
plt.savefig("spectrogram.png")
plt.show()
