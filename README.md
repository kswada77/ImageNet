# ImageNet dataset preparation for deep learning study

** CURRENTLY EDITING **  
I have been really inspired :smiley: and motivated :satisfied: by [PyImageSearchGurus](https://www.pyimagesearch.com) for studying and challenging deep learning for computer vision.  
This is really awesome resources. :heart_eyes:  I could have challenged to various deep learning architectures, techniques and data preparation, including one of most famous dataset, **ImageNet**.  
ImageNet dataset is available at [here](http://www.image-net.org), but only for non-commercial research and/or educational purposes. Unfortunately not available to me. :disappointed:   
Instead, I tried downloading via Academic Torrents and prepare data for my deep learning studies. I would like to share the steps for this preparation from my experience. :+1: :+1:    

---
This page
* describes the step to **prepare** ImageNet dataset
  - From:   downloading torrent file from  **Academic Torrents**
  - To:   
* also, provides related **python scripts** for the dataset preparations.

Please note that currently largest ILSVRC dataset available via **Academic Torrents** is:  
  - **ImageNet LSVRC 2012 Training Set (Object Detection)** (147.9GB).  
I believe that the image datasets of other ILSVRC (2013, 2014, 2015) available at official ILSVRC organization are same as or not much different from that of ILSVRC 2012.

---
## Overview of the step
Regarding to **estimated required time**:
  - depends on your machine and network environment.
  - Estimated time shown in the table below is **the case of my machine and network environment** for reference. At my environment, STEP No.2 and No.5 took more than 30 hours for each. :bangbang:  

**You can start No.5 in parallel** with No.3 and No.4 after finishing No.2.

No. | step | file size | required est. time | emoji
:---:|:---|:---|:---|:---
1|download torrent file for ILSVRC 2012 dataset|(small)|1-2 min.|:rocket:
2|download ILSVRC 2012 dataset by torrenting|147.9+6.7 GB|35 hrs.|:astonished::sleepy:
3|unarchive datasets and untar training dataset|n/a|50-60 min.|:fire:
4|download ILSVRC 2015 development kit|7.4 MB|2-3 min.|:rocket:
5|download ILSVRC 2015 CLS-LOC dataset|155 GB|30 hrs.|:astonished::sleepy:

---
## 1. Download torrent file for ImageNet LSVRC 2012 from Academic Torrents
* Go to [Academic Torrents](http://www.academictorrents.com)

* "Browse" --> select "Dataset" and "Go"

* You can find following 2 files
  - ImageNet LSVRC 2012 Training Set (Object Detection)  147.9 GB
  - ImageNet LSVRC 2012 Validation Set (Object Detection)  6.7 GB

* Select those files and "Download"  --> torrent file is downloaded


---
## 2. Download ILSVRC 2012 datasets by torrenting
* By clicking the downloaded torrent file, you can start application "Transmission" (if your OS is Ubuntu 18.04 LTS) to download dataset.

* **You may need to change configuration of "Transmission"** to start download dataset.

* For watching log, go to "Help" --> "Message Log".

* :ballot_box_with_check: **My case and tips** are:
  - Downloading never started after waiting 24 hours. I checked "Message Log" and noticed that some relevant peers were found but the log message kept showing "Ipv4 DHT not ready" and "IPv6 DHT not ready" endlessly.
  - So I opened "Settings" of the "Transmission" and go to "Network" tab.  Changed receiving connection port to 80
  - **Uncheck**: using random ports, using UPnP or NAT-PMP
  - **Uncheck** also:  all options  
    These unchecking might result to **slower** downloading though.

---
## 3. Unarchive donwloaded dataset files and untar training dataset
* Unarchive downloaded training set and validation set files
```
  linux command example:  tar -xvf ILSVRC2012_img_train.tar
```
* You notice that validation set folder has **50,000 JPEG files**, but training set folder has **1,000 tar files**, which correspond to each image category.  You need to untar those files by youself.

* In order to untar those files, you can use python scipt :ballog_box_with_check: **01_untar_all_tarfiles.py**  
Note that this is **NOT** batch script (such as using "argparse").

This **python script** does:  
  - create new directory for each tar file  
  - untar original tar file into newly created directory  
  - rename original tar file adding "Z_" prefix to be listed at the end of current directory, which is convenient deleting original tar files manually afterward.  
 
After executing the script successfully, you should in find 1,000 subdirectories storing untarred JPEG files and 1,000 original but renamed (with "Z_" prefix) tar files. :clap: :clap:  
You can delete those renamed tar files if you do not need.  
:ballot_box_with_check:  But **please check before deleting** whether untarring finishes successfully.


---
## 4. Download ILSVRC 2015 development kit
* Go to [ImageNet LSVRC (ILSVRC) 2015 web page](http://image-net.org/challenges/LSVRC/2015/download-images-3j16.php)

* You can find link for downloading **development kit** in the middle of the page

* Click the link, download and unarchive the file  --> file name:  ILSVRC2014_devkit 


---
## 5. Download ILSVRC2015 CLS-LOC dataset
* Go to [ImageNet LSVRC (ILSVRC) 2015 web page](http://image-net.org/challenges/LSVRC/2015/download-images-3j16.php), same as development kit above

* You can find link for downloading **CLS-LOC dataset** in the middle of the page

* Click the link, download the file, and unarchive the file  --> file name: 
