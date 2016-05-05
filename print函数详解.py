#print语法
'''print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.'''
'''print 有四个可以设定的参数：sep，end，file，flush
   sep   表示输出后该print的value之间用什么隔开，默认是一个空格。
   end   表示一个print完成之后接什么符号，默认是换行。
   file  表示value输出在什么位置，默认在sys.stdout。
   flush 表示是否立即输出，尤其在是文件写入时候。'''

#关于flush参数的解释
'''正如hidh214版主所说，flush为True时是立即输出。
举个例子，我们知道print也可输出到文件。
在IDLE中输入：
f = open('text.txt', 'w')
print('ABC',  file = f)
可以看到text.txt文件这时还是为空，只有f.close()后才将内容写进文件中。
如果改为：
print('ABC', file = f, flush = True)
则不用close文件立即就能看到文件有内容了。
来源：http://bbs.fishc.com/thread-68419-1-1.html'''

#关于sys.stdout
'''

'''
#示例
a,b,c=1,2,3 #默认输出
print(a)  
print(b)
print(c)
a,b,c=1,2,3 #改变end的输出
print(a,end=',')  
print(b,end=',')
print(c,end='\n')
a,b,c=1,2,3 #改变sep的输出
print(a,b,c)  
print(a,b,c,sep='|')
f = open('text.txt', 'w') #改变输出位置
print('ABC',file = f)
