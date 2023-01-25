#Import API to parse XML data
import re
from health_path.path import Path

class Record:
#Extract all the XML Record tags and output the number of each tag
    def record_dictionary(root):
        """
        Summary: 
            Output a dictionary containg all the type attributes of each record tag and the number of each record.

        Args:
            root: The path comtaining your health biometrics.
        
        Returns: 
            A dictionary containing biometrics as keys and the corresponding number of records for each biometric as values.
        
        Ex:
            Analysis.data_tag(root)
        """
        record_dict = {}
        for activity in root.findall('Record'):
             record_dict[activity.get('type')] = record_dict.get(activity.get('type'), 0) + 1
        return record_dict

#Concise naming conventions for health biometric
    @staticmethod
    def biometric(root):
        """
        Summary:
        This function takes in a single argument "root" and returns a dictionary of biometric data with modified keys that are more readable and consistent.

        Args:
        root (str): The root directory of the biometric data.
        
        Returns:
        record_dict (dict): A dictionary of biometric data with modified keys.
        
        Ex:
        record_dict = concise_biometric_dict("Root/data/biometric")
        """
        
        record_dict = Record.record_dictionary(root)
        remove_prefix = [re.sub(r'^HKQuantityTypeIdentifier|^HKDataType|^HKCategoryTypeIdentifier', "", records) for records in record_dict.keys()]
        edit_name = [re.sub(r"([a-z])([A-Z])", r"\1_\2", t) for t in remove_prefix]
        return(dict(zip(edit_name, record_dict.keys())))

#Determine the date range (Use excerciseID function to obtain data_type)
    """
    Extracts the date range
    Ex.
    dataRange('HeartRate')

    Note: In order to use the condenced naming conventions you must call the exerciseID function.
    """
    @staticmethod
    def data_range_of_biometric(name):

        dates = []
        name_biometric = Record.concise_biometric_name(root)[name]
        for record in root.findall('Record'):
            if record.get('type') == name_biometric:
                creationDate = record.get('creationDate')
                dates.append(creationDate)
        print('First Date:',dates[0])
        print('Last Date:', dates[-1])

    #Show preliminary data about the specified biometric such as the number of data points and date range.

    def prelimData(self, name, path):
        """
        Gives a general description of the biometric data given a particular health metric. The following information should be given
        1.) Name of the health metric
        2.) First date the particular health metric was recoreded
        3.) Last recorded date of the specified health metric
        4.) Test case that checks if there are any missing data entries in the dataset
        """
        print('Preliminary',self.name,'Data')
        print('--------------------------------------')
        
        #Number of child elements in root 
        exerciseData = []
        for record in self.fileRoot(path).findall('Record'):
            if record.get('type') == self.exerciseID(name):
                value = record.get('value')
                exerciseData.append(value)
        lengthOfDataEntries = len(exerciseData)
        print('The number of entries:',lengthOfDataEntries)

        #Display the number of attributes within each element
        numDict = []
        for record in self.fileRoot(path).iter('Record'):
            if record.get('type') == self.exerciseID(name):
                numDict.append(record.attrib)
        lengthOfDiction = len(numDict)
        
        #List the date range for exercise data
        self.dataRange(self.name)

    #Test Case: The number of child elements in the root should equal the number of dictionaries. If this is not the case then we have missing data entries.
        def testElementEqualChild(): 
            assert  exerciseData != lengthOfDiction, "Missing data entries (Warning)"

        testElementEqualChild()
        print("(No missing data entries)")
