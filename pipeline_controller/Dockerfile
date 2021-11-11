FROM continuumio/miniconda

COPY . /pipeline_controller

RUN conda create -n pipeline_controller_base python=3.8.2 R=3.6
SHELL ["conda", "run", "-n", "pipeline_controller_base", "/bin/bash", "-c"]

RUN conda install -n pipeline_controller_base -c anaconda -y graphviz

WORKDIR /pipeline_controller
RUN pip install -r requirements.txt

RUN python -c "import flask"
#CMD ["conda", "run", "-n", "pipeline_controller_base", "gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--threads", "4", "--worker-class", "gthread", "connector:app"]