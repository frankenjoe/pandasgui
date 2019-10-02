import sounddevice as sd
import numpy as np
import audiofile as af
import warnings


_play_channel = None


def set_channel(channel: int):
    global _play_channel
    _play_channel = channel


def play(x: np.ndarray, sampling_rate: int):
    sd.play(x, sampling_rate)


def play_file(path: str, *, start: float = 0, end: float = None):
    global _play_channel
    duration = end - start if end else None
    x, sr = af.read(path, offset=start, duration=duration, always_2d=True)
    print(_play_channel)
    if _play_channel is not None:
        if _play_channel >= x.shape[0]:
            warnings.warn('Cannot play channel ', _play_channel)
            return
        x = x[_play_channel, :]
    play(x, sr)

