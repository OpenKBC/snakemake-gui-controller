__author__ = "Junhee Yoon"
__version__ = "1.0.0"
__maintainer__ = "Junhee Yoon"
__email__ = "swiri021@gmail.com"

from flask_wtf import Form
from wtforms import SubmitField, SelectField

import glob

# Form ORM
class InitForm(Form):

    # Internal function to create form
    def _get_directory_name():
        dir_list = glob.glob("pipelines/*/") # Get DIR list
        dir_names = [x.replace("pipelines/","")[:-1] for x in dir_list] # Cleanup names of dir

        # SelectField: choices=[(value, showing key on page)]
        choice_output = [(x, y) for x, y in zip(dir_list, dir_names) if y!='pipeline_controller']
        return choice_output

    pipeline_name = SelectField('Please select your pipeline to run: ', choices=_get_directory_name())
    submit = SubmitField('Submit')