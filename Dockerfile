FROM python:3.9
RUN apt-get update -y
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash
RUN apt-get install -y nodejs
COPY setup-env /setup-env
WORKDIR /setup-env
RUN ./guest-build.sh

CMD sleep infinity
