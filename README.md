# 🧪 Flaky Tests Vocabulary: The Reproduction Efforts

This is a reproduction efforts to re-create the original paper: "What is the Vocabulary of Flaky Tests?" as part of the 
study program "Mining Software Repositories (MSR 2020-21)" provided by SoftLang Team at University of Koblenz-Landau.

* Important 1: Please refer to the section: "Extra: A) How to start?" to see how to start the project.

* Important 2: The diagrams are created or re-created by me however they might be subject to copy-right so use or adopt with your own risk.

## MetaData:
This paper is inspired by the 2020 Paper What is the Vocabulary of Flaky Tests?" written by: Gustavo Pinto and
               Breno Miranda and
               Supun Dissanayake and
               Marcelo d'Amorim and
               Christoph Treude and
               Antonia Bertolino.
Here, we simply try to re-create what the original work has achieved to re-confirm and evaludate the challenges invloved in
making or verification of a MSR paper. The flaky tests are tests that pass and fail periodically without any code changes. 
There might be different underlying reasons causing such tests to occur. This paper continues investigations of 2 existing papers.
They used the base dataset of manually tracked flaky tests and automated the suggested framework to find vocabulary (simply tokens and keywords) that relate to flakiness using NLP. 


Links to Original Work:

DBLP: https://dblp.org/rec/conf/msr/0001MDdTB20.html?view=bibtex

Conference Link: https://2020.msrconf.org/details/msr-2020-papers/43/What-is-the-Vocabulary-of-Flaky-Tests-

GitHub Link: https://github.com/damorimRG/msr4flakiness

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

Hardware:

Software:
- Base ZSH bash (or equivalent)

- Python 3.8 or above (or use Conda)

- Open Source Machine Learning Software WEKA (used for algorithms: : Random Forest, Decision Tree, Naive Bayes,
Support Vector Machine, and Nearest Neighbour)

// My Machine:

MacOs Catalina, 16 GB RAM, 2.6 GHZ Intel's Core-i7 x 6 CORES

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
# to initialize and run everything
zsh ./process/initialization.sh



# You can activate the environment if you want but the initialization does that Automatically
source ez_env/bin/activate
# to exit env simply type
deactivate
```


#### B) Known Issues:

None.

Further potential issues are explained in Project management summary.