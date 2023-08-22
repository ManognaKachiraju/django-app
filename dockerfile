FROM python
COPY . .
RUN pip install django
EXPOSE 8000
CMD ["py","manage.py","runserver"]
