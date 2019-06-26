from sin_gen import SinGen

y = SinGen(500)
y.make_sin()
y.soundcard_play()

z = SinGen(300)
z.make_sin()
z.sounddevice_play()
