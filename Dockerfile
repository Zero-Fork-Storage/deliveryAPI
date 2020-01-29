FROM tiangolo/uwsgi-nginx-flask:python3.7
LABEL maintainer="zeroday0619 <zeroday0619@zeroday0619.kr>"
COPY . /deliveryApi
WORKDIR /deliveryApi
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["main.py"]