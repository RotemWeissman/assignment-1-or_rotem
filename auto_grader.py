'''
Main script for testing the assignment.
Runs the tests on the results json file.
'''

import argparse
import json

def get_args():
    parser = argparse.ArgumentParser(description='Language Modeling')
    parser.add_argument('test', type=str, help='The test to perform.')
    return parser.parse_args()

def test_preprocess(results):
    if results["vocab_length"] != 1803:
        return f"Vocab length is {results['vocab_length']}, expected 1724"
    return 1

def test_lm(results):
    if results["english_2_gram_length"] != 725:
        return f"English 2-gram length is {results['english_2_gram_length']}, expected 697"
    if results["english_3_gram_length"] != 7932:
        return f"English 3-gram length is {results['english_3_gram_length']}, expected 4841"
    if results["french_3_gram_length"] != 7972:
        return f"French 3-gram length is {results['french_2_gram_length']}, expected 4756"
    if results["spanish_3_gram_length"] != 8035:
        return f"Spanish 3-gram length is {results['spanish_2_gram_length']}, expected 4760"
    return 1
    
def test_eval(results):
    if int(results["english_on_english"]) not in [8, 9]:
        return f"English on English is {results['english_on_english']}, expected 9.32"
    if int(results["english_on_french"]) not in [27, 28]:
        return f"English on French is {results['english_on_french']}, expected 27.82"
    if int(results["english_on_spanish"]) not in [25, 26]:
        return f"English on Spanish is {results['english_on_spanish']}, expected 26.46"
    return 1

def test_match(results):
    if results["df_shape"] != list((256, 4)):
        return f"Dataframe shape is {results['df_shape']}, expected (256, 4)"
    
    res = [
        int(results["en_en_1"]),
        int(results["tl_tl_1"]),
        int(results["tl_nl_4"])
    ]
    if sorted(res) != res:
        return f"En on En should be the lowest, followed by Tl on Tl, and Tl on Nl. Got {res}"
    return 1

def test_generate(results):
    if not results["english_2_gram"].startswith("I am"):
        return f"English 2-gram does not start with 'I am', but with {results['english_2_gram']}"
    if not results["french_3_gram"].startswith("Je suis"):
        return f"French 3-gram does not start with 'Je suis', but with {results['french_3_gram']}"
    return 1

def main():
    # Get command line arguments
    args = get_args()

    # Read results.json
    with open('results.json', 'r') as f:
        results = json.load(f)

    # Switch between the tests
    match args.test:
        case 'test_preprocess':
            return test_preprocess(results["test_preprocess"])
        case 'test_lm':
            return test_lm(results["test_lm"])
        case 'test_eval':
            return test_eval(results["test_eval"])
        case 'test_match':
            return test_match(results["test_match"])
        case 'test_generate':
            return test_generate(results["test_generate"])
        case _:
            print('Invalid test.')

if __name__ == '__main__':
    main()