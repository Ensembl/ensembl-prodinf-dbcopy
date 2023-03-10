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

FROM python:3.8.9-alpine

RUN apk update
RUN apk add git
RUN apk add --no-cache mariadb-dev
RUN apk add --no-cache musl-dev
RUN apk add --no-cache gcc
RUN apk add --no-cache libffi-dev
RUN adduser -D appuser
USER appuser
WORKDIR /home/appuser

ENV PIP_ROOT_USER_ACTION=ignore
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=ensembl_prodinf_dbcopy.settings
ENV PATH="/home/appuser/.local/bin:${PATH}"
# Copy the current directory contents into the container
COPY --chown=appuser . /home/appuser

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --user -r requirements.txt
RUN pip install --user gunicorn~=20.1.0
RUN pip install .

ENV PYTHONPATH=$PYTHONPATH:/home/appuser/src
EXPOSE 8000

CMD  ["gunicorn", "-c", "/home/appuser/gunicorn.conf.py", "ensembl_prodinf_dbcopy.wsgi:application"]

