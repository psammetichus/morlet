import hdf2webeeg
from sys import argv

def main():
    try:
        with open("output.webeeg", "w") as outfile:
            outfile.write(hdf2webeeg.convert(argv[1]))
    except e:
        print "didn't work out"
        exit()


if __name__ == "__main__":
    main()



    
    
