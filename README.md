# flaky-tests-reproduction
Reproduction efforts to re-create the orginal paper "What is the Vocabulary of Flaky Tests?"


DBLP: https://dblp.org/rec/conf/msr/0001MDdTB20.html?view=bibtex
GitHub Link: https://github.com/damorimRG/msr4flakiness
 
Idea:
The flaky tests are tests that pass and fail periodically without any code changes. There might be different underlying reasons causing such tests to occur. This paper continues investigations of 2 existing papers. They used the base dataset of manually tracked flaky tests and automated the suggested framework to find vocabulary (simply tokens and keywords) that relate to flakiness using NLP. 
 
Phases: 
0- Re-organize: the orginal repository is very poorly organized the data and codes are mixed we will reorganize it.
1- Detection: flaky detection uses a base dataset to derive features of flaky and non-flaky tests. We check the csv and txt files here and try to recreate them.
2- Identification: Use NLP approaches to find tokens prevalent in flaky tests and make a classifier.
3- Discovery: Fetch and go through Github to see if we can identify flakiness using the selected features — We will recreate this part for only a few repositories.
?- Evaluation: The code that generated their evaluations seem to not be included — we will investigate this.
4- Correlation and Delta: We will make an iPython for comparisons, final reports and summaries.
 
Research Questions -- from paper:
RQ1. How prevalent and elusive are flaky tests?
RQ2. How accurately can we predict test flakiness based on source code identifiers in the test cases?
RQ3. What value do different features add to the classifier?
RQ4. Which test code identifiers are most strongly associated with test flakiness?
 
Constraints:
2 Max
+ We would need the  knowledge of Python, Java, OOP, Machine Learning, Data-structures.
+ We  would  use: Conda for iPython + Python, WEKA (open source analysis tool used also in paper).
 
Extra:
Link to Explination Video: https://2020.msrconf.org/details/msr-2020-papers/43/What-is-the-Vocabulary-of-Flaky-Tests-
 
Why? (Why did I discontinue the previous paper):
Unfortunately, even-though the paper has the data publicly available and the process is explained throughly; it does not have the source codes available and as a result the re-production of it is out of the scope of this course. 


# Installation:

0- Activate the environment
source ez_env/bin/activate

// to exit always
deactivate