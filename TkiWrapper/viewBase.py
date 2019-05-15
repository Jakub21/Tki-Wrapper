import tkinter as tk
from tkinter import ttk
from TkiWrapper.namespace import Namespace
from TkiWrapper.grid import Grid

class ViewBase:
    def __init__(self, root, positioner=None):
        self.root = root
        if positioner is None:
            positioner = Grid()
        self.positioner = positioner

        self.frame = ttk.Frame(root.backFrame)
        self.displayRow = 1
        self.isSpecial = False
        self.dialogs = {}

    #----------------------------------------------------------------
    # Appearance

    def setRowWeights(self, *weights):
        for row, weight in enumerate(weights):
            self.frame.rowconfigure(row, weight=weight)

    def setColWeights(self, *weights):
        for col, weight in enumerate(weights):
            self.frame.columnconfigure(col, weight=weight)

    #----------------------------------------------------------------
    # Displaying, view type and role

    def hide(self):
        self.frame.grid_forget()

    def show(self):
        self.frame.grid(row=self.displayRow, sticky=(tk.N, tk.S, tk.E, tk.W))

    def setDisplayRow(self, row):
        '''Called by root when assigned as header or footer'''
        self.displayRow = row

    def setSpecial(self, state):
        '''Called by root when assigned as header or footer'''
        self.isSpecial = state

    #----------------------------------------------------------------
    # Positioner

    def setPositioner(self, positioner):
        self.positioner = positioner

    #----------------------------------------------------------------
    # Static widgets

    def addText(self, label, stretch=1):
        widget = ttk.Label(self.frame , text=label)
        widget.grid(**self.positioner.getParams(stretch))

    def addHeading(self, label, level=2, stretch=1):
        if level < 1 or level > 3:
            raise Exception('Invalid heading level. Only 1-3 are supported.')
        widget = ttk.Label(self.frame, text=label, style=f'heading{level}.TLabel')
        widget.grid(**self.positioner.getParams(stretch))

    def addSeparator(self, stretch=2):
        widget = ttk.Separator(self.frame)
        widget.grid(**self.positioner.getParams(stretch))

    #----------------------------------------------------------------
    # Data Output widgets

    def addOutputText(self, key, value='', stretch=1):
        widget = ttk.Label(self.frame, text=value, style='output.TLabel')
        widget.grid(**self.positioner.getParams(stretch))
        self.root.outWidgets.texts[key] = widget

    #----------------------------------------------------------------
    # Data Input widgets

    def addButton(self, key, label, onclick=None, enabled=True, stretch=1):
        if onclick is None: command = lambda: None
        else: command = onclick
        widget = ttk.Button(self.frame, text=label, command=command)
        widget.state(['!disabled'] if enabled else ['disabled'])
        widget.grid(**self.positioner.getParams(stretch))
        self.root.inWidgets.buttons[key] = widget

    def addInputText(self, key, password=False, enabled=True, stretch=1):
        show = '*' if password else ''
        state = 'normal' if enabled else 'disabled'
        style = self.root.style
        if style is None:
            raise Exception('Please apply style to root first')
        font = (style.fontFam.mono, style.fontSize['textInput'])
        widget = tk.Entry(self.frame, font=font, show=show,
            disabledbackground=style.colors.disabled, state=state)
        widget.grid(**self.positioner.getParams(stretch))
        self.root.inWidgets.texts[key] = widget

    def addInputBool(self, key, label='', enabled=True, stretch=1):
        widget = ttk.Checkbutton(self.frame, text=label)
        widget.state(['!alternate'])
        widget.state(['!disabled'] if enabled else ['disabled'])
        widget.grid(**self.positioner.getParams(stretch))
        self.root.inWidgets.bools[key] = widget

    def addInputCombo(self, key, values, allowUnlisted=False, enabled=True, stretch=1):
        widget = ttk.Combobox(self.frame, values=values, exportselection=0)
        widget.state(['!disabled'] if enabled else ['disabled'])
        widget.grid(**self.positioner.getParams(stretch))
        self.root.inWidgets.combos[key] = widget
        self.root.inputData.combos[key] = Namespace(
            allowUnlisted = allowUnlisted,
            values=values,
        )

    def addInputList(self, key, values, selMode='browse', enabled=True, stretch=1):
        state = 'normal' if enabled else 'disabled'
        selMode = {
            'browse': tk.BROWSE,
            'single': tk.SINGLE,
            'multiple': tk.MULTIPLE,
            'extended': tk.EXTENDED,
        }[selMode]
        style = self.root.style
        if style is None:
            raise Exception('Please apply style to root first')
        font = (style.fontFam.mono, style.fontSize['listInput'])
        widget = tk.Listbox(self.frame, font=font, state=state, selectmode=selMode)
        widget.insert(0, *values)
        widget.grid(**self.positioner.getParams(stretch))
        self.root.inWidgets.lists[key] = widget

    def addInputRadio(self, groupKey, value, label, enabled=True, stretch=1):
        try: group = self.root.inputData.radioGroups[groupKey]
        except KeyError:
            raise Exception(f'Group "{groupKey}" does not exist. Please create it first')
        if group.command is not None: command = lambda: group.command(value)
        else: command = lambda: None
        widget = ttk.Radiobutton(self.frame, text=label, value=value,
            variable=group.variable, command=command)
        widget.state(['!disabled'] if enabled else ['disabled'])
        widget.grid(**self.positioner.getParams(stretch))
        self.root.inWidgets.radios[groupKey][value] = widget

    def addInputFile(self, key, type, label, fileParams={}, enabled=True, stretch=1):
        onclick = lambda: self.root.onFileButton(key, type, **fileParams)
        widget = ttk.Button(self.frame, text=label, command=onclick)
        widget.state(['!disabled'] if enabled else ['disabled'])
        widget.grid(**self.positioner.getParams(stretch))
        self.root.inWidgets.fileSelectors[key] = widget

    #----------------------------------------------------------------
