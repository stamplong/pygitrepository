from sys import argv
from os.path import exists


script,from_file,to_file = argv

print "copying from %s to %s"%(from_file,to_file)


input = open(from_file)
indate = input.read()

print "The input file is %d bytes long"%len(indate)

print "Dose the output file exist?%r"%exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file,"w")
out_file.writelines(indate) #problems modification can't write

print "Alright, all done."

out_file.close()
input.close()
