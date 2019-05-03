import tkinter as tk
from tkinter import ttk
from TkiWrapper.namespace import Namespace

class View:
    def __init__(self, root):
        self.root = root
        self.frame = ttk.Frame(root.backFrame)
        self.widgets = []
        self.role = 'content'

    #----------------------------------------------------------------
    # Appearance and Utilities

    def setRowWeights(self, *weights):
        for row, weight in enumerate(weights):
            self.frame.rowconfigure(row, weight=weight)

    def setColWeights(self, *weights):
        for col, weight in enumerate(weights):
            self.frame.columnconfigure(col, weight=weight)

    def show(self):
        row = {'header': 0, 'content': 1, 'footer': 2}[self.role]
        self.frame.grid(row=row, sticky=(tk.N, tk.S, tk.E, tk.W))

    def hide(self):
        self.frame.grid_forget()

    def setRole(self, role):
        role = role.lower()
        if role not in ['content', 'header', 'footer']:
            raise Exception(f'Invalid role {role} parameter')
        self.role = role

    #----------------------------------------------------------------
    # Static widgets

    def addLabel(self, grid, label, stretch=1):
        widget = ttk.Label(self.frame, text=label)
        widget.grid(**grid.getParams(stretch))
        self.widgets.append(widget)

    def addHeading(self, grid, label, level=2, stretch=1):
        if level < 1 or level > 3:
            raise Exception('Invalid heading level. Only 1-3 are supported.')
        widget = ttk.Label(self.frame, text=label, style=f'heading{level}.TLabel')
        widget.grid(**grid.getParams(stretch))
        self.widgets.append(widget)

    def addSeparator(self, grid, stretch=2):
        widget = ttk.Separator(self.frame)
        widget.grid(**grid.getParams(stretch))
        self.widgets.append(widget)

    #----------------------------------------------------------------
    # Data Output widgets

    def addTextOut(self, grid, outputKey, stretch=1):
        widget = ttk.Label(self.frame, text='-', style='output.TLabel')
        widget.grid(**grid.getParams(stretch))
        self.root.outputTexts[outputKey] = widget
        self.widgets.append(widget)

    def addBoolOut(self, grid, outputKey, stretch=1):
        widget = ttk.Checkbutton(self.frame, style='output.TCheckbutton')
        widget.grid(**grid.getParams(stretch))
        widget.invoke()
        widget.invoke()
        self.root.outputBools[outputKey] = widget
        self.widgets.append(widget)

    #----------------------------------------------------------------
    # Data Input widgets

    def addButton(self, grid, btnKey, label, onclick=None, args=[], enabled=True, stretch=1, **kwargs):
        if onclick is None: command = lambda: None
        else: command = lambda: onclick(*args, **kwargs)
        widget = ttk.Button(self.frame, text=label, command=command)
        widget.state(['!disabled'] if enabled else ['disabled'])
        widget.grid(**grid.getParams(stretch))
        self.root.buttons[btnKey] = widget
        self.widgets.append(widget)

    def addFileButton(self, grid, btnKey, type, label, *args, enabled=True, stretch=1, **kwargs):
        onclick = lambda: self.root.onFileButton(btnKey, type, *args, **kwargs)
        widget = ttk.Button(self.frame, text=label, command=onclick)
        widget.state(['!disabled'] if enabled else ['disabled'])
        widget.grid(**grid.getParams(stretch))
        self.root.fileButtons[btnKey] = widget
        self.widgets.append(widget)

    def addInput(self, grid, inpKey, password=False, enabled=True, stretch=1):
        show = '*' if password else ''
        state = 'normal' if enabled else 'disabled'
        widget = tk.Entry(self.frame, font=('Courier New', 12), show=show,
            disabledbackground='#AAA', state=state)
        widget.grid(**grid.getParams(stretch))
        self.root.inputs[inpKey] = widget
        self.widgets.append(widget)

    def addRadio(self, grid, groupKey, value, label, enabled=True, stretch=1):
        try: group = self.root.radioGroups[groupKey]
        except KeyError:
            raise Exception(f'Group "{groupKey}" does not exist. Please create it first')
        if group.command is not None: command = lambda: group.command(value)
        else: command = lambda: None
        state = 'normal' if enabled else 'disabled'
        widget = ttk.Radiobutton(self.frame, text=label, value=value,
            variable=group.variable, command=command, state=state)
        widget.grid(**grid.getParams(stretch))
        self.root.radios[groupKey][value] = widget
        self.widgets.append(widget)

    def addBoolIn(self, grid, boxKey, enabled=True, stretch=1):
        widget = ttk.Checkbutton(self.frame)
        widget.state(['!alternate'])
        widget.state(['!disabled'] if enabled else ['disabled'])
        widget.grid(**grid.getParams(stretch))
        self.root.boolIns[boxKey] = widget
        self.widgets.append(widget)

    #----------------------------------------------------------------
    # Other widget related methods

    def addWidget(self, grid, widget, stretch=1):
        widget.grid(**grid.getParams(stretch))
        self.widgets.append(widget)

    def createRadioGroup(self, key, varType, command=None):
        if varType not in ['int', 'flt', 'str']:
            raise Exception('Parameter varType must be one of: "int" "flt" "str"')
        if varType == 'int':   variable = tk.IntVar()
        elif varType == 'flt': variable = tk.DoubleVar()
        elif varType == 'str': variable = tk.StringVar()
        group = Namespace()
        group.variable = variable
        group.command = command
        self.root.radios[key] = {}
        self.root.radioGroups[key] = group

    #----------------------------------------------------------------
