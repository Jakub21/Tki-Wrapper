from TkiWrapper.canvas.elements.Image import Image
from TkiWrapper.config import conf
from PIL import ImageTk, Image as PImage

try:
  import cv2
  class OcvImage(Image):
    def __init__(self, canvas, anchor, size, image):
      image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
      image = PImage.fromarray(image)
      super().__init__(canvas, anchor, size, image)
except ImportError:
  if not conf.WARNINGS_SILENCED:
    print('[TkiWrapper]: OpenCV is not installed,' + \
      'canvas.elements.OcvImage will not be available')
  class Ocvimage: pass
