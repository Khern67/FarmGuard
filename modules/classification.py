SEVERITY_VALUES = {"Low": 1, "Moderate": 2, "High": 3, "Critical": 4}

def classify_severity(affected_area, progression, plant_condition, recurrence_count):
    """Prototype rule-based classification for inspection triage, not disease diagnosis."""
    area = max(0.0, min(float(affected_area), 100.0))
    recurrence = max(0, min(int(recurrence_count), 5))
    progression = str(progression).strip().lower()
    condition = str(plant_condition).strip().lower()

    if condition == "severe" or progression == "rapidly spreading" or area > 40:
        return "Critical", "Severe plant condition, rapid spread, or more than 40% affected area."
    if condition == "significant" or progression == "increasing" or area > 20:
        return "High", "Significant plant condition, increasing symptoms, or more than 20% affected area."
    if condition == "moderate" or area > 5 or recurrence > 0:
        return "Moderate", "Moderate condition, more than 5% affected area, or a recurring observation."
    return "Low", "Minor, stable observation affecting 5% or less of the crop area."

def calculate_urgency(severity, affected_area, recurrence_count):
    severity_score = {k: v / 4 * 100 for k, v in SEVERITY_VALUES.items()}.get(severity, 25)
    area_score = max(0, min(float(affected_area), 100))
    recurrence_score = max(0, min(int(recurrence_count), 5)) / 5 * 100
    return round(0.50 * severity_score + 0.30 * area_score + 0.20 * recurrence_score, 2)

def priority_label(score):
    if score >= 75:
        return "Critical"
    if score >= 50:
        return "High"
    if score >= 25:
        return "Moderate"
    return "Low"
