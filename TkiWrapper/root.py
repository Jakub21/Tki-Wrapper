import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as tkFile

class Root:
    def __init__(self):
        self.root = tk.Tk()
        self.backFrame = ttk.Frame(self.root, style='back.TFrame')
        self.root.protocol('WM_DELETE_WINDOW', self.quit)
        self.views = {}
        self.leave = False
        self.backFrame.columnconfigure(0, weight=1)
        self.setSectionWeights(0, 1, 0)
        self.backFrame.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        # Input Widgets
        self.inputs = {}
        self.buttons = {}
        self.fileButtons = {}
        self.radios = {}
        self.boolIns = {}
        # Widgets data
        self.files = {}
        self.radioGroups = {}
        # Output Widgets
        self.outputTexts = {}
        self.outputBools = {}

    def update(self):
        if not self.leave:
            self.root.update()

    def quit(self):
        self.root.destroy()
        self.leave = True

    #----------------------------------------------------------------
    # General window settings

    def setTitle(self, title):
        self.root.title(title)

    def setIcon(self, path):
        self.root.iconbitmap(path)

    def setWindowSize(self, x, y):
        self.root.geometry(f'{x}x{y}')

    def setMinSize(self, x, y):
        self.root.minsize(x, y)

    #----------------------------------------------------------------
    # Views related

    def addView(self, view, key):
        self.views[key] = view

    def setHeader(self, view):
        self.header = view
        view.setRole('header')
        view.show()

    def setFooter(self, view):
        self.footer = view
        view.setRole('footer')
        view.show()

    def showView(self, key):
        for k, view in self.views.items():
            view.hide()
        self.views[key].show()

    def setSectionWeights(self, header, content, footer):
        self.backFrame.rowconfigure(0, weight=header)
        self.backFrame.rowconfigure(1, weight=content)
        self.backFrame.rowconfigure(2, weight=footer)

    #----------------------------------------------------------------
    # Setting output widgets' values

    def setOutputText(self, key, value):
        try: self.outputTexts[key]['text'] = f'{value}'
        except KeyError: return False
        return True

    def setOutputBool(self, key, value):
        try: widget = self.outputBools[key]
        except KeyError: return False
        current = 'selected' in widget.state()
        if current != value:
            widget.invoke()
        return True

    #----------------------------------------------------------------
    # Reading input widgets' values

    def getInputVal(self, key):
        try: return self.inputs[key].get()
        except KeyError: pass

    def getRadioVal(self, groupKey):
        try: return self.radioGroups[groupKey].variable.get()
        except KeyError: pass

    def getFileVal(self, btnKey):
        try: return self.files[btnKey]
        except KeyError: pass

    def getBoolVal(self, key):
        try: return 'selected' in self.boolIns[key].state()
        except KeyError: pass

    #----------------------------------------------------------------
    # Setting output widgets' default values

    def setInputDefault(self, key, value):
        self.inputs[key].delete(0, tk.END)
        self.inputs[key].insert(0, value)

    def setRadioDefault(self, groupKey, value):
        self.radios[groupKey][value].invoke()

    def setFileDefault(self, key, value):
        self.files[key] = value

    def setBoolDefault(self, key, value):
        widget = self.boolIns[key]
        current = 'selected' in widget.state()
        if current != value:
            widget.invoke()

    #----------------------------------------------------------------
    # Enabling / disabling input widgets

    def buttonState(self, key, state):
        try: self.buttons[key].state(['!disabled'] if state else ['disabled'])
        except KeyError: return False
        return True

    def fileButtonState(self, key, state):
        try: self.fileButtons[key].state(['!disabled'] if state else ['disabled'])
        except KeyError: return False
        return True

    def inputState(self, key, state):
        try: self.inputs[key]['state'] = 'normal' if state else 'disabled'
        except KeyError: return False
        return True

    def radioState(self, groupKey, radioValue, state):
        try: self.radios[groupKey][radioValue].state(['!disabled'] if state else ['disabled'])
        except KeyError: return False
        return True

    def boxState(self, key, state):
        try: self.boolIns[key].state(['!disabled'] if state else ['disabled'])
        except KeyError: return False
        return True

    #----------------------------------------------------------------
    # Other widgets related

    def onFileButton(self, btnKey, type, *args, **kwargs):
        if   type == 'openFile':    method = tkFile.askopenfile
        elif type == 'openFName':   method = tkFile.askopenfilename
        elif type == 'saveAsFName': method = tkFile.asksaveasfilename
        elif type == 'directory':   method = tkFile.askdirectory
        else: raise Exception(f'Invalid file button type "{type}"')
        filename = method(*args, **kwargs).name
        if filename != '':
            self.files[btnKey] = filename
        else:
            print('Invalid filename or cancelled')
