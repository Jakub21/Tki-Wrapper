import tkinter as tk
from tkinter import ttk
from TkiWrapper.namespace import Namespace

mkDict = lambda **kw: kw

class Style:
    def __init__(self):
        self.theme = None
        self.btnWidth = None
        self.fontSize = mkDict(
            heading1 = 25, heading2 = 20, heading3 = 15,
            label = 11, output = 12,
            button = 10, radio = 11, checkbox = 11,
            textInput = 12, listInput = 12,
        )
        self.fontFam = Namespace(
            std = 'Verdana',
            mono = 'Courier New',
        )
        self.colors = Namespace(
            bg = '#CFCFCF', fg = '#000',
            disabled = '#AAA',
        )

    def apply(self, root):
        style = ttk.Style()
        # Set theme
        if (self.theme is not None):
            style.theme_use(self.theme)
        # Helpers
        getFontStd = lambda k: (self.fontFam.std, self.fontSize[k])
        getFontMono = lambda k: (self.fontFam.mono, self.fontSize[k])
        kw = mkDict(background=self.colors.bg, foreground=self.colors.fg)
        # Configure TTK widget styles
        style.configure('TFrame', **kw)
        style.configure('TLabel', font=getFontStd('label'), **kw)
        style.configure('heading1.TLabel', font=getFontStd('heading1'), **kw)
        style.configure('heading2.TLabel', font=getFontStd('heading2'), **kw)
        style.configure('heading3.TLabel', font=getFontStd('heading3'), **kw)
        style.configure('output.TLabel', font=getFontMono('output'), **kw)
        style.configure('TRadiobutton', font=getFontStd('radio'), **kw)
        style.configure('TCheckbutton', font=getFontStd('checkbox'), **kw)
        style.configure('TSeparator', **kw)
        if self.btnWidth == None:
            style.configure('TButton', font=getFontStd('button'),
                background=self.colors.bg)
        else:
            style.configure('TButton', font=getFontStd('button'),
                width=self.btnWidth, background=self.colors.bg)
        # Copy settings to root for TK widgets
        root.style = Namespace(
            fontSize = self.fontSize, fontFam=self.fontFam, colors=self.colors
        )

    #----------------------------------------------------------------
    # Font attribute setters

    def setFontSize(self, key, size):
        size = int(size)
        self.fontSize[key] = size

    def setStdFont(self, family):
        self.fontFam.std = family

    def setMonoFont(self, family):
        self.fontFam.mono = family

    #----------------------------------------------------------------
    # Color attribute setters

    def setBgColor(self, color):
        if not(color.startswith('#') and len(color) in (4, 7)):
            raise Exception('Invalid color format. Use HTML hex with # prefix')
        self.colors.bg = color

    def setFgColor(self, color):
        if not(color.startswith('#') and len(color) in (4, 7)):
            raise Exception('Invalid color format. Use HTML hex with # prefix')
        self.colors.fg = color

    def setDisabledColor(self, color):
        if not(color.startswith('#') and len(color) in (4, 7)):
            raise Exception('Invalid color format. Use HTML hex with # prefix')
        self.colors.disabled = color

    #----------------------------------------------------------------
    # Other setters

    def useTheme(self, theme):
        self.theme = theme

    def setBtnWidth(self, width):
        self.btnWidth = width
