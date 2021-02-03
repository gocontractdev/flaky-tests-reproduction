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

## Process:
The general re-creation work done by us goes through the following steps:

![Alt text](doc/diagrams/general-procedure.png?raw=true "General Procedure")


0- Re-organize: the orginal repository is very poorly organized the data and codes are mixed we will reorganize it.

1- Detection: flaky detection uses a base dataset to derive features of flaky and non-flaky tests. We check the csv and txt files here and try to recreate them.

2- Identification: Use NLP approaches to find tokens prevalent in flaky tests and make a classifier.

3- Discovery: Fetch and go through Github to see if we can identify flakiness using the selected features — We will recreate this part for only a few repositories.

?- Evaluation: The code that generated their evaluations seem to not be included — we will investigate this.

4- Correlation and Delta: We will make an iPython for comparisons, final reports and summaries.


Please refer to
[Process iPython](/process/process.ipynb) file to see the explanations about the project's data.

 ✅  How to Validate the works?

## Requirements:

Minimum Hardware:
- Intel Core-i7 x ,2.2 GHZ 6 Cores  
- RAM 8 GB (I recommend at least 16 GB)

Software:
- MacOs Catalina or Linux Distributions
  
- Vanilla ZSH bash (or equivalent)

- Python 3.8 or above (use Conda)

- Docker (already running)
  
- Extra: Open Source Machine Learning Software WEKA (used for algorithms: : Random Forest, Decision Tree, Naive Bayes,
Support Vector Machine, and Nearest Neighbour)

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


Please refer to
[Data iPython](/data/data.ipynb) file to see the explanations about the project's data.




## 🔥 Delta:

Please refer to
[Delta iPython](/process/delta.ipynb) file to see the explanations about the project's delta.

#### A) about Process:

#### B) about Data:


## Extra:
#### A) How to start?

If you have a compatible extended shell simply running the 'initialization' file will execute 
everything necessary for this project. From there follow the steps console asks (it automatically sets the right environment):

- Important 1: The password is your machine's password (needed for Git Clone).

```shell
# to initialize and run everything -- it will prompt and asks question if needed
zsh ./process/initialization.sh

# Please choose the mode? [Easy Mode (e or ez) | Heavy Mode (h or hv)]
> h # if you want full process
> e # if you want demo process

# extra -- only try if something failed

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

Further potential issues are explained in Project management summary.