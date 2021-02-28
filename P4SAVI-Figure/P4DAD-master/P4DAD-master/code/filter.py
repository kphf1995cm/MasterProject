

def getStats(secs, base):
    res  = []
    num = 0
    i = 1
    for sec in secs:
        num += 1
        if sec > i * base:
            i += 1
            res.append(num - 1)
    if num > res[-1]:
        res.append(num)
    print res
    return res

def getData(filename, offset):
    with open(filepath) as fp:
        content=fp.readlines()
        for c in content:
            # print c
            tuples= c.strip().split('[')
            secs_str = tuples[-1].split(']')[0]
            secs = [x/1000000-offset+0.1 for x in map(float, secs_str.split(', '))]
            getStats(secs, 5)
            # print secs
            # print len(secs), '-'*100


if __name__ == "__main__":

    filepath = 'result.txt'
    offset = 23
    getData(filepath, offset)
    