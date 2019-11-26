import os;


def IsSubString(SubStrList, Str):
    flag = True
    for substr in SubStrList:
        if not (substr in Str):
            flag = False

    return flag


def GetFileList(FindPath, FlagStr=[]):
    FileList = []
    FileNames = os.listdir(FindPath)
    if (len(FileNames) > 0):
        for fn in FileNames:
            if (len(FlagStr) > 0):
                if (IsSubString(FlagStr, fn)):
                    fullfilename = os.path.join(FindPath, fn)
                    FileList.append(fullfilename)
            else:
                fullfilename = os.path.join(FindPath, fn)
                FileList.append(fullfilename)
    if (len(FileList) > 0):
        FileList.sort()

    return FileList


basePath = "/Users/penghuiping/Desktop/joinsoft-docker/html/mijiemonitor/upload/"
list = GetFileList(basePath, ".3gp");

for fullFileName in list:
    fullFileName = fullFileName[len(basePath):len(fullFileName)];
    fileName = fullFileName[0:fullFileName.find(".")];
    print(fileName)
    print(fullFileName)
    cmd = "/bin/bash -c \"ffmpeg -i  {} -r 25 -b:v 1500k -strict -2 {}.mp4\"".format(fullFileName, fileName);
    os.popen(cmd);
