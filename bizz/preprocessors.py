import cv2
import imutils

class AspectAwarePreprocessor:
  def __init__(self, width, height, inter=cv2.INTER_AREA):
    self.width = width
    self.height = height
    self.inter = inter

  def preprocess(self, image):
    (h, w) = image.shape[:2]
    assert len(image.shape) == 3
    dW = 0
    dH = 0

    if w < h:
      image = imutils.resize(image, width=self.width, inter=self.inter)
      assert len(image.shape) == 3
      dH = int((image.shape[0] - self.height) / 2.0)

    else:
      image = imutils.resize(image, height=self.height, inter=self.inter)
      assert len(image.shape) == 3
      dW = int((image.shape[1] - self.width) / 2.0)

    # get the new image dimensions
    (h, w) = image.shape[:2]
    # crop the image
    assert len(image.shape) == 3
    image = image[dH:h - dH, dW:w - dW]
    
    

    # we ensure that image dimensions have a fixed value(not float)
    # hence we resize again.
    

    return cv2.resize(image, (self.width, self.height), interpolation=self.inter)