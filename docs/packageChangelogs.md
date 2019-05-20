# Changelogs

### Version `0.5`
**XX May 2019**
- Added sub-package `canvas`
- Sub package Canvas:
    - Updated class `Canvas`
    - Added class `Point` used to perform calculations related with
        canvas geometry
    - Added class `Element` that represents element added to canvas to display.
    - Added class `Line` that inherits from `Element`
    - Added class `Circle` that inherits from `Element`
    - Added class `Vector` that inherits from `Line`
    - Added class `Image` that represents image added to canvas to display.
        This class has multiple creator methods that allow creation images
        from file, `PIL` Image or `cv2` image.
- Moved class `Canvas` to sub-package

### Version `0.4`
**16 May 2019**
- Added Class `Style`
    - Wrapper of `ttk.Style`
    - Manages appearance of both `Tk` and `TTK` widgets
- Class `ViewBase`
    - Methods that create widgets no longer require `grid` parameter.
        Widgets are positioned according to new `ViewBase`'s attribute: positioner.
    - Added method `setPositioner` that is used to change view's positioner.
    - Added optional constructor parameter: `positioner`.
        To make view use other positioner than grid pass the positioner object here.
- Class `View`
    - Added optional constructor parameter: `positioner` (passed to `ViewBase`).
- Class `Dialog`
    - Added optional constructor parameter: `positioner` (passed to `ViewBase`).
- Class `Root` was modified to use new `Style` class but its API did not change
- Updated Package Guide

#### Version `0.3.2`
**10 May 2019**
- Added widget `List` (wrapper around `tkinter.Listbox`)
This widget does not have method that sets its default value.
- Changes in docs
    - In reference: Parameter type is now in `inline code` span.
    - In changelog:
        - Version heading size now depends on version significance
        - Added version release date
- Class `ViewBase`
    - Added method `addInputList` which creates a List widget
- Class `Root`
    - Added method `readInputList` which returns all selected values of a List widget

#### Version `0.3.1`
**09 May 2019**
- Added widget `ComboBox` (wrapper around `ttk.Combobox`)
- Class `ViewBase`
    - Add method `addInputCombo` which creates a ComboBox widget
    - Repair bug in `addInputFile` method
    - In method `addInputBool` parameter `label` has now default value `''`
- Class `Root`
    - Add method `readInputCombo` which returns value of a ComboBox widget
    - Add method `defaultInputCombo` which sets default value of a ComboBox widget

### Version `0.3`
**08 May 2019**
- Class `Root`
    - Calling methods with invalid widget key will now raise an error
    - Some methods were renamed to be more memorable
    - Added method `createRadioGroup`
- Class `Grid`
    - Some methods were renamed to be more memorable
- Added Class `ViewBase`
    - This class exists for inheritance purposes, no instances should be created
    - Most contents of the `View` class were moved to this one
- Class `View`
    - Class now inherits from new class `ViewBase`
    - Removed `widgets` member variable, it was not utilized
    - Some methods were renamed to be more memorable
    - Removed method `addWidget`
    - Removed method `createRadioGroup`
    - Added method `addDialog`
    - Added method `showDialog`
- Added Class `Dialog`
    - Class inherits from `ViewBase`
    - Added method `setEndProtocol`
- Removed `output bool` widget type completely

### Version `0.2`
**04 May 2019**
- Added package guide
- Added package reference

### Version `0.1`
**02 May 2019**
Initial Version of the Package
