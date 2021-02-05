# This script will only work if you run it from the main not within the process folder

# reactivate the env (if forgotten)
deactivate
# create environment:
if [ -d "venv/ez_env/" ]; then
  echo 'env exists'
else
  python -m venv venv/ez_env
fi

source venv/ez_env/bin/activate
# pip install --upgrade pip
pip --version
echo 'Installing requirements'
pip install -r requirements.txt
pip install "textdistance[extras]" # for speed performance
echo 'DONE'

# clone the directory or skip

if [ -d "data/input/original_repo/" ]; then
    echo "Already exists -- skipped the cloning..."
    # just run the main python file
else
  echo "Cloning the original repository; Please Wait..."
  cd  data/input
  mkdir "original_repo/"
  sudo chown -R "original_repo/"
  sudo chmod -R g+rw "original_repo/"
  cd "original_repo/"
  git clone https://github.com/damorimRG/msr4flakiness.git
  # back to the process to run the main python file
  cd ../../../
fi

python process/actuall.py