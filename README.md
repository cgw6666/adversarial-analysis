# README for Evaluating This Model
1. Steps for Preprocessing Data
* Download 14 edf patient data.
* Create a list of directories in txt.
* Include 14 edf directory txt path in half_half_advanced_manual_preprocess.py.
* run the following command in your terminal
	* python half_half_advanced_manual_preprocess.py
2. Specification of dependencies
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
3. Training code
Running Training Code
* In your Terminal, please enter python author_main_v1.py
Hyperparameters
* depth_AE = 4, Autoencoder Depth Layer
* decay = 0.9
* lr, 0.00005, learning rate
* Evaluation Code
* Running Evaluation Code
* Evaluation is also done in the same file. In your Terminal, please enter python author_main_v1.py. Your results, including test accuracy rate and training accuracy rate, will be stored in ./results and ./result.csv.

4. Table of results
| Model Hyperparameter Description                                             | Average Training Accuracy | Average Testing Accuracy | Average Testing AE Cost  | Average Diagnosis Model Testing Cross Entropy  | Total Training Cost | Training AE Cost | Person Detection Cross Entropy | Diagnosis Model Cross Entropy  |
|------------------------------------------------------------------------------|---------------------------|--------------------------|--------------------------|------------------------------------------------|---------------------|------------------|--------------------------------|--------------------------------|
| Our Own Data with Original Hyperparameters                                   | 0.5021157659              | 0.4965775578             | 0.2387831375             | 6.972470323                                    | 12.84448104         | 0.2408124713     | 6.951138047                    | 2.565816404                    |
| Author’s Original Data with Original Hyperparameters                         | 0.459538465               | 0.7555714286             | 0.1207760636             | 5.534599529                                    | 6.9780918           | 0.1218919836     | 3.535303864                    | 1.008313099                    |
| Depth_AE=12                                                                  | 0.5035674351              | 0.5013329694             | 0.2186241782             | 6.955525744                                    | 12.86205288         | 0.2181938311     | 6.941493441                    | 2.578973174                    |
| Depth_AE=8                                                                   | 0.5043560447              | 0.4999                   | 0.08418201223            | 6.977689026                                    | 10.82755782         | 0.08414575561    | 6.89504804                     | 1.618578494                    |
| lr=0.005                                                                     | 0.5035921387              | 0.4973197802             | 0.1450377634             | 7.003598636                                    | 11.69126362         | 0.1441404073     | 6.938183412                    | 1.929839263                    |
| lr=0.001                                                                     | 0.5020197789              | 0.4981                   | 0.1848740608             | 6.953791737                                    | 12.73147571         | 0.1859549816     | 6.932600124                    | 2.524739234                    |
| decay=0.5                                                                    | 0.5020887579              | 0.4981417582             | 0.3046278579             | 6.981926914                                    | 12.9451114          | 0.3034750085     | 6.958628536                    | 2.59563433                     |
| decay=0.7                                                                    | 0.5017236702              | 0.4967736264             | 0.2928191495             | 6.96737065                                     | 12.89364802         | 0.2910375515     | 6.942397582                    | 2.580484584                    |
| Random Seizure Interval Composition (Our Own Dataset, failed at 8th Subject) | 0.5319346195              | 0.528475                 | 0.0559582993             | 11.4685816                                     | 4.93997344          | 0.07415821718    | 3.285945508                    | 0.1159703172                   |

5. Dependencies
  - ca-certificates=2022.3.29=hecd8cb5_0
  - certifi=2020.6.20=pyhd3eb1b0_3
  - libcxx=12.0.0=h2f01273_0
  - libedit=3.1.20210910=hca72f7f_0
  - libffi=3.2.1=h0a44026_1007
  - ncurses=6.3=hca72f7f_2
  - openssl=1.0.2u=h1de35cc_0
  - parso=0.7.0=py_0
  - pip=10.0.1=py35_0
  - python=3.5.6=hc167b69_0
  - readline=7.0=h1de35cc_5
  - setuptools=40.2.0=py35_0
  - sqlite=3.33.0=hffcf06c_0
  - tk=8.6.11=h7bc2e8c_0
  - wheel=0.37.1=pyhd3eb1b0_0
  - xz=5.2.5=h1de35cc_0
  - zlib=1.2.12=h4dc903c_0
  - pip:
    - absl-py==0.15.0
    - bleach==1.5.0
    - enum34==1.1.10
    - html5lib==0.9999999
    - importlib-metadata==2.1.3
    - joblib==0.14.1
    - markdown==3.2.2
    - numpy==1.18.5
    - protobuf==3.19.4
    - scikit-learn==0.22.2.post1
    - scipy==1.4.1
    - six==1.16.0
    - sklearn==0.0
    - tensorflow==1.5.0
    - tensorflow-tensorboard==1.5.1
    - werkzeug==1.0.1
    - zipp==1.2.0

5. Reference
* The author's original code is available [here](https://isip.piconepress.com/projects/tuh_eeg/html/downloads.shtml)
* The dataset can be accessed [here via request](https://github.com/xiangzhang1015/adversarial_seizure_detection)