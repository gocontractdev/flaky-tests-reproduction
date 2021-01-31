# reactivate the env (if forgotten)
deactivate
source ../venv/ez_env/bin/activate
# pip install --upgrade pip
pip --version
echo 'Installing requirements'
pip install -r ../requirements.txt
echo 'DONE'


# clone the directory or skip

if [ -d "../data/input/original_repo/" ]; then
    echo "Already exists -- skipped the cloning..."
else
  echo "Cloning the original repository; Please Wait..."
  cd  ../data/input
  mkdir "original_repo/"
  sudo chown -R "original_repo/"
  sudo chmod -R g+rw "original_repo/"
  cd "original_repo/"
  git clone https://github.com/damorimRG/msr4flakiness.git
  # back to the process and run the main python file
  cd ../../../process/
fi

python actuall.py