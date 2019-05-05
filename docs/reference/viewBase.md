# `Class ViewBase`
Wrapper around `ttk.Frame` class. View is frame with widgets.

Note that this class exists for inheritance purposes.
No instances of this class should be created.

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
