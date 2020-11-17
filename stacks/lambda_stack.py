from aws_cdk import (
    aws_lambda as lambda_,
    aws_apigateway as apigw,
    core
)


class LambdaStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        lambda_function = lambda_.Function(self, "hiuserfunction",
                                           runtime=lambda_.Runtime.PYTHON_3_8,
                                           code=lambda_.Code.asset('lambda'),
                                           handler='hello.sayHi',
                                           function_name="hello-user-cdk",
                                           description='Second lambda function created to say hi to user'
                                           )

        api_gateway = apigw.LambdaRestApi(self, 'helloworld',
                                          handler=lambda_function,
                                          rest_api_name='mylambdaapimarco'
                                          )
