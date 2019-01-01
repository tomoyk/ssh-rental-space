import re
import sys
from Compose import Compose

def arg_to_dict(args):
    params = {}
    args = (' ' + ' '.join(args)).split(' -')
    args = [a for a in args if a] # remove blank elements

    for arg in args:
        split_arg = arg.split(' ')
        key = re.sub('^-*', '', split_arg[0])
        val = ' '.join(split_arg[1:])
        params[key] = val

    return params


def main(args):
    params = arg_to_dict(args)
    
    # help
    if 'h' in params.keys():
        print("Usage: main.py [-s base-yaml-file] [-c credetial-csv] [-o output-yaml-file]")
        return

    # original source yaml used
    if 's' in params.keys():
        comp = Compose(params['s'])
    else:
        comp = Compose()
    
    # original credential used
    if 'c' in params.keys():
        credentials = Compose.csv_dump(params['c'])
    else:
        credentials = Compose.csv_dump()
    for c in credentials:
        comp.add_service(c)
    
    comp.build()

    # original export file used
    if 'o' in params.keys():
        comp.write(params['o'])
    else:
        comp.write()


if __name__ == '__main__':
    main(sys.argv[1:])

