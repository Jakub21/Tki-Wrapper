# Package Guide
TkiWrapper package guide.

This section describes how to start project that utilizes this package.
Knowledge of Python 3 is assumed.

Attached screenshots were made on Windows.

### Creating app base
This code creates Hello World app that will be further developed.
```python
import TkiWrapper as tkw

if __name__ == '__main__':
    root = tkw.Root() # Create app root
    root.setTitle('My First App')

    grid = tkw.Grid() # Grid object for managing widget positions
    grid.setIncrementWrap(1) # Widgets will occupy only 1 column

    header = tkw.View(root) # Create header view
    root.setHeader(header) # Add header to root
    header.addHeading(grid, 'My First App', level=1) # Add lv.1 heading to header
    header.addSeparator(grid)
    grid.resetPointer() # Do this if this grid will be used in another view

    footer = tkw.View(root) # Create footer view
    root.setFooter(footer) # Add footer to root
    footer.addSeparator(grid)
    footer.addLabel(grid, 'Created by me, just now. Version 1') # Add static text
    grid.resetPointer() # Do this if this grid will be used in another view

    view1 = tkw.View(root) # Create center-frame view
    root.addView(view1, 'home') # Add view under "home" key
    view1.addHeading(grid, 'Hello World') # Default heading level is 2

    root.showView('home') # Start app with this view shown

    while not root.leave:
        root.update()
        # A loop like this will continue unless app is closed
        # or user presses Ctrl-C in console in which code was executed
        # You can add other things your app should do every frame
```

![Screenshot](screenshots/screenshot1_1.png)

This app lacks styling, configuration of expansion weights and many more to look good.
Unfortunatelly **styling wrapper is not yet done** and usage of raw TkInter styles is required.

Copy and paste this function (preferably in separate file to avoid spaghetti)
and call it after root object is created and configured.

I will not explain what this code does because it's plain TkInter.
Additionally I'm planning to add wrapper to styles so this will be eventually replaced.

```python
from tkinter import ttk

def styleWidgets():
    background = '#242932'
    foreground = '#FFFFFF'
    fontFamNormal = 'Verdana'
    fontFamMonospace = 'Courier New'
    fontLabel = 11
    fontOutput = 12
    fontButton = 10
    fontRadio = 11
    fontHeading3 = 15
    fontHeading2 = 20
    fontHeading1 = 25
    style = ttk.Style()
    style.theme_use('vista')
    style.configure('TFrame',
        background=background)
    style.configure('TLabel',
        background=background, foreground=foreground,
        font=(fontFamNormal, fontLabel))
    style.configure('heading1.TLabel',
        font=(fontFamNormal, fontHeading1))
    style.configure('heading2.TLabel',
        font=(fontFamNormal, fontHeading2))
    style.configure('heading3.TLabel',
        font=(fontFamNormal, fontHeading3))
    style.configure('output.TLabel',
        font=('Courier New', fontOutput))
    style.configure('TButton',
        background=background, width=11, font=(fontFamNormal, fontButton))
    style.configure('TRadiobutton',
        background=background, foreground=foreground,
        font=(fontFamNormal, fontRadio))
    style.configure('TCheckbutton',
        background=background, foreground=foreground)
    style.configure('TSeparator',
        background=background, foreground=foreground)
```

![Screenshot](screenshots/screenshot2_2.png)

Styles were added. Execute the code again, check results.


### Improving the app
The next step is to add more widgets and see how expansion weights affect the app.
I will also split up the code info functions to avoid pasting the came code multiple times.

Note that root variable was made global. Root will have to be accessible
from every place so either make it a global or use OOP and make root a member of
some application class.

```python
import TkiWrapper as tkw

# replace "style" with name of file with styling function
from style import styleWidgets

def createHeader(root):
    '''Create and fill header view'''
    grid = tkw.Grid()
    header = tkw.View(root)
    header.setColWeights(1)
    root.setHeader(header)
    header.addHeading(grid, 'My First App', level=1)
    header.addSeparator(grid)

def createFooter(root):
    '''Create and fill footer view'''
    grid = tkw.Grid()
    footer = tkw.View(root)
    footer.setColWeights(1)
    root.setFooter(footer)
    footer.addSeparator(grid)
    footer.addLabel(grid, 'Created by me, just now. Version 1.1')
    grid.resetPointer()

def createHomeView(root):
    grid = tkw.Grid()
    view = tkw.View(root)
    view.setColWeights(1)
    root.addView(view, 'home')
    view.addHeading(grid, 'Hello World')

if __name__ == '__main__':
    global root
    root = tkw.Root()
    root.setTitle('My First App')
    styleWidgets()

    createHeader(root)
    createFooter(root)
    createHomeView(root)
    root.showView('home')

    while not root.leave:
        root.update()
```

