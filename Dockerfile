# .. See the NOTICE file distributed with this work for additional information
#    regarding copyright ownership.
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#        http://www.apache.org/licenses/LICENSE-2.0
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image

FROM python:3.9

RUN apt-get update && apt-get -y install \
    build-essential \
    default-mysql-client && \
    rm -rf /var/lib/apt/lists/*

RUN useradd --create-home appuser
USER appuser

#create virtual env
RUN python -m venv /home/appuser/venv
ENV PATH="/home/appuser/venv/bin:$PATH"

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

ENV DJANGO_SETTINGS_MODULE=ensembl_prodinf_dbcopy.settings

# Set the working directory
WORKDIR /usr/src/app

# Copy the current directory contents into the container
COPY --chown=appuser . /usr/src/app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install gunicorn~=20.1.0
RUN pip install -r requirements.txt
RUN pip install .


ENV PYTHONPATH=$PYTHONPATH:/usr/src/app/src
EXPOSE 8000

CMD  ["gunicorn", "--config", "/usr/src/app/gunicorn.conf.py", "-b", "0.0.0.0:8000", "ensembl_prodinf_dbcopy.wsgi:application"]

