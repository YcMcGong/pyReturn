# pyReturn
A python package to provide auto-formatted json response for web services. It follows the MySmileApp protocol.

#### MySmileApp protocol

   Every micro services return a JSON object with the following attributes:     
  
    [status]: A boolean indicating if the requested-action is successful
    [errorMessage]: A message to provide some information about the status
    [*other keys]: Additional key to store the data returned from the microservices

### Installation
    pip install pyReturn
  
### Usage

   Currently only has the status_response class.
   
    A status_response class include an attribute data
    status_response.data has the following keys:

    [status]: A boolean indicating if the requested-action is successful
    [errorMessage]: A message to provide some information about the status
    [*data]: User use the attach_data method to insert an object to the *data key
   
   #### Import
   
     from pyReturn.response import status_response
     sr = status_response()
     
   #### Set Status
   status is set to False by default. 
   
      sr.set_status(True or False)
      
   #### Set errorMessage
      sr.set_errorMessage('user defined message')
      
   #### Attach data to the response
      sr.attach_data(key, value, isSuccess = False)
      [set isSuccess = True is this data attachment means a successful request]
      
   #### Generate a JSON response
      ...
      response_json = sr.get_response()
      return response_json
   
