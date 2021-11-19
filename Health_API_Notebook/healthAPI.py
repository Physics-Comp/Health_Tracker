#Import API to parse XML data
import xml.etree.ElementTree as ET
import pandas as pd
tree = ET.parse("datasubset.xml")
root = tree.getroot()

#Dictionary for filtering through data set
def exerciseID (name):
    exerciseDict = {
        "HeartRate": "HKQuantityTypeIdentifierHeartRate",
        "StepCount": "HKQuantityTypeIdentifierStepCount",
        "Distance" : "HKQuantityTypeIdentifierDistanceWalkingRunning",
        "BasalEnergyBurned": "HKQuantityTypeIdentifierBasalEnergyBurned",
        "ActiveEnergy":"HKQuantityTypeIdentifierActiveEnergyBurned",
        "FlightsOfStairs":"HKQuantityTypeIdentifierFlightsClimbed",
        "ExerciseTime": "HKQuantityTypeIdentifierAppleExerciseTime",
        "RestingHeartRate":"HKQuantityTypeIdentifierRestingHeartRate",
        "V02Max":"HKQuantityTi:::ypeIdentifierVO2Max",
        "WalkingHRAvg":"HKQuantityTypeIdentifierWalkingHeartRateAverage",
        "AudioLevels":"HKQuantityTypeIdentifierHeadphoneAudioExposure",
        "WalkingDoubleSupport":"HKQuantityTypeIdentifierWalkingDoubleSupportPercentage",
        "SixMinWalkingDist":"HKQuantityTypeIdentifierSixMinuteWalkTestDistance",
        "StandTime":"HKQuantityTypeIdentifierAppleStandTime",
        "WalkingSpeed":"HKQuantityTypeIdentifierWalkingSpeed",
        "WalkingStepLength":"HKQuantityTypeIdentifierWalkingStepLength",
        "WalkingAsymmetry":"HKQuantityTypeIdentifierWalkingAsymmetryPercentage",
        "SleepingGoal":"HKDataTypeSleepDurationGoal",
        "SleepAnalysis":"HKCategoryTypeIdentifierSleepAnalysis",
        "StandHour":"HKCategoryTypeIdentifierAppleStandHour",
        "Meditation":"HKCategoryTypeIdentifierMindfulSession",
        "HighHeartRate":"HKCategoryTypeIdentifierHighHeartRateEvent",
        "LowHeartRate":"HKCategoryTypeIdentifierLowHeartRateEvent",
        "HeartRateVarSDNN":"HKQuantityTypeIdentifierHeartRateVariabilitySDNN"
    }
    # Test case to see if key is in dictionary
    def testKeyInDict(): 
        assert name in exerciseDict, "Key not found in dictionary"

    testKeyInDict()
    return exerciseDict[name]

#Determine the date range (Use excerciseID function to obtain data_type)
def data_range(name):
    dates = []
    for record in root.findall('Record'):
        if record.get('type') == exerciseID(name):
            creationDate = record.get('creationDate')
            dates.append(creationDate)
    print(len(dates))
    print('First Date',dates[0])
    print('Last Date', dates[-1])

#Columns
columns = []

#Rows
rows = []

#Show preliminary data about the specified biometric such as the number of data points and date range. 
rows = []
def prelimData(name):
    print('Preliminary',name,'data')
    #Number of child elements in root 
    numChildren = []
    for child in root:
        numChildren.append(child.tag)
        lengthNumChildren = len(numChildren)
    print('The number of entries for',name,':', lengthNumChildren)

    #Display the number of attributes within each element
    numDict = []
    for record in root.iter('Record'):
        numDict.append(record.attrib)
        lengthOfDiction = len(numDict)
    print('The number of dictionaries:',lengthOfDiction)

    #Test Case: The number of child elements in the root should equal the number of dictionaries. If this is not the case then we have missing data entries.
    def testElementEqualChild(): 
        assert lengthNumChildren == lengthOfDiction, "The number of elements do not match the"

    if __name__ == "__main__":
        testElementEqualChild()
        print("Number of elements is equal to the number of dictionaries")


#Extract attributes from record element (Heart Rate in beats per min.)
def exerciseData(start_date,end_date,name):
    heartRate = [] #Numerical Heart Rate 
    timeOfEntry = [] #Date of heart rate record

    #Extract values for heart rate and time
    for record in root.findall('Record'):
        if record.get('type') == exerciseID(name):
            unit = record.get('unit') #Units of heart rate
            value = record.get('value') #Value of heart rate
            creationDate = record.get('creationDate') #Date recorded
            heartRate.append(value) #Append value (count/min)
            timeOfEntry.append(creationDate) #Append creation dates to the Dates
    print("Type:", exerciseID(name))
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
#     parse_dates.to_csv('health.csv')
    return parse_dates

# exerciseData('2018-07-19','2018-07-21','HeartRate')



 
