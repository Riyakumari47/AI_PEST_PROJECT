from ultralytics import YOLO

model = YOLO("model/best.pt")
results = model.predict(source=r"C:\Users\91826\OneDrive\AI_PEST_PROJECT\insect.jpg", save=True, conf=0.25)
print("Prediction complete.")