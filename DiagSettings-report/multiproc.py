from multiprocessing import Pool
import time
work = (["1", 5], ["2", 2], ["3", 1], ["4", 3], ["5", 5], ["6", 2], ["7", 1], ["8", 3])
new_work = ()
for i in range(1000):
    r = str(i)
    my_list= [r, 3 ]
    new_work = new_work + (my_list,)
# print (new_work)
def work_log(work_data):
    print(" Process %s waiting %s seconds" % (work_data[0], work_data[1]))
    time.sleep(int(work_data[1]))
    work_data[1] = work_data[1] * 100989
    print(" Process %s Finished." % work_data[0])
    return work_data
def pool_handler():
    p = Pool(100)
    result = p.map(work_log, new_work)
    # print(result)
if __name__ == '__main__':
    pool_handler()
    