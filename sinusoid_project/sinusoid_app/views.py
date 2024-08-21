from django.shortcuts import render
import numpy as np
import matplotlib.pyplot as plt
from django.http import HttpResponse
from io import BytesIO

class Sinusoid:
    def __init__(self, freq=440, amp=1.0, offset=0, func=np.sin):
        self.freq = freq
        self.amp = amp
        self.offset = offset
        self.func = func

    def evaluate(self, ts):
        phases = 2 * np.pi * self.freq * ts + self.offset
        ys = self.amp * self.func(phases)
        return ys

    def make_wave(self, duration=1, start=0, framerate=11025):
        n = round(duration * framerate)
        ts = start + np.arange(n) / framerate
        ys = self.evaluate(ts)
        return ts, ys

def plot_sinusoid(request):
    sinusoid = Sinusoid(freq=440, amp=1.0, offset=0, func=np.sin)
    ts, ys = sinusoid.make_wave(duration=1.0, start=0, framerate=44100)

    fig, ax = plt.subplots()
    ax.plot(ts, ys)
    ax.set(xlabel='time (s)', ylabel='amplitude', title='Sinusoid Wave')
    ax.grid()

    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    return HttpResponse(buf, content_type='image/png')

