# FOMCTranscriptAnalysis
Textual analysis of FOMC Transcripts. My research examines the relationship between words said during FOMC meetings, and changes in Federal Funds Rate. You can walk through my data cleaning, processing, and analysis process here. The final paper is linked in the README.

The relevant data is in the feddata/ folder, organized by year. Each year contains three versions of ever transcript organized in the following way:

```
FOMC19820202meeting.pdf - PDF of transcript directly from website
FOMC19820202meeting.txt - PDF converted into text file
FOMC19820202meetingStop.txt - text file with stop words (the, and, is, I, etc) removed
FOMC19820202meetingStopstemmed.txt - text file with stop words removed and all remaining words stemmed (i.e. 'increases', 'increasing' and 'increase' correspond to 'increas')
```

You can understand how I came up with the results of my paper by opening data_manipulations.py. It contains over 1500 lines of python code, and is laid out in a format that is relatively easy to understand. Includes regression + graphs that are in paper.

To run data_manipulations.py (the notebook with the process of how I conducted this research):

0) You will need Anaconda. You can download it here: https://www.anaconda.com/download/
1) Clone this repo
1) Open your terminal (or powershell in windows) and navigate to this repo
2) Type in "jupyter notebook" for Mac or "ipython notebook" for Windows
3) Select data_manipulations.py

**Warning** : _Read the final paper for a deeper understanding of the mathematics behind the methods and model used._ There are 3 lines of code for the regression, but there is an entire section of the paper devoted to explaining why those lines of code actually work.

## Introduction of Final Paper

Textual analysis applied to economic research has undergone a renaissance of sorts in recent years. With significant advancements in machine learning and computing power, formerly qualitative data embedded in texts has now become available for economists to quantify, classify, and incorporate into their models. These developments have created an opportunity to answer questions from level of individual actors and their reactions, rather than summary statistics describing their interactions with markets. Through applying new machine learning methods, researchers can gain a more granular understanding of how individual reactions affect different economic outcomes.

In this paper, we explore the reactions of a small set of actors with outsized influence on economic policy: members of the Federal Open Market Committee (FOMC). We attempt to understand what concerns are the most important in determining a change in Federal Reserve policy regarding interest rates. Previous research analyzes quantitative measures, such as unemployment and inflation, to understand what prompts policymakers to change interest rates. In undergoing a textual analysis, we can answer this question by looking directly at qualitative data from these policymakers.

The Federal Reserve releases qualitative information in the form of meeting minutes, statements, press releases, reports and transcripts. Transcripts of meetings and conference calls are released to the public with a five-year lag. As FOMC members’ comments are relatively protected from scrutiny by this lag, we can use these transcripts to understand which issues drive changes in interest rate policy.

Through textual analysis of transcripts of FOMC meetings, can we identify the primary concerns that cause the Federal Reserve to change the target federal funds rate? Can we do this by quantifying the content of the meeting? By answering these questions, we can take a closer look at our traditional economic understanding of the factors that influence the federal funds rate. We can attempt to understand if the FOMC members’ words reflect the actions of the market.

To achieve this, we first collect, clean and transform data with the goal of isolating relevant word counts. Our outcome variable is the target federal funds rate. We focus on years 1982 – 2008, as pre-1982 there was no target rate and post-2008 the Federal Reserve switched to a target range. We began by scraping FOMC transcripts from this time period, in total amounting to nearly 18,741 pages. Each document is stripped of formatting, converted into text, removed of stop words, and passed to the Porter algorithm to reduce to stems. We then preselect a list of relevant word stems to observe, chosen by examining descriptive statistics and economic intuition. After pre-processing we count words, scale by size of document, and associate the words with the relevant change in federal funds rate.

We then examine the relationship between these words and our outcome variable. We use a linear model using least-squares penalty trained with an L1 prior (also known as Lasso), with iterative fitting along a regularization path to derive our regression coefficients. We select the best model using a 20-fold cross validation scheme fitted with coordinate descent and least angle regression. We also compile various summary statistics, examining how the weighted frequency of these words changes over time, and how they vary across positive and negative changes in interest rate.

We conduct two separate the regressions on reductions in federal funds rate and increases in federal funds rate. In both, we do not find no relevant word stems that are statistically significant in determining the federal funds rate. We test our regressions with t-statistics to confirm our model's result. We then conduct a textual analysis of our sample, revealing a lack of variability in our outcome variables with regard to reductions in federal funds rate, and additionally a lack of variability in proportions of word counts across transcripts associated with increases in federal funds rate. We are able to deduce that FOMC transcripts in our sample roughly touch the same topics in similar proportion regardless of the outcome of the meeting. This suggests that there may be unobserved factors that FOMC members do not reveal in meetings that determine their vote, and that FOMC meetings are more of a discussion of possibilities with few subtleties revealing voting decision.
