# Import the Gtts module for text  
# to speech conversion
#pip install gTTS
from gtts import gTTS 
  
# import Os module to start the audio file
import os 
  
mytext = 'Hello my name is manas kumar mahanandia'
  
# Language we want to use 
language = 'en-US'
  

myobj = gTTS(text=mytext, lang=language, slow=False) 
  

myobj.save("output.mp3") 
  
# Play the converted file 
os.system("start output.mp3") 