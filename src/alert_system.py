from datetime import datetime

def generate_alert(risk_level, reason, motion, density):
    """
    Generates a clear, human-readable alert.
    """

    time_now = datetime.now().strftime("%H:%M:%S")

    print("\n" + "=" * 50)
    print("CROWD SAFETY ALERT")
    print("Time           :", time_now)
    print("Avg Motion     :", round(motion, 2))
    print("Avg Density    :", round(density, 2))
    print("Risk Level     :", risk_level)
    print("Explanation    :", reason)
    print("=" * 50)

    with open("alerts.log", "a") as log:
        log.write(
    "CROWD SAFETY ALERT\n"
    f"Time           : {time_now}\n"
    f"Avg Motion     : {round(motion, 2)}\n"
    f"Avg Density    : {round(density, 2)}\n"
    f"Risk Level     : {risk_level}\n"
    f"Explanation    : {reason}\n"
    + "-" * 50 + "\n"
)

