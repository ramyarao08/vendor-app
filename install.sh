##INSTALL THE DEPENDENT SOFTWARE PACKAGES
export TESSERACT=tesseract
echo $TESSERACT
echo "Begin Install"
pip install -r requirements.txt
sudo apt-get install -y --no-install-recommends tesseract-ocr-deu
sudo pip install libtesseract
sudo pip install tesseract
##pip install cuneiform
sudo apt-get install tesseract-ocr libtesseract-dev libleptonica-dev cython
sudo pip install tesserocr
echo "Installation Completed"
