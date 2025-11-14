import sys, subprocess

def ensure(module):
    try:
        __import__(module)
        print(f"[✓] {module} 已安裝")
    except ImportError:
        print(f"[✗] {module} 未安裝，正在安裝...")
        subprocess.run([sys.executable, "-m", "pip", "install", module])

print("🔍 Python 路徑：", sys.executable)
ensure("moviepy")