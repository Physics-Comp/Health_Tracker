import xml.etree.ElementTree as ET
tree = ET.parse("test2.xml")
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


#Define exercise identifiers
def unique_data_types():
    list1 = []
    #Output different types health data
    for record in root.findall('Record'):
        type1 = record.get('type')
        list1.append(type1)

    #Unique identifiers in export.xml
    #Initialize a null list
    unique_list = []
        
    #Traverse all elements
    for x in list1:
        #Check if element exists in unique_list array or not
        if x not in unique_list:
            unique_list.append(x)
    print('Unique elements in list',unique_list)

#Determine the date range (Use excerciseID function to obtain data_type)
def data_range(data_type):
    dates = []
    for record in root.findall('Record'):
        if record.get('type') == data_type:
            creationDate = record.get('creationDate')
            dates.append(creationDate)
    print(len(dates))
    print('First Date',dates[0])
    print('Last Date', dates[-1])