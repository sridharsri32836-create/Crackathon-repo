from ultralytics import YOLO

model = YOLO("best.pt")

model.predict(
    source="test/images",
    save_txt=True,
    save_conf=True,
    imgsz=768
)
