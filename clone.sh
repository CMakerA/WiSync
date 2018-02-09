if hash git 2>/dev/null; then
    rm -rf WiSync
    git clone https://github.com/CMakerA/WiSync.git
    echo 'Repository cloned.'
else
    echo -e 'Git is not installed. Please, run \e[4minstall_dependencies.sh\e[0m, or \e[4mapt-get install git\e[0m to install it.'
fi
