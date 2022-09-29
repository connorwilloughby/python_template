# harmless package used to track progress of loops
from tqdm import tqdm
from time import sleep


def intro_python():

    print('Introduction to python!')

    # simple loop to print 0-9
    for i in range(3):
        out_string = f'\tHello World: {i}'
        print(out_string)

    return NotImplementedError

def intro_tqdm():
    print('Introduction to tqdm')

    # loop to run 0-9 with tqdm
    for i in tqdm(range(3)):
        sleep(3)
    
    print('CODE DONE')
    
    return NotImplementedError

def main():

    intro_python()
    
    intro_tqdm()

if __name__ == '__main__':
    main()