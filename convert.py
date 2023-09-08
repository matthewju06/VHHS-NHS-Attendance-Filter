import pandas as pd

attendance = pd.read_csv('/Users/matthewju/Developer/VHHS NHS Attendance Filter/NHS Attendance.csv')
members = pd.read_csv('/Users/matthewju/Developer/VHHS NHS Attendance Filter/NHS Members.csv')

members.columns.values[1] = 'Last Name' #Renaming index 1 (unnamed) to "Last Name"
members = members[['Last Name', 'First Name', 'Student ID']] #Members dataset with only name and student ID
members['Attendance'] = ['Did Not Attend'] * len(members.index)

didntAttend = [] #Will hold names that didnt attend

for i in range(len(members)):
    #Checks every member through attendance
    if members['Student ID'].iloc[i] in set(attendance['ID']):
        members.loc[i, 'Attendance'] = 'Attended'
    else:
        #Adding name and ID to didntAttend list
        didntAttend.append(members['First Name'].iloc[i] + " " + members['Last Name'].iloc[i] + " (" + str(members['Student ID'].iloc[i]) + ")")

#Saving new file with attendance figures
members.to_csv('NHS Member Attendance Filtered.csv', index=False)

print(didntAttend)