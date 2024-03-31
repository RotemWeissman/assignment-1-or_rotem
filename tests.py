# Create tests
def test_preprocess():
    assert preprocess() == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

TESTS = [test_preprocess]

# Run tests and save results
res = {}
for test in TESTS:
    try:
        cur_res = test()
        res.update({test.__name__: cur_res})
    except RuntimeError as e:
        res.update({test.__name__: str(e)})

with open('results.json', 'w') as f:
    json.dump(res, f)

# Download the results.json file
files.download('results.json')