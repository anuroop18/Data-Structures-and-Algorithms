#----------------------------Pseudo-code----------------------------------------
"""
Algorithm DiskUsage(path):
    Input: A string designating a path to a file-system entry
    Output: The cumulative disk space used by that entry and any nested entries
    total = size(path)
    if path represents a directory hen
        for each child entry stored within directory path do
            total = total + DiskUsage(child)
    return total
"""
#----------------------------Pseudo-code----------------------------------------

#----------------------------Python-code----------------------------------------
import os
def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            child_path = os.path.join(path, filename)
            total += disk_usage(child_path)
            print('{0:<7}'.format(total), path)
    return total

if __name__ == '__main__':
    path = input("Enter the path of file/directory : ")
    disk_usage(path)
