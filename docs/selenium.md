# Selenium

Install the recommended version of the pip package listed below for a stable run, or you can just use "pip install -r requirements.txt" in frontend_selenium directory.

Prerequisites | version | 
--- | --- |
[Python](https://www.python.org/downloads/) | `3.10.4` |
[pytest](https://pypi.org/project/pytest/) | `7.1.2` |
[selenium](https://pypi.org/project/selenium/) | `4.4.3` |
[webdriver-manager](https://pypi.org/project/webdriver-manager/) | `3.8.3` |


## Running selenium

- First change direcotry to frontend_selenium through the command line using `cd tests/frontend_selenium`
- You can run selenium with pytest through the command line using  `python3 -m pytest`
- You can also run single test file through the command line using `python3 -m pytest tests/test_file.py`
- You can also run specific test case through the command line using `python3 -m pytest tests/test_file.py::test_func` 
