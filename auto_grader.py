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
    if results["vocab_length"] != 1804:
        return f"Vocab length is {results['vocab_length']}, expected 1804"
    return 1

def test_lm(results):
    if results["english_2_gram_length"] != 748:
        return f"English 2-gram length is {results['english_2_gram_length']}, expected 748"
    if results["english_3_gram_length"] != 8239:
        return f"English 3-gram length is {results['english_3_gram_length']}, expected 8239"
    if results["french_3_gram_length"] != 8286:
        return f"French 3-gram length is {results['french_3_gram_length']}, expected 8286"
    if results["spanish_3_gram_length"] != 8469:
        return f"Spanish 3-gram length is {results['spanish_3_gram_length']}, expected 8469"
    return 1
    
def relative_difference(expected, actual):
    """Calculate the relative difference between expected and actual values."""
    return abs(expected - actual) / expected

def test_eval(results):
    
    expected_english_on_english = 9.39
    expected_english_on_french = 27.75
    expected_english_on_spanish = 26.61
    
    tolerance = 0.05  # Accept up to 5% difference

    diff_english_on_english = relative_difference(expected_english_on_english, float(results["english_on_english"]))
    diff_english_on_french = relative_difference(expected_english_on_french, float(results["english_on_french"]))
    diff_english_on_spanish = relative_difference(expected_english_on_spanish, float(results["english_on_spanish"]))

    if diff_english_on_english > tolerance:
        return f"English on English is {results['english_on_english']}, expected approximately {expected_english_on_english} (within {tolerance*100}% tolerance)"
    if diff_english_on_french > tolerance:
        return f"English on French is {results['english_on_french']}, expected approximately {expected_english_on_french} (within {tolerance*100}% tolerance)"
    if diff_english_on_spanish > tolerance:
        return f"English on Spanish is {results['english_on_spanish']}, expected approximately {expected_english_on_spanish} (within {tolerance*100}% tolerance)"
    
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

    # Initialize the result variable
    result = None

    # Switch between the tests
    match args.test:
        case 'test_preprocess':
            result = test_preprocess(results["test_preprocess"])
        case 'test_lm':
            result = test_lm(results["test_lm"])
        case 'test_eval':
            result = test_eval(results["test_eval"])
        case 'test_match':
            result = test_match(results["test_match"])
        case 'test_generate':
            result = test_generate(results["test_generate"])
        case _:
            print('Invalid test.')

    # Print the result for the autograder to capture
    if result is not None:
        print(result)

if __name__ == '__main__':
    main()
