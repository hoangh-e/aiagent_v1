# trên colab dùng 
# !nohup python3 run_ollama.py > ollama_log.txt 2>&1 &
# để chạy trong nền

import time
import threading
import subprocess
def ollama_service_start():
    subprocess.Popen(['ollama', 'serve'])

if __name__ == '__main__':
    thread = threading.Thread(target=ollama_service_start)
    thread.start()

    print("Đang khởi động Ollama server...")
    time.sleep(5)  
    print("Ollama server đã được khởi động trong background.")
