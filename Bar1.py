from progress.bar import Bar

l = list(range(10000))

bar = Bar('Processing...', max = len(l))

for i,j in enumerate(l):
    l[i] = j+1
    bar.next()

bar.finish()
