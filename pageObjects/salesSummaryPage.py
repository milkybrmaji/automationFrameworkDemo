import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 

class searchSalesSummary():
  lnk_CustomersMenu_Xpath =  "//a[@href='#']//p[contains(text(),'Reports')]"
  lnk_CustomersPage_Xpath = "//a[@href='/Admin/Report/SalesSummary']//p[contains(text(),'Sales summary')]"

  txtInput_StartDate_Id = "StartDate"
  txtInput_EndDate_Id = "EndDate"
  
