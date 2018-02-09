if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

if hash git 2>/dev/null; then
    echo 'Git already installed.'
else
    echo "I require git but it's not installed. Installing..."
    apt-get install git -y
fi
if hash python3 2>/dev/null; then
    echo 'Python3 already installed.'
else
    echo "I require python3 but it's not installed. Installing..."
    apt-get install python3 -y
fi

if python3 -c "import pip" &> /dev/null; then
    echo 'Pip already installed.'
else
    echo 'Pip not installed, installing...'
    wget https://bootstrap.pypa.io/get-pip.py

    python3 get-pip.py

    rm get-pip.py
fi
if python3 -c "import pygame" &> /dev/null; then
    echo 'Pygame already installed.'
else
    echo 'Pygame not installed, installing...'
    python3 -m pip install pygame
fi
if python3 -c "import wheel" &> /dev/null; then
    echo 'Wheel already installed.'
else
    echo 'Wheel not installed, installing...'
    python3 -m pip install wheel
fi

if python3 -c "import wheel" &> /dev/null; then
    if python3 -c "import pygame" &> /dev/null; then
        if python3 -c "import pip" &> /dev/null; then
            if hash python3 2>/dev/null; then
                if hash git 2>/dev/null; then
                    echo 'All dependencies installed.'
                else
                    echo 'Git is missing.'
                fi
            else
                echo 'Python3 is missing.'
            fi
        else
            echo 'Pip is missing.'
        fi
    else
        echo 'Pygame is missing.'
    fi
else
    echo 'Wheel is missing.'
fi
