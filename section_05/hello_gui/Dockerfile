# run with command:
#    docker run -ti --rm --net=host -e DISPLAY="$DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" hello-qt

FROM alpine:3.12

RUN apk update
RUN apk add py3-qt5 ttf-ubuntu-font-family

COPY hello.py /

CMD ["python3","hello.py"]
