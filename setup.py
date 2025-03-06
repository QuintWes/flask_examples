import os
import subprocess
import sys
import venv


def create_venv():
    print("🚀 Creating virtual environment...")
    venv_dir = "venv"
    venv.EnvBuilder(with_pip=True).create(venv_dir)


def install_requirements():
    print("📦 Installing requirements...")
    # Windows
    if os.name == 'nt':
        pip_path = os.path.join("venv", "Scripts", "pip.exe")
    # MacOS/Linux
    else:
        pip_path = os.path.join("venv", "bin", "pip")

    subprocess.check_call([pip_path, "install", "--upgrade", "pip"])
    subprocess.check_call([pip_path, "install", "-r", "requirements.txt"])


def main():
    if not os.path.exists("requirements.txt"):
        print("❌ requirements.txt not found!")
        sys.exit(1)

    create_venv()
    install_requirements()

    print("\n✅ Setup complete!")
    print("\n👉 To activate your virtual environment:")
    if os.name == 'nt':
        print("   venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")

    print("\n👉 Then run the app with:")
    print("   python app.py\n")


if __name__ == "__main__":
    main()
