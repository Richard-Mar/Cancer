import openslide
import numpy as np
from openslide.deepzoom import DeepZoomGenerator
slide = openslide.open_slide('TCGA-AG-A002-01A-01-BS1.48af6e9c-1874-4294-ba2c-c2e5666ca0d0.svs')
selector = np.random()