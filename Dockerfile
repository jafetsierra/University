FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /universidad
WORKDIR /universidad
ADD . /universidad
RUN pip install -r requirements.txt
EXPOSE 8080
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver