# ImageNet dataset preparation

** CURRENTLY EDITING **

Describe the process to **prepare** ImageNet dataset STARTING FROM downloading from **Academic Torrents** TO ...  
Also, provide related **python scripts** for those preparations.  note: OS of my machine is **Ubuntu 18.04 LTS**

Please note that largest ILSVRC dataset available from Academic Torrents is **ImageNet LSVRC 2012 Training Set (Object Detection)** (147.9GB). ImageNet LSVRC (ILSVRC) 2015 web page [http://image-net.org/challenges/LSVRC/2015/download-images-3j16.php] states that "This dataset (CLS-LOC (object classification and localization) dataset: 155GB) is unchanged from ILSVRC2012 and ILSVRC2013.".  Therefore I downloaded **ImageNet LSVRC 2012 Training Set (Object Detection)** as CLS-LOC 2015 dataset from Academic Torrents and development kit from ILSVRC 2015 web page.


1. Find ImageNet LSVRC 2012 dataset and download torrent file
2. Download dataset
3. 
4.
5.


### 1. Find ImageNet LSVRC 2012 dataset and download torrent file
* Go to Academic Torrents [http://www.academictorrents.com.]
* "Browse" --> select "Dataset" and "Go"
* You can find those 2 files
  - ImageNet LSVRC 2012 Training Set (Object Detection)
  - ImageNet LSVRC 2012 Validation Set (Object Detection)
* Select those files and "Download"


### 2. Download the dataset from Academic Torrents
**Note that downloading entire dataset takes time !!!**  (my case: about 35 hours)
* Right after you click "Download" at Academic Torrents, torrent file is downloaded
* Click the downloaded torrent file, you can start application "Transmission" (Ubuntu 18.04 LTS) to download dataset.
* **You may need to change configuration of "Transmission"** to start download dataset.
* For watching log, go to "Help" --> "Message Log".
* **My case** is that:
  - Downloading never started after waiting 24 hours.
  - Check "Message Log" and find that some relevant peers are found but "IPv6 DHT not ready"
  - Open "Settings" of the "Transmission" and go to "Network" tab.  Chang receiving connection port to 80
  - **Uncheck**: using random ports, using UPnP or NAT-PMP
  - **Uncheck** also:  all options
    -->  This may result to **slower** downloading though.


### 3. Unarchive donwloaded dataset files
* Unarchive downloaded files (training set and validation set). Note that only unarchiving took almost 20 minutes on my machine.


### 4. Download development kit from ILSVRC 2015
 * Go to **Large Scale Visual Recognition Challenge 2014 (ILSVRC2014)** [http://www.image-net.org/challenges/LSVRC/2014/]
 * You can find link for **development kit** download link in the middle of the page
 * Click the link and download the file and unarchive the file  --> file name:  ILSVRC2014_devkit
 * 

### 3. 
