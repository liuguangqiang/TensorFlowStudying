
## Install virtualenv
* pip3 install -U pip virtualenv

## Create Environment
* virtualenv --system-site-packages -p python3 ./venv
* source ./venv/Scripts/activate

## Install TensorFlow
* pip install —upgrade tensorflow
* pip install --index-url https://pypi.douban.com/simple tensorflow
* pip install tensorflow —upgrade —force-reinstall