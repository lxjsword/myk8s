FROM python:latest
ADD cgi-bin /home/sapp/cgi-bin
WORKDIR /home/sapp
ENTRYPOINT ["python", "-m", "http.server", "--cgi"]