![Screenshot](screenshots/screenshot2.png)

This code creates much better looking application.
Still, there is not much content in there.


### Creating interactive app
In next step I will create something more interactive.
There will be an input field, output text and a button.
Pressing a button will read contents of input field, reverse it and paste in output.

First, create required widgets in `home` view.

```python
def createHomeView(root):
    grid = tkw.Grid()
    grid.setMargin(5, 5) # Add margin to widgets for better appearance
    grid.setIncrementWrap(2) # Widgets automatically occupy 2 columns
    view = tkw.View(root)
    view.setColWeights(1, 1) # Columns #0 and #1 will expand in same rates
    root.addView(view, 'home')
    view.addHeading(grid, 'Reverser')
    grid.newLine() # Move widget position pointer to next line, to column #0
    view.addInput(grid, 'textInput') # Add input widget
    view.addButton(grid, 'reverser', 'Reverse!', onClickReverse) # Add button
        # Parameters are: Widget key, button label and on-click function
    view.addTextOut(grid, 'textOutput') # Add output widget
```

Then define function that was passed in `addButton` function.

```python
def onClickReverse():
    global root
    text = root.getInputVal('textInput')[::-1] # Read text and reverse it
    root.setOutputText('textOutput', text) # Put text in output widget
```

![Screenshot](screenshots/screenshot3.png)

As you can see reading and writting values to widgets is very easy.
You have to remember what keys you typed in adding function.
Then just ask root for the values.


### Adding multiple views
Last thing in this guide is adding more views.
If another view was added and shown it would appear in place of our `home` view
defined before. First I will add buttons in header that are linked to function
that changes currently shown view.

```python
def createHeader(root):
    '''Create and fill header view'''
    grid = tkw.Grid()
    grid.setMargin(5, 5)
    grid.setIncrementWrap(2)
    grid.setSpan(3)
    header = tkw.View(root)
    root.setHeader(header)
    header.setColWeights(1, 1, 1)
    header.addHeading(grid, 'My First App', level=1)
    grid.newLine() # Go to next row, column #0
    header.addButton(grid, 'viewHome', 'Home', root.showView, ['home'])
    header.addButton(grid, 'viewSettings', 'Settings', root.showView, ['settings'])
    grid.newLine() # Go to next row, column #0
    grid.setSpan(3)
    header.addSeparator(grid)
```

Then define function that creates `settings` view.
Remember to call it in `if __name__ == '__main__'` section, just under `createHomeView()`
with root argument.

```python
def createSettingsView(root):
    grid = tkw.Grid()
    grid.setMargin(5, 5)
    grid.setIncrementWrap(3)
    view = tkw.View(root)
    root.addView(view, 'settings')
    view.addLabel(grid, 'Label 0')
    view.addLabel(grid, 'Label 1')
    view.addLabel(grid, 'Label 2')
    view.addLabel(grid, 'Label 3')
    view.addLabel(grid, 'Label 4')
    view.addLabel(grid, 'Label 5')
```

![Screenshot](screenshots/screenshot4_1.png)

![Screenshot](screenshots/screenshot4_2.png)

There is not much content in there, just some placeholder labels.
You can check how it works now.


### Window size
When switching views you can note that
window will always resize to minimum size that is required by widgets.
You can set minimum size yourself to avoid this behaviour.

This can be done by adding this line just below root title is defined.
```python
root.setMinSize(350, 250) # Minimum size is 350px width and 250px height
```

![Screenshot](screenshots/screenshot5.png)

### Conclusion
The package offers much more complex functionalities.
This guide could be much longer but these basics will get you started.
For more details check Reference section.
It contains list of all classes, their methods and parameters.
