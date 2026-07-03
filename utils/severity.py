def get_severity(confidence):

    if confidence >= 90:
        return "🔴 High"

    elif confidence >= 70:
        return "🟡 Medium"

    else:
        return "🟢 Low"