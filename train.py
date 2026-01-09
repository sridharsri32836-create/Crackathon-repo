from ultralytics import YOLO

model = YOLO("yolov8s.pt")

model.train(
    data="data.yaml",
    imgsz=768,
    epochs=50,
    batch=16,
    device="cpu"
)

