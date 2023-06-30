FROM python:3.8-slim-buster

# Download Package Information
RUN apt-get update -y

# Install Tkinter
RUN apt-get install tk -y

ENV LANG C.UTF-8

# Commands to run Tkinter application
CMD capstone_IV_main.py
ENTRYPOINT ["python3"]