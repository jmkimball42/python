import wikipedia 
query = 'Chris Hardwick'
results = wikipedia.summary(query, sentences=2) ## change the number of sentence to get a larger words summary
print(results)
