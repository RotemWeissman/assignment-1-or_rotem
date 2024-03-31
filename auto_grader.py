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

def test_preprocess():
    assert False

def main():
    # Get command line arguments
    args = get_args()

    # Read results.json
    with open('results.json', 'r') as f:
        results = json.load(f)

    # Switch between the tests
    match args.test:
        case '1':
            test_preprocess(results["test_preprocess"])
        case '2':
            pass
        case '3':
            pass
        case '4':
            pass
        case '5':
            pass
        case _:
            print('Invalid test.')

if __name__ == '__main__':
    main()