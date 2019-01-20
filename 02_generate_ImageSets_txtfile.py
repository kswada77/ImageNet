#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
os.chdir("/media/kswada/MyFiles/data/imagenet/ILSVRC2015")
print(os.getcwd())



# ------------------------------------------------------------------------
# Generate "train_cls.txt" file
# ------------------------------------------------------------------------
base_dir = "/media/kswada/MyFiles/data/imagenet/ILSVRC2015/Data/CLS-LOC/train"
cls_paths = sorted(os.listdir(base_dir))


idx = 0
cls_cnt = 0

with open("train_cls.txt", "w") as f:

    for cls_path in cls_paths:
        cls_cnt += 1
        msg = "processing : " + cls_path + " " + str(cls_cnt) + " / " + str(len(cls_paths))
        print(str(msg))
       
        file_names = sorted(os.listdir(os.path.join(base_dir, cls_path)))
    
        for file_name in file_names:
            idx += 1
            img = str.split(file_name, ".")[0]    
            result = "{}/{}\t{}\n".format(cls_path, img, idx)    
            f.write(result)


    

# ------------------------------------------------------------------------
# Generate "val.txt" file
# ------------------------------------------------------------------------
base_dir = "/media/kswada/MyFiles/data/imagenet/ILSVRC2015/Data/CLS-LOC/train/"
file_names = sorted(os.listdir(base_dir))


idx = 0

with open("val.txt", "w") as f:

    for file_name in file_names:
        idx += 1
        img = str.split(file_name, ".")[0]
        result = "{}\t{}\n".format(img, idx)    
        f.write(result)
