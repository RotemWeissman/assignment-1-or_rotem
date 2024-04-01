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
    if results["vocab_length"] != 1724:
        return f"Vocab length is {results['vocab_length']}, expected 1724"
    return 1

def test_lm(results):
    if results["english_2_gram_length"] != 697:
        return f"English 2-gram length is {results['english_2_gram_length']}, expected 697"
    if results["english_3_gram_length"] != 4841:
        return f"English 3-gram length is {results['english_3_gram_length']}, expected 4841"
    if results["french_3_gram_length"] != 4756:
        return f"French 3-gram length is {results['french_2_gram_length']}, expected 4756"
    if results["spanish_3_gram_length"] != 4760:
        return f"Spanish 3-gram length is {results['spanish_2_gram_length']}, expected 4760"
    return 1
    
def test_eval(results):
    if int(results["english_on_english"]) != 22:
        return f"English on English is {results['english_on_english']}, expected 22.24"
    if int(results["english_on_french"]) != 46:
        return f"English on French is {results['english_on_french']}, expected 46.44"
    if int(results["english_on_spanish"]) != 43:
        return f"English on Spanish is {results['english_on_spanish']}, expected 43.76"
    return 1

def test_match(results):
    if results["df_shape"] != list((256, 4)):
        return f"Dataframe shape is {results['df_shape']}, expected (256, 4)"
    if int(results["en_en_1"]) not in [29, 30]:
        return f"English on English 1-gram is {results['en_en_1']}, expected 29.95"
    if int(results["tl_tl_1"]) not in [60, 61]:
        return f"Tagalog on Tagalog 1-gram is {results['tl_tl_1']}, expected 61.04"
    if int(results["tl_nl_4"]) not in [285, 286]:
        return f"Tagalog on Dutch 4-gram is {results['tl_nl_4']}, expected 286.05"
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