README for Evaluating This Model
1. Specification of dependencies
* requirements.txt is included for installing dependencies
* environment.yml is provided for activating Anacaonda environments.
To install dependencies, please perform the following steps:
* Using environment.yml
   * conda env create -f environment.yml
* Using pip
   * Install Anaconda
   * conda create --name env1 pip python=3.5 parso=0.7
   * conda activate env1
   * pip install sklearn
   * pip install tensorflow==1.5.0
2. Training code
Running Training Code
* In your Terminal, please enter python author_main_v1.py
Hyperparameters
* depth_AE = 4, Autoencoder Depth Layer
* decay = 0.9
* lr, 0.00005, learning rate
* Evaluation Code
* Running Evaluation Code
* Evaluation is also done in the same file. In your Terminal, please enter python author_main_v1.py. Your results, including test accuracy rate and training accuracy rate, will be stored in ./results and ./result.csv.

Reference
* The author's original code is available here: https://isip.piconepress.com/projects/tuh_eeg/html/downloads.shtml
* The dataset can be accessed here via request: https://github.com/xiangzhang1015/adversarial_seizure_detection