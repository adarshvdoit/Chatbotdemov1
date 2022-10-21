import subprocess 
from gtts import gTTS
import os
mytext = 'Welcome to Innovate Yourself!'

#Language in which you want to convert 
language = 'en'

# Passing the text and language to the engine # here we have marked slow False. Which tells

# the module that the converted audio should

# have a high speed

myobj = gTTS (text=mytext, lang=language)

#Saving the converted audio in a mp3 file na
myobj.save("welcome.wav")
# #welcome
# file="welcome.mp3"

# os.system("afplay " + file)
subprocess.call(['mpg321', "welcome.mp3", '--play-and-exit'])
# # from gtts import gTTS
# # import pygame  #to play the audio
# # pygame.init()
# # pygame.mixer.init()
# # text="Hello Rasa Bot User! I am a Bot"
# # tts = gTTS(text=text, lang="en")
# # tts.save("temp.mp3") # save the audio in a temp file 
# # pygame.mixer.music.load("temp.mp3")
# # print('sound')
# # pygame.mixer.music.play()


# from pydub import AudioSegment
# from pydub.playback import play

# song = AudioSegment.from_wav("welcome.wav")
# play(song)