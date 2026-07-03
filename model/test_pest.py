from ultralytics import YOLO

model = YOLO("model/best.pt")

print(model.task)
print(model.names)