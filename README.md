# Containerized Python script deployed on DockerHub 


The following project deploys a simple Python script from a customized Docker container. The resulting image is pushed to DockerHub and can be pulled down and run on a cloud platform shell: AWS Cloud9 or Google Cloud Shell. CircleCI is setup for continous integration.


The docker image can be found [here](https://hub.docker.com/repository/docker/abbarcenasj/hello_world)


### Guide to use the container
* [Download and install Docker](https://docs.docker.com/docker-for-mac/install/) to your local machine to execute the container.
* (Optional) Download and sign up to either AWS Cloud9 or Google Cloud Shell. This step is optional since the Docker image could be deployed on your local Terminal as well.
* To pull the image to your local machine, run `docker pull abbarcenasj/hello_world` on the desired shell.
* Once all the files have been dragged to your machine, run the command `docker run -it abbarcenasj/hello_world bash` to create the environment needed to run the Python script.
* Finally, to deploy the Python script run `python app.py`.
* You will be asked to write your name and the Python application will output a personalized greeting.


Reference: 
* https://noahgift.github.io/cloud-data-analysis-at-scale/topics/docker-format-containers.html
* https://www.youtube.com/watch?v=WVifwRIwSmo&feature=youtu.be
