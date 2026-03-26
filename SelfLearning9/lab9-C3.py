from pydub import AudioSegment, silence

audio = AudioSegment.from_file("489578__leonseptavaux__dogs_moan_sound_1.wav")

chunks = silence.split_on_silence(audio, min_silence_len=500, silence_thresh=-40)

combined = sum(chunks)

print("Before:", len(audio)/1000)
print("After:", len(combined)/1000)

combined.export("trimmed.wav", format="wav")
