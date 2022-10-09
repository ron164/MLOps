# -*- coding: utf-8 -*-
# @Time : 09-10-2022 17:01
# @Author : rohan
# @File : track_dvc.py
import os
from glob import glob

data_dirs = ["Training_Batch_Files", "Prediction_Batch_files"]

for data_dir in data_dirs:
    files = glob(data_dir + r"/*.csv")
    for filePath in files:
        # print(f"dvc add {filePath}")
        os.system(f"dvc add {filePath}")

print("\n #### all files added to dvc ####")
