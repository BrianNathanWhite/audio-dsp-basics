import numpy as np
import librosa

def mel_spectrogram_db(audio, sr, n_mels=80):
    mel = librosa.feature.melspectrogram(
        y=audio,
        sr=sr,
        n_mels=n_mels
    )
    mel_db = librosa.power_to_db(mel, ref=np.max)
    return mel_db
