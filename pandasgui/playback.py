import sounddevice as sd
import numpy as np
import audiofile as af


def play(x: np.ndarray, sampling_rate: int):
    sd.play(x, sampling_rate)


def play_file(path: str, *, start: float = 0, end: float = None):
    duration = end - start if end else None
    x, sr = af.read(path, offset=start, duration=duration)
    play(x, sr)

