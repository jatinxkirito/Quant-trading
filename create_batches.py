# creating a function for generating batckes form ticker column of database. We will create a generator function using yield keyword
def create_batches(lst,n):
    for i in range (0,len(lst),n):
        yield lst[i:i+n]