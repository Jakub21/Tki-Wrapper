import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as tkFile
from TkiWrapper.namespace import Namespace

class Root:
    def __init__(self):
        self.initTkinter()
        self.configBackFrame()
        self.views = {}
        self.leave = False
        self.inWidgets = Namespace(
            texts = {},
            bools = {},
            combos = {},
            lists = {},
            buttons = {},
            radios = {},
            fileSelectors = {},
        )
        self.outWidgets = Namespace(
            texts = {},
        )
        self.inputData = Namespace(
            combos = {},
            radioGroups = {},
            files = {},
        )
        self.style = None

    #----------------------------------------------------------------
    # General core methods

    def update(self):
        if not self.leave:
            self.root.update()

    def quit(self):
        self.root.destroy()
        self.leave = True

    #----------------------------------------------------------------
    # Constructor sub-methods

    def initTkinter(self):
        self.root = tk.Tk()
        self.backFrame = ttk.Frame(self.root)
        self.root.protocol('WM_DELETE_WINDOW', self.quit)

    def configBackFrame(self):
        self.backFrame.columnconfigure(0, weight=1)
        self.setSectionWeights(0, 1, 0)
        self.backFrame.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

    #----------------------------------------------------------------
    # Root window configuration

    def setTitle(self, title):
        self.root.title(title)

    def setIcon(self, path):
        self.root.iconbitmap(path)

    def setWindowSize(self, x, y):
        self.root.geometry(f'{x}x{y}')

    def setMinSize(self, x, y):
        self.root.minsize(x, y)

    def setSectionWeights(self, header, content, footer):
        self.backFrame.rowconfigure(0, weight=header)
        self.backFrame.rowconfigure(1, weight=content)
        self.backFrame.rowconfigure(2, weight=footer)

    #----------------------------------------------------------------
    # Adding views

    def addView(self, view, key):
        self.views[key] = view

    def setHeader(self, view, role='m'):
        if role not in ['m', 'd']:
            raise Exception('Invalid header role')
        if role == 'm':
            self.headerMain = view
        elif role == 'd':
            self.headerDialog = view
        view.setDisplayRow(0)
        view.setSpecial(True)

    def setFooter(self, view, role='m'):
        if role not in ['m', 'd']:
            raise Exception('Invalid footer role')
        if role == 'm':
            self.footerMain = view
        elif role == 'd':
            self.footerDialog = view
        view.setDisplayRow(2)
        view.setSpecial(True)

    #----------------------------------------------------------------
    # Displaying views

    def switchToView(self, key):
        for k, view in self.views.items():
            view.hide()
        self.views[key].show()
        self.currentView = key

    def dialogMode(self, state):
        if state: # Switch to dialog mode
            try:
                self.headerMain.hide()
                self.headerDialog.show()
            except AttributeError:
                try: self.headerMain.show()
                except AttributeError: pass
            try:
                self.footerMain.hide()
                self.footerDialog.show()
            except AttributeError:
                try: self.footerMain.show()
                except AttributeError: pass
        else: # Swtich to normal mode
            try:
                self.headerMain.show()
                self.headerDialog.hide()
            except AttributeError:
                try: self.headerMain.show()
                except AttributeError: pass
            try:
                self.footerMain.show()
                self.footerDialog.hide()
            except AttributeError:
                try: self.footerMain.show()
                except AttributeError: pass

    def dialogEnd(self):
        '''Make this method an onclick of "back" button in dialog header'''
        self.views[self.currentView].dialogEnd()

    #----------------------------------------------------------------
    # Setting output widgets' values

    def setOutputText(self, key, value):
        self.outWidgets.texts[key]['text'] = f'{value}'

    #----------------------------------------------------------------
    # Reading input widgets' values

    def readInputText(self, key):
        return self.inWidgets.texts[key].get()

    def readInputBool(self, key):
        return 'selected' in self.inWidgets.bools[key].state()

    def readInputCombo(self, key):
        meta = self.inputData.combos[key]
        if meta.allowUnlisted:
            return self.inWidgets.combos[key].get()
        else:
            index = self.inWidgets.combos[key].current()
            if index == -1: raise IndexError('Invalid Choice')
            return meta.values[index]

    def readInputList(self, key):
        widget = self.inWidgets.lists[key]
        selection = list(widget.curselection())
        return [widget.get(i) for i in selection]

    def readInputRadio(self, groupKey):
        return self.inputData.radioGroups[groupKey].variable.get()

    def readInputFile(self, key):
        return self.inputData.files[key]

    #----------------------------------------------------------------
    # Setting input widgets' default values

    def defaultInputText(self, key, value):
        self.inWidgets.texts[key].delete(0, tk.END)
        self.inWidgets.texts[key].insert(0, value)

    def defaultInputBool(self, key, value):
        widget = self.inWidgets.bools[key]
        current = 'selected' in widget.state()
        if current != value:
            widget.invoke()

    def defaultInputCombo(self, key, value):
        widget = self.inWidgets.combos[key]
        meta = self.inputData.combos[key]
        if not meta.allowUnlisted and value not in meta.values:
            raise IndexError(f'Value "{value}" was not found in allowed list')
        widget.delete(0, tk.END)
        widget.insert(0, value)

    def defaultInputRadio(self, groupKey, value):
        self.inWidgets.radios[groupKey][value].invoke()

    def defaultInputFile(self, key, value):
        self.inputData.files[key] = value

    #----------------------------------------------------------------
    # Enabling / disabling input widgets

    def stateButton(self, key, state):
        self.inWidgets.buttons[key].state(['!disabled'] if state else ['disabled'])

    def stateInputText(self, key, state):
        self.inWidgets.texts[key]['state'] = 'normal' if state else 'disabled'

    def stateInputBool(self, key, state):
        try: self.inWidgets.bools[key].state(['!disabled'] if state else ['disabled'])
        except KeyError: return False
        return True

    def stateInputRadio(self, groupKey, radioValue, state):
        state = ['!disabled'] if state else ['disabled']
        self.inWidgets.radios[groupKey][radioValue].state(state)

    def stateInputFile(self, key, state):
        self.inWidgets.fileSelectors[key].state(['!disabled'] if state else ['disabled'])

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
            self.inputData.files[btnKey] = filename
        # else cancelled

    def createRadioGroup(self, key, varType, command=None):
        if varType not in ['int', 'flt', 'str']:
            raise Exception('Parameter varType must be one of: "int" "flt" "str"')
        if varType == 'int':   variable = tk.IntVar()
        elif varType == 'flt': variable = tk.DoubleVar()
        elif varType == 'str': variable = tk.StringVar()
        group = Namespace()
        group.variable = variable
        group.command = command
        self.inWidgets.radios[key] = {}
        self.inputData.radioGroups[key] = group

    #----------------------------------------------------------------
