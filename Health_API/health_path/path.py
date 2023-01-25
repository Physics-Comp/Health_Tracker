#Import packages
import xml.etree.ElementTree as ET
import os
import platform

class Path:
#Define the path of the XML file from which we want to analyze
    def health_file_path(path_parts):
        """
        Summary:
        The method health_file_path is used to define the location of your XML health data file and return the root
        of the XML file.

        The parameter of the method is the absoluth path containing your health records. We do not have to include the the home 
        directory as this is defined by an environment variable which depends on the operating system.
        
        Args:
            path_parts (list): Absolute path of health data
        
        Returns:
            <class 'xml.etree.ElementTree.Element'>
        """
        # Determine the current operating system
        current_os = platform.system()

        # Use the appropriate environment variables for the current operating system
        if current_os == 'Windows':
            home_dir = os.environ['HOMEPATH']
            desktop_dir = os.environ['DESKTOP']
        else:
            home_dir = os.environ['HOME']
            desktop_dir = home_dir

        # Use the appropriate path separator for the current operating system
        if current_os == 'Windows':
            separator = '\\'
        else:
            separator = '/'

        # Use the separator to join the desktop directory and the rest of the path
        path = desktop_dir + separator + separator.join(path_parts)
            
        #Return the root
        tree = ET.parse(path)
        root = tree.getroot()
        return root