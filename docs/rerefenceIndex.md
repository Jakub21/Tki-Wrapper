# Reference Index
TkiWrapper package reference.

Note that there are methods and attributes that are not listed in reference but
modifying / calling them manually may cause wrapper to fail.

At the end of this document there is Other Info section that contains
in-depth details that were too long to fit in reference.


## Classes reference
- [`Class Root`](reference/root.md)
- [`Class ViewBase`](reference/viewBase.md)
    - [`Class View`](reference/view.md) (not available yet)
    - [`Class Dialog`](reference/dialog.md) (not available yet)
- [`Class Grid`](reference/grid.md)


## Other Info
Other info that could be useful in understanding features of this package.

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
