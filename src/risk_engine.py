def classify_risk(avg_motion, density):
    """
    Rule-based, explainable risk classification.
    """

    if avg_motion > 3.5 and density > 0.65:
        return "HIGH", "Sudden crowd acceleration with high density"

    elif avg_motion > 2.5 or density > 0.65:
        return "MEDIUM", "Unusual movement or congestion detected"

    else:
        return "LOW", "Normal crowd behavior"
