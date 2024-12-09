venv_dir=".venv"
echo $venv_dir

if [ ! -d "$venv_dir" ]; then
  echo "Venv does not exist; Creating one"
  python3 -m venv $venv_dir
else
  echo "Venv already exists."
fi

echo "Activating venv"
source $venv_dir/bin/activate

echo "Installing requirements"
pip3 install -r requirements.txt