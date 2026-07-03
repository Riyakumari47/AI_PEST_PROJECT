def estimate_crop_loss(severity):

    if severity == "🔴 High":
        return "Estimated Crop Loss: 50% - 80%"

    elif severity == "🟡 Medium":
        return "Estimated Crop Loss: 20% - 50%"

    else:
        return "Estimated Crop Loss: Less than 20%"