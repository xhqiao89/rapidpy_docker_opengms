## Streamflow Prediction Web Service
#### This is the source code for publishing the Dockerized streamflow prediction system as a web service in OpenGMS Wrapper System (OGMS-WS). OpenGMS is a platform for sharing geographic and environmental data and models among multi-disciplinary users. OGMS-WS is an open source software tool in OpenGMS platform used to publish models as web services. It uses a standardized method to encapsulate models and deploy them as RESTful web services ![image](https://user-images.githubusercontent.com/13894631/115332083-c2ab4700-a15c-11eb-9ea1-010b01045bdd.png)
Instructions on publishing web services through OGMS-WS can be found at https://geomodeling.njnu.edu.cn/Development/doc.

#### The dockerized streamflow prediction model can be found at: https://hub.docker.com/r/xhqiao89/rapidpy. Detailed introduction on the streamflow prediction model can be found in this paper: https://doi.org/10.1016/j.envsoft.2019.104501.

#### This figure shows the encapsulatiztion method.
![alt text](https://github.com/xhqiao89/rapidpy_docker_opengms/blob/master/pics/2.png?raw=true)

#### The SPT.zip file is the ready-to-use encapsulatized package to deploy the streamflow prediction service in OGMS-WS. You can directly download it from here and upload it to OGMS-WS server through the "Deployment" module shown as below.
![alt text](https://github.com/xhqiao89/rapidpy_docker_opengms/blob/master/pics/1.png?raw=true)

#### A set fo TEST data is provided in the "testify" folder, including a "data.zip" for "LSM_DATA", a "input.zip" for "RAPID_IO_FILES", and a "run_rapid.py" for "PYTHON_FILE". 
![alt text](https://github.com/xhqiao89/rapidpy_docker_opengms/blob/master/pics/InputsOutputs.png?raw=true)
