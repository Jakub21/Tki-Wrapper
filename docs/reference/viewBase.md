# `Class ViewBase`
Wrapper around `ttk.Frame` class. View is frame with widgets.

Note that this class exists for inheritance purposes.
No instances of this class should be created.

## Methods

### Setting expansion weights

##### `setRowWeights`
Sets expand rate weights or view's rows
- Parameters
    - `int *weights` - Expand rates

##### `setColWeights`
Sets expand rate weights or view's columns
- Parameters
    - `int *weights` - Expand rates


### Adding static widgets

##### `addText`
Adds label. Label is static a text widget.
- Parameters
    - `Grid grid` - Object of grid class
    - `str label` - Text to put in widget
    - `int stretch = 1` - See Other Info section

##### `addHeading`
Adds heading. Heading is a widget with large static text.
- Parameters
    - `Grid grid` - Object of grid class
    - `str label` - Text to put in widget
    - `int level = 2` - Heading level. Only 1, 2 and 3 are supported.
    - `int stretch = 1` - See Other Info section

##### `addSeparator`
Adds horizontal separator (line).
- Parameters
    - `Grid grid` - Object of grid class
    - `int stretch = 2` - See Other Info section


### Adding output widgets

##### `addOutputText`
Adds text output widget.
- Parameters
    - `Grid grid` - Object of grid class
    - `str key` - Widget key
    - `str value = ''` - Widget value
    - `int stretch = 1` - See Other Info section


### Adding input widgets

##### `addButton`
Adds button widget.
- Parameters
    - `Grid grid` - Object of grid class
    - `str key` - Widget key
    - `str label` - Button label
    - `func onclick` - Function called on click
    - `bool enabled = True` Create enabled / disabed widget
    - `int stretch = 1` - See Other Info section

##### `addInputText`
Adds text input widget.
- Parameters
    - `Grid grid` - Object of grid class
    - `str key` - Widget key
    - `str password = False` - If `True` contents will be hidden
    - `bool enabled = True` Create enabled / disabed widget
    - `int stretch = 1` - See Other Info section

##### `addInputBool`
Adds boolean input widget (clickable checkbox).
- Parameters
    - `Grid grid` - Object of grid class
    - `str key` - Widget key
    - `str label = ''` - Widget label
    - `bool enabled = True` Create enabled / disabed widget
    - `int stretch = 1` - See Other Info section

##### `addInputCombo`
Adds ComboBox widget. This widget consists of text entry field and a drop-down menu.
User can choose one of the options from menu or type value into entry field.
- Parameters
    - `Grid grid` - Object of grid class
    - `str key` - Widget's key
    - `[str] values` - Values to put in drop-down menu.
    - `bool allowUnlisted = False` Allow user to type in value that is not
        in list of values
    - `bool enabled = True` Create enabled / disabed widget
    - `int stretch = 1` - See Other Info section

##### `addInputList`
Adds a List widget. This widget in a list of text lines that can be selected by user.
- Parameters
    - `Grid grid` - Object of grid class
    - `str key` - Widget's key
    - `[str] values` - List of string lines to put in widget
    - `str selMode` - Selection mode. See Other Info section
    - `bool enabled = True` Create enabled / disabed widget
    - `int stretch = 1` - See Other Info section

##### `addInputRadio`
Adds radio button widget. Note that radio group has to be created first
with `createRadioGroup` method.
- Parameters
    - `Grid grid` - Object of grid class
    - `str groupKey` - Radio group key
    - `str value` - Value assigned to group when this button is selected
    - `str label` - Button label
    - `bool enabled = True` Create enabled / disabed widget
    - `int stretch = 1` - See Other Info section

##### `addFileButton`
Adds file button widget. File buttons open dialog in which user can select
file, directory or unexisting file name. To get user's selection call root's
method `getFileVal` with same key as in this method.
- Parameters
    - `Grid grid` - Object of grid class
    - `str key` - Widget key
    - `str type` - Type of file dialog. More in Other Info section
    - `str label` - Button label
    - `dict fileParams` - Keywords passed to Tk method
        (see `reference/other-info`)
    - `bool enabled = True` Create enabled / disabed widget
    - `int stretch = 1` - See Other Info section
