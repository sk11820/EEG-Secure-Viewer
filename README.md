# 🧠 EEG Secure Viewer

A simple and secure EEG data visualization app built with Streamlit. Upload `.csv` files, select EEG channels, and interactively explore brainwave data.

## 🚀 Features
- Upload `.csv` EEG files
- View data by channel
- Interactive time-series plots
- Real-time file inspection
- Built for future encryption & ML integration

## 🖥️ Demo
<img src="assets/demo.png" width="700">

## 🛠️ Tech Stack
- **Frontend**: Streamlit
- **Data**: pandas, NumPy
- **Visualization**: Matplotlib, Streamlit line chart
- **(Optional)**: PyCryptodome for encryption

## 📂 Example File Format
```csv
Time,Channel_1,Channel_2,Channel_3
0.0,12.3,13.2,11.4
0.1,12.1,13.0,11.2
...
```

## 🧪 Getting Started

### 🔧 Install dependencies
```bash
pip install -r requirements.txt
```

### ▶️ Run the app
```bash
streamlit run app.py
```

### 📦 Optional
To enable auto-reload:
```bash
pip install watchdog
```

## 🔐 Future Features
- AES encryption of EEG data
- Flask/FastAPI backend support
- Real-time EEG streaming
- ML classification integration

## 📄 License
MIT — feel free to use, extend, and contribute!
