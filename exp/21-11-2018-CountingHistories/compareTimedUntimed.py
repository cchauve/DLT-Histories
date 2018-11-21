import os,stats

cats = [("TimedTransfer","--timed 1"),("UntimedTransfer","--timed 0"),("TimedNoTransfer","--timed 1 --noTransfers"),("UntimedNoTransfer","--timed 0 --noTransfers")]
N = 10
print "k\tn\t",
for s,opts in cats:
    print s,
print
for i in range(1,N+1):
        for j in range(i+1,3*i+1):
            print "%s\t%s\t"%(i,j),
            for s,opts in cats:
                path = "out.txt"
                os.system("python stats.py %s %s %s > %s"%(i,j, opts, path))
                for l in open(path,"r"):
                    data = l.split()
                    print (data[1]),
                    break
            print
