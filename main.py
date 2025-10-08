# main.py - Translation App Entry Point

from ui import TranslationApp
from translator import GoogleTranslator
import tkinter as tk

def main():
    """Main function to start the translation application"""
    root = tk.Tk()
    
    # Initialize translator
    translator = GoogleTranslator()
    
    # Create and run the application
    app = TranslationApp(root, translator)
    root.mainloop()

if __name__ == "__main__":
    main()