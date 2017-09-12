from urllib import request
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print(data,'::',f.status,f.reason)
    for k,v in f.getheaders():
        print(k,'--',v)

    print('data:',data.decode('utf-8'))