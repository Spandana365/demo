import sys
import platform

def test_deployment():
    print("--- Deployment Test ---")
    print(f"Python Version: {sys.version}")
    print(f"Operating System: {platform.system()} {platform.release()}")
    print("Status: Success! The script is running on the server.")

if __name__ == "__main__":
    test_deployment()
