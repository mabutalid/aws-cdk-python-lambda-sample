#!/usr/bin/env python3

from aws_cdk import core

from stacks.lambda_stack import LambdaStack

env_northvirginia = core.Environment(
    account="1111111111111111", region="us-east-1")


app = core.App()
LambdaStack(app, "aws-lambda", env=env_northvirginia)

app.synth()
