FROM python:3.6-slim
COPY dist/online_eks_cross_az-0.1.0.tar.gz .
RUN pip install online_eks_cross_az-0.1.0.tar.gz