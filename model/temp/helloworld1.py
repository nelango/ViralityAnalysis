import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

class input(messages.Message):
	title = messages.StringField(1, required = True)
	content = messages.StringField(2)

# class output(messages.Message):
# 	shares = messages.StringField(1)

@endpoints.api(name = 'input', version = 'v1', description = "API for ML model")
class sharesAPI(remote.Service):
	
	@endpoints.method(input,input, name = "input.parse", path='input', http_method ='POST')
	def parse(self, request):
		return request

application = endpoints.api_server([sharesAPI])
