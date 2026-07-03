from ultralytics import YOLO

def main():
    model = YOLO("yolov8m-cls.pt")

    model.train(
        data="data.yaml",
        epochs=30,
        imgsz=224,
        batch=8,
        device="cpu"
    )

if __name__ == "__main__":
    main()