# tests/test_translator.py - Unit Tests for Translation Module

import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add parent directory to path to import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from translator import GoogleTranslator, LibreTranslator

class TestGoogleTranslator(unittest.TestCase):
    """Test cases for GoogleTranslator class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.translator = GoogleTranslator()
    
    def test_get_supported_languages(self):
        """Test getting supported languages list"""
        languages = self.translator.get_supported_languages()
        self.assertIsInstance(languages, list)
        self.assertIn('english', languages)
        self.assertIn('spanish', languages)
        self.assertIn('french', languages)
    
    def test_supported_languages_dict(self):
        """Test supported languages dictionary"""
        self.assertIsInstance(self.translator.supported_languages, dict)
        self.assertEqual(self.translator.supported_languages['english'], 'en')
        self.assertEqual(self.translator.supported_languages['spanish'], 'es')
    
    @patch('translator.GT')
    def test_translate_text_success(self, mock_gt):
        """Test successful translation"""
        # Mock the translator
        mock_translator_instance = MagicMock()
        mock_translator_instance.translate.return_value = "Hola mundo"
        mock_gt.return_value = mock_translator_instance
        
        result = self.translator.translate_text("Hello world", "english", "spanish")
        
        self.assertEqual(result, "Hola mundo")
        mock_gt.assert_called_once_with(source='en', target='es')
        mock_translator_instance.translate.assert_called_once_with("Hello world")
    
    @patch('translator.GT')
    def test_translate_text_auto_detect(self, mock_gt):
        """Test translation with auto-detect source"""
        mock_translator_instance = MagicMock()
        mock_translator_instance.translate.return_value = "Bonjour le monde"
        mock_gt.return_value = mock_translator_instance
        
        result = self.translator.translate_text("Hello world", "auto", "french")
        
        self.assertEqual(result, "Bonjour le monde")
        mock_gt.assert_called_once_with(source='auto', target='fr')
    
    def test_translate_text_unsupported_language(self):
        """Test translation with unsupported target language"""
        result = self.translator.translate_text("Hello", "english", "klingon")
        self.assertIn("Error: Target language not supported", result)
    
    @patch('translator.GT')
    def test_translate_text_exception(self, mock_gt):
        """Test handling of translation exceptions"""
        mock_gt.side_effect = Exception("Network error")
        
        result = self.translator.translate_text("Hello", "english", "spanish")
        self.assertIn("Translation error:", result)
    
    def test_detect_language(self):
        """Test language detection"""
        # Note: This is a placeholder implementation
        result = self.translator.detect_language("Hello world")
        self.assertIsInstance(result, str)


class TestLibreTranslator(unittest.TestCase):
    """Test cases for LibreTranslator class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.translator = LibreTranslator()
    
    def test_init_default_values(self):
        """Test initialization with default values"""
        self.assertEqual(self.translator.base_url, "https://libretranslate.com/translate")
        self.assertIsNone(self.translator.api_key)
    
    def test_init_custom_values(self):
        """Test initialization with custom values"""
        custom_url = "https://custom.translate.api"
        custom_key = "test_api_key"
        
        translator = LibreTranslator(base_url=custom_url, api_key=custom_key)
        
        self.assertEqual(translator.base_url, custom_url)
        self.assertEqual(translator.api_key, custom_key)
    
    @patch('translator.requests.post')
    def test_translate_text_success(self, mock_post):
        """Test successful translation via LibreTranslate API"""
        # Mock successful API response
        mock_response = MagicMock()
        mock_response.json.return_value = {'translatedText': 'Hola mundo'}
        mock_post.return_value = mock_response
        
        result = self.translator.translate_text("Hello world", "en", "es")
        
        self.assertEqual(result, "Hola mundo")
        mock_post.assert_called_once()
        
        # Check the data sent to API
        call_args = mock_post.call_args
        expected_data = {
            'q': 'Hello world',
            'source': 'en',
            'target': 'es',
            'format': 'text'
        }
        self.assertEqual(call_args[1]['data'], expected_data)
    
    @patch('translator.requests.post')
    def test_translate_text_with_api_key(self, mock_post):
        """Test translation with API key"""
        translator = LibreTranslator(api_key="test_key")
        
        mock_response = MagicMock()
        mock_response.json.return_value = {'translatedText': 'Translated text'}
        mock_post.return_value = mock_response
        
        translator.translate_text("Test", "en", "es")
        
        call_args = mock_post.call_args
        self.assertIn('api_key', call_args[1]['data'])
        self.assertEqual(call_args[1]['data']['api_key'], "test_key")
    
    @patch('translator.requests.post')
    def test_translate_text_api_error(self, mock_post):
        """Test handling of API errors"""
        mock_response = MagicMock()
        mock_response.json.return_value = {'error': 'Translation failed'}
        mock_post.return_value = mock_response
        
        result = self.translator.translate_text("Hello", "en", "es")
        self.assertEqual(result, "Translation failed")
    
    @patch('translator.requests.post')
    def test_translate_text_exception(self, mock_post):
        """Test handling of request exceptions"""
        mock_post.side_effect = Exception("Connection error")
        
        result = self.translator.translate_text("Hello", "en", "es")
        self.assertIn("API error:", result)


class TestTranslatorIntegration(unittest.TestCase):
    """Integration tests for translator modules"""
    
    def test_language_code_consistency(self):
        """Test that language codes are consistent across translators"""
        google_translator = GoogleTranslator()
        
        # Check common languages exist
        common_languages = ['english', 'spanish', 'french', 'german']
        
        for lang in common_languages:
            self.assertIn(lang, google_translator.supported_languages)
            self.assertIsInstance(google_translator.supported_languages[lang], str)
            self.assertTrue(len(google_translator.supported_languages[lang]) >= 2)


if __name__ == '__main__':
    unittest.main()