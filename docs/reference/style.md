# `Class Style`
Style class manages widgets appearance. It's basically a wrapper of `ttk.Style`
but in this wrapper styles affect both `Tk` and `TTK` widgets.

**NOTE** Default font families are Windows fonts.
To make your app work properly on non-Windows mashines please change the fonts.


## Constructor
- No parameters

## Methods

##### `apply`
Applies styles to root and widgets.
This method should be called before adding any widgets.
- Parameters
    - `Root root` - Root object to apply styles to


### Attribute setters - Font

##### `setFontSize`
Sets font size for specified widget type
- Parameters
    - `str key` - Widget type key,
    valid values are keys of `fontSize` dictionary (`Defaults` section)
    - `int size` - Font size in pixels

##### `setStdFont`
Sets font family for static widgets and buttons
- Parameters
    - `str family` - Font family name

##### `setMonoFont`
Sets font family for input and output widgets
- Parameters
    - `str family` - Font family name


### Attribute setters - Font

##### `setBgColor`
Sets background color of the window
- Parameters
    - `hexColor color` - Color to set

##### `setFgColor`
Sets foreground color of all widgets except buttons
- Parameters
    - `hexColor color` - Color to set

##### `setDisabledColor`
Sets background color of disabled `Input` and `List` widgets
- Parameters
    - `hexColor color` - Color to set


### Other setters

##### `useTheme`
Sets base `TTK` theme.
- Parameters
    - `str theme` - Theme name

##### `setBtnWidth`
Sets constant button width.
- Parameters
    - `int width` - Button width in characters


## Defaults

##### Font size
```python
fontSize = {
    'heading1': 25,
    'heading2': 20,
    'heading3': 15,
    'label': 11,
    'output':12,
    'button': 10,
    'radio': 11,
    'checkbox': 11,
    'textInput': 12,
    'listInput': 12
}
```

##### Font family
```python
fontFam.std = 'Verdana'
fontFam.mono = 'Courier New'
```

##### Colors
```python
colors.bg = '#CFCFCF'
colors.fg = '#000'
colors.disabled = '#AAA'
```
