echo "CLONING REPOSITORY"
mkdir ~/Desktop/craftgame
git clone https://github.com/pyudev-x-projects/craftgame.git ~/Desktop/craftgame
cd ~/Desktop/craftgame

echo "INITILIZING PYTHON"
python3 -m venv .
source ./bin/activate
echo "INSTALLING PACKAGES"

cp -R ./pkgs/ursina "./lib/python3.11/site-packages/"
pip install screeninfo
pip install Panda3D
pip install pyperclip
pip install panda3d-gltf 
pip install panda3d-simplepbr 
pip install pyobjc-core
pip install pyobjc-framework-Cocoa 
pip install Pillow
echo "craftgame is ready to go :)"
echo "running craftgame"
python3 main.py