#### This is the encapsulation script to connect the model entry function with the .mdl file
# Basically it reads in inputs, executes the service, and returns the results

from modelservicecontext import EModelContextStatus
from modelservicecontext import ERequestResponseDataFlag
from modelservicecontext import ERequestResponseDataMIME
from modelservicecontext import ModelServiceContext
from modeldatahandler import ModelDataHandler

import sys
import os

# Begin
if len(sys.argv) < 4:
    exit()

ms = ModelServiceContext()
ms.onInitialize(sys.argv[1], sys.argv[2], sys.argv[3])
mdh = ModelDataHandler(ms)

# State - mainProcess
ms.onEnterState('mainProcess')
state_folder= ms.getCurrentDataDirectory()

#### Model inputs
# Event - rapid_io_files_location
ms.onFireEvent('rapid_io_files')

ms.onRequestData()

rapid_io_files = None
if ms.getRequestDataFlag() == ERequestResponseDataFlag.ERDF_OK:
    if ms.getRequestDataMIME() == ERequestResponseDataMIME.ERDM_RAW_FILE:
        rapid_io_files = ms.getRequestDataBody()
    if ms.getRequestDataMIME() == ERequestResponseDataMIME.ERDM_ZIP_FILE:
        rapid_io_files = ms.getRequestDataBody()
        ms.mapZipToCurrentDataDirectory(rapid_io_files)
        # Current data directory : ~/mainProcess/rapid_io_files/
else:
    ms.onFinalize()

# Event - lsm_data_location
ms.onFireEvent('lsm_data')

ms.onRequestData()

lsm_data = None
if ms.getRequestDataFlag() == ERequestResponseDataFlag.ERDF_OK:
    if ms.getRequestDataMIME() == ERequestResponseDataMIME.ERDM_RAW_FILE:
        lsm_data = ms.getRequestDataBody()
    if ms.getRequestDataMIME() == ERequestResponseDataMIME.ERDM_ZIP_FILE:
        lsm_data = ms.getRequestDataBody()
        ms.mapZipToCurrentDataDirectory(lsm_data)
        # Current data directory : ~/mainProcess/lsm_data/
else:
    ms.onFinalize()

# Event - python file
ms.onFireEvent('python_file')

ms.onRequestData()

python_file = None
if ms.getRequestDataFlag() == ERequestResponseDataFlag.ERDF_OK:
    if ms.getRequestDataMIME() == ERequestResponseDataMIME.ERDM_RAW_FILE:
        python_file = ms.getRequestDataBody()
        # map uploaded file to current directory and change back to its original name
        ms.mapFileToCurrentDataDirectory(python_file, "run_rapid.py")
        # Current data directory : ~/mainProcess/python_file/
else:
    ms.onFinalize()

# Event - streamflow
ms.onFireEvent('streamflow')

ms.setResponseDataFlag(ERequestResponseDataFlag.ERDF_OK)

ms.setResponseDataMIME(ERequestResponseDataMIME.ERDM_RAW_FILE)

result_folder = ms.getCurrentDataDirectory()
# Current data directory : ~/mainProcess/steamflow/

#docker run --name rapidpy -w /home/python_file -v ~/mainProcess:/home xhqiao89/rapidpy:1.0 python run_rapid.py
mycmd = "docker run --rm --name rapidpy -w /home/python_file -v " + state_folder + ":/home xhqiao89/rapidpy:1.0 python run_rapid.py"
print(mycmd)
os.system(mycmd)

#### find the Qout nc file from the results folder and return as response
for file in os.listdir(result_folder):
    if file.startswith("Qout"):
        Qout_file = os.path.join(result_folder, file)

ms.setResponseDataFlag(ERequestResponseDataFlag.ERDF_OK)

ms.setResponseDataMIME(ERequestResponseDataMIME.ERDM_RAW_FILE)

ms.setResponseDataBody(Qout_file)

ms.onResponseData()

ms.onLeaveState()

print('Start to finalize!')

ms.onFinalize()