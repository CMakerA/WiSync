echo "Generating dist"
sudo python3 setup.py bdist_wheel --universal
echo "Uploading"
twine upload dist/*
