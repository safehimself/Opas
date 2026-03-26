from pydub import AudioSegment

audio = AudioSegment.from_file("489578__leonseptavaux__dogs_moan_sound_1.wav")

print("Before:", audio.dBFS)

normalized = audio.apply_gain(-1 - audio.max_dBFS)

print("After:", normalized.dBFS)

normalized.export("Normalized.wav", format="wav")
