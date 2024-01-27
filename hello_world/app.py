import json
import zeep

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
    client = zeep.Client(wsdl=wsdl)
    #print(client.service.Method1('Zeep', 'is cool'))
    returneddata = client.service.Method1('Zeep', 'is cool')

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": returneddata,
            }
        ),
    }
