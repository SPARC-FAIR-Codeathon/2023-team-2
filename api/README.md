# API

This folder is about the API that connects frontend to backend for the neuron data. It contains different files like below.

## Folder Structure

### helpers

## File Structure

### Dockerfile

Contains the instructions to generate a Docker Image and defines the port number. 

### requirements.txt

This file contains the required packages with version numbers.

### app.py

This is the main entrypoint for the flask app. It has:
* `hello` function that returns a friendly greeting.
* `generate` function that generates neuron visualizations
* `cache` function that caches this response
* `info` function that returns headers and other information
* `flask_health_check` function that returns health checks

### wsgi.py

This is the entrypoint for the flask app.
