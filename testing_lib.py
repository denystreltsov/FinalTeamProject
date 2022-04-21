import ctypes

dl = ctypes.CDLL("./libdeniaudio.so")

dl.AudioInit()

s = "SpecifyPathToMusic"
s2 = "SpecifyPathToAnotherMusic"

c_s = ctypes.c_char_p(s.encode("utf-8"))
c_s2 = ctypes.c_char_p(s2.encode("utf-8"))

dl.MixingTwoAudio(c_s,c_s2)

dl.PlayAudio()

dl.AudioExit()
