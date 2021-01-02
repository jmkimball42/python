from progress.bar import Bar
bar = Bar('Loading', max=20)
for i in range(20):
        # Any Task
            bar.next()
            bar.finish()
