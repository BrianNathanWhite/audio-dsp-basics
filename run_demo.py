from src.load_audio import load_audio
from src.features import mel_spectrogram_db
from src.visualize import plot_waveform, plot_mel_spectrogram

audio, sr = load_audio("data/13 - Glenn Gould - Variation V.flac")
plot_waveform(audio, sr)

mel_db = mel_spectrogram_db(audio, sr)
plot_mel_spectrogram(mel_db, sr)
