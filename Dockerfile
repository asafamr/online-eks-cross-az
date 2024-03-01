FROM python:3.10-slim
RUN pip install --no-cache-dir quick_eks_cross_az
ENTRYPOINT [ "quick-eks-cross-az" ] 