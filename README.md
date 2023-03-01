# Indian_city_rent_predictor_ci-cd
predicts rent for flats in different cities based on amenities provided.

This project has been developed along with github actions ci/cd and Dockerfile .
.Rent data in kaggle has been used for modelling , prepared a random forest regression model and got an accuracy of over 81 %.check out the jupyter filer for model developement code

Flask has been  used to develop this python web app .
To use this web app in ur local system

1. Clone it in ur local system 
2. Navigate to the directory containing the Dockerfile.
3. Build the Docker image by running the
  following command:
   docker build -t <image_name> .
4. After the build is complete, you can run the Docker image by using the
  following command:
   docker run -p <host_port>:<container_port> <image_name>



Check out the app

https://jittery-army-production.up.railway.app



![image](https://user-images.githubusercontent.com/73159496/212893473-2adbf030-3a47-473f-8a8f-4477b435fbbd.png)


![image](https://user-images.githubusercontent.com/73159496/212893674-74eff969-760f-4de4-8a10-04c9cdd75cc2.png)


![image](https://user-images.githubusercontent.com/73159496/212893767-150513b4-9e15-45a2-8a23-14d93ee8f68b.png)


