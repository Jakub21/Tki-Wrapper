# `Class Grid`
Grid class manages position, grid span, margin and padding of widgets.
When widget is added, its position is taken from object of Grid class.
All parameters set in grid object affect next added widget(s).

## Constructor
- No parameters

## Methods

### Pointer auto-increment settings

##### `setColWrap`
When pointer auto increment reaches some column it will automatically
move to column 0 in the next row. This specifies the column.
- Parameters
    - `int width` - Amount of columns to wrap at


### Widget pointer manipulation

##### `resetPointer`
Sets pointer position to `x = 0, y = 0` and resets span.
Recommended to use after creating view when re-using grid in other views.
- No parameters

##### `setPointer`
Moves pointer to some absolute position and changes span.
- Parameters
    - `int x` - Grid column to put next widget in
    - `int y` - Grid row to put next widget in
    - `int spanX = 1` - Horizontal span
    - `int spanY = 1` - Vertical span

##### `setSpan`
Changes span of next added element.
- Parameters
    - `int spanX = 1` - Horizontal span
    - `int spanY = 1` - Vertical span

##### `newLine`
Move pointer 1 row down to first column
- No parameters

##### `shift`
Move pointer to the right by some amount of cells (Auto wrap enabled)
- Parameters
    - `int amount = 1` - Amount of steps


### Default margin settings

##### `setMargin`
Sets default widget outer margin
- Parameters
    - `int x` - Horizontal margin
    - `int y` - Vertical margin

##### `setPadding`
Sets default widget inner margin (padding)
- Parameters
    - `int x` - Horizontal padding
    - `int y` - Vertical padding
