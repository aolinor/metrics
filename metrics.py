import sys
import psutil

def use_help():
    print("Usage")

    print("\nTo provide CPU stats use command")
    print("metrics cpu")

    print("\nTo provide MEM stats use command")
    print("metrics mem")

def print_cpu_stats(cpu_stats):
    #print(cpu_stat)
    print("system.cpu.idle " + str(cpu_stats[3]))
    print("system.cpu.user " + str(cpu_stats[0]))
    print("system.cpu.guest " + str(cpu_stats[8]))
    print("system.cpu.iowait " + str(cpu_stats[4]))
    print("system.cpu.stolen " + str(cpu_stats[7]))
    print("system.cpu.system " + str(cpu_stats[2]))

def print_mem_stats(mem_virt, mem_swap):
    #print(mem_virt)
    print("virtual total " + str(mem_virt[0]))
    print("virtual used " + str(mem_virt[3]))
    print("virtual free " + str(mem_virt[4]))
    print("virtual shared " + str(mem_virt[9]))

    #print(mem_swap)
    print("swap total " + str(mem_swap[0]))
    print("swap used " + str(mem_swap[1]))
    print("swap free " + str(mem_swap[2]))

def main():
    arg_qty = len(sys.argv) - 1

    if(arg_qty != 1):
        print("Please provide 1 mandatory argument\n")
        use_help()
    else:
        stat_type = str(sys.argv[1])

        if (stat_type == "cpu"):
            cpu_stats = psutil.cpu_times_percent(interval=1, percpu=False)
            print_cpu_stats(cpu_stats)
        elif(stat_type == "mem"):
            mem_virt = psutil.virtual_memory()
            mem_swap = psutil.swap_memory()
            print_mem_stats(mem_virt, mem_swap)
        else:
            print("Wrong argument\n")
            use_help()

if __name__ == "__main__":
    main()
