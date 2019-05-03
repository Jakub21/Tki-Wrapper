# Reference
TkiWrapper package reference.

Note that there are methods and attributes that are not listed in reference but
modifying / calling them manually may cause wrapper to fail.

At the end of this document there is Other Info section that contains
in-depth details that were too long to fit in reference.


### Table of contents
- [`Class Root`](#class-root)
    - [Constructor](#constructor)
    - [Root window configuration](#root-window-configuration)
    - [Managing views](#managing-views)
    - [Setting values of output widgets](#setting-values-of-output-widgets)
    - [Reading values of input widgets](#reading-values-of-input-widgets)
    - [Setting default values of input widgets](#setting-default-values-of-input-widgets)
    - [Enabling and disabling widgets](#enabling-and-disabling-widgets)
- [`Class View`](#class-view)
    - [Constructor](#constructor-1)
    - [Setting expanstion weights](#setting-expanstion-weights)
    - [Adding static widgets](#adding-static-widgets)
    - [Adding output widgets](#adding-output-widgets)
    - [Adding input widgets](#adding-input-widgets)
    - [Other widget - related methods](#other-widget---related-methods)
- [`Class Grid`](#class-grid)
    - [Constructor](#constructor-2)
    - [Pointer auto-increment options](#pointer-auto-increment-options)
    - [Widget pointer manipulation](#widget-pointer-manipulation)
    - [Setting default parameters](#setting-default-parameters)
- [Other Info](#other-info)



# `Class Root`
Wrapper around `tk.Tk` class. Manages root window parameters.
In the root window there are 3 main sections: Header, Main View and Footer.
There can be multiple views added but only one is visible at a time.

Root class also manages all input and output widgets added through views.

## Constructor
- No parameters

## Methods

### Root window configuration

##### `setTitle`
Sets window title.
- Parameters
    - str `title` - Title string

##### `setIcon`
Sets window icon.
- Parameters
    - path `path` - Image's path

##### `setWindowSize`
Sets starting window size. Does not disable window resizing.
- Parameters
    - int `x` - Window's width
    - int `y` - Window's height

##### `setMinSize`
Sets minimum window size. Window can not be resized under those values.
- Parameters
    - int `x` - Window's min width
    - int `y` - Window's min height


### Managing views

##### `addView`
Adds app view.
- Parameters
    - View `view` - View object to be added
    - str `key` - View's key

##### `showView`
Hides other views and displays one with specified key.
- Parameters
    - str `key` - View's key

##### `setHeader`
Add view as header. Header is always visible on top of the window.
- Parameters
    - View `view` - View object to be added as header

##### `setFooter`
Add view as footer. Footer is always visible on bottom of the window.
- Parameters
    - View `view` - View object to be added as header

##### `setSectionWeights`
Sets vertical expand weights. By default those values are `0` for header and footer
and `1` for main view.
- Parameters
    - int `header` - Header's weight
    - int `content` - Main view's weight
    - int `footer` - Footer's weight


### Setting values of output widgets

##### `setOutputText`
Sets value of text output widget.
- Parameters
    - str `key` - Widget's key
    - str `value` - Text to put in widget

##### `setOutputBool`
Sets value of boolean output widget.
- Parameters
    - str `key` - Widget's key
    - bool `value` - Set widget's value to this


### Reading values of input widgets

##### `getInputVal`
Returns value of text input widget.
- Parameters
    - str `key` - Widget's key
- Returns
    - str - Text written by user

##### `getRadioVal`
Returns value of radio buttons group.
- Parameters
    - str `groupKey` - Radio group's key
- Returns
    - str - Boolean chosen by user

##### `getFileVal`
Returns path that was supplied through file button.
- Parameters
    - str `btnKey` - Button's key
- Returns
    - path - Path supplied by user

##### `getBoolVal`
Returns value of boolean input widget.
- Parameters
    - str `key` - Widget's key
- Returns
    - str - Boolean chosen by user


### Setting default values of input widgets

##### `setInputDefault`
Sets default value of input widget.
- Parameters
    - str `key` - Widget's key
    - str `value` - Text to put in widget

##### `setRadioDefault`
Sets default value of input widget.
- Parameters
    - str `groupKey` - Radio group's key
    - str `value` - Value of button that is to be marked

##### `setFileDefault`
Sets default value of input widget.
- Parameters
    - str `key` - Widget's key
    - str `value` - File path

##### `setBoolDefault`
Sets default value of input widget.
- Parameters
    - str `key` - Widget's key
    - bool `value` - Selected or unselected


### Enabling and disabling widgets

##### `buttonState`
Enables or disables button.
- Parameters
    - str `key` - Widget's key
    - bool `state` - `True` - Enabled, `False` - Disabled

##### `fileButtonState`
Enables or disables file button.
- Parameters
    - str `key` - Widget's key
    - bool `state` - `True` - Enabled, `False` - Disabled

##### `inputState`
Enables or disables input.
- Parameters
    - str `key` - Widget's key
    - bool `state` - `True` - Enabled, `False` - Disabled

##### `radioState`
Enables or disables radio button.
- Parameters
    - str `key` - Widget's key
    - bool `state` - `True` - Enabled, `False` - Disabled

##### `boxState`
Enables or disables boolean input widget.
- Parameters
    - str `key` - Widget's key
    - bool `state` - `True` - Enabled, `False` - Disabled



# `Class View`
Wrapper around `ttk.Frame` class. View is frame with widgets.

## Constructor
- Parameters
    - Root `root` - App's root window

## Methods


### Setting expansion weights

##### `setRowWeights`
Sets expand rate weights or view's rows
- Parameters
    - int  `*weights` - Expand rates

##### `setColWeights`
Sets expand rate weights or view's columns
- Parameters
    - int  `*weights` - Expand rates


### Adding static widgets

##### `addLabel`
Adds label. Label is static a text widget.
- Parameters
    - Grid `grid` - Object of grid class
    - str `label` - Text to put in widget
    - int `stretch = 1` - See Other Info section

##### `addHeading`
Adds heading. Heading is a widget with large static text.
- Parameters
    - Grid `grid` - Object of grid class
    - str `label` - Text to put in widget
    - int `level = 2` - Heading level. Only 1, 2 and 3 are supported.
    - int `stretch = 1` - See Other Info section

##### `addSeparator`
Adds horizontal separator (line).
- Parameters
    - Grid `grid` - Object of grid class
    - int `stretch = 2` - See Other Info section


### Adding output widgets

##### `addTextOut`
Adds text output widget.
- Parameters
    - Grid `grid` - Object of grid class
    - str `outputKey` - Widget key
    - int `stretch = 1` - See Other Info section

##### `addBoolOut`
Adds boolean output widget.
- Parameters
    - Grid `grid` - Object of grid class
    - str `outputKey` - Widget key
    - int `stretch = 1` - See Other Info section


### Adding input widgets

##### `addButton`
Adds button widget.
- Parameters
    - Grid `grid` - Object of grid class
    - str `btnKey` - Widget key
    - str `label` - Button label
    - func `onclick` - Function called on click
    - list `args` - Args passed to `onclick` function
    - bool `enabled = True` Create enabled / disabed widget
    - int `stretch = 1` - See Other Info section
    - `**kwargs` - Keywords passed to `onclick` function

##### `addFileButton`
Adds file button widget. File buttons open dialog in which user can select
file, directory or unexisting file name. To get user's selection call root's
method `getFileVal` with same key as in this method.
- Parameters
    - Grid `grid` - Object of grid class
    - str `btnKey` - Widget key
    - str `type` - Type of file dialog. More in Other Info section
    - str `label` - Button label
    - list `args` - Args passed to `onclick` function
    - bool `enabled = True` Create enabled / disabed widget
    - int `stretch = 1` - See Other Info section
    - `**kwargs` - Keywords passed to `onclick` function

##### `addInput`
Adds text input widget.
- Parameters
    - Grid `grid` - Object of grid class
    - str `inpKey` - Widget key
    - str `password = False` - If `True` contents will be hidden
    - bool `enabled = True` Create enabled / disabed widget
    - int `stretch = 1` - See Other Info section

##### `addRadio`
Adds radio button widget. Note that radio group has to be created first
with `createRadioGroup` method.
- Parameters
    - Grid `grid` - Object of grid class
    - str `groupKey` - Radio group key
    - str `value` - Value assigned to group when this button is selected
    - str `label` - Button label
    - bool `enabled = True` Create enabled / disabed widget
    - int `stretch = 1` - See Other Info section

##### `addBoolIn`
Adds boolean input widget (clickable checkbox).
- Parameters
    - Grid `grid` - Object of grid class
    - str `boxKey` - Widget key
    - bool `enabled = True` Create enabled / disabed widget
    - int `stretch = 1` - See Other Info section


### Other widget - related methods

##### `addWidget`
Adds pre-defined widget.
Only use if result can not be recreated with other add methods.
- Parameters
    - Grid `grid` - Object of grid class
    - TkInter Widget `widget` - Widget to add to view
    - int `stretch = 1` - See Other Info section

##### `createRadioGroup`
Creates radio button group. This is required to add radio buttons.
- Parameters
    - str `key` - Group key
    - str `varType` - Variable type (one of: `int`, `flt`, `str`)
    - func `command` - Command called when button from group is clicked



# `Class Grid`
Grid class manages position, grid span, margin and padding of widgets.
When widget is added, its position is taken from object of Grid class.
All parameters set in grid object affect next added widget(s).

## Constructor
- No parameters

## Methods

### Pointer auto-increment options

##### `setIncrementWrap`
When pointer auto increment reaches some column it will automatically
move to column 0 in the next row. This specifies the column.
- Parameters
    - int `width` - Amount of columns to wrap at


### Widget pointer manipulation

##### `resetPointer`
Sets pointer position to `x = 0, y = 0` and resets span.
Recommended to use after creating view when re-using grid in other views.
- No parameters

##### `setPointer`
Moves pointer to position and changes span.
- Parameters
    - int `x` - Grid column to put next widget in
    - int `y` - Grid row to put next widget in
    - int `spanX = 1` - Horizontal span
    - int `spanY = 1` - Vertical span

##### `setSpan`
Changes span.
- Parameters
    - int `spanX = 1` - Horizontal span
    - int `spanY = 1` - Vertical span

##### `newLine`
Move pointer to column 0 of the row below
- No parameters

##### `shiftX`
Move pointer to the right (Auto wrap enabled)
- Parameters
    - int `amount = 1` - Amount of steps

### Setting default parameters

##### `setMargin`
Sets default widget outer margin
- Parameters
    - int `x` - Horizontal margin
    - int `y` - Vertical margin

##### `setPadding`
Sets default widget inner margin (padding)
- Parameters
    - int `x` - Horizontal padding
    - int `y` - Vertical padding



# Other Info

##### Expand rate weights
Expand rates of section when window is larger than size propagated
by grid manager (when root's minimum size is not set, app starts with this size).
`0` means no expansion.
For example section with weight `2` will expand twice as fast
as section with weight `1`.

##### `Stretch` widget parameter
This parameter manages placement and size of widgets.
With value `1` widgets stick to North-West corner of the grid cell they occupy
and occupy as small space as they can.
With value `2` widgets stick to all walls of the cell and expand to fill whole cell.  
**TODO**: value `0`.

##### File dialog types
Dialog type affects dialog window title, button labels, wildcards and validation.
Buttons onclicks call functions from `tkinter.filedialog` module.
- `openFile` button calls `askopenfile` function
- `openFName` button calls `askopenfilename` function
- `saveAsFName` button calls `asksaveasfilename` function
- `directory` button calls `askdirectory` function
