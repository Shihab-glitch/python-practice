# Dictionary Works_Basic

newdic = { 'ID': [101, 110, 115, 102, 105, 103, 104],
              'Name': ['Ali', 'Ahmed', 'Sara', 'Ali', 'Sara', 'Ali', 'Ahmed'],
              'Grade': ['A', 'A', 'A-', 'F', 'C', 'B', 'B+'] }
print(newdic['ID'])
print(newdic['Name'])
print(newdic['Grade'])
newdic['ID'].sort() #sorts the list in ascending order
newdic.pop('Grade') #removes the key-value pair from the dictionary
newdic['Name'].remove('Ali') #removes the first occurrence of the specified value
newdic['ID'].remove(101) #removes the first occurrence of the specified value
newdic['Name'].append('Hafez') #adds the specified value at the end of the list
newdic['ID'].append(120) #adds the specified value at the end of the list
print(newdic)
