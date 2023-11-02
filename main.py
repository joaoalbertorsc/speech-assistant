import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS

rec = sr.Recognizer()


def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            sexta_feira_speak(ask)
        audio = rec.listen(source)
        try:
            voice_data = rec.recognize_google(audio)
        except sr.UnknownValueError:
            sexta_feira_speak('Desculpe, eu não entendi o que você disse.')
            exit()
        except sr.RequestError:
            sexta_feira_speak('Desculpe, meu serviço de assistencia está desativado.')
            exit()
        return voice_data


def sexta_feira_speak(audio_string):
    text_to_speech = gTTS(text = audio_string,lang = 'pt')
    ran = random.randint(1,10000000)
    audio_file = 'audio-' + str(ran) + '.mp3'
    text_to_speech.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)



def respond(voice_data):
    what_time = ['quantas horas sao', 'que horas sao', 'que hora e essa']
    search = ['realizar pesquisa', 'fazer pesquisa', 'pesquisar']
    find_location = ['procurar localização', 'encontrar localização', 'localização']

    if 'qual o seu nome' in voice_data:
        sexta_feira_speak('Meu nome é Sexta-Feira, é um prazer ser sua assistente!')
    elif voice_data in what_time:
        sexta_feira_speak(time.ctime())
    elif voice_data in search :
        search_query = record_audio('O que deseja pesquisar?')
        url = 'https://google.com/search?q=' + search_query
        webbrowser.get().open(url)
        sexta_feira_speak('Aqui está o que eu encontrei para ' + search_query)
    elif voice_data in find_location:
        location = record_audio('Qual localização você deseja encontrar?')
        url = 'https://www.google.com/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        sexta_feira_speak('Aqui está a localização que eu encontrei para ' + location)
    elif 'sair' in voice_data:
        exit()



time.sleep(1)
sexta_feira_speak('Olá, como posso ajudá-lo?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
