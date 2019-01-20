#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
os.chdir("/media/kswada/MyFiles/data/ImageNet_ILSVRC2012/")
print(os.getcwd())


import tarfile



# ------------------------------------------------------------------------
# Untar all subdirectories into new directories
# ------------------------------------------------------------------------
base_dir = "/media/kswada/MyFiles/data/ImageNet_ILSVRC2012/Data/train/"
paths = sorted(os.listdir(base_dir))


cnt = 0

for path in paths:
    cnt += 1
    tar_path = base_dir + path
    print(str("processing: " + tar_path + " : " + str(cnt) + " / " + str(len(paths))))

    # newly unarchived directory does not need ".tar" in its name
    new_dir = str.split(tar_path, ".")[0]
    
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    
    tar = tarfile.open(tar_path)
    tar.extractall(path=new_dir)
    tar.close()

    # rename original tar directory to be listed in the end of the folder
    os.rename(tar_path, base_dir + "Z_" + path)

