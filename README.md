# blood-group-detector-by-image-processing
This project leverages the YOLOv8 object detection model to identify and classify human blood groups (A, B, AB, O) from blood sample images. The model is trained on labeled datasets and optimized for real-time and accurate detection, potentially useful in healthcare, emergencies, and diagnostic applications.

# 🩸 Blood Group Detection using YOLOv8

A deep learning project that uses **YOLOv8** for detecting and classifying human blood groups (A, B, AB, O) from blood sample images. This model can assist in healthcare applications for real-time and accurate blood group recognition.

---

## 📂 Project Structure

```
blood-group-detector/
├── dataset/              # Blood sample images and YOLO labels
├── runs/                 # Training/testing outputs
├── yolov8_config/        # Config and YAML files
├── project.py             # Inference script
├── main.py              # YOLOv8 training code
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/ranazain9/blood-group-detector-by-image-processing.git
cd blood-group-detector
```

2. **Create a virtual environment (optional)**
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
pip install ultralytics
pip install stremlit '''for GUI  
```

---

## 📁 Dataset Format

- Organize dataset in YOLO format:

```
blood-group/
├── images/
│   ├── train/
│   └── val/
├── labels/
│   ├── train/
│   └── val/
```

- Each `.txt` file should follow this format:
```
<class_id> <x_center> <y_center> <width> <height>
```

---

## 🧠 Training

Edit `blood_group.yaml`:

```yaml
train: dataset/images/train
val: dataset/images/val
nc: 4
names: ['A', 'B', 'AB', 'O']
```

Run training:

```bash
yolo task=detect mode=train model=yolov8n.pt data=yolov8_config/blood_group.yaml epochs=50 imgsz=640
```

---

## 🔍 Inference

Run detection on a single image:

```bash
yolo task=detect mode=predict model=runs/detect/train/weights/best.pt source="sample.jpg"
```

Or on a folder:

```bash
yolo task=detect mode=predict model=runs/detect/train/weights/best.pt source="test_images/"
```

---

## 📊 Results

Example output:

![output](sample_output.jpg)

---

## 🧪 Sample Predictions

| Image | Prediction |
|-------|------------|
| ![A](samples/a_sample.jpg) | Blood Group A |
| ![O](samples/o_sample.jpg) | Blood Group O |

---

## 📌 Future Work

- Detect Rh factor (+ / -)
- Improve model accuracy with more data
- Deploy to web or mobile app

---

## 🤝 Contributing

Feel free to fork the repo, make changes, and open a pull request!

---

## 📜 License

Licensed under the MIT License.
