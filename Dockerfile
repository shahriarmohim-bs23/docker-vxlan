FROM rgielen/postgresql-ubuntu
ENV PG_PASSWORD=1234
RUN apt-get update && apt-get install -y python3-pip
WORKDIR /.termplugin
ENV TERM=xterm
ENV DOCKER_HOST=36.255.70.177:2375
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
WORKDIR /
CMD ["python3", "/.termplugin/app.py"]
CMD["docker","run" ,"--name", "postgresql","-e", "POSTGRES_USER=myusername","-e"," POSTGRES_PASSWORD=mypassword","-p","5432:5432","-v", /data:/var/lib/postgresql/data -d postgres]
confidance accuracy
bolt classsification confusion matrix roc curve precesion 


FROM ubuntu:20.04
WORKDIR /.termplugin
ENV TERM=xterm
ENV TZ=Asia/Kolkata \
    DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y python3-pip && apt-get install -y postgresql postgresql-contrib
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
WORKDIR /
CMD ["python3", "/.termplugin/app.py"]

FROM ubuntu:20.04
WORKDIR /.termplugin
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=poridhi
ENV TERM=xterm
ENV TZ=Asia/Kolkata \
    DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y python3-pip && apt-get install -y postgresql postgresql-contrib
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
WORKDIR /
CMD ["python3", "/.termplugin/app.py"]



docker run -d --name postgres-container -e TZ=UTC -p 5432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=pass ubuntu/postgres:14-22.04_beta


FROM ubuntu/postgres
WORKDIR /.termplugin
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=poridhi
ENV TERM=xterm
RUN apt-get update && apt-get install -y python3-pip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
WORKDIR /
CMD ["postgres"]