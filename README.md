# Food-recipe-app-api
* This repository contains the code for a food recipe app API. With this API, users can easily access a wide range of recipes and enhance their cooking experience.
* The API allows users to browse and search for various recipes, as well as create and manage their own recipes.
* It provides endpoints for retrieving recipe details, adding ingredients, and saving favorite recipes.
* The app is built using Django and follows RESTful principles for API design.
* It also utilizes a PostgreSQL database for storing recipe data.


## Tools & Technologies
* Python - Programming Language
* Django - Python Web Framework
* Django REST Framework - API development
* drf-spectacular - Schema generation for the REST APIs
* Pillow - Python Image Manipulation Library
* flake8 - Python Linting Tool
* PostgreSQL - RDBMS for backend
* Docker - Containerized Local Devlopment
* Docker Compose - Run multiple containers with spcefied configs
* GitHub Actions - CI tool for automated Unit-testing & Linting
* Swagger - Browsable Documentation for the APIs
* Nginx - Reverse Proxy
* uWSGI - Server for the Django app


## Connect to EC2 Deployment Server via SSH [WSL2 Agent]
* Run these commands from ~/.ssh/ directory

* Create SSH key-pairs, if you have not set them up already

    ``` ssh-keygen -t rsa -b 4096 ```

* Start SSH agent

    ```eval `ssh-agent -s` ```

* Add your SSH key to your SSH-agent

    ``` ssh-add <private_ssh_key> ```

    > **Note:** The command `ssh-add` adds private key identities (from your `~/.ssh` directory) to the authentication agent (`ssh-agent`), so that the ssh agent can take care of the authentication for you, and you don’t have to type in passwords at the terminal.

* Connect to EC2 server

    ``` ssh ec2-user@<Public IPv4 address> ```

* Now, you have access to EC2 deployment server from you local machine
