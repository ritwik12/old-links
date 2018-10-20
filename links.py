lines = tuple(open("Links.txt", 'r'))
file = open("line.txt","w")
for i in range(0, len(lines)):
	line = lines[i]
	#line = "|"+lines[i]
	http = line.find("http") - 1
	http1 = line[http+1:len(line)]
	http2 = http1.find(" ")
	http3 = http1[0:http2]
	#http1 = line[http+1:len(line)].find(" ")
	#line2 = line[http+1:http1+1]
	line = "|"+line[0:http]+"|"+http3+"|"+http1[http2:len(http1)-1]+"|"+"\n"
	file.write(line)
	#print(http3)
	#print(line)
	#print(http)
	#rint(line)