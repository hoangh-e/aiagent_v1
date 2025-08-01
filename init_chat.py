import subprocess

def run_shell_commands():
    # Cập nhật và cài đặt pciutils
    subprocess.run(['sudo', 'apt', 'update'])
    subprocess.run(['sudo', 'apt', 'install', '-y', 'pciutils'])

    # Cài đặt Ollama
    subprocess.run(['curl', '-fsSL', 'https://ollama.com/install.sh', '|', 'sh'])

    # Di chuyển đến thư mục dự án
    subprocess.run(['cd', '/qld-agentsys'])

    # Chạy Ollama server
    subprocess.run(['nohup', 'python3', 'run_ollama.py', '>', 'ollama_log.txt', '2>&1', '&'])

    # Pull các mô hình Ollama
    # subprocess.run(['ollama', 'pull', 'deepseek-r1:14b'])
    subprocess.run(['ollama', 'pull', 'llama3'])
    subprocess.run(['ollama', 'pull', 'vi-dominic/phogpt:4b'])

    # Cài đặt các dependencies
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

    # Chạy ứng dụng
    subprocess.run(['python', 'run_app.py'])

if __name__ == "__main__":
    run_shell_commands()