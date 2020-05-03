import os

cur_dir = os.path.dirname(__file__)
contacts_dir = os.path.join(cur_dir, 'data','contacts.tsv')
headers = []
row = []
with open(contacts_dir, 'r') as contacts:
    for i,line in enumerate(contacts):
        if i == 0:
           headers = line.strip().split("\t")
        else:
            pass
print(headers)
        
