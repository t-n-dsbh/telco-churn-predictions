import logging

import azure.functions as func

from prediction import make_prediction

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="predict")
def predict(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    tenure = req.params.get('tenure')
    monthly = req.params.get('monthly')
    techsupport = req.params.get('techsupport')
    
    prediction = make_prediction(tenure=tenure, 
                                 MonthlyCharges=monthly, 
                                 TechSupport_yes=techsupport)

    if tenure and monthly and techsupport:
        return func.HttpResponse(f"The Customer will churn with probability {prediction}.")
    else:
        return func.HttpResponse(
             "You have not provided the required parameters to make a prediction.",
             status_code=200
        )