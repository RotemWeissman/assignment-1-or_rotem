import pandas as pd

def preprocess() -> list[str]:
    '''
    Return a list of characters, representing the shared vocabulary of all languages
    '''
    return []

def lm(lang: str, n: int) -> dict[str, dict[str, float]]:
    '''
    Return a language model for the given lang and n_gram (n)
    :param lang: the language of the model
    :param n: the n_gram value
    :return: a dictionary where the keys are n_grams and the values are dictionaries
    '''
    return dict()

def eval(model: dict, target_lang: str) -> float:
    '''
    Return the perplexity value calculated over applying the model on the text file
    of the target_lang language.
    :param model: the language model
    :param target_lang: the target language
    :return: the perplexity value
    '''
    return -1

def match(source_lang: str, target_lang: str) -> pd.DataFrame:
    '''
    Return a DataFrame containing one line per every language pair and n_gram.
    Each line will contain the perplexity calculated when applying the language model
    of the source language on the text of the target language.
    :param source_lang: the source language
    :param target_lang: the target language
    :return: a DataFrame containing the perplexity values
    '''
    return pd.DataFrame()

def generate(lang: str, n: int, prompt: str, number_of_tokens: int, r: int) -> str:
    '''
    Generate text in the given language using the given parameters.
    :param lang: the language of the model
    :param n: the n_gram value
    :param prompt: the prompt to start the generation
    :param number_of_tokens: the number of tokens to generate
    :param r: the number of tokens to consider for the next token
    '''
    return ""