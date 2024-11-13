\# First stage: build the Python app
FROM python:3.12-bookworm AS build

# install dependencies
COPY ./req.txt .
RUN pip install --upgrade pip
RUN pip install -r req.txt

# copy project source code
COPY ./main_project /main_project

# set working directory
WORKDIR /main_project

# entrypoint shell scripts to be executed
COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
