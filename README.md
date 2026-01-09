 Model
- YOLOv8s (Ultralytics)
- Input size: 768×768
- 5 damage classes
 Class Mapping
0 – Longitudinal crack  
1 – Transverse crack  
2 – Alligator crack  
3 – Other corruption  
4 – Pothole 
yolo detect val model=best.pt data=data.yaml
python predict.py

mAP@50 ≈ 58%

mAP@50–95 ≈ 30%
