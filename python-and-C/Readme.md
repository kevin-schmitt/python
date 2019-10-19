#Description

Example for use custom librarie from C langage. C is fast and can improve performance of
application  with that.

#Run
Run `pip3 install -r requirements.txt` for install depencies
Run `python main.py` 
compile files for generate libarie wtih gcc 
`gcc -Wall -o5 -fPIC -shared C/factoriel.c -o factoriel.so`

#Test
Run `python test\test_factoriel.py`