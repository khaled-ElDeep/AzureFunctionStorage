import azure.functions as func
import logging
from azure.storage.blob import BlockBlobService

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)
ACCOUNT_NAME = "dlstorage231"
SAS_TOKEN='sv=2024-11-04&ss=bfqt&srt=c&sp=rwdlacupyx&se=2025-11-08T22:16:33Z&st=2025-11-08T14:01:33Z&spr=https&sig=YB5I99URcKaGLHLHUgy13dLsIzD5mon6q64SqTB8UeQ%3D'
@app.route(route="http_trigger_github")
def http_trigger_github(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # name = req.params.get('name')
    file="" 
    fileContent=""       
    blob_service = BlockBlobService(account_name=ACCOUNT_NAME,account_key=None,sas_token=SAS_TOKEN)
    containername="filetransfer"
    generator = blob_service.list_blobs(container_name=containername) #lists the blobs inside containers
    for blob in generator:
        file=blob_service.get_blob_to_text(containername,blob.name) 
        logging.info(file.content)
        fileContent+=blob.name+'\n'+file.content+'\n\n'

    return func.HttpResponse(f"{fileContent}")
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')

    # if name:
    #     return func.HttpResponse(f"Hello {name} From Github")
    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed normaly. Pass a name in the query string or in the request body for a personalized response.",
    #          status_code=200
    #     )