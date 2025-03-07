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
        python_path = os.path.join("venv", "Scripts", "python.exe")
    else:
        python_path = os.path.join("venv", "bin", "python")

    subprocess.check_call([python_path, "-m", "pip", "install", "--upgrade", "pip"])
    subprocess.check_call([python_path, "-m", "pip", "install", "-r", "requirements.txt"])
    print("🔥 Requirements installed!")


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
        print("   source venv/bin/activate in bash")

    print("\n👉 Then run the app with:")
    print("   python app.py\n")


if __name__ == "__main__":
    main()

# source venv/Scripts/activate
# python setup.py install
# python app.py

# python app.py
# python flask_swagger_example.py
# python flask_restx_example.py
# python apifairy_example.py
# python connexion_example.py

# taskkill //IM python.exe //F