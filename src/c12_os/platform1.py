import platform
import psutil

def machine_info():
    uname = platform.uname()
    print("操作系统信息:")
    print("\t{}".format(uname[0]))
    print("\t{}".format(uname[1]))
    print("\t{}".format(uname[2]))
    print("\t{}".format(uname[3]))
    print("\t{}".format(uname[4]))
    print("\t{}".format(uname[5]))

    

def disk_info():
    disks = psutil.disk_partitions(False);
    print("磁盘信息:") 
    for disk in disks:
        usage = psutil.disk_usage(disk[1])
        info = {
            "总共(MB)":usage[0]/1024**2,
            "已用(MB)":usage[1]/1024**2,
            "空闲(MB)":usage[2]/1024**2,
            "使用率":usage[3],
        }
        print("\t名称:{}".format(disk[0]))
        print("\t路径:{}".format(disk[1]))
        print("\t使用信息:{}".format(info))
        print()



def memo_info():
    memo = psutil.virtual_memory();  
    print("内存信息:")  
    print("\t总共:{:.2f} MB".format(memo[0]/1024**2))
    print("\t空闲:{:.2f} MB".format(memo[1]/1024**2))
    print("\t已用:{:.2f} MB".format(memo[3]/1024**2))
    print("\t使用率:{}%".format(memo[2]))


def cpu_info():
    print("cpu信息:")
    print("\tcpu统计信息:{}".format(psutil.cpu_stats()))
    print("\t逻辑cpu数量:{}".format(psutil.cpu_count(True)))
    print("\t物理cpu数量:{}".format(psutil.cpu_count(False)))
    print("\tcpu使用信息:{}".format(psutil.cpu_times_percent(interval=1)))


def all_info():
    machine_info()
    print()
    cpu_info()
    print()
    memo_info()
    print()
    disk_info()
    print()



all_info()

