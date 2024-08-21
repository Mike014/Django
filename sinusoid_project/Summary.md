# Sinusoid Project

## Overview
The Sinusoid Project is a Django application designed to generate and visualize sinusoidal waves. This project demonstrates the integration of Django with Matplotlib to create dynamic plots that can be rendered in a web application.

## Features
- Sinusoidal Wave Generation: Generates a sinusoidal wave with a fixed frequency of 440 Hz, amplitude of 1.0, and no phase offset.
- Dynamic Plotting: Uses Matplotlib to create and display the sinusoidal wave plot within the web application.

## Key Files and Their Roles
- sinusoid_app/urls.py: Defines the URL patterns for the application.
- sinusoid_app/views.py: Contains the view logic for generating and displaying the sinusoidal wave plot.
- sinusoid_app/templates/plot.html: The HTML template for rendering the plot.
- sinusoid_project/urls.py: Includes the URL configurations for the entire project.
- requirements.txt: Lists the dependencies required for the project.

## Key Files and Their Roles
- Fixed Parameters: The view function plot_sinusoid in views.py generates a sinusoidal wave with a fixed frequency of 440 Hz, amplitude of 1.0, and no phase offset.
- Wave Generation: The Sinusoid class is used to create the wave data. The make_wave method generates the time series (ts) and the corresponding wave values (ys).
- Plot Generation: Matplotlib is used to create a plot of the sinusoidal wave. The plot includes labels for the x-axis (time in seconds) and y-axis (amplitude), and a title.
- Rendering: The plot is saved to a buffer in PNG format and returned as an HTTP response with the content type image/png.

## Getting Started
To run the Sinusoid Project locally, follow these steps:

- Clone the repository:
git clone https://github.com/MikyMikeMusic/Django.git
cd your-repository

- Install dependencies:
pip install -r requirements.txt           

- Run migrations:
python manage.py migrate

- Start the development server:
python manage.py runserver

- Access the application: Open your web browser and navigate to http://127.0.0.1:8000/sinusoid/plot/.

# Example Usage
- The application will generate and display a plot of a sinusoidal wave with a frequency of 440 Hz and amplitude of 1.0.




