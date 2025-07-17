📝 Sample Test Automation
This is sample robust pytest framework to automate web application.

📝Key features
1.Page object model 
2.Data driven from yaml files
3.Data encoding & decoding using base64
4.Singleton pattern for object creation
5.HTML report generation with error screenshot

Getting Started::
Installations
1. Download Python from https://www.python.org/downloads/
   After downloading run .exe file from downloads 
   After successful installation validate it by running below command in terminal
   pytest --version
   It will show the python version installed
2. Next command to run "pip install pytest"
3. Next download and install the convenient IDE 
4. Install Git 
5. Clone repo by running this in terminal https://github.com/yourusername/yourproject.git
6. Create virtual environment if required via command 
    python3 -m venv venv
7. Install dependencies
    pip install -r requirements.txt

Testing/Run:
1. Navigate to project directory from terminal
2. Follow below criteria to run the tests
    pytest tests/<testfilename>
   Additional parameters can be used to run the tests
    -k "matchingTextFromTest" #which will run tests matching provided text
    -m "testMarker" Run test marked with specified marker
3. Example Run command
    pyest tests/test_login.py -v --html="reports/test_report.html"
4. Validate results by opening report generated