import datetime
import sys
import os
from scipy.misc import imread
#import skimage

class image_extractor():
  def __init__(self, path= None):
    self.img_dir= path
