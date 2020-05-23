# DefinitiaonExtraction-Defteval-
## This Repo contains our contribution to the sem-eval task6 Definition extraction subtask 1 and 2

# Requirements:
- pytorch 2.x 
- transformers [[link] https://github.com/huggingface/transformers]
- flair nlp [[link] https://github.com/flairNLP/flair]]
- allennlp [[link] https://allennlp.org/]]

# Task and Data:
* full data attached to this task can be found in the official repo of the task in the following link [[link] https://github.com/adobe-research/deft_corpus]


# Task1 Description:
* This task aims at classifying each sentence whether it contains a defintion or not

# Task2 Description:
* This is a sequence labeling task aims at classifiying each token to definition class 

# Results (currently Subtask2):

Model     | F1- macro Score
-----     | -----
semi-crf    | 15%
-----     | -----
BERT         |  39%
-----     | -----
BiLSTM CRF GLOVE  | 32.2%
-----     | -----
BiLSTM CRF Character | 37.1%
-----     | -----
BILSTM CRF char+GLOVE | 38.2%
-----     | -----
BILSTM CRF ELMO | 42.1%
-----     | -----
BILSTM CRF BERT | 43.8%
-----     | -----
BILSTM CRF RoBERTA | 43.2%
-----     | -----
# BILSTM CRF flairs | 47%

# Rankings
Task1: 29/55
Task2: 33/55
