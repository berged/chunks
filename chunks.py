import urllib2

url = 'http://f39bf6aa.bwtest-aws.pravala.com/384MB.jar'
totalDownloaded = 0
chunkSize = 1024000  # 1MB

httpRequest = urllib2.Request(url)
httpResponse = urllib2.urlopen(httpRequest)
fileSize = int(httpResponse.headers['Content-Length'])
print 'Total file size is %s bytes' %  fileSize

outputFile = open('delete_this_file.txt', 'wb')
while totalDownloaded < 4096000 or totalDownloaded <fileSize:  #first 4MB
    amountToRead = min(chunkSize, fileSize - totalDownloaded)
    httpRequest = urllib2.Request(url)
    httpRequest.add_header("Range","bytes=%s-%s" % (totalDownloaded, totalDownloaded+amountToRead))
    httpResponse = urllib2.urlopen(httpRequest)
    data = httpResponse.read()
    outputFile.write(data)
    totalDownloaded += amountToRead
    print "Read so far %s bytes" % totalDownloaded

outputFile.close()
httpResponse.close()
