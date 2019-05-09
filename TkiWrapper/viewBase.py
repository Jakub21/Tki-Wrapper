import tkinter as tk
from tkinter import ttk
from TkiWrapper.namespace import Namespace

class ViewBase:
    def __init__(self, root):
        self.root = root
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
    # Static widgets

    def addText(self, grid, label, stretch=1):
        widget = ttk.Label(self.frame , text=label)
        widget.grid(**grid.getParams(stretch))

    def addHeading(self, grid, label, level=2, stretch=1):
        if level < 1 or level > 3:
            raise Exception('Invalid heading level. Only 1-3 are supported.')
        widget = ttk.Label(self.frame, text=label, style=f'heading{level}.TLabel')
        widget.grid(**grid.getParams(stretch))

    def addSeparator(self, grid, stretch=2):
        widget = ttk.Separator(self.frame)
        widget.grid(**grid.getParams(stretch))

    #----------------------------------------------------------------
    # Data Output widgets

    def addOutputText(self, grid, key, value='', stretch=1):
        widget = ttk.Label(self.frame, text=value, style='output.TLabel')
        widget.grid(**grid.getParams(stretch))
        self.root.outWidgets.texts[key] = widget

    #----------------------------------------------------------------
    # Data Input widgets

    def addButton(self, grid, key, label, onclick=None, enabled=True, stretch=1):
        if onclick is None: command = lambda: None
        else: command = onclick
        widget = ttk.Button(self.frame, text=label, command=command)
        widget.state(['!disabled'] if enabled else ['disabled'])
        widget.grid(**grid.getParams(stretch))
        self.root.inWidgets.buttons[key] = widget

    def addInputText(self, grid, key, password=False, enabled=True, stretch=1):
        show = '*' if password else ''
        state = 'normal' if enabled else 'disabled'
        widget = tk.Entry(self.frame, font=('Courier New', 12), show=show,
            disabledbackground='#AAA', state=state)
        widget.grid(**grid.getParams(stretch))
        self.root.inWidgets.texts[key] = widget

    def addInputBool(self, grid, key, label, enabled=True, stretch=1):
        widget = ttk.Checkbutton(self.frame, text=label)
        widget.state(['!alternate'])
        widget.state(['!disabled'] if enabled else ['disabled'])
        widget.grid(**grid.getParams(stretch))
        self.root.inWidgets.bools[key] = widget

    def addInputRadio(self, grid, groupKey, value, label, enabled=True, stretch=1):
        try: group = self.root.inputData.radioGroups[groupKey]
        except KeyError:
            raise Exception(f'Group "{groupKey}" does not exist. Please create it first')
        if group.command is not None: command = lambda: group.command(value)
        else: command = lambda: None
        widget = ttk.Radiobutton(self.frame, text=label, value=value,
            variable=group.variable, command=command)
        widget.state(['!disabled'] if enabled else ['disabled'])
        widget.grid(**grid.getParams(stretch))
        self.root.inWidgets.radios[groupKey][value] = widget

    def addInputFile(self, grid, key, type, label, fileParams={}, enabled=True, stretch=1):
        onclick = lambda: self.root.onFileButton(key, type, **fileParams)
        widget = ttk.Button(self.frame, text=label, command=onclick)
        widget.state(['!disabled'] if enabled else ['disabled'])
        widget.grid(**grid.getParams(stretch))
        self.root.inWidgets.fileSelectors[key] = widget

    #----------------------------------------------------------------
