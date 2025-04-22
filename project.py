import streamlit as st
from PIL import Image
from ultralytics import YOLO
import os

# --- Streamlit Config ---
st.set_page_config(page_title="Blood Group Detection", layout="centered")

# --- Login System ---
def login():
    st.title("🔐 Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state["logged_in"] = True
            st.success(" Login successful!")
        else:
            st.error(" Invalid credentials!")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login()
    st.stop()

# --- Title ---
st.markdown("<h1 style='color: red;'>🩸 Blood Group Detection using YOLOv8</h1>", unsafe_allow_html=True)
st.write("Upload a blood sample image and press **Process** to detect the blood group.")

# --- Upload Section ---
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

# --- Load YOLOv8 Model ---
model_path = r"D:\SEMESTER 4\PYTHON Filnal project\runs\detect\train7\weights\best.pt"  # Update path
model = YOLO(model_path)

# --- Output directory ---
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# --- Show Image & Button ---
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="🖼️ Uploaded Image", use_container_width=True)

    input_path = os.path.join(output_dir, "input.jpg")
    image.save(input_path)

    if st.button("🔍 Process"):
        with st.spinner("Detecting..."):
            results = model(input_path)
            results[0].save(filename=os.path.join(output_dir, "detected.jpg"))

        st.success("✅ Detection Complete")
        st.image(os.path.join(output_dir, "detected.jpg"), caption="Detected Output", use_container_width=True)

        try:
            class_names = results[0].names
            boxes = results[0].boxes
            class_ids = boxes.cls.tolist()

            if class_ids:
                detected_labels = [class_names[int(cls)] for cls in class_ids]
                unique_labels = set(label.lower() for label in detected_labels)

                st.info(f"🧪 Detected Components: **{', '.join(unique_labels).upper()}**")

                # --- Blood Group Decision Logic ---
                if unique_labels == {"a", "d"}:
                    st.success("🅰️+ (A Positive)")
                elif unique_labels == {"a"}:
                    st.success("🅰️- (A Negative)")
                elif unique_labels == {"b", "d"}:
                    st.success("🅱️+ (B Positive)")
                elif unique_labels == {"b"}:
                    st.success("🅱️- (B Negative)")
                elif unique_labels == {"a", "b", "d"}:
                    st.success("AB+ (AB Positive)")
                elif unique_labels == {"a", "b"}:
                    st.success("AB- (AB Negative)")
                elif unique_labels == {"d"}:
                    st.success("🅾️+ (O Positive)")
                elif not unique_labels.intersection({"a", "b", "d"}):
                    st.success("🅾️- (O Negative)")
                else:
                    st.warning("⚠️ Unknown Combination")
            else:
                st.warning("No blood group markers detected.")
        except Exception as e:
            st.error(f"❌ Error: {e}")

# # --- Dataset Evaluation Section ---
# st.markdown("---")
# st.subheader("📊 Dataset Evaluation")
# st.write("""
# - ✅ **Model:** YOLOv8 (custom-trained)
# - ✅ **Dataset Source:** Manually labeled blood smear images
# - ✅ **Classes:** A, B, D
# - ✅ **Total Images:** 500+
# - ✅ **Training Accuracy:** ~95%
# - ✅ **Validation Accuracy:** ~93%
# - ✅ **Augmentation:** Applied (rotation, brightness, noise)
# """)

# st.markdown("> This model was trained using annotated datasets and evaluated using metrics such as **precision**, **recall**, and **mAP** for each class (A, B, D).")

#streamlit run "D:\SEMESTER 4\PYTHON Filnal project\project.py"