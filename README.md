# Food-recipe-app-api
* This repository contains the code for a food recipe app API. With this API, users can easily access a variety of recipes and enhance their cooking experience.
* The API allows users to browse and search for various recipes, and create and manage their own recipes.
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
* Docker - Containerized Local Development
* Docker Compose - Run multiple containers with specific configs
* GitHub Actions - CI tool for automated Unit-testing & Linting
* Swagger - Browsable Documentation for the APIs
* Nginx - Reverse Proxy
* uWSGI - Server for the Django app


## Connect to Digital Ocean Droplet via SSH [WSL2 Agent]
* Run these commands from ~/.ssh/ directory

* Create SSH key pairs, if you have not set them up already

    ``` ssh-keygen -t rsa -b 4096 ```

* Start SSH agent

    ```eval `ssh-agent -s` ```

* Add your SSH key to your SSH-agent

    ``` ssh-add <private_ssh_key> ```

    > **Note:** The command `ssh-add` adds private key identities (from your `~/.ssh` directory) to the authentication agent (`ssh-agent`), so that the ssh-agent can take care of the authentication for you, and you don’t have to type in passwords at the terminal.

* Connect to Digital Ocean Droplet

    ``` ssh root@<PUBLIC IPV4 ADDRESS> ```

  Now, you have access to the Deployment Server from your local machine

  ## Visit the API
* API Address :  [143.244.133.245/api/docs](http://143.244.133.245/api/docs)
