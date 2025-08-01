import os
import threading
import time
from pyngrok import ngrok
import subprocess

# STEP 1: Cài đặt authtoken cho ngrok (chạy 1 lần duy nhất)
NGROK_AUTH_TOKEN = "2wmdILru8gdg87barV9WQLYRwA1_2vnDiRunvhV3amQws6wPv"
os.system(f"ngrok config add-authtoken {NGROK_AUTH_TOKEN}")


# STEP 3: Tạo tunnel đến cổng 8501 (port mặc định của Streamlit)
public_url = ngrok.connect(8501)
print(f"\n🌐 Public app URL: {public_url}")

def run_streamlit():
    print("🚀 Ngrok đang khởi chạy streamlit...")
    subprocess.run(["streamlit", "run", "app_streamlit.py"])

thread = threading.Thread(target=run_streamlit)
thread.start()
