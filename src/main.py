import cv2
from src.motion_analysis import compute_average_motion
from src.density_analysis import DensityEstimator
from src.risk_engine import classify_risk
from src.alert_system import generate_alert

VIDEO_PATH = "./input/c.mp4"

# ---------------- VIDEO INITIALIZATION ----------------
cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    print("Error: Video file not found")
    exit()

density_estimator = DensityEstimator()
prev_gray = None

motion_values = []
density_values = []

FRAME_SKIP = 5        # ✅ Increased skip for faster processing
WARMUP_FRAMES = 10    # ✅ Allow background model to stabilize
frame_count = 0

print("Analyzing video... Please wait...\n")

# ---------------- VIDEO PROCESSING LOOP ----------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    # Skip frames for performance
    if frame_count % FRAME_SKIP != 0:
        continue

    # Resize once (used for both motion & density)
    frame_small = cv2.resize(frame, (640, 360))
    gray = cv2.cvtColor(frame_small, cv2.COLOR_BGR2GRAY)

    # Skip initial frames to stabilize background subtractor
    if frame_count <= WARMUP_FRAMES:
        prev_gray = gray
        continue

    if prev_gray is not None:
        motion = compute_average_motion(prev_gray, gray)
        density = density_estimator.estimate_density(frame_small)

        motion_values.append(motion)
        density_values.append(density)

    prev_gray = gray

cap.release()

# ---------------- FINAL DECISION (SINGLE OUTPUT) ----------------
if motion_values and density_values:
    avg_motion = sum(motion_values) / len(motion_values)
    avg_density = sum(density_values) / len(density_values)

    risk, reason = classify_risk(avg_motion, avg_density)

    if risk != "LOW":
        generate_alert(risk, reason, avg_motion, avg_density)
    else:
        print("Video Analysis Completed: No significant risk detected.")

else:
    print("No usable frames found in video.")
