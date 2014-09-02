import re

keys = ("protocol", "domain", "path")

def URL_split(url):
    return {"protocol": None, "domain": None, "path": None}


def test_each(src, key, result):
    return URL_split(src)[key] == result

test_cases = [("http://www.google.se", "protocol", "http"),
              ("http://www.google.se", "domain", "www.google.se"),
              ("http://www.google.se", "path", ""),
              ("http://some.thing", "protocol", "http"),
              ("ftp://a.large.site", "domain", "a.large.site"),
              ("http://a.site.with/a-path", "path", "a-path")]

def test_runner(cases):
    total = len(cases)
    passed = 0
    for case in cases:
        print(case[0], "should give", case[1], "==", case[2],)
        if test_each(case[0], case[1], case[2]):
            print("SUCCEED")
            passed += 1
        else:
            print("FAILED")
    print(passed, "passed among", total, "cases.")

# run the test cases
test_runner(test_cases)
