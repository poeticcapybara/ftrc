# Futurice Data Science Task

- Author: José Pedro Silva
- Date: 2018-10-28
- Python 3.7.0
- Libraries: _see requirements.txt_

This repository contains the code necessary to create and serve a regression model for the housing dataset available 
[here](https://archive.ics.uci.edu/ml/datasets/Housing).

## Prepare environment

Although recommendable to run in a dedicated virtual environment, it is left to the user to set-up 
the one he is more comfortable with. Regardless of the choice, the necessary libraries can be installed by running

    pip install -r requirements.txt
    
for the flask application and 

    pip install -r DS-requirements.txt
    
for the DS needs.


## Data Science

The DS folder contains:
 - _train_and_export.py_ - a Python script which
serializes a scikit-learn LinearRegression model.
 - _HouseValuePrediction.ipynb_ - a jupyter notebook where some exploratory analysis 
 and model selection was performed.
 - _HouseValuePrediction.html_ - a rendering of the above mentioned jupyter notebook
 - _DS-requirements.txt_ - a requirements.txt file with the necessary libraries to be able to 
 run the files in the DS folder

To run the script

    python train_and_export.py -o output_dir

with output_dir the absolute path of the folder in which to save the model.

The following regression models were explored:

- Linear Regression from [scikit-learn](http://scikit-learn.org/)
- GLM from [h2o](http://docs.h2o.ai/h2o/latest-stable/h2o-docs/welcome.html)
- Regression Random Forest from [h2o](http://docs.h2o.ai/h2o/latest-stable/h2o-docs/welcome.html)
- Probabilistic Linear Regression from [PyMC3](https://docs.pymc.io/)

## Flask

The model is served with an application written in flask with 
a single POST endpoint (/predict) on port 5000.
- _app.py_ - application logic containing the views
- _templates_ - folder containing templates for 404 and 400 errors
- _static_ - folder containing image to be displayed in 404 error
- _forms.py_ - WTForm to validate the JSON received
- _requirements.txt_ - a requirements.txt file with the necessary libraries to be able to 
 run the flask application (including an overlap when it is necessary to run
 _train_and_export.py_)
 
 To run the application
 
     python app.py
