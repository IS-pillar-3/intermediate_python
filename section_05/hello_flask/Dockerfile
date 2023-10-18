from python
ENV FLASK_APP hello_flask.py
COPY hello_flask.py /
RUN pip install flask

EXPOSE 5000

CMD ["flask","run","--host=0.0.0.0"]
