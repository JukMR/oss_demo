# project2/module.py

import repo3

def function1() -> str:
    # Call functions or use features provided by project3
    project3_call = repo3.function3()
    print(project3_call)
    if isinstance(project3_call, str):
        return project3_call

def function2()-> int:
    return 4

if __name__  == "__main__":
    function1()