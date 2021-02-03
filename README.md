# 🧪 Flaky Tests Vocabulary: The Reproduction Efforts

This is a reproduction efforts to re-create the original paper: "What is the Vocabulary of Flaky Tests?" as part of the 
study program "Mining Software Repositories (MSR 2020-21)" provided by SoftLang Team at University of Koblenz-Landau.

* Important: Please refer to the section: "Extra: A) How to start?" to see how to start the project.

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

- Docker (already running)
  
- Extra: Open Source Machine Learning Software WEKA (used for algorithms: : Random Forest, Decision Tree, Naive Bayes,
Support Vector Machine, and Nearest Neighbour)

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

The structure of our data:

A) Input:

B) Temp:

C) Output:


## 🔥 Delta:

Please refer to
[Delta iPython](/process/delta.ipynb) file to see the explanations about the project's delta.

#### A) about Process:

#### B) about Data:


## Extra:
#### A) What should I do if installing pyCurl failed?

```shell
# if pycurl failed for you on MAC -- couldn't find any other solution 
xcode-select --install

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
