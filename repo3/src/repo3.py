# project3/module.py

import requests

def function3() -> str:
    webpage = requests.get("https://www.google.com")
    print(webpage)
    return "Repo3.function3 called"

if __name__  == "__main__":
    function3()