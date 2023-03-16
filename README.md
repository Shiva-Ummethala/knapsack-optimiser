# ReadMe

>This repository tells how to build a knapsack optimizer service using Python Django and Django Rest Framework.
>
>The knapsack django web service/application is built and containerized using docker compose. 
>
>The Dockerfile will create an image and install all the prerequisites required for the Django application.
>
>To 

## To setup dev environment and run the application
>Navigate to knapsack-optimiser directory and execute the below commands

```sh
$ docker-compose build
$ docker-compose up
```

>Once the docker container created and is running successfully, Navigate to below url
>
>`http://127.0.0.1:8000/knapsack/` 
> and pass the below json data in the content and media type as application/json as shown below
>

```json

{
    "items": [
        [2, 10],
        [3, 15],
        [5, 25],
        [7, 30],
        [9, 35]
    ],
    "capacity": 10
}
```
![My Image](images/KnapsackWebappwithRequestjson.png)

>Click on POST to get the response of the capacity with items and values and sample response is shown below

```json

{
    "result": 50,
    "items": [
        [2,10],
        [3,15],
        [5,25]
    ]
}

```

![My Image](images/KnapsackResponseJson.png)

>In this way, a knapsack optimiser service can be created using Django application and containerized using docker compose

>This application can be deployed to cloud inclucing services like LoadBalancer, Redis Cache, Firewall and Authorization Server etc.
>
>Load balancer is used to distribute traffic to multiple instances of Django Application coming from the client app.
>
>Redis cache is used to store the frequent API calls, decrease data access latency, increase throughput, and ease the load off your database and application.  

![My Image](images/design.png)



# Instructions to create a Django project

>
>From the command line, cd into a directory where you’d like to store your code, then run the following command:
>
 
```sh
$ django-admin startproject knapsack_optimiser
```

> Then create an Django App 
> Navigate inside the directory and run the following command
>

```sh
$ python manage.py startapp knapsack_api
```
>

> Navigate to settings.py and add "rest_framework" and "knapsack_api" to INSTALLED_APPS
>
> Refer to the code inside the repo and modify accordingly as per your requirement!
