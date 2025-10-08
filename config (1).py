# config.py - Configuration Settings for Translation App

import os
from typing import Dict, List

class Config:
    """Configuration settings for the translation app"""
    
    # App Settings
    APP_NAME = "Universal Language Translator"
    APP_VERSION = "1.0.0"
    
    # Window Settings
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    WINDOW_MIN_WIDTH = 600
    WINDOW_MIN_HEIGHT = 400
    
    # API Settings
    GOOGLE_TRANSLATE_API_KEY = os.getenv('GOOGLE_TRANSLATE_API_KEY', None)
    DEEPL_API_KEY = os.getenv('DEEPL_API_KEY', None)
    LIBRE_TRANSLATE_URL = os.getenv('LIBRE_TRANSLATE_URL', 'https://libretranslate.com/translate')
    
    # Translation Settings
    DEFAULT_SOURCE_LANGUAGE = 'auto-detect'
    DEFAULT_TARGET_LANGUAGE = 'english'
    MAX_TEXT_LENGTH = 5000
    REQUEST_TIMEOUT = 10  # seconds
    
    # UI Theme Settings
    UI_THEME = {
        'bg_color': '#f0f0f0',
        'primary_color': '#4CAF50',
        'secondary_color': '#2196F3',
        'error_color': '#f44336',
        'text_color': '#333333',
        'font_family': 'Arial',
        'font_size': 11
    }
    
    # Supported Languages (can be extended)
    SUPPORTED_LANGUAGES = {
        'afrikaans': 'af',
        'albanian': 'sq', 
        'amharic': 'am',
        'arabic': 'ar',
        'armenian': 'hy',
        'azerbaijani': 'az',
        'basque': 'eu',
        'belarusian': 'be',
        'bengali': 'bn',
        'bosnian': 'bs',
        'bulgarian': 'bg',
        'catalan': 'ca',
        'cebuano': 'ceb',
        'chinese': 'zh',
        'corsican': 'co',
        'croatian': 'hr',
        'czech': 'cs',
        'danish': 'da',
        'dutch': 'nl',
        'english': 'en',
        'esperanto': 'eo',
        'estonian': 'et',
        'finnish': 'fi',
        'french': 'fr',
        'frisian': 'fy',
        'galician': 'gl',
        'georgian': 'ka',
        'german': 'de',
        'greek': 'el',
        'gujarati': 'gu',
        'haitian': 'ht',
        'hausa': 'ha',
        'hawaiian': 'haw',
        'hebrew': 'he',
        'hindi': 'hi',
        'hmong': 'hmn',
        'hungarian': 'hu',
        'icelandic': 'is',
        'igbo': 'ig',
        'indonesian': 'id',
        'irish': 'ga',
        'italian': 'it',
        'japanese': 'ja',
        'javanese': 'jv',
        'kannada': 'kn',
        'kazakh': 'kk',
        'khmer': 'km',
        'kinyarwanda': 'rw',
        'korean': 'ko',
        'kurdish': 'ku',
        'kyrgyz': 'ky',
        'lao': 'lo',
        'latin': 'la',
        'latvian': 'lv',
        'lithuanian': 'lt',
        'luxembourgish': 'lb',
        'macedonian': 'mk',
        'malagasy': 'mg',
        'malay': 'ms',
        'malayalam': 'ml',
        'maltese': 'mt',
        'maori': 'mi',
        'marathi': 'mr',
        'mongolian': 'mn',
        'burmese': 'my',
        'nepali': 'ne',
        'norwegian': 'no',
        'odia': 'or',
        'pashto': 'ps',
        'persian': 'fa',
        'polish': 'pl',
        'portuguese': 'pt',
        'punjabi': 'pa',
        'romanian': 'ro',
        'russian': 'ru',
        'samoan': 'sm',
        'scots_gaelic': 'gd',
        'serbian': 'sr',
        'sesotho': 'st',
        'shona': 'sn',
        'sindhi': 'sd',
        'sinhala': 'si',
        'slovak': 'sk',
        'slovenian': 'sl',
        'somali': 'so',
        'spanish': 'es',
        'sundanese': 'su',
        'swahili': 'sw',
        'swedish': 'sv',
        'tajik': 'tg',
        'tamil': 'ta',
        'tatar': 'tt',
        'telugu': 'te',
        'thai': 'th',
        'turkish': 'tr',
        'turkmen': 'tk',
        'ukrainian': 'uk',
        'urdu': 'ur',
        'uyghur': 'ug',
        'uzbek': 'uz',
        'vietnamese': 'vi',
        'welsh': 'cy',
        'xhosa': 'xh',
        'yiddish': 'yi',
        'yoruba': 'yo',
        'zulu': 'zu'
    }
    
    # Common language pairs for quick access
    POPULAR_LANGUAGES = [
        'english', 'spanish', 'french', 'german', 'italian', 
        'portuguese', 'russian', 'chinese', 'japanese', 'korean',
        'arabic', 'hindi', 'dutch', 'swedish', 'norwegian'
    ]
    
    @classmethod
    def get_language_code(cls, language_name: str) -> str:
        """Get language code from language name"""
        return cls.SUPPORTED_LANGUAGES.get(language_name.lower(), 'en')
    
    @classmethod
    def get_language_name(cls, language_code: str) -> str:
        """Get language name from language code"""
        for name, code in cls.SUPPORTED_LANGUAGES.items():
            if code == language_code:
                return name
        return 'english'
    
    @classmethod
    def get_popular_languages(cls) -> List[str]:
        """Get list of popular languages"""
        return cls.POPULAR_LANGUAGES
    
    @classmethod
    def validate_language(cls, language: str) -> bool:
        """Check if language is supported"""
        return language.lower() in cls.SUPPORTED_LANGUAGES


