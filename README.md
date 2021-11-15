## Pipeline Controller
* This is pipeline controller(SnakeMake) for pipeline container by using Flask, Jinja2 and Bootstrap. This controller provides config.yaml form for executing snakemake and it will execute the workflow after submission.
* Docker location: https://github.com/OpenKBC/snakemake-gui-controller-image
* Images status: 
[![Docker Image CI](https://github.com/OpenKBC/snakemake-gui-controller-image/actions/workflows/docker-image.yml/badge.svg)](https://github.com/OpenKBC/snakemake-gui-controller-image/actions/workflows/docker-image.yml)
[![Pytest for images](https://github.com/OpenKBC/snakemake-gui-controller-image/actions/workflows/python-app.yml/badge.svg)](https://github.com/OpenKBC/snakemake-gui-controller-image/actions/workflows/python-app.yml)

### Warning
* Current version has a problem with CSRF token. If you have BAD REQUEST error, click refresh button on your browser(Sorry!)

### Version history (Development phase)
* version(v1.0.2) docker-compose is ready
* version(v1.0.1) imported celery-redis for workers and communication
* version(v1.0.0) does not have loading spinner, please wait for browser spinne instead of it

### Requirements
- The controller should be located to same root folder with pipeline folders
- All pipelines should have same snakefile name(Snakemake) and configuration(config.yaml)
- Memory usage: 4-5gb for DEG pipeline (Please change your docker manager setting for this)
- Requirements of pipeline needs to be imported on the pipeline_controller requirements.txt
- Structure example:
```
(root)
|---pipeline_controller/
|---pipelines/
|---|---test-pipeline1/
|---|---test-pipeline2/
```
- Before running docker, please change path(Line 9 and Line 34) in **docker-compose.yaml**
```yaml
# Line 9 and 34
# Change volumes to your path
    # /your-git-clone-folder/snakemake-gui-controller/pipelines:/pipeline_controller/pipelines
    volumes:
      - /Users/junheeyoon/Desktop/OpenKBC/snakemake-gui-controller/pipelines:/pipeline_controller/pipelines
```


- Docker-compose:
```
docker-compose up --build
```

### Usage
* Using docker-compose is highly recommended, but you can run pipeline manually by modifying snakefile and launching flask, celery in local
* After ```docker-compose -f docker-compose.yaml up --build```, go to the browser and http://localhost for pipeline

### Importing pipeline
- Create your pipeline folder inside ```pipelines``` directory
- Make snakefile and check all the path is **based on your pipeline folder(treat your pipeline folder as root)**
- Make **config.yaml** for template
