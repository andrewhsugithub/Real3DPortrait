#! /bin/bash

echo "source /mnt/Nami/users/Jason0411202/anaconda3/bin/activate"
source /mnt/Nami/users/Jason0411202/anaconda3/bin/activate
echo "conda activate real3dportrait"
conda activate real3dportrait
echo "python inference/app_real3dportrait.py"
python inference/app_real3dportrait.py