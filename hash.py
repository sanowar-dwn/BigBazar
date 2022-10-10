from builtins import dict, list
from collections import Counter
passwords = ['pass', 'password', 'senha', 'password', 'picture', 'python', 'shaikatsir', 'pass', 'newpass', 'passsenha']
pass_list = len(passwords)

for i in range(pass_list):
    hashed_passwords = hash(passwords[i])
    


