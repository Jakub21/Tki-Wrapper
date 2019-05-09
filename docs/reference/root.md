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

##### `setSectionWeights`
Sets vertical expand weights. By default those values are `0` for header and footer
and `1` for main view.
- Parameters
    - int `header` - Header's weight
    - int `content` - Main view's weight
    - int `footer` - Footer's weight


### Managing views

##### `addView`
Adds app view.
- Parameters
    - View `view` - View object to be added
    - str `key` - View's key

##### `setHeader`
Add view as header. Header is always visible on top of the window.
- Parameters
    - View `view` - View object to be added as header
    - str `role = 'm'` - Header role (`'m'` - main, `'d'` - dialog);
        `main header` is always displayed but if `dialog header` is set, it is
        displayed instad when user enters dialog

##### `setFooter`
Add view as footer. Footer is always visible on bottom of the window.
- Parameters
    - View `view` - View object to be added as header
    - str `role = 'm'` - Footer role (`'m'` - main, `'d'` - dialog);
        `main footer` is always displayed but if `dialog footer` is set, it is
        displayed instad when user enters dialog

##### `switchToView`
Hides other views and displays one with specified key.
- Parameters
    - str `key` - View's key


### Setting values of output widgets

##### `setOutputText`
Sets value of text output widget.
- Parameters
    - str `key` - Widget's key
    - str `value` - Text to put in widget


### Reading values of input widgets

##### `readInputText`
Returns value of text input widget.
- Parameters
    - str `key` - Widget's key
- Returns
    - str - Text written by user

##### `readInputBool`
Returns value of boolean input widget.
- Parameters
    - str `key` - Widget's key
- Returns
    - bool - Boolean chosen by user

##### `readInputRadio`
Returns value of radio buttons group.
- Parameters
    - str `groupKey` - Radio group's key
- Returns
    - str - Boolean chosen by user

##### `readInputFile`
Returns path that was supplied through file button.
- Parameters
    - str `key` - Button's key
- Returns
    - path - Path supplied by user


### Setting default values of input widgets

##### `defaultInputText`
Sets default value of input widget.
- Parameters
    - str `key` - Widget's key
    - str `value` - Text to put in widget

##### `defaultInputBool`
Sets default value of input widget.
- Parameters
    - str `key` - Widget's key
    - bool `value` - Selected or unselected

##### `defaultInputRadio`
Sets default value of input widget.
- Parameters
    - str `groupKey` - Radio group's key
    - str `value` - Value of button that is to be marked

##### `defaultInputFile`
Sets default value of input widget.
- Parameters
    - str `key` - Widget's key
    - str `value` - File path


### Enabling and disabling widgets

##### `stateButton`
Enables or disables button.
- Parameters
    - str `key` - Widget's key
    - bool `state` - `True` - Enabled, `False` - Disabled

##### `stateInputText`
Enables or disables input.
- Parameters
    - str `key` - Widget's key
    - bool `state` - `True` - Enabled, `False` - Disabled

##### `stateInputBool`
Enables or disables boolean input widget.
- Parameters
    - str `key` - Widget's key
    - bool `state` - `True` - Enabled, `False` - Disabled

##### `stateInputRadio`
Enables or disables radio button.
- Parameters
    - str `groupKey` - Radio group's key
    - str `radioValue` - Radio's value
    - bool `state` - `True` - Enabled, `False` - Disabled

##### `stateInputFile`
Enables or disables file button.
- Parameters
    - str `key` - Widget's key
    - bool `state` - `True` - Enabled, `False` - Disabled


### Other widget methods

##### `createRadioGroup`
Creates radio button group. This is required to add radio buttons.
- Parameters
    - str `key` - Group key
    - str `varType` - Variable type (one of: `int`, `flt`, `str`)
    - func `command` - Command called when button from group is clicked
