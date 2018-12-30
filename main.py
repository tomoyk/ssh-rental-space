import sys
from Compose import Compose

def main(args):

    '''
    # check parameter 
    if len(args) != 1:
        print("Error:\t you have to set one parameter")
        print("Usage:\t ./gen-compose.py [template-yaml-file]")
        return
    '''
    
    # set original base-yaml-file
    # comp = Compose(args[1]) if args[0] == '-s' else Compose()
    comp = Compose()
    
    # create container from csv
    # credentials = Compose.csv_dump(args[3]) if args[2] == '-c' else Compose.csv_dump()
    # for c in credentials:
    for c in Compose.csv_dump():
        comp.add_service(c)
    
    comp.build()

    # save original yaml-file
    # if args[4] == '-f':
    #     comp.write(args[5])
    # else:
    comp.write()


if __name__ == '__main__':
    main(sys.argv[1:])

