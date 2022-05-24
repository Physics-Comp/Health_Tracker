#Import API to parse XML data
import xml.etree.ElementTree as ET
import pandas as pd
tree = ET.parse("datasubset.xml")
root = tree.getroot()


class Anlaysis:
#Dictionary for filtering through data set
    def exerciseID (name):
        """
        exerciseID is a function containing a dictionary that converts Apple's naming convention to a more condenced naming convention.

        The function contains the following syntax, exerciseID('Health Metric')

        Ex.
        exerciseID('HeartRate')
        """
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
    """
    Extracts the date range of a given biometric. The argument in the function should be the biometric of interest.

    Ex.
    dataRange('HeartRate')

    Note: In order to use the condenced naming conventions you must call the exerciseID function.
    """
    def dataRange(name):
        dates = []
        for record in root.findall('Record'):
            if record.get('type') == exerciseID(name):
                creationDate = record.get('creationDate')
                dates.append(creationDate)
        print('First Date:',dates[0])
        print('Last Date:', dates[-1])

    #Show preliminary data about the specified biometric such as the number of data points and date range.

    def prelimData(name):
        """
        Gives a general description of the biometric data given a particular health metric. The following information should be given
        1.) Name of the health metric
        2.) First date the particular health metric was recoreded
        3.) Last recorded date of the specified health metric
        4.) Test case that checks if there are any missing data entries in the dataset
        """
        print('Preliminary',name,'Data')
        print('--------------------------------------')
        
        #Number of child elements in root 
        exerciseData = []
        for record in root.findall('Record'):
            if record.get('type') == exerciseID(name):
                value = record.get('value')
                exerciseData.append(value)
        lengthOfDataEntries = len(exerciseData)
        print('The number of entries:',lengthOfDataEntries)

        #Display the number of attributes within each element
        numDict = []
        for record in root.iter('Record'):
            if record.get('type') == exerciseID(name):
                numDict.append(record.attrib)
        lengthOfDiction = len(numDict)
        
        #List the date range for exercise data
        dataRange(name)

    #Test Case: The number of child elements in the root should equal the number of dictionaries. If this is not the case then we have missing data entries.
        def testElementEqualChild(): 
            assert  exerciseData != lengthOfDiction, "Missing data entries (Warning)"

        testElementEqualChild()
        print("(No missing data entries)")


    #Extract attributes from record element
    def exerciseData(start_date,end_date,name):
        """
        Create a pandas dataframe of a given health metric listing two columns containing the dates and measured values.

        Documentation: exerciseData('start date','end date','health metric')

        Ex. exerciseData("2018-07-19","2018-07-21",'HeartRate')
        """
        columns = []
        rows = []
        measurment = [] #Measured values of health metric
        timeOfEntry = [] #Date 

        #Extract values for specified health metric
        for record in root.findall('Record'):
            if record.get('type') == exerciseID(name):
                unit = record.get('unit') #Units 
                value = record.get('value') #Values
                creationDate = record.get('creationDate') #Date recorded
                measurment.append(value) #Append value (count/min)
                timeOfEntry.append(creationDate) #Append creation dates to the Dates
        print("Type:", exerciseID(name)) #Output name of health biometric
        columns.append('Heart Rate:' + unit)
        columns.append('Date')
        
        # Convert XML into CSV utilizing Pandas
        for i in range(len(measurment)):
            rows.append({columns[0]:measurment[i],columns[1]:timeOfEntry[i]})

        # Create the pandas dataframe
        df = pd.DataFrame(rows,columns = columns)
    
        #Parse data by dates
        df = df.set_index(['Date'])
        exercise_data = df.loc[start_date:end_date]
        
        #Return dataframe 
        return exercise_data