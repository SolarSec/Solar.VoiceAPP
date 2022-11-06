# Solar TTS (Text-to-speech)
> SolarSec TTS library made for [Solar Security](https://solarsec.fbi.gov/) Version 0.01


## Parameter Defenition
```py
    def __init__ (self, 
        google_access_token: str, 
        text: str, 
        voice: str, 
        languagecode: str, 
        name: str, 
        gender: str,
        audio_encoding: str = "MP3") -> None:
```
google_access_token[str] := Google Authorization Token (Bearer)
text[str] := Text to convert to speech
voice[str] := The voice of the speech
languagecode[str] := The language and region of the speech
name[str] := Name of the speaker
gender[str] := Gender of the speech
audi_encoding^[str] := File type to format the speech to (The audio file will be stored in Google Clouds webservers)
## Usage
### Python
```py
_tts = SolarTTS("Google_Access_Token_here", "text_for_tts", "voice_", "language (en-US)", "name-of-language_code (en-GB-Standard-A)", "gender") # Constructing the class
__response__ = _tts.TTS_() # Calling the function to do the job.
```
