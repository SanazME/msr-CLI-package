import argparse
import os
from shutil import copyfile



def read(args):
    filename = args.readFile[0]
    with filename as f:
        print('Reading from %s file'%(f.name))
        print(f.read())

def show(args):
    path = args.show[0]
    fileList = os.listdir(path)
    print('%s files are found'%(len(fileList)))
    for file in fileList:
        print(file)

def delete(args):
    path = args.delete[0]
    os.remove(path)
    print('Successfully deleted %s'%(path))

def copy(args):
    OrgFile = args.copy[0]
    DesFile = args.copy[1]
    copyfile(OrgFile, DesFile)
    print('Successfully copied %s to %s'%(OrgFile, DesFile))

def rename(args):
    OrgFile = args.rename[0]
    DesFile = args.rename[1]
    os.rename(OrgFile,DesFile)
    print('Successfully renamed %s to %s'%(OrgFile, DesFile))



def main():
    parser = argparse.ArgumentParser(
        description='A text file manager with the following flags.')
    parser.add_argument('-r', '--read', dest='readFile',metavar='file_name', nargs=1,
                        type=argparse.FileType('r', encoding='UTF-8'), 

                        help='Opens and reads the specified text file.')
    parser.add_argument('-s', '--show', metavar='path', nargs=1,
                        help='Show all the text files on specified directory path. Type \'.\' for current directory')
    parser.add_argument('-d', '--delete', metavar='file_name', nargs=1,
                        help='Deletes the specified text file.')
    parser.add_argument('-c', '--copy', metavar=('file1', 'file2'), nargs=2,
                        help='Copy file1 contents to file2 Warning: file2 will get overwritten.')
    parser.add_argument('--rename', metavar=('old_name', 'new_name'), nargs=2,
                        help='Renames the specified file to a new name.')
    
    args = parser.parse_args()
    
    if args.readFile != None:
        read(args)
    elif args.show != None:
        show(args)
    elif args.delete != None:
        delete(args)
    elif args.copy != None:
        copy(args)
    elif args.rename != None:
        rename(args)


if __name__ == "__main__":
    # calling the main function
    main()
