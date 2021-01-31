# 🧪 Flaky Tests Vocabulary: The Reproduction Efforts

This is a reproduction efforts to re-create the original paper: "What is the Vocabulary of Flaky Tests?" as part of the 
study program "Mining Software Repositories (MSR 2020-21)" provided by SoftLang Team at University of Koblenz-Landau.

* Important 1: Please refer to the section: "Extra: A) How to start?" to see how to start the project.

* Important 2: The diagrams are created or re-created by me however they might be subject to copy-right so use or adopt with your own risk.

## MetaData
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

Research Questions -- grabbed from the paper:
RQ1. How prevalent and elusive are flaky tests?
RQ2. How accurately can we predict test flakiness based on source code identifiers in the test cases?
RQ3. What value do different features add to the classifier?
RQ4. Which test code identifiers are most strongly associated with test flakiness?

## Process:
The general re-creation work done by us goes through the following steps:

![Alt text](doc/diagrams/general-procedure.png?raw=true "General Procedure")


0- Re-organize: the orginal repository is very poorly organized the data and codes are mixed we will reorganize it.

1- Detection: flaky detection uses a base dataset to derive features of flaky and non-flaky tests. We check the csv and txt files here and try to recreate them.

2- Identification: Use NLP approaches to find tokens prevalent in flaky tests and make a classifier.

3- Discovery: Fetch and go through Github to see if we can identify flakiness using the selected features — We will recreate this part for only a few repositories.

?- Evaluation: The code that generated their evaluations seem to not be included — we will investigate this.

4- Correlation and Delta: We will make an iPython for comparisons, final reports and summaries.


 ✅  How to Validate the works?

## Requirements:

Hardware:

Software:
- Python 3.8

// My Machine:

MacOs Catalina, 16 GB RAM, 2.6 GHZ Intel's Core-i7 x 6 CORES

## Data:
Following is the general description of data types along with the schema overview:


## 🔥 Delta:

#### A) about Process:

#### B) about Data:


## Extra:
#### A) How to start?

0- Activate the environment
source ez_env/bin/activate

// to exit always
deactivate

#### B) Known Issues: