import streamlit as st
from PIL import Image
import pytesseract
import pandas as pd
from fuzzywuzzy import fuzz
from groq import Groq

pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract" 
GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

@st.cache_data
def load_dataset(file_path):
    """
    Load the preprocessed dataset and cache it.
    """
    try:
        dataset = pd.read_csv(file_path)
        if dataset.empty:
            st.error("The dataset is empty. Please check the file.")
        return dataset
    except Exception as e:
        st.error(f"Failed to load dataset: {e}")
        return pd.DataFrame()

def extract_text_from_image(image):
    """
    Extract text using Tesseract OCR from an uploaded or captured image.
    """
    try:
        img = Image.open(image).convert("L")  # Convert to grayscale
        extracted_text = pytesseract.image_to_string(img, lang="eng").strip()
        return extracted_text
    except Exception as e:
        st.error(f"Failed to process the image: {e}")
        return None

def match_text(uploaded_text, dataset, threshold=80):
    """
    Match the uploaded text with the preprocessed dataset using fuzzy matching.
    """
    best_match = None
    best_score = 0

    for _, row in dataset.iterrows():
        preprocessed_text = row.get("Extracted Text", "")
        if pd.notna(preprocessed_text):
            score = fuzz.token_sort_ratio(uploaded_text, preprocessed_text)
            if score > best_score:
                best_score = score
                best_match = row

    if best_score >= threshold:
        return best_match, best_score
    else:
        return None, best_score

def fetch_additional_info_with_groq(medicine_name):
    """
    Fetch additional information for a medicine using Groq API.
    """
    try:
        prompt = (
            f"As a professional doctor, provide a **brief summary** for the medicine '{medicine_name}': "
            "Include simple dosage instructions and 2-3 key precautions. "
            "Make the response clean and elegant."
            "Don't use **"
        )
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
        )
        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        return f"Error fetching details: {e}"

st.title("🩺 MediScan")
st.write("Upload an image or use your camera to identify a medicine and fetch additional details.")

dataset_path = "Preprocessed_Dataset.csv"
dataset = load_dataset(dataset_path)

if "cart" not in st.session_state:
    st.session_state.cart = []

option = st.radio("Choose an option:", ["📂 Upload Image", "📸 Capture from Camera"])

if option == "📂 Upload Image":
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    image_source = uploaded_file
elif option == "📸 Capture from Camera":
    captured_image = st.camera_input("Take a picture")
    image_source = captured_image

if image_source is not None:
    st.image(image_source, caption="Selected Image", use_container_width=True)

    extracted_text = extract_text_from_image(image_source)
    if extracted_text:

        threshold = 80
        matched_row, confidence = match_text(extracted_text, dataset, threshold)
        if matched_row is not None:
            medicine_name = matched_row['Medicine Name']

            additional_info = fetch_additional_info_with_groq(medicine_name)

            uses = matched_row.get('Uses', 'Not available')
            dosage = matched_row.get('Dosage', 'Not available')
            precautions = matched_row.get('Precautions', 'Not mentioned')

            final_info = f"""
            <div style="border: 1px solid #ddd; padding: 15px; border-radius: 10px; background-color: #f9f9f9; color: black;">
                <h3 style="color: black;">🩹 {medicine_name}</h3>
                <p><strong>🔍 Confidence Score:</strong> {confidence}%</p>
                <p><strong>💊 Uses:</strong> {uses if uses != 'Not available' else 'Fetching details...'}</p>
                <p>💊{additional_info}</p>
            </div>
            """

            st.markdown(final_info, unsafe_allow_html=True)

            if st.button("➕ Add to Cart"):
                st.session_state.cart.append(medicine_name)
                st.success(f"✅ {medicine_name} added to cart!")

        else:
            st.error("❌ No matching medicine found in the dataset.")
    else:
        st.error("❌ No text detected in the uploaded image. Please try again.")

st.write("---")
st.subheader("🛒 Your Cart")

if len(st.session_state.cart) > 0:
    for index, item in enumerate(st.session_state.cart):
        col1, col2 = st.columns([4, 1])
        col1.write(f"**{item}**")
        if col2.button("❌ Remove", key=f"remove_{index}"):
            st.session_state.cart.pop(index)
            st.experimental_rerun()

    if st.button("🗑️ Clear Cart"):
        st.session_state.cart.clear()
        st.experimental_rerun()
else:
    st.info("Your cart is empty. Add some medicines!")

st.write("---")
st.write("💡 Developed with ❤️ by Ankan")
