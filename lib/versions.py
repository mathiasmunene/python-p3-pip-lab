import sys
import requests
import pytest

def python_version():
    return sys.version_info

def requests_version():
    return requests.__version__

def pytest_version():
    return pytest.__version__

print("Python version:", python_version())
print("Requests version:", requests_version())
print("Pytest version:", pytest_version())
