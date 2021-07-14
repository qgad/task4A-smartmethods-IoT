# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 23:25:53 2021

@author: dooda
"""

from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = 'oNJw3zSODiR04aJdx8S3hjy4eV-MpICzyOPc-_WUR1Tb'
url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/00562f82-b6af-4619-8d42-4aedd6ff08b1'

#Service
authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)



with open('output.txt', 'r') as f:
    text = f.readlines()
text = [line.replace('\n','') for line in text]   
text = ''.join(str(line) for line in text)
with open('./winston.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='en-GB_JamesV3Voice').get_result()
    audio_file.write(res.content)