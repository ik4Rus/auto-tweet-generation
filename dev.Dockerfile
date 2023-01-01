# AWS python base image
FROM python:3.10

# Prepare env
ARG OPENAI_KEY
ENV OPENAI_KEY $OPENAI_KEY

# Install requirements
COPY ./requirements.txt ./
RUN pip3 install  --no-cache-dir -r  ./requirements.txt

EXPOSE 8080