"""错误处理"""
'''class try_except():
    try:
        n = 23/1
        print(n)
    except Exception as e:
        print(e)
    except ValueError as e:
        print(e)
        raise  #处理不了 向上一层跑出错误
    else:print('woshi else  ::没有错误执行')
    finally:print('wo shi zui hou yige：：：总会执行的 ')

#try_except()

"""调试"""
#print的替代品
class loggingg():
    import logging
    logging.basicConfig(level=logging.INFO)

    s = '0'
    n = int(s)
    logging.info('这是：', n)
    print(10 / n)'''

"""pbd"""'''l 查看    n 单不执行    p 查看变量名  q  结束'''
class pbdbd():
    import pdb
    s = '0'
    n = int(s)
    #pdb.set_trace()
    print(10/2)

# pbdbd()


"""d单元测试"""