# ui.py - User Interface for Translation App

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import pyperclip

class TranslationApp:
    """Main GUI application for translation"""
    
    def __init__(self, root, translator):
        self.root = root
        self.translator = translator
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the user interface"""
        # Configure main window
        self.root.title("Universal Language Translator")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        # Create main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="Universal Language Translator", 
                               font=("Arial", 20, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Source language selection
        ttk.Label(main_frame, text="From:", font=("Arial", 12)).grid(row=1, column=0, sticky=tk.W, padx=(0, 10))
        self.source_lang_var = tk.StringVar()
        self.source_combo = ttk.Combobox(main_frame, textvariable=self.source_lang_var, 
                                        values=['auto-detect'] + self.translator.get_supported_languages(),
                                        state="readonly", width=15)
        self.source_combo.grid(row=1, column=1, sticky=tk.W, padx=(0, 20))
        self.source_combo.set('auto-detect')
        
        # Target language selection
        ttk.Label(main_frame, text="To:", font=("Arial", 12)).grid(row=1, column=2, sticky=tk.W, padx=(20, 10))
        self.target_lang_var = tk.StringVar()
        self.target_combo = ttk.Combobox(main_frame, textvariable=self.target_lang_var,
                                        values=self.translator.get_supported_languages(),
                                        state="readonly", width=15)
        self.target_combo.grid(row=1, column=3, sticky=tk.W)
        self.target_combo.set('english')
        
        # Input text area
        ttk.Label(main_frame, text="Enter text to translate:", font=("Arial", 12)).grid(row=2, column=0, columnspan=4, sticky=tk.W, pady=(20, 5))
        self.input_text = scrolledtext.ScrolledText(main_frame, height=8, width=70, 
                                                   wrap=tk.WORD, font=("Arial", 11))
        self.input_text.grid(row=3, column=0, columnspan=4, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=0, columnspan=4, pady=10)
        
        # Translate button
        self.translate_btn = ttk.Button(button_frame, text="Translate", 
                                       command=self.translate_text,
                                       style="Accent.TButton")
        self.translate_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Clear button
        self.clear_btn = ttk.Button(button_frame, text="Clear All", 
                                   command=self.clear_all)
        self.clear_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Copy button
        self.copy_btn = ttk.Button(button_frame, text="Copy Translation", 
                                  command=self.copy_translation)
        self.copy_btn.pack(side=tk.LEFT)
        
        # Output text area
        ttk.Label(main_frame, text="Translation:", font=("Arial", 12)).grid(row=5, column=0, columnspan=4, sticky=tk.W, pady=(20, 5))
        self.output_text = scrolledtext.ScrolledText(main_frame, height=8, width=70, 
                                                    wrap=tk.WORD, font=("Arial", 11),
                                                    state=tk.DISABLED)
        self.output_text.grid(row=6, column=0, columnspan=4, sticky=(tk.W, tk.E))
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready to translate")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, 
                              font=("Arial", 10), foreground="gray")
        status_bar.grid(row=7, column=0, columnspan=4, sticky=tk.W, pady=(10, 0))
    
    def translate_text(self):
        """Handle translation button click"""
        # Get input text
        input_text = self.input_text.get(1.0, tk.END).strip()
        
        if not input_text:
            messagebox.showwarning("Warning", "Please enter text to translate")
            return
        
        # Get selected languages
        source_lang = self.source_lang_var.get()
        target_lang = self.target_lang_var.get()
        
        if not target_lang:
            messagebox.showwarning("Warning", "Please select a target language")
            return
        
        # Show progress
        self.status_var.set("Translating...")
        self.translate_btn.config(state=tk.DISABLED)
        self.root.update()
        
        try:
            # Perform translation
            if source_lang == 'auto-detect':
                source_lang = 'auto'
            
            result = self.translator.translate_text(input_text, source_lang, target_lang)
            
            # Display result
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(1.0, result)
            self.output_text.config(state=tk.DISABLED)
            
            self.status_var.set("Translation completed successfully")
            
        except Exception as e:
            messagebox.showerror("Error", f"Translation failed: {str(e)}")
            self.status_var.set("Translation failed")
        
        finally:
            self.translate_btn.config(state=tk.NORMAL)
    
    def clear_all(self):
        """Clear all text areas"""
        self.input_text.delete(1.0, tk.END)
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.config(state=tk.DISABLED)
        self.status_var.set("Ready to translate")
    
    def copy_translation(self):
        """Copy translation to clipboard"""
        translation = self.output_text.get(1.0, tk.END).strip()
        if translation:
            try:
                pyperclip.copy(translation)
                self.status_var.set("Translation copied to clipboard")
            except:
                # Fallback if pyperclip is not available
                self.root.clipboard_clear()
                self.root.clipboard_append(translation)
                self.status_var.set("Translation copied to clipboard")
        else:
            messagebox.showwarning("Warning", "No translation to copy")


class SimpleTranslationApp:
    """Simplified version using basic tkinter widgets"""
    
    def __init__(self, root, translator):
        self.root = root
        self.translator = translator
        self.setup_simple_ui()
    
    def setup_simple_ui(self):
        """Setup a simpler UI version"""
        self.root.title("Simple Translator")
        self.root.geometry("600x400")
        
        # Input
        tk.Label(self.root, text="Enter text:", font=("Arial", 12)).pack(pady=10)
        self.input_entry = tk.Text(self.root, height=5, width=60)
        self.input_entry.pack(pady=5)
        
        # Language selection
        lang_frame = tk.Frame(self.root)
        lang_frame.pack(pady=10)
        
        tk.Label(lang_frame, text="To:").pack(side=tk.LEFT)
        self.lang_var = tk.StringVar()
        lang_menu = tk.OptionMenu(lang_frame, self.lang_var, *self.translator.get_supported_languages())
        lang_menu.pack(side=tk.LEFT, padx=10)
        self.lang_var.set('english')
        
        # Translate button
        tk.Button(self.root, text="Translate", command=self.simple_translate, 
                 font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=10)
        
        # Output
        tk.Label(self.root, text="Translation:", font=("Arial", 12)).pack()
        self.output_text = tk.Text(self.root, height=5, width=60, state=tk.DISABLED)
        self.output_text.pack(pady=5)
    
    def simple_translate(self):
        """Simple translation function"""
        text = self.input_entry.get(1.0, tk.END).strip()
        target_lang = self.lang_var.get()
        
        if text and target_lang:
            result = self.translator.translate_text(text, 'auto', target_lang)
            
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(1.0, result)
            self.output_text.config(state=tk.DISABLED)