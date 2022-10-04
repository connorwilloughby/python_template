import requests
import logging as logs

# harmless package used to track progress of loops
from tqdm import tqdm
from time import sleep

"""\
    A simple introduction to python as a language    
"""
def intro_python():

    print('Introduction to python!')

    # simple loop to print 0-3
    for i in range(3):
        out_string = f'\tHello World: {i}'
        print(out_string)

    return NotImplementedError

"""\
    A quick demo of a loop operation
"""
def intro_tqdm():
    print('Introduction to tqdm')

    # loop to run 0-3 with tqdm
    for _ in tqdm(range(3)):
        sleep(3)
    
    print('CODE DONE')
    
    return NotImplementedError

"""\
    An example web call with parameters
"""
def intro_web_call(page):

    print('Introduction to web calls')

    # web call to get the data from the page
    response = requests.get(page)

    # check to see if the response was good
    if response.status_code == 200:
        # print the data from the page
        print(response.text)
    else:
        print(f'ERROR: {response.status_code}')

    return response

"""\
    A function which calls another function
"""
def intro_to_function_calls():

    intro_web_call('https://linkedin.com')

def main():

    # intro_python()
    
    # intro_tqdm()

    # intro_web_call('https://savills.co.uk')

    intro_to_function_calls()

if __name__ == '__main__':
    main()