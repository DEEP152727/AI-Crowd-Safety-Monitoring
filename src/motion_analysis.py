import cv2
import numpy as np

def compute_average_motion(prev_gray, curr_gray):
    """
    Computes average crowd motion using optical flow.
    Uses reduced resolution and simplified parameters
    to ensure faster execution.
    """

    # Smaller resolution → faster computation
    small_prev = cv2.resize(prev_gray, (320, 180))
    small_curr = cv2.resize(curr_gray, (320, 180))

    flow = cv2.calcOpticalFlowFarneback(
        small_prev,
        small_curr,
        None,
        0.5,
        2,
        7,
        2,
        5,
        1.2,
        0
    )

    magnitude, _ = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    return float(np.mean(magnitude))
