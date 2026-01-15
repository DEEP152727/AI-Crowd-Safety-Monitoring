import cv2
import numpy as np

class DensityEstimator:
    """
    Estimates crowd density using
    foreground pixel ratio.
    """

    def __init__(self):
        self.bg_subtractor = cv2.createBackgroundSubtractorMOG2()

    def estimate_density(self, frame):
        fg_mask = self.bg_subtractor.apply(frame)
        moving_pixels = np.count_nonzero(fg_mask)
        return moving_pixels / fg_mask.size
