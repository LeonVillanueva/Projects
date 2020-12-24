'''
On election day, a voting machine writes data in the form (voter_id, candidate_id) to a text file. Write a program that reads this file as a stream and returns the top 3 candidates at any given time. If you find a voter voting more than once, report this as fraud.
'''

def candidate (x, c):
    if x not in c:
        c[x] = 1
    else:
        c[x] +=1
    return (sorted(c, key=c.get, reverse=True)[:3], c)

def voter (x, v):
    if x in v:
        print ('Fraud')
        return v
    else:
        v.add (x)
        print ('Good')
        return v

c = {}
v = ()

def voting_machine (voter_id, candidate_id, c=c, v=v):
    c = candidate (candidate_id, c)[1]
    v = voter (voter_id, v)
    print (candidate(candidate_id, c)[0])
    return c, v

c, v = voting_machine voting_machine (voter_id, candidate_id, c=c, v=v)
