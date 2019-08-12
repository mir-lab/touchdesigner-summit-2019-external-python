import time
from argparse import ArgumentParser

def My_python_method(kwargs):

    disp_str = 'key: {} | value: {} | type: {}'
    for each_key, each_value in kwargs.items():
        formatted_str = disp_str.format(each_key, each_value, type(each_value))
        print(formatted_str)

    # keep the shell open so we can debug
    time.sleep(int(kwargs.get('delay')))

# execution order matters -this puppy has to be at the bottom as our functions are defined above
if __name__ == '__main__':
    parser = ArgumentParser(description='Set up a file watcher to stylize files that are added to the specified folder')
    parser.add_argument("-i", "--input", dest="in", help="an input string", required=True)
    parser.add_argument("-i2", "--input2", dest="in2", help="another input", required=True)    
    parser.add_argument("-d", "--delay", dest="delay", help="how long our terminal stays up", required=False, default=10)
    args = parser.parse_args()
    print(vars(args))
    My_python_method(vars(args))
    # My_python_method(args.input, args.intput2, args.delay)
    pass

# example
# python .\cmd_line_python_args.py -i="a string" -i2="another string" -d=15

