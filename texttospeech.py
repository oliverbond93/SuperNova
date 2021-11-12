import pyttsx3

def speak(word):

    # Initialise the text-to-speech object
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    for voice in voices:
        engine.setProperty('voice', voice.id)
        print(voice.id)
        engine.say('The quick brown fox jumped over the lazy dog.')

    # Make changes to the engine properties:
    # Speed of speech / Volume / Voice Type
    # N.B. You might need to comment out the 'set voice property' command if not on Windows
    engine.setProperty('rate', 125)
    engine.setProperty('volume',1)
    engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')


    # Say the word
    engine.say(word)
    engine.runAndWait()

    return

if __name__ == '__main__':
    speak('Hi there!')