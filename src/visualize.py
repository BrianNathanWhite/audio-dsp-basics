import matplotlib.pyplot as plt
import librosa.display

def plot_waveform(audio, sr, out_path="waveform.png"):
    plt.figure(figsize=(10, 3))
    librosa.display.waveshow(audio, sr=sr)
    plt.title("Waveform")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

def plot_mel_spectrogram(mel_db, sr, out_path="mel_spectrogram.png"):
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(
        mel_db,
        sr=sr,
        x_axis="time",
        y_axis="mel"
    )
    plt.colorbar(format="%+2.0f dB")
    plt.title("Mel Spectrogram (dB)")
    plt.tight_layout()
    plt.show()
    plt.savefig(out_path)
    plt.close()
