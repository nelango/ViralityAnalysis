from google.appengine.ext import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

class Greeting(messages.Message):
  """Greeting that stores a message."""
  message = messages.StringField(1)

class input(messages.Message):
	title = messages.StringField(1, required = True)
	content = messages.StringField(2)

# class output(messages.Message):
# 	shares = messages.StringField(1)

@endpoints.api(name = 'input', version = 'v1', description = "API for ML model")
class sharesAPI(remote.Service):
	@endpoints.method(message_types.VoidMessage, Greeting,
                    path='input', http_method='GET',
                    name='input.parse')
	def map_list(self, unused_request):
    	return Greeting(message="HELLO") 
	
	@endpoints.method(input,input, name = "input.parse", path='input', http_method ='POST')
	def parse(self, request):
		return request

	# def analyze(self, request):
	# 	pass

app = endpoints.api_server([sharesAPI])
