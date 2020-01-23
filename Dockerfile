FROM python:3.7
LABEL maintainer="zeroday0619 <zeroday0619@zeroday0619.kr>"
COPY . /deliveryApi
WORKDIR /deliveryApi
RUN pip3 install pipenv
RUN pipenv install
ENTRYPOINT ["pipenv", "run"]
CMD ["start"]