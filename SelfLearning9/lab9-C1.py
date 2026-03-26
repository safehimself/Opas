import librosa

file = "489578__leonseptavaux__dogs_moan_sound_1.wav"

y, sr = librosa.load(file, sr=None,mono=False)
duration = int(y.shape[-1] / sr)
if y.ndim == 1:
    channels = 'mono'
else:
    channels = 'stereo'

print("ความยาว:", duration, "วินาที")
print("Sample rate:", sr)
print("จำนวนช่อง:", channels)
