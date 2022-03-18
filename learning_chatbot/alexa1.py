import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes
from gtts import gTTS
from playsound import playsound

# TODO: Aplicar para português: https://letscode.com.br/blog/speech-recognition-com-python

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk_portuguese(audio):
    tts = gTTS(audio, lang='pt-br')
    #Salva o arquivo de audio
    tts.save('hello.mp3')
    #Da play ao audio
    playsound('hello.mp3')


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    
    command = ''

    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='pt-BR')
            command = command.lower()
            
            if 'joelma' in command:
                command = command.replace('alexa', '')
                print(command)
    except Exception as e:
        print('Erro', e)

    return command


def run_alexa():
    
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
    
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    
    else:
        # talk('Por favor fale novamente')
        talk_portuguese('Por favor, fale novamente')

    
while True:
    run_alexa()
