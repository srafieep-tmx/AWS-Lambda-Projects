import jason

def lambda_handler(event, context):
    print("Lambda from my code")

    return {
        'statuscode' : 200,
        "body" : jason.dumps ("Hello Lambda from my code!")
    }