class APIKeys:
    """Manage API keys securely"""
    
    @staticmethod
    def get_google_api_key() -> str:
        """Get Google Translate API key from environment"""
        return os.getenv('GOOGLE_TRANSLATE_API_KEY', '')
    
    @staticmethod
    def get_deepl_api_key() -> str:
        """Get DeepL API key from environment"""
        return os.getenv('DEEPL_API_KEY', '')
    
    @staticmethod
    def set_api_key(service: str, key: str):
        """Set API key in environment (for current session)"""
        if service.lower() == 'google':
            os.environ['GOOGLE_TRANSLATE_API_KEY'] = key
        elif service.lower() == 'deepl':
            os.environ['DEEPL_API_KEY'] = key


class AppSettings:
    """User preferences and app settings"""
    
    def __init__(self):
        self.settings = {
            'last_source_language': Config.DEFAULT_SOURCE_LANGUAGE,
            'last_target_language': Config.DEFAULT_TARGET_LANGUAGE,
            'window_size': f"{Config.WINDOW_WIDTH}x{Config.WINDOW_HEIGHT}",
            'theme': 'default',
            'auto_detect_language': True,
            'save_history': True,
            'translation_service': 'google'  # google, deepl, libre
        }
    
    def get(self, key: str, default=None):
        """Get setting value"""
        return self.settings.get(key, default)
    
    def set(self, key: str, value):
        """Set setting value"""
        self.settings[key] = value
    
    def save_to_file(self, filepath: str):
        """Save settings to file"""
        try:
            import json
            with open(filepath, 'w') as f:
                json.dump(self.settings, f, indent=2)
        except Exception as e:
            print(f"Error saving settings: {e}")
    
    def load_from_file(self, filepath: str):
        """Load settings from file"""
        try:
            import json
            with open(filepath, 'r') as f:
                self.settings.update(json.load(f))
        except Exception as e:
            print(f"Error loading settings: {e}")


# Create global config instance
app_config = Config()
app_settings = AppSettings()