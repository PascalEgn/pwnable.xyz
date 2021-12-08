FROM ree_image:latest
RUN apt-get update
RUN apt-get install -y vim
RUN apt-get install -y python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade pwntools