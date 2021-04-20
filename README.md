## Streamflow Prediction Web Service
#### This is the source code for publishing the Dockerized streamflow prediction system as a web service in OpenGMS Wrapper System (OGMS-WS). OGMS-WS is an open source software tool used to publish models as web services. It uses a standardized method to encapsulate models and deploy them as RESTful web services.

#### OGMS-WS is a portable application that can be easily launched from an executable file. It have Windows, Linux, and macOS versions for different users. It can be downloaded from https://geomodeling.njnu.edu.cn/Development/download (Tools->Model Service Container).

#### Detailed instruction on hwo to publish web services through OGMS-WS can be found at https://geomodeling.njnu.edu.cn/Development/doc. 

#### The dockerized streamflow prediction model can be found at: https://hub.docker.com/r/xhqiao89/rapidpy. 

#### Detailed introduction on the streamflow prediction model can be found in this paper: https://doi.org/10.1016/j.envsoft.2019.104501.

#### This figure shows the folder structure of the encapsulated streamflow prediction model package. The model encapsulation file defines the interaction between users and the model service, including accepting requests from users and extracting model inputs, invoking and executing the model, and returning model outputs as responses to users when completed. Model-related files include the model executable files or scripts (model folder), dependency libraries that support model execution (assembly folder), model running instances (instance folder), environment dependencies for model encapsulation (supportive folder), and model test data (testify folder).
![alt text](https://github.com/xhqiao89/rapidpy_docker_opengms/blob/master/pics/2.png){:height="50%" width="50%"}

#### The service is deployed by uploading the zipped encapsulated model package to the ‘Deployment’ module in OGMS-WS. You can directly download the SPT.zip file from here and upload it to OGMS-WS server through the "Deployment" module shown as below.
![alt text](https://github.com/xhqiao89/rapidpy_docker_opengms/blob/master/pics/1.png){:height="50%" width="50%"}

#### A set fo TEST data is provided in the "testify" folder, including a "data.zip" for "LSM_DATA", a "input.zip" for "RAPID_IO_FILES", and a "run_rapid.py" for "PYTHON_FILE". 
![alt text](https://github.com/xhqiao89/rapidpy_docker_opengms/blob/master/pics/InputsOutputs.png)

