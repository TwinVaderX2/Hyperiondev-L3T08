FROM python:latest

# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /usr/app/src

# Install tkinter
RUN apt-get update && apt-get install -y python3-tk

#to COPY the remote file at working directory in container
COPY src/* ./
COPY requirements.txt ./
# Now the structure looks like this:
# '/usr/app/src/
#    app/capstone_*.py'
#    images/*.png'
#    textfiles/*.txt'
#    requirements.txt'

# install requirements
RUN pip install --no-cache-dir -r requirements.txt

#CMD instruction should be used to run the software
#contained by your image, along with any arguments.
CMD [ "./capstone_IV_main.py"]
ENTRYPOINT [ "python3" ]
