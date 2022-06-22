FROM python:3.9
RUN apt-get update -y
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash
RUN apt-get install -y nodejs
COPY setup-env /app
WORKDIR /app
RUN ./guest-build.sh

EXPOSE 8501
CMD sleep infinity
