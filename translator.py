# translator.py - Translation Backend Logic

from deep_translator import GoogleTranslator as GT
import requests
import json

class GoogleTranslator:
    """Translation service using deep-translator library"""
    
    def __init__(self):
        self.supported_languages = {
            'english': 'en',
            'spanish': 'es', 
            'french': 'fr',
            'german': 'de',
            'hindi': 'hi',
            'italian': 'it',
            'japanese': 'ja',
            'chinese': 'zh',
            'russian': 'ru',
            'arabic': 'ar',
            'portuguese': 'pt',
            'dutch': 'nl',
            'korean': 'ko',
            'swedish': 'sv',
            'norwegian': 'no',
            'danish': 'da',
            'finnish': 'fi',
            'greek': 'el',
            'hebrew': 'he',
            'thai': 'th',
            'vietnamese': 'vi',
            'turkish': 'tr'
        }
    
    def get_supported_languages(self):
        """Return list of supported language names"""
        return list(self.supported_languages.keys())
    
    def translate_text(self, text, source_lang, target_lang):
        """
        Translate text from source to target language
        
        Args:
            text: Text to translate
            source_lang: Source language name
            target_lang: Target language name
            
        Returns:
            Translated text or error message
        """
        try:
            # Convert language names to codes
            source_code = self.supported_languages.get(source_lang.lower(), 'auto')
            target_code = self.supported_languages.get(target_lang.lower())
            
            if not target_code:
                return "Error: Target language not supported"
            
            # Perform translation
            translator = GT(source=source_code, target=target_code)
            result = translator.translate(text)
            
            return result
            
        except Exception as e:
            return f"Translation error: {str(e)}"
    
    def detect_language(self, text):
        """Detect language of input text"""
        try:
            translator = GT(source='auto', target='en')
            # This is a workaround - deep_translator doesn't have direct detection
            # In a real app, you might use langdetect library
            return "auto-detected"
        except:
            return "unknown"


class LibreTranslator:
    """Alternative translation service using LibreTranslate API"""
    
    def __init__(self, base_url="https://libretranslate.com/translate", api_key=None):
        self.base_url = base_url
        self.api_key = api_key
    
    def translate_text(self, text, source_lang, target_lang):
        """Translate using LibreTranslate API"""
        try:
            data = {
                'q': text,
                'source': source_lang,
                'target': target_lang,
                'format': 'text'
            }
            
            if self.api_key:
                data['api_key'] = self.api_key
            
            response = requests.post(self.base_url, data=data)
            result = response.json()
            
            if 'translatedText' in result:
                return result['translatedText']
            else:
                return "Translation failed"
                
        except Exception as e:
            return f"API error: {str(e)}"