# 🧪 Flaky Tests Vocabulary: The Reproduction Efforts
"
This is a reproduction efforts to re-create the original paper: "What is the Vocabulary of Flaky Tests?" as part of the 
study program "Mining Software Repositories (MSR 2020-21)" provided by SoftLang Team at University of Koblenz-Landau. 
" - Amir Dashti

## MetaData:
This repository describes the recreation of 2020 Paper "What is the Vocabulary of Flaky Tests?" written by: Gustavo Pinto and
               Breno Miranda and
               Supun Dissanayake and
               Marcelo d'Amorim and
               Christoph Treude and
               Antonia Bertolino.


Here, we try to re-create what the original work has achieved to re-confirm and evaluate the challenges involved in
making or verification of an MSR paper. The flaky tests are tests that pass and fail periodically without any code changes. 
There might be different underlying reasons causing such tests to occur. This paper continues investigations of 2 existing papers.
They used the base dataset of manually tracked flaky tests and automated the suggested framework to find vocabulary (simply tokens and keywords) that relate to flakiness using NLP. 


Links to Original Work:

DBLP: https://dblp.org/rec/conf/msr/0001MDdTB20.html?view=bibtex

Conference Link: https://2020.msrconf.org/details/msr-2020-papers/43/What-is-the-Vocabulary-of-Flaky-Tests-

GitHub Link: https://github.com/damorimRG/msr4flakiness

-----------------
Research Questions (*** adopted from the paper):

RQ1. How frequently do flaky tests happen and how prevalent they are?

RQ2. What is the precision of predicting test flakiness using tokens collected from the source code?

RQ3. What is the importance of different features within the model?

RQ4. Find the tokens that are highly connected to flakiness of a tests.

## Requirements:

Minimum Hardware:
- MacOs Catalina or Linux Distributions
  
- Intel Core-i7 x ,2.2 GHZ 6 Cores  

- RAM 8 GB (I recommend at least 16 GB)
  
Software:
  
- Vanilla ZSH bash (or equivalent)

- Python 3.8 or above (use Conda)

- Docker (already running) * ⛴ Docker is only needed if you use the heavy mode

## Process:
The general re-creation work done by us goes through the following steps:

![Alt text](doc/diagrams/general-procedure.png?raw=true "General Procedure")

0- Re-organize: the original repository is very poorly organized the data and codes are mixed we will automatically clone and reorganize it in right places.

1- Detection: Depending on your decision can prepare flaky / non-flaky samples:

> e - EASY mode will use already processed initial data.
> 
> h - HEAVY mode will fully re-calculate flaky and non-flaky samples.

2- Identification (tokenization): Uses NLP approaches to find tokens and candidate features.

3- Discovery: Finalizes the classifier model and produces the outputs.

4- Comparison: Open-ended process to check and verify the output.


If you have a compatible extended shell simply running the 'initialization' file will execute 
everything necessary for this project. From there follow the steps console asks (it automatically sets the right environment and installs necessary packages):


```shell
# to initialize and run everything
zsh ./process/initialization.sh

# it will prompt and asks question if needed

# Please choose the mode? [Easy Mode (e or ez) | Heavy Mode (h or hv)]

> h # if you want full process
> e # if you want demo process

# the process might take few minutes
```

👉 Please refer to
[Process iPython](/process/process.ipynb) file to see the full explanations about the process.


- Important 1: The password is your machine's password (needed for Git Clone).

- Important 2: Refer to the extra section if something did not work.


 ✅  How to Validate the works?
--------------------
If everything works properly, the output produced by the code 'features_frequency.csv' will include the
top most related vocabulary to flakiness of the tests. You can quickly verify this by running coe in the easy (e) mode.

Refering to the paper: "we noted that
job, action, and services are commonly associated with flaky tests.".
So, the output here should be also similar.



## Data:
Following is the general description of data types along with the schema overview:

---
- Basics:

> Positive === Flaky Test
> 
> Negative === Estimated Flaky Test (a test that is not proven to be flaky so far)

- Initial Dataset:

#### The main dataset that has been used for this work is called "DeFlaker".


> The original paper faces the following issues using the dataset:
>
> 1- The dataset does not list the non-flaky tests but since it was needed for their model training; they ran the tests multiple times to find possible candidates.
>
> 2- One of the projects fails in build so they use 24 out of 25 Java projects provided by the dataset.
>
>
>For further on DeFlaker: http://www.deflaker.org/icsecomp/
> 
>  <sup>Note: This part is adopted (in simple words) from the paper. </sup>

The structure of our data: (To see sample parts of data refer to: [Delta iPython](/process/delta.ipynb))

A) Input:

- historical_projects_copied.csv: A csv file used as an input in original paper. It includes list of github projects that have been monitored.

- histoircal_rerun_flaky_tests.csv: A csv file used as an initial input that includes detailed list of test files and test methods that are known as being flaky.

- list-flaky.csv: A csv file very similar to histoircal_rerun_flaky_tests.csv but it also includes SHA and version of flakiness since they might have change or fixed.

- ez/ : This directory includes a copy of the mentioned files for representation purposes. It is not used in real processes.

B) Temp:

- test_files/ : Includes multiple text files each file including the full text from a specific test file.
  File name represents the test file name and its category.

- test_cases/ : Running methods jar file will separate test files to test cases. This directory includes multiple text files; 
 each file includes text of a specific test known to be flaky.

- sample_flaky/ : Includes multiple text files that are separated line by line; each line has a token grabbed and processed from a respective
test case file.

C) Output:

- features_raw.csv: Includes raw list of all tokens with their frequencies. It is not yet decided how effective they are in flakiness.

- features_frequency.csv: It includes top filtered tokens that associate with flaky tests and make the vocabulary of flaky tests.

- total_process_original.txt: This file includes the whole code strings of original repository. -- Used to calculated Levenshtein distance.
  
- total_process_rework.txt: This file includes the whole code strings of re-production repository. -- Used to calculated Levenshtein distance.

- total_data_original.txt: This file includes the whole data string of rhe original repository. -- Used to calculated Levenshtein distance.
  
- total_data_rework.txt: This file includes the whole data string of rhe re-production repository. -- Used to calculated Levenshtein distance.

- ez/ : This directory includes a copy of the mentioned files for representation purposes. It is not used in real processes.


## 🔥 Delta:

Please refer to
[Delta iPython](/process/delta.ipynb) file to see the explanations about the project's delta. Here is the summary:
#### A) about Process:


### 📊 Levenstein Distance: 

#### B) about Data:

###  📊 Levenstein Distance: 

## Extra:
#### A) What should I do if installing pyCurl failed?

```shell
# if pycurl failed for you on MAC -- couldn't find any other solution 
xcode-select --install

# quick login to alpein (it is only used for builds and running java) 
docker container exec -it my_little_alpine bin/bash

# You can activate the environment if you want but the initialization does that Automatically
source ez_env/bin/activate
# to exit env simply type
deactivate
```

#### B) Known Issues:

1- The environment which comes along with the project is broken.
It fails in installation of 'pyCurl' depending on you O.S. and your SSL settings it may happen or not happen.

2- Some python files do not actually work. I have modified them to achieve the goals; further on this is explained in 
[Process iPython](/process/process.ipynb).
