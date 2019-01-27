import time
 
 
def consumer():
    r = ''
    while True:
       n = yield r
       if not n:
           return
       print('[CONSUMR] Consuming %s' %n)
       time.sleep(1)
       r = '200 OK'


def produce(c):
    next(c)
    n = 0
    while n < 5:
        n += 1
        print('[PRODUCE] Producing %s' % n)
        r = c.send(n)
        print('[PRODUCE] Producing %s' % r)
    c.close()
 

if __name__ == '__main__':
    c = consumer()
    produce(c)
