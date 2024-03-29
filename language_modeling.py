from typing import List, Dict
import pandas as pd

def preprocess() -> List[str]:
    # return a list of characters, representing the shared vocabulary of all languages
    return []

def lm(lang: str, n: int) -> Dict[str, Dict[str, float]]:
    # return a language model for the given lang and n_gram (n)
    return dict()

def eval(model: dict, target_lang: str) -> float:
    # return the perplexity value calculated over applying the model on the text file 
    # of the target_lang language.
    return -1

def match(source_lang: str, target_lang: str) -> pd.DataFrame:
    # return a DataFrame containing one line per every language pair and n_gram.
    # each line will contain the perplexity calculated when applying the language model
    # of the source language on the text of the target language.
    return pd.DataFrame()

def generate(lang: str, n: int, prompt: str, number_of_tokens: int, r: int) -> str:
    # generate text accoring to the given parameters.
    return ""