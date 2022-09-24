import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 

class SearchCustomer():
    txtInput_Email_Id = "SearchEmail"
    txtInput_FirstName_Id = "SearchFirstName"
    txtInput_LastName_Id = "SearchLastName"

    dropDown_DOB_Month_Id = ""
    dropDown_DOB_Day_Id = ""

    txtInput_Company_Id = "SearchCompany"
    txtInput_IPAddress_Id = "SearchIpAddress"
    btn_Search_Id = "search-customers"
    
    tableSearchResults_Xpath = "//table[@role='grid']"
    table_Xpath = "//table[@id='customers-grid']"
    tableRows_Xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_Xpath = "//table[@id='customers-grid']//tbody/tr/td"


    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txtInput_Email_Id).clear()
        self.driver.find_element(By.ID, self.txtInput_Email_Id).send_keys(email) 

    def setFirstName(self, fname):
        self.driver.find_element(By.ID, self.txtInput_FirstName_Id).clear()
        self.driver.find_element(By.ID, self.txtInput_FirstName_Id).send_keys(fname)   

    def setLastName(self, lname):
        self.driver.find_element(By.ID, self.txtInput_LastName_Id).clear()
        self.driver.find_element(By.ID, self.txtInput_LastName_Id).send_keys(lname)   

    def clickDOBMonth(self, month):
        self.driver.find_element(By.ID, self.dropDown_DOB_Month_Id)

    def clickDOBDay(self, day):
        self.driver.find_element(By.ID, self.dropDown_DOB_Day_Id)    

    def setCompanyName(self, company):
        self.driver.find_element(By.ID, self.txtInput_Company_Id).clear()
        self.driver.find_element(By.ID, self.txtInput_Company_Id).send_keys(company) 

    def setIPAddress(self, ip):
        self.driver.find_element(By.ID, self.txtInput_IPAddress_Id).clear()
        self.driver.find_element(By.ID, self.txtInput_IPAddress_Id).send_keys(ip)   

    def clickSearch(self):
        self.driver.find_element(By.ID, self.btn_Search_Id).click()

    def getNumberOfColumns(self):
        self.numberOfColumns = self.driver.find_elements(By.XPATH, self.tableColumns_Xpath)
        return len(self.numberOfColumns)

    def getNumberOfRows(self):
        self.numberOfRows = self.driver.find_elements(By.XPATH, self.tableRows_Xpath)
        return len(self.numberOfRows)

    def searchCustomerByEmail(self, email):
        flag = False
        table = self.driver.find_element(By.XPATH, self.table_Xpath)
        noEmailID = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr").text
        if noEmailID == "No data available in table":
            return flag
        else:
            for row in range(1, self.getNumberOfRows()+1):
                EmailID = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(row)+"]/td[2]").text
                if email in EmailID:
                    flag = True
                    return flag
            return flag        


    def searchCustomerByName(self, name):
        flag = False
        table = self.driver.find_element(By.XPATH, self.table_Xpath)
        noNameID = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr").text
        if noNameID == "No data available in table":
            return flag
        else:
            for row in range(1, self.getNumberOfRows()+1):
                nameID = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(row)+"]/td[3]").text
                if name in nameID:
                    flag = True
                    return flag
            return flag 
        
        
        '''
        flag = False
        for row in range(1, self.getNumberOfRows()+1):
            table = self.driver.find_element(By.XPATH, self.table_Xpath)
            nameID = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(row)+"]/td[3]").text
            if name in nameID:
                flag = True
                return flag
        return flag       
        '''

                 