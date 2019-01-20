# ImageNet dataset preparation

** CURRENTLY EDITING **

Describe the process to **prepare** ImageNet dataset FROM downloading from **Academic Torrents** TO ...  
Also, provide related **python scripts** for those preparations.  note: OS of my machine is **Ubuntu 18.04 LTS**

1. Find ImageNet LSVRC 2012 dataset and download torrent file
2. Download dataset
3. 
4.
5.


### 1. Find ImageNet LSVRC 2012 dataset and download torrent file
* Go to Academic Torrents (academictorrents.com)
* "Browse" --> select "Dataset" and "Go"
* you can find those 2 files
  - ImageNet LSVRC 2012 Training Set (Object Detection)
  - ImageNet LSVRC 2012 Validation Set (Object Detection)
* Select those files and "Download"


### 2. Download dataset
**IT TAKES TIME !!!**  (my case: about 35 hours)

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
  
### 3. 
