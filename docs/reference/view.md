# `Class View`
Inherits from [`Class ViewBase`](`viewBase.md`)

## Constructor
- Parameters
    - `Root root` - App's root window
    - `obj positioner = None` - Widget positioner

## Mehods

##### `showDialog`
Call this method to activate dialog mode.
Dialog will be displayed in place where this view was placed.
- Parameters
    - `str key` - Dialog's key

##### `addDialog`
Adds dialog view to view.
- Parameters
    - `Dialog dlgView` - Dialog view
    - `str key` - Dialog's key
