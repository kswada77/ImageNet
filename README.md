# ImageNet dataset preparation

** CURRENTLY EDITING **

Describe the step to **prepare** ImageNet dataset STARTING FROM downloading from **Academic Torrents** TO ...  
Also, provide related **python scripts** for those preparations.  note: OS of my machine is **Ubuntu 18.04 LTS**

Please note that largest ILSVRC dataset available from Academic Torrents is **ImageNet LSVRC 2012 Training Set (Object Detection)** (147.9GB).  
Therefore, I downloaded **ImageNet LSVRC 2012 Training Set (Object Detection)** as CLS-LOC 2015 dataset from Academic Torrents and **2015 development kit** from ILSVRC 2015 web page.  

## Step Overview

STEP | Size | TIME
--------------|------------|------------
1. Find ImageNet LSVRC 2012 dataset and download torrent file | |
2. Download the datasets from Academic Torrents | 147.9 GB + 6.74 GB | about 35 HOURS
3. Unarchive donwloaded dataset files and Untar training dataset  | | 50 - 60 minutes
4. Download ILSVRC 2015 development kit | XX MB | 2-3 minutes
5. Download ILSVRC 2015 CLS-LOC dataset | 155 GB | about XXX HOURS


## 1. Find ImageNet LSVRC 2012 dataset and download torrent file
* Go to [Academic Torrents](http://www.academictorrents.com)

* "Browse" --> select "Dataset" and "Go"

* You can find those 2 files
  - ImageNet LSVRC 2012 Training Set (Object Detection)  147.GB
  - ImageNet LSVRC 2012 Validation Set (Object Detection)  6.74 GB

* Select those files and "Download"


## 2. Download the datasets from Academic Torrents
**Note that downloading entire dataset takes time !!!**  (my case: **about 35 HOURS** :astonished: :sleepy:)
* Right after you click "Download" at Academic Torrents, torrent file is downloaded

* Click the downloaded torrent file, you can start application "Transmission" (Ubuntu 18.04 LTS) to download dataset.

* **You may need to change configuration of "Transmission"** to start download dataset.

* For watching log, go to "Help" --> "Message Log".

* **My case** is:
  - Downloading never started after waiting 24 hours.
  - Check "Message Log" and find that some relevant peers are found but "IPv6 DHT not ready"
  - Open "Settings" of the "Transmission" and go to "Network" tab.  Chang receiving connection port to 80
  - **Uncheck**: using random ports, using UPnP or NAT-PMP
  - **Uncheck** also:  all options
    These unchecking may result to **slower** downloading though.


## 3. Unarchive donwloaded dataset files and Untar training dataset
* Unarchive downloaded training set and validation set files.
  - example command: tar -xvf ILSVRC2012_img_train.tar
  Note that only unarchiving took **almost 20 minutes** on my machine

* You notice that validation set folder has **50,000 JPEG files**, but training set folder has **1,000 tar files**, which correspond to each image category.  You need to untar those files by youself.

* In order to untar those files, you can use python scipt **01_untar_all_tarfiles.py**. Note that this is **NOT** batch script (such as using "argparse").  
```
* This python script does:
  - create new directory for each tar file
  - untar original tar file into newly created directory
  - rename original tar file adding "Z_" prefix to be listed at the end of current directory, which is convenient deleting original tar files manually afterward.
 ```
  Note that untaring those 1000 tar files took **almost 30-40 minutes** :fire: on my machine
  
* After executing the script, you find 2,000 files and subdirectories. 1,000 subdirestories are untarred one and the other 1,000 are original but renamed with "Z_" prefix tar files, which can be deleted manually if you do not need.
**BUT PLEASE CHECK THAT UNTARING FINISHED SUCCESSFULLY :clap: :clap:  BEFORE DELETING ORIGINAL TAR FILES**


## 4. Download ILSVRC 2015 development kit
* Go to [ImageNet LSVRC (ILSVRC) 2015 web page](http://image-net.org/challenges/LSVRC/2015/download-images-3j16.php)

* You can find link for downloading **development kit** in the middle of the page

* Click the link, download the file, and unarchive the file  --> file name:  ILSVRC2014_devkit 


## 5. Download ILSVRC2015 CLS-LOC dataset
**Note that downloading entire dataset takes time !!!**  (my case: **about 35 HOURS** :astonished: :sleepy:)
* Go to [ImageNet LSVRC (ILSVRC) 2015 web page](http://image-net.org/challenges/LSVRC/2015/download-images-3j16.php), same as development kit above

* You can find link for downloading **CLS-LOC dataset** in the middle of the page

* Click the link, download the file, and unarchive the file  --> file name: 
