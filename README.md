# 🩺 MediScan - Your AI-Powered Medicine Identifier 🚀

Welcome to **MediScan**, the ultimate AI-powered tool that helps you identify medicines from images and fetch essential medical details. Whether you're a pharmacist, a curious user, or someone who just found an old pill in their drawer—**MediScan has your back!** 💊

---

## 🎯 Features:
✅ **Upload or Capture** - Upload an image or take a live photo using your webcam.  
✅ **Instant OCR Analysis** - Extracts text from medicine labels using Tesseract OCR.  
✅ **AI-Powered Insights** - Fetches additional details via **Groq AI**.  
✅ **Confidence Matching** - Uses **fuzzy logic** to match medicine names accurately.  
✅ **Cart System** - Add medicines to a cart for later reference.  
✅ **Sleek UI** - Styled with a modern, user-friendly design.  

---

## 🛠️ Installation Guide

### 1️⃣ Install Dependencies
First, install all required Python packages:
```bash
pip install -r requirements.txt
```

### 2️⃣ Install Tesseract OCR (Required for Image Processing)

#### **macOS:**
```bash
brew install tesseract
```

#### **Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install tesseract-ocr -y
```

#### **Windows:**
1. **Download Tesseract OCR** from [this link](https://github.com/UB-Mannheim/tesseract/wiki).
2. **Install it** and note the installation path (usually `C:\Program Files\Tesseract-OCR`).
3. **Add Tesseract to the System PATH:**
   - Search for **"Environment Variables"** in Windows.
   - Under **"System Variables"**, find and edit `Path`.
   - Click **New** and add:  
     ```
     C:\Program Files\Tesseract-OCR
     ```
   - Click **OK** to save.
4. **Verify Installation:**
   ```bash
   tesseract --version
   ```

#### **Verify Tesseract Installation**
After installation, check if Tesseract is working by running:
```bash
tesseract --version
```

---

## 🔑 Secure API Key Setup
To use **Groq AI API**, create a `.env` file in your project directory and add:
```plaintext
GROQ_API_KEY=your_secret_api_key_here
```
⚠ **DO NOT** share your API key publicly!

---

## 🚀 How to Run the Streamlit App
Once dependencies and Tesseract are installed, run:
```bash
streamlit run app.py
```

---

## 📸 Screenshots
![MediScan Screenshot](https://via.placeholder.com/800x400?text=Your+Awesome+App+Screenshot)

---

## 💡 How It Works:
1️⃣ Upload a **medicine label image** or capture a new one.  
2️⃣ OCR extracts text and identifies the medicine name.  
3️⃣ AI fetches relevant **dosage, precautions, and uses**.  
4️⃣ Add medicines to the **cart** and keep track of them.  
5️⃣ Enjoy the **power of AI in healthcare!**  

---

## 🤖 Tech Stack:
- **Python** 🐍
- **Streamlit** 🖥️
- **Pytesseract (OCR)** 🔍
- **Groq AI API** 🤯
- **Fuzzy Matching** 🔢
- **Pandas** 📊

---

## 🚀 Future Updates:
- [ ] 🔥 **Voice Command Support**
- [ ] 📍 **Nearby Pharmacy Locator**
- [ ] 🏥 **Medicine Alternatives Suggestions**
- [ ] 🌎 **Multi-Language OCR Support**

---

## 🏆 Contributing:
Want to make MediScan even cooler? Fork the repo, make changes, and send a **pull request**! 🚀

---

## 📜 License:
**MediScan** is licensed under the **MIT License**. Feel free to use, modify, and improve!

---

## 💙 Developed with Passion by **Ankan** 🔥
