import os, pathlib

BASE_URL = "https://build.fillout.com/"
EMAIL_ADDRESS = "sipoto5605@cumzle.com"
COLLABORATOR_EMAIL = "suresh@gmail.com"
PASSWORD = "password@123"
INCORRECT_PASSWORD = "Password123"
WORKSPACE_NAME = "sample"
FIRST_NAME = "Ram"
LAST_NAME = "Kumar"


ROOT_DIRECTORY = pathlib.Path(__file__).parent.resolve()
LOG_FILE_LOCATION = f"{ROOT_DIRECTORY}/logs/report.log"
REPORTS_DIRECTORY = f"{ROOT_DIRECTORY}/reports"
TEST_DATA_DIRECTORY = f"{ROOT_DIRECTORY}/data"

