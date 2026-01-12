import librosa

def load_audio(path, sr=22050):
    audio, sr = librosa.load(path, sr=sr)
    return audio, sr
