import os
os.chdir("/media/kswada/MyFiles/data/imagenet/ILSVRC2015/images/")
print(os.getcwd())


import tarfile



# ------------------------------------------------------------------------
# Untar all subdirectories into new directories
# ------------------------------------------------------------------------
# set base path and tar file name
# YOU NEED TO CHANGE HERE FOR YOUR ENVIRONMENT
base_dir = "/media/kswada/MyFiles/data/imagenet/ILSVRC2015/images/ILSVRC2012_img_train/"


paths = sorted(os.listdir(base_dir))

len(paths)



# ----------
# loop over each tar file path

# 1. create new directory for storing untar files
# 2. untar file in the new directory
# 3. rename original tarfile name adding "Z_" preffix in order to be listed in the end in the directory,
#    which is convenient for deleting those original tar file manually afterward.

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

    # rename original tar file adding "Z_" predix to be listed in the end of the directory
    os.rename(tar_path, base_dir + "Z_" + path)

