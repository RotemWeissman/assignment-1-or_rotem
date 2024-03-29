# Assignment 1

In this assignment you will be creating tools for learning and testing language models. The corpora that you will be working with are lists of tweets in 8 different languages that use the Latin script. The data is provided either formatted as CSV or as JSON, for your convenience. The end goal is to write a set of tools that can detect the language of a given tweet.


The relevant files are under the data folder:

- en.csv (or the equivalent JSON file)
- es.csv (or the equivalent JSON file)
- fr.csv (or the equivalent JSON file)
- in.csv (or the equivalent JSON file)
- it.csv (or the equivalent JSON file)
- nl.csv (or the equivalent JSON file)
- pt.csv (or the equivalent JSON file)
- tl.csv (or the equivalent JSON file)

#### PART 1
In the language_modeling.py file, implement the function *preprocess* that iterates over all the data files and creates a single vocabulary, containing all the tokens in the data. Our token definition is a single UTF-8 encoded character. So, the vocabulary list is a simple Python list of all the characters that you see at least once in the data.

#### PART 2
In the language_modeling.py file, implement the function *lm* that generates a language model from a textual corpus. The function should return a dictionary (representing a model) where the keys are all the relevant *n*-1 sequences, and the values are dictionaries with the *n*_th tokens and their corresponding probabilities to occur. For example, for a trigram model (tokens are characters), it should look something like:

{ "ab":{"c":0.5, "b":0.25, "d":0.25}, "ca":{"a":0.2, "b":0.7, "d":0.1} }

which means for example that after the sequence "ab", there is a 0.5 chance that "c" will appear, 0.25 for "b" to appear and 0.25 for "d" to appear.

Note - You should think how to add the add_one smoothing information to the dictionary and implement it.

#### PART 3
In the language_modeling.py file, implement the function *eval* that returns the perplexity of a model (dictionary) running over the data file of the given target language.

#### PART 4
In the language_modeling.py file, implement the *match* function that calls *eval* using a specific value of *n* for every possible language pair among the languages we have data for. You should call *eval* for every language pair four times, with each call assign a different value for *n* (1-4). Each language pair is composed of the source language and the target language. Before you make the call, you need to call the *lm* function to create the language model for the source language. Then you can call *eval* with the language model and the target language. The function should return a pandas DataFrame with the following four columns: *source_lang*, *target_lang*, *n*, *perplexity*. The values for the first two columns are the two-letter language codes. The value for *n* is the *n* you use for generating the specific perplexity values which you should store in the forth column.

#### PART 5
In the language_modeling.py file, implement the *generate* function which takes a language code, *n*, the prompt (the starting text), the number of tokens to generate, and *r*, which is the random seed for any randomized action you plan to take in your implementation. The function should start generating tokens, one by one, using the language model of the given source language and *n*. The prompt should be used as a starting point for aligning on the probabilities to be used for generating the next token.

#### PART 6
Play with your generate function, try to generate different texts in different language and various values of *n*. No need to submit anything of that.

## General instructions
Please make sure to commit and push only the language_modeling.py file. Please avoid changing/deleting any files under the .github folder as it may interfer with the autograding operation.

GOOD LUCK!
