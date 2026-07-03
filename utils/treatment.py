treatments = {

    "Cashew Anthracnose": {
        "organic": "Spray Neem Oil every 7 days.",
        "chemical": "Apply Copper Oxychloride fungicide.",
        "prevention": "Avoid water logging and remove infected leaves."
    },

    "Cashew Gumosis": {
        "organic": "Use Trichoderma around roots.",
        "chemical": "Apply Bordeaux Paste.",
        "prevention": "Maintain proper drainage."
    },

    "Cashew Healthy": {
        "organic": "No treatment required.",
        "chemical": "No treatment required.",
        "prevention": "Maintain regular irrigation and nutrition."
    },

    "Maize Fall Armyworm": {
        "organic": "Spray Neem Oil or Bt (Bacillus thuringiensis).",
        "chemical": "Apply Emamectin Benzoate.",
        "prevention": "Regular field monitoring."
    },

    "Maize Grasshopper": {
        "organic": "Use Garlic-Chili Spray.",
        "chemical": "Spray Lambda Cyhalothrin.",
        "prevention": "Keep field weed free."
    },

    "Maize Healthy": {
        "organic": "Healthy Crop.",
        "chemical": "No Chemical Required.",
        "prevention": "Continue good farming practices."
    },

    "Tomato Healthy": {
        "organic": "Healthy Crop.",
        "chemical": "No Chemical Required.",
        "prevention": "Regular watering and nutrition."
    },

    "Tomato Leaf Curl": {
        "organic": "Neem Oil Spray.",
        "chemical": "Imidacloprid.",
        "prevention": "Control whiteflies."
    },

    "Tomato Leaf Blight": {
        "organic": "Compost Tea Spray.",
        "chemical": "Mancozeb Fungicide.",
        "prevention": "Avoid excess moisture."
    },

    "Tomato Septoria Leaf Spot": {
        "organic": "Neem Oil.",
        "chemical": "Chlorothalonil.",
        "prevention": "Remove infected leaves."
    }

}

def get_treatment(disease):

    if disease in treatments:
        return treatments[disease]

    return {
        "organic": "No information available.",
        "chemical": "No information available.",
        "prevention": "Consult Agriculture Expert."
    }