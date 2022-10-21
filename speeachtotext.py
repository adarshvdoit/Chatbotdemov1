# import the library

import speech_recognition as sr

# initialize recognizer
r=sr.Recognizer()


with sr.Microphone() as source: # mention source it will be

    print("Speak Anything :")

    audio = r.listen(source)

    # listen to the source

    try:
        text = r. recognize_google(audio) # use recognizer to print("You said: {}".format(text))
        print("Your Said:{}".format(text))
    except:
        print("Sorry could not recognize your voice")