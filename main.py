''' Main script for testing the assignment. '''

import argparse
from language_modeling import preprocess, lm, eval, match, generate

def get_args():
    parser = argparse.ArgumentParser(description='Language Modeling')
    parser.add_argument('test', type=str, help='The test to perform.')
    return parser.parse_args()

def test_preprocess():
    assert preprocess() == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def main():
    # Get command line arguments
    args = get_args()
    # Switch between the tests
    match args.test:
        case '1':
            test_preprocess()
        case '2':
            print(lm('en', 3))
        case '3':
            print(eval(lm('en', 3), 'en'))
        case '4':
            print(match('en', 'en'))
        case '5':
            print(generate('en', 3, 'The', 10, 3))
        case _:
            print('Invalid test.')

if __name__ == '__main__':
    main()