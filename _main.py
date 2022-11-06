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


    def TTS_ (self) -> None:
        _constructed_headers: dict = {"Authorization": "Bearer {}".format(self.google_access_token), "Content-Type" : "application/json; charset=utf-8"}
        _constructed_payload: dict = json.dumps({"input" : {"text" : self.text},"voice" : {"languageCode" : self.languagecode,"name" : self.name,"ssmlGender" : self.gender},"audioConfig" : {"audioEncoding" : self.audio_encoding}})

        with requests.get("https://texttospeech.googleapis.com/v1/text:synthesize", headers=_constructed_headers, data=_constructed_payload) as _a:
            _response = _a.text
        
        return _response if bool(_response) else    0

if __name__ == '__main__':
    pass