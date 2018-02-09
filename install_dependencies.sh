if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

command -v git >/dev/null 2>&1 || { echo >&2 "I require git but it's not installed. Installing..."; apt-get install git; }

apt-get install python3 -y

wget https://bootstrap.pypa.io/get-pip.py

python3 get-pip.py

rm get-pip.py

python3 -m pip install pygame
python3 -m pip install wheel
