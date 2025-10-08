# README.md - Universal Language Translator

## Universal Language Translator

A powerful, user-friendly desktop application for translating text between multiple languages using various translation engines.

### Features

- **Multi-language Support**: Translate between 100+ languages
- **Multiple Translation Engines**: Google Translate, LibreTranslate, and more
- **Auto Language Detection**: Automatically detect source language
- **User-friendly Interface**: Clean, intuitive GUI built with Tkinter
- **Copy to Clipboard**: Easy copying of translated text
- **Offline Capability**: Optional offline translation models
- **Free and Open Source**: No API keys required for basic functionality

### Screenshots

![Translation App Interface](screenshot.png)

### Installation

#### Method 1: Using Git Clone

```bash
# Clone the repository
git clone https://github.com/yourusername/translation-app.git
cd translation-app

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

#### Method 2: Download ZIP

1. Download the ZIP file from GitHub
2. Extract to your desired location
3. Follow steps 2-5 from Method 1

### Usage

1. **Launch the App**: Run `python main.py`
2. **Enter Text**: Type or paste text in the input area
3. **Select Languages**: Choose source (or auto-detect) and target languages
4. **Translate**: Click the "Translate" button
5. **Copy Result**: Use "Copy Translation" to copy the result

### Supported Languages

The app supports 100+ languages including:
- **European**: English, Spanish, French, German, Italian, Portuguese, Russian, Dutch, Swedish, etc.
- **Asian**: Chinese, Japanese, Korean, Hindi, Arabic, Thai, Vietnamese, etc.
- **African**: Swahili, Yoruba, Zulu, etc.
- **And many more...**

### Configuration

#### API Keys (Optional)

For enhanced features, you can set API keys:

```bash
# Google Translate API
export GOOGLE_TRANSLATE_API_KEY="your-api-key"

# DeepL API
export DEEPL_API_KEY="your-api-key"
```

#### Settings

Modify `config.py` to customize:
- Default languages
- UI theme colors
- Window dimensions
- Translation timeout settings

### File Structure

```
translation-app/
├── main.py              # Application entry point
├── translator.py        # Translation logic
├── ui.py               # User interface
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── tests/             # Unit tests
│   ├── test_translator.py
│   └── test_ui.py
└── docs/              # Documentation
    └── user_guide.md
```

### Contributing

We welcome contributions! Here's how to help:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature-name`
3. **Commit** your changes: `git commit -m 'Add feature'`
4. **Push** to the branch: `git push origin feature-name`
5. **Open** a Pull Request

### Development

#### Running Tests

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=.
```

#### Adding New Translation Services

1. Create new translator class in `translator.py`
2. Implement required methods: `translate_text()`, `get_supported_languages()`
3. Update `config.py` with new service settings
4. Add tests in `tests/`

### Troubleshooting

#### Common Issues

**Import Error: No module named 'tkinter'**
- On Ubuntu/Debian: `sudo apt-get install python3-tk`
- On CentOS/RHEL: `sudo yum install tkinter`

**Translation Not Working**
- Check internet connection
- Verify selected languages are supported
- Try different translation service

**GUI Not Displaying Properly**
- Update Python to 3.7+
- Install latest tkinter version

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Changelog

#### v1.0.0
- Initial release
- Support for Google Translate via deep-translator
- Basic GUI with Tkinter
- Auto language detection
- Copy to clipboard functionality

### Acknowledgments

- **Deep Translator**: For translation API integration
- **Tkinter**: For GUI framework
- **Argos Translate**: For offline translation capabilities
- **LibreTranslate**: For free translation API

### Support

- **Issues**: Report bugs on [GitHub Issues](https://github.com/yourusername/translation-app/issues)
- **Discussions**: Join [GitHub Discussions](https://github.com/yourusername/translation-app/discussions)
- **Email**: contact@yourdomain.com

### Roadmap

- [ ] Speech-to-text translation
- [ ] Document translation (PDF, Word)
- [ ] Translation history
- [ ] Batch translation
- [ ] Web interface version
- [ ] Mobile app version
- [ ] Plugin system for custom translators

---

**Made with ❤️ for breaking down language barriers**