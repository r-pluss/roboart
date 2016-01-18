import datetime
import sys
import os
from scipy.misc import imread
#import skimage

class image_extractor():
  def __init__(self, path= None):
    self.img_dir= path
    if self.img:
        if os.path.isdir(self.img_dir):
            #awesome
            pass
        else:
            raise ValueError(str(self.img_dir) + ' is not a directory.')
