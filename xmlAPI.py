#Import API to parse XML data
import xml.etree.ElementTree as ET
import pandas as pd
import sys 
import os
sys.path.append(os.path.abspath("/Users/andrewmatthews/Desktop/Code/Health_Tracker"))   
import healthAnz
tree = ET.parse("datasubset1.xml")
root = tree.getroot()

#Print root (Which should be data as defined in test1.xml)
print(root)

#Columns
columns = []

#Rows
rows = []

print('Analytics of xml health Data')
#Number of child elements in root 
numChildren = []
for child in root:
    numChildren.append(child.tag)
    lengthNumChildren = len(numChildren)
print('The number of child elements in root:', lengthNumChildren)

#Display the number of attributes within each element
numDict = []
for record in root.iter('Record'):
    numDict.append(record.attrib)
    lengthOfDiction = len(numDict)
print('The number of dictionaries:',lengthOfDiction)

#Test Case: The number of child elements in the root should equal the number of dictionaries. If this is not the case then we have elements that do not have data entries.
def testElementEqualChild(): 
    assert lengthNumChildren == lengthOfDiction, "The number of elements do not match the"

if __name__ == "__main__":
    testElementEqualChild()
    print("Number of elements is equal to the number of dictionaries")


#Extract attributes from record element (Heart Rate in beats per min.)
def exerciseID(start_date,end_date,name):
    heartRate = [] #Numerical Heart Rate 
    timeOfEntry = [] #Date of heart rate record

    #Extract values for heart rate and time
    for record in root.findall('Record'):
        if record.get('type') == healthAnz.exerciseID(name):
            unit = record.get('unit') #Units of heart rate
            value = record.get('value') #Value of heart rate
            creationDate = record.get('creationDate') #Date recorded
            heartRate.append(value) #Append value (count/min)
            timeOfEntry.append(creationDate) #Append creation dates to the Dates
        print("Type",healthAnz.exerciseID(name))
    columns.append('Heart Rate:' + unit)
    columns.append('Date')
    
    # Convert XML into CSV utilizing Pandas
    for i in range(len(heartRate)):
        rows.append({columns[0]:heartRate[i],columns[1]:timeOfEntry[i]})

    # Create the pandas dataframe
    df = pd.DataFrame(rows,columns = columns)
    
    #Parse data by dates
    df.set_index(['Date'])
    df = df.set_index(['Date'])
    parse_dates = df.loc[start_date:end_date + '1']
    print(parse_dates)
    #Writing dataframe to csv
    parse_dates.to_csv('health.csv')
    return parse_dates

exerciseID('2018-07-19','2018-07-21','HeartRate')


 
