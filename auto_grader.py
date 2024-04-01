'''
Main script for testing the assignment.
Runs the tests on the results json file.
'''

import argparse
import json

def get_args():
    parser = argparse.ArgumentParser(description='Language Modeling')
    parser.add_argument('test', type=str, help='The test to perform.')
    parser.add_argument('num', type=int, help='The number of the test.', default=0)
    return parser.parse_args()

def test_preprocess(results, num):
    return results["vocab_length"]

def test_lm(results, num):
    return '''English 2-gram: {english_2_gram_length}
    English 3-gram: {english_3_gram_length}
    French 3-gram: {french_3_gram_length}
    Spanish 3-gram: {spanish_3_gram_length}'''.format(**results)

def test_eval(results, num):
    assert False

def test_match(results, num):
    assert False

def test_generate(results, num):
    assert False

def main():
    # Get command line arguments
    args = get_args()

    # Read results.json
    with open('results.json', 'r') as f:
        results = json.load(f)

    # Switch between the tests
    match args.test:
        case 'test_preprocess':
            test_preprocess(results["test_preprocess"], args.num)
        case 'test_lm':
            test_lm(results["test_lm"], args.num)
        case 'test_eval':
            test_eval(results["test_eval"], args.num)
        case 'test_match':
            test_match(results["test_match"], args.num)
        case 'test_generate':
            test_generate(results["test_generate"], args.num)
        case _:
            print('Invalid test.')

if __name__ == '__main__':
    main()