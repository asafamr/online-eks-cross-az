FROM python:3.10-slim
RUN pip install quick_eks_cross_az
CMD quick-eks-cross-az