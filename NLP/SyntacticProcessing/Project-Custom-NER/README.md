
## Training and test sentences

In this ‘train_sent’ dataset, there are a total of 2,599 sentences when you form the sentences from the words. Similarly, there are a total of 1,056 sentences in the ‘test_sent’ dataset when you form the sentences from the words. Here, you need to understand that each word in this dataset is provided in a single line. So, first, you need to club all these words together to form the sentences. Moreover, there are blank lines given in the dataset. These blank lines indicate that a new sentence is starting from the next line onwards to the next blank line.<br><br>

## Training and test labels

 There are three labels that have been used in this dataset: O, D and T, which are corresponding to ‘Other’, ‘Disease’ and ‘Treatment’, respectively.These labels correspond to each word that is available in the ‘train_sent’ and 'test_sent' datasets. So, there is one-to-one mapping of each label available in the 'train_label' and 'test_label' datasets with the words that are available in the 'train_sent' and 'test_sent' datasets, respectively.
 
##  Expected tasks

- You need to process and modify the data into sentence format. This step has to be done for the 'train_sent' and ‘train_label’ datasets and for test datasets as well.
- After that, you need to define the features to build the CRF model.
- Then, you need to apply these features in each sentence of the train and the test dataset to get the feature values.
- Once the features are computed, you need to define the target variable and then build the CRF model.
- Then, you need to perform the evaluation using a test data set.
- After that, you need to create a dictionary in which diseases are keys and treatments are values.

## Additional info.
**Data preprocessing:** As you are already aware that the dataset is in the token format instead of sentences, you need to construct the sentences from the words. There are blank lines after the completion of each sentence or a set of labels in label files ('train_label' and 'test_label') and you need to build a logic to arrange them into sentences or a sequence of labels in the case of label files. 
A similar step is to be performed for the 'train_label' and 'test_label' datasets.

**Concept identification:** After preprocessing, we will first explore what are the various concepts present in the dataset. For this task, we will use PoS tagging. It is good to identify all the words from the corpus that have a tag of NOUN or PROPN (nouns) and prepare a dictionary of their counts. We will then output the top 25 most frequently discussed concepts in the entire corpus.
An important point to note here is that we are using both test and train sentences for concept identification. This is an exploratory analysis on the complete data. 

**Defining the features for CRF:** Here, you need to perform the following three steps:

- Define the features with the PoS tag as one of the features.
- While defining the features in which you have used the PoS tags, you also need to consider the preceding word of the current word. The use of the information of the preceding word makes the CRF model more accurate and exhaustive.
- Mark the beginning and the end words of a sentence correctly in the form of features.
 
**Getting the features and the labels of sentences:** In this step, you need to perform the following two tasks:
Write the code to get the features' value of a sentence after defining the features in the previous step.
Write the code to get a list of labels of a given preprocessed label line that you have created earlier.
 

**Defining input and target variables:** In this step, you need to perform the following two tasks:
Extract the features' values for each sentence as an input variable for the CRF model in the test and the train dataset.
Extract the labels as the target variable for the test and the train dataset.
 
**Building the model:** You need to build the CRF model for a custom NER application using the features and the target variables.

**Evaluation:** Evaluate the model using the following two steps:

Predict the labels of each of the tokens in each sentence of the test dataset that has been preprocessed earlier.
Calculate the f1 score using the actual and the predicted labels of the test dataset.
 
**Identifying the diseases and treatment using a custom NER: **

Create the code or logic to get all the predicted treatments (T) labels corresponding to each disease (D) label in the test dataset. You can refer to the following image to get an idea on how to create a dictionary where diseases are working as keys and treatments are working as values.
Please note that here, we are assuming that if there is a disease in the sentences, then the treatment mentioned in that sentence can be assumed to be the treatment for that disease. Also, there is an assumption that the same treatment can work for different diseases.
