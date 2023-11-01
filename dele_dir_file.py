import os
import sys
import time


def get_all_path(open_file_path):
    rootdir = open_file_path
    path_list = []
    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        com_path = os.path.join(rootdir, list[i])
        #print(com_path)
        if os.path.isfile(com_path):
            path_list.append(com_path)
        if os.path.isdir(com_path):
            path_list.extend(get_all_path(com_path))
    #print(path_list)
    return path_list

def deletefile(filename,DAYS_N):

    if os.path.isfile(filename):
        lastmodifytime = os.stat(filename).st_mtime
        # print lastmodifytime
        # Sets how many days old files are deleted
        endfiletime = time.time() - 3600 * 24 * DAYS_N
        if endfiletime > lastmodifytime:
            # To remove the following comment is to delete the.log suffix file
            # Comment is delete path under all files do not match
            if filename[-4:] == ".txt":
                os.remove(filename)
                pstr = "del "+filename+" success!!!"
                print(pstr)


if __name__ == '__main__':
         
    # path =r'D:\BaiduNetdiskDownload'
    path = sys.argv[1]
    # DAYS_N=10
    DAYS_N = int(sys.argv[2])
    path_list = get_all_path(path)     

    for i in path_list:
        deletefile(i,DAYS_N)

    
    time.sleep(1)
    print ('Deleting completed,success')
