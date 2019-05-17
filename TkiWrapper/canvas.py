import tkinter as tk
from PIL import Image, ImageTk
from TkiWrapper.namespace import Namespace

class Canvas:
    def __init__(self, view, width=None, height=None):
        self.view = view
        self.canvas = tk.Canvas(view.frame, highlightthickness=0)
        self.color = '#FFF'
        self.scaleMethod = 'RATIO'
        self.scaleAnchor = 'CENTER'
        self.images = [] # keep references to images so they do not disappear
        self.objects = []
        self.WIDTH = 100
        self.HEIGHT = 100
        self.MAX_IMAGES_AMOUNT = 1

    #----------------------------------------------------------------
    # General

    def setSize(self, width, height):
        '''Changes range of coordinates (default is 100x100)
        Use this to normalize canvas coords for your project
        Or to change aspect ratio
        '''
        self.WIDTH, self.HEIGHT = width, height

    def bgColor(self, color):
        '''Set canvas background'''
        self.canvas.config(bg=color)

    def fgColor(self, color):
        '''Set foreground color for next elements'''
        self.color = color

    def update(self):
        self.canvas.delete('all')
        for obj in self.objects:
            obj.method(*obj.args, **obj.kwargs)

    def clear(self):
        self.objects = []

    #----------------------------------------------------------------
    # Adding Low-level Elements

    def addLine(self, *args, color=None, **kwargs):
        '''Adds line to object that will be drawn'''
        kwargs['color'] = self.color if color is None else color
        self.objects.append(Namespace(
            method=self.drawLine, args=args, kwargs=kwargs))

    def addPoint(self, *args, color=None, **kwargs):
        '''Adds point to object that will be drawn'''
        kwargs['color'] = self.color if color is None else color
        self.objects.append(Namespace(
            method=self.drawPoint, args=args, kwargs=kwargs))

    def addCustom(self, obj, *args, color=None, **kwargs):
        '''Adds custom object with specific interface to draw list'''
        kwargs['color'] = self.color if color is None else color
        args = [self] + list(args)
        self.objects.append(Namespace(method=obj.draw, args=args, kwargs=kwargs))

    #----------------------------------------------------------------
    # Drawing Elements

    def drawLine(self, pt1, pt2, width=2, color=None):
        pt1_ = pt1
        pt1 = self._scale(pt1)
        pt2 = self._scale(pt2)
        self.canvas.create_line((*pt1, *pt2), fill=color, width=width)

    def drawPoint(self, pt, width=3, color=None):
        pt = self._scale(pt)
        self.canvas.create_arc(
            (pt[0]-width, pt[1]-width, pt[0]+width, pt[1]+width),
            fill=color, width=width, extent=359, outline='')

    #----------------------------------------------------------------
    # Drawing Images

    def drawCv2Image(self, image, position=None):
        '''Draw CV2 image (numpy 2D BGR)'''
        tkImage = ImageTk.PhotoImage(image=Image.fromarray(image))
        self._drawImage(tkImage, position)

    def drawPilImage(self, image, position=None):
        '''Draw Pillow Image'''
        tkImage = ImageTk.PhotoImage(image=image)
        self._drawImage(tkImage, position)

    def drawOpenImage(self, path, position=None):
        '''Draw Image read from storage'''
        tkImage = ImageTk.PhotoImage(file=path)

    def _drawImage(self, image, position):
        '''Sub method for drawing image after it was normalized'''
        # Calculate position
        x, y = 0, 0
        if position is None:
            cnvSize = self._getSelfSize()
            imgHeight, imgWidth, _ = image.shape
            x, y = (cnvSize[0] - imgWidth) // 2, (cnvSize[1] - imgHeight) // 2
        else:
            x, y = position
        # Draw and keep reference
        self.canvas.create_image(x, y, image=tkImage, anchor=tk.NW)
        self._addImageRef(tkImage)

    def _addImageRef(self, image):
        '''Adds image reference to it is not deleted by garbage collector'''
        self.images.push(image)
        if len(self.images) > self.MAX_IMAGES_AMOUNT:
            self.images = self.images[1:]

    #----------------------------------------------------------------
    # Geometry

    def setScalingMethod(self, method):
        '''Changes scaling method'''
        if method.upper() not in ['FILL', 'RATIOFILL', 'RATIO', 'NOSCALING']:
            raise Exception(f'Invalid scaling method {method}')
        self.scaleMethod = method.upper()

    def setScalingAnchor(self, mode):
        '''Changes scaling anchor'''
        if mode.upper() not in ['CENTER', 'UPPERLEFT']:
            raise Exception(f'Invalid scaling anchor mode {mode}')
        self.scaleAnchor = mode.upper()

    def _scale(self, point):
        '''Converts point expressed in percentage of canvas size
            to real canvas coordinates'''
        if self.scaleMethod == 'NOSCALING':
            return point
        elif self.scaleMethod == 'FILL':
            return self._scaleFill(point)
        elif self.scaleMethod == 'RATIOFILL':
            return self._scaleRatioFill(point)
        elif self.scaleMethod == 'RATIO':
            return self._scaleRatio(point)

    def _scaleFill(self, point):
        '''Sub-method of _scale: Scale with FILL method'''
        cnvWidth, cnvHeight = self._getSelfSize()
        aspect = self.WIDTH / self.HEIGHT
        x = point[0] / self.WIDTH * cnvWidth
        y = point[1] / self.HEIGHT * cnvHeight / aspect
        return x, y

    def _scaleRatioFill(self, point):
        '''Sub-method of _scale: Scale with RATIOFILL method'''
        cnvWidth, cnvHeight = self._getSelfSize()
        xScale, yScale = self._calcScale(max)
        x, y = point[0] * xScale, point[1] * yScale
        x, y = self._applyAnchor((x, y), xScale)
        return x, y

    def _scaleRatio(self, point):
        '''Sub-method of _scale: Scale with RATIO method'''
        cnvWidth, cnvHeight = self._getSelfSize()
        xScale, yScale = self._calcScale(min)
        x, y = point[0] * xScale, point[1] * yScale
        x, y = self._applyAnchor((x, y), xScale)
        return x, y

    def _calcScale(self, comprator):
        '''Helper method for _scaleRatioFill and _scaleRatio'''
        cnvWidth, cnvHeight = self._getSelfSize()
        aspect = self.WIDTH / self.HEIGHT
        xxScale = cnvWidth / self.WIDTH
        yxScale = cnvHeight / self.WIDTH
        xyScale = cnvWidth / self.HEIGHT
        yyScale = cnvHeight / self.HEIGHT
        xScale = comprator(yyScale, xyScale/aspect)
        yScale = comprator(xxScale, yxScale*aspect)
        return xScale, yScale

    def _applyAnchor(self, point, scale):
        '''Adds anchor offset to point'''
        cnvWidth, cnvHeight = self._getSelfSize()
        x, y = point
        if self.scaleAnchor == 'CENTER':
            x += (cnvWidth - scale*self.WIDTH) / 2
            y += (cnvHeight - scale*self.HEIGHT) / 2
        return x, y

    def _getSelfSize(self):
        '''Returns real canvas size'''
        return self.canvas.winfo_width(), self.canvas.winfo_height()
