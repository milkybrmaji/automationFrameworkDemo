import configparser

#This file is created to read the config.ini file and parse it so that we can pass its values into our test cases

#1. We read the config.ini file using the configparser.RawConfigParser() class

#2. We create a class to get the value for each data that was read in 
#the config.ini file by creating a staticmethod function for each of them

config = configparser.RawConfigParser()
config.read(".//Configurations//config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url  

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password         