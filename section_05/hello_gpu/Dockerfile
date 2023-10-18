FROM nvidia/cuda:10.1-cudnn7-runtime-ubuntu18.04

RUN apt-get update
RUN apt-get install python3 python3-pip -y
RUN pip3 install torch==1.5.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html

CMD ["python3","-c","import torch; print(torch.__version__, torch.cuda.device_count())"]
