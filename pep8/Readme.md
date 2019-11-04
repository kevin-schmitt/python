# Description

Pep is standard coding for python, this example show how to detectec violation of standard

# Expplain
Run `sudo pip3 install -r requirements.txt` install pylint check problem with standard python code (you can use too pep8, flake8,pycodestyle)
You can now use pylint for check coce `pylint code_not_respect_pep.py`
``` 
************* Module code_not_respect_pep
code_not_respect_pep.py:1:24: C0326: No space allowed around keyword argument assignment
def bad_function(val, b = 5):
                        ^ (bad-whitespace)
code_not_respect_pep.py:2:10: C0326: Exactly one space required around comparison
    if val<0:
          ^ (bad-whitespace)
code_not_respect_pep.py:9:0: C0304: Final newline missing (missing-final-newline)
code_not_respect_pep.py:1:0: C0111: Missing module docstring (missing-docstring)
code_not_respect_pep.py:1:0: C0103: Argument name "b" doesn't conform to snake_case naming style (invalid-name)
code_not_respect_pep.py:1:0: C0111: Missing function docstring (missing-docstring)
code_not_respect_pep.py:2:4: R1705: Unnecessary "else" after "return" (no-else-return)

------------------------------------
Your code has been rated at -1.67/10
```
We can see all violation in source code

