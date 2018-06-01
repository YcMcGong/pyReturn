# pyReturn
A python package to provide auto-formatted json response for web services. It follows the MySmileApp protocol.

#### MySmileApp protocol

   Every micro services return a JSON object with the following attributes:     
  
    [status]: A boolean indicating if the requested-action is successful
    [errorMessage]: A message to provide some information about the status
    [*data]: User use the attach_data method to insert an object to the *data tag
    (*data is an user-defined name)


### Installation
    pip install pyReturn
  
### Usage

   Currently only has the status_response class.
   
    A status response class include an attribute data
    status_response.data has the following tags:

    [status]: A boolean indicating if the requested-action is successful
    [errorMessage]: A message to provide some information about the status
    [*data]: User use the attach_data method to insert an object to the *data tag
    (*data is an user-defined name)
   
   #### Import
   
     from pyReturn.response import status_response
     sr = status_response()
     
   #### Set Status
      sr.set_status(True or False)
      
   #### Set errorMessage
      sr.set_errorMessage('user defined message')
      
   #### Attach data to the response
      sr.attach_data(attribute_name, attribure_value, isSuccess = False)
      [set isSuccess = True is this data attachment means a successful request]
      
   #### Generate a JSON version response
      sr.get_response()
   
