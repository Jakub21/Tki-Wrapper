# `Class Canvas`
Canvas class wraps `tk.Canvas` widget.
Class contains methods that allow drawing shapes, plots.
Canvas can also display images from both PIL and OpenCV.

## Constructor
- Parameters
    - `View view` - View that canvas will be displayed in


## Properties
- `WIDTH = 100` - Canvas coordinates range in `X` axis.  Use method `setSize` to change its value.
- `HEIGHT = 100` - Canvas coordinates range in `Y` axis. Use method `setSize` to change its value.
- `MAX_IMAGES_AMOUNT = 1` - Amount of images that canvas keeps reference of.
    If reference slots are all full and next image is added the least recently one is forgotten, allowing garbage collector to delete it. Setter method not defined, user can change the value directly.
- `scaleMethod = 'RATIO'` - Method used to scale canvas contents.
    - `NOSCALING` - Contents will not be scaled, turning properties `WIDTH` and `HEIGHT` into canvas size expressed in pixels.
    - `FILL` - Contents will be scaled to fill whole canvas.
    - `RATIO` - Contents will be scaled to maximum possible size that fits inside canvas and preserves aspect ratio.
    - `RATIOFILL` - Contents will be scaled in a way that aspect ratio is preserved but if aspect ratio of canvas is different content will overflow.
- `scaleAnchor = 'CENTER'` - Only in use when `scaleMethod` is set to `RATIO` or `RATIOFILL`. Manages placement of contents.
    - `UPPERLEFT` - Canvas upper-left corner will always match upper-left corner of content space. Content overflow or blank space caused by difference in aspect ratio will appear on the bottom and to the right.
    - `CENTER` - Canvas center will always match content space center. Content overflow or blank space caused by difference in aspect ratio will appear on both top + bottom or left + right.


## Methods

### Core methods

##### `setSize`
Changes properties `WIDTH` and `HEIGHT`.
Use this to normalize canvas coordinates to system you use
in your project or to change aspect ratio of canvas content space.
- Parameters
    - `int width` - Canvas coordinates range in `X` axis
    - `int height` - Canvas coordinates range in `Y` axis


##### `update`
Call this method every time canvas content needs to be re-drawn.
In most applications this means after initialization is complete
or every time after root is updated.
- No parameters


### Color methods

##### `bgColor`
Changes canvas background.

##### `fgColor`
Sets default color for canvas elements.
If color is not defined in method that adds element this one will be used. Value set in constructor is `'#FFF'`.


### Add basic shapes
Methods from this section will most probably be changed.

##### `addLine`
Add line to draw no canvas.

##### `addPoint`
Add point to draw on canvas.


### Drawing images
This section is not finished.

##### `drawCv2Image`
Draws image from OpenCV package on canvas.

##### `drawPilImage`
Draws image from Pillow package on canvas.

##### `drawOpenImage`
Opens file, loads image and draws it on canvas.


### Modifying geometry properties
This section is not finished.

##### `setScalingMethod`
Setter method for `scaleMethod` property.

##### `setScalingAnchor`
Setter method for `scaleAnchor` property.
