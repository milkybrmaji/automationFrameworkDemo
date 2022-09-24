from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == "safari":
        pass 
        #driver = webdriver.Safari()
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())        
    return driver


def pytest_addoption(parser):   # This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  #This will return the browser value to setup method
    return request.config.getoption("--browser")



############### PYTEST HTML REPORT #############

#This is a hook for adding enviroment info to the HTML report
def pytest_configure(config):
    config._metadata["Project Name"] = "nop Commerce"
    config._metadata["Module Name"] = "Customers"
    config._metadata["Tester"] = "Milky"


#This is a hook to delete/modify enviroment info in the HTML report
#This function is removing metadata I do not need
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)    