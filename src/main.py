# Resolve the problem!!
import re

def run():
    # Start coding here
   with open('encoded.txt', 'r', encoding='utf-8') as f:
       text = f.read()
       secret_message = re.findall('[a-z]', text)
       print(''.join(secret_message))
       
if __name__ == '__main__':
    run()
