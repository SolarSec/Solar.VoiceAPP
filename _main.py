import requests, json



class SolarTTS:
    def __init__ (self, 
        google_access_token: str, 
        text: str, 
        voice: str, 
        languagecode: str, 
        name: str, 
        gender: str,
        audio_encoding: str = "MP3") -> None:
        self.google_access_token = google_access_token
        self.text: str = text
        self.voice: str = voice
        self.languagecode: str = languagecode
        self.name: str = name
        self.gender: str = gender
        self.audio_encoding: str = audio_encoding
    
    def _handle_tts_errors (self, _response: dict) -> dict:
        if _response['error']['message'] == "Request had invalid authentication credentials. Expected OAuth 2 access token, login cookie or other valid authentication credential. See https://developers.google.com/identity/sign-in/web/devconsole-project.":
            return json.dumps(dict({"Error" : True, "Message" : "The 'google_access_token' is invalid."}), indent=6)

    def TTS_ (self) -> None:
        _constructed_headers: dict = {"Authorization": "Bearer {}".format(self.google_access_token), "Content-Type" : "application/json; charset=utf-8"}
        _constructed_payload: dict = json.dumps({"input" : {"text" : self.text},"voice" : {"languageCode" : self.languagecode,"name" : self.name,"ssmlGender" : self.gender},"audioConfig" : {"audioEncoding" : self.audio_encoding}})

        with requests.post("https://texttospeech.googleapis.com/v1/text:synthesize", headers=_constructed_headers, data=_constructed_payload) as _a:
            _response = _a.json()
        
        return _response if bool(_response) else    0

if __name__ == '__main__':
    pass

_tts = SolarTTS("Google_Access_Token_here", "text_for_tts", "voice_", "language (en-US)", "name-of-language_code (en-GB-Standard-A)", "gender")
__response__ = _tts._handle_tts_errors(_tts.TTS_())

print(__response__)
