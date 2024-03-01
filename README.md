# Quick EKS cross az

This project is based on [existing AWS open solution](https://aws.amazon.com/blogs/containers/getting-visibility-into-your-amazon-eks-cross-az-pod-to-pod-network-bytes/).
It simplifies operations by using your current AWS role directly from your shell session, and without using any iam:* permission...


## Features

* **Runs With Your Current AWS Credentials:** Uses the AWS credentials and settings you already have configured in your shell session. No need to configure special credentials just for the demo.
* **Works Without Administrator Privileges:** No need for IAM modification permissions - it's designed to work seamlessly with PowerUser access.  

* **Reuses Your EKS Authentication:** Uses the active Kubernetes context in your shell to get pod and node metadata.
* **Simple Exectuion:** One line execution with `pipx` or `docker` for all orachstration icnluding cleanup: enabling then aggragating flowlogs, then cleanup.

## techincally whats happens 
Like the original solution, flow logs, buckets are provisioned via cloudformation. Unlike the original solution everything is orchetrated by the script
* flow logs for the EKS VPC temporarily and buckets create via cloudformation
* Pods metadata is collected: 
    * pod `app` label
    * node ip
* After a configurable amount of time has passed, the flow logs are aggreagted in Athena
* results downloaded as a csv
* cleanup of any changes to infrastructe

## Getting Started


### Prerequisites
* python >=3.6 installed
* make sure you have cluster API access
* AWS role active in current shell should be able to create flow logs, s3 buckets and run Athena queries

#### Using Pipx
esisest way to run the script is with [pipx](https://github.com/pypa/pipx). pipx lets you run python packages quickly in isolation 
```bash
python3 -m pip install --user pipx
python3 -m pipx run quick-eks-cross-az
```


#### Using Docker
[TODO]