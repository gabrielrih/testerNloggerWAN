# Reference: https://docs.python.org/3/library/urllib.request.html
import urllib.request
import time
from urllib.error import URLError, HTTPError
from socket import timeout

FIRST_WEBSITE_TO_TEST = 'https://www.google.com'
TIME_OUT = 10

def test_connection():
    try:
        response = urllib.request.urlopen(FIRST_WEBSITE_TO_TEST, timeout=TIME_OUT)
    except timeout:
        return False, "Request has reached the timeout!"
    except HTTPError as e:
        return False, str(e.reason)
    except URLError as e:
        return False, str(e.reason)
    else:
        return True, None

st = time.time()
isUp, error = test_connection()
et = time.time()
elapsed_time = et- st
print(isUp)
print(error)
print('Execution time:', elapsed_time, 'seconds')
print(st)