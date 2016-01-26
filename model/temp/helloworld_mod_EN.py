"""This is the homerwork for CS8803 ASE 
implemented using Google Cloud Endpoints.

Defined here are the ProtoRPC messages needed to define Schemas for methods
as well as those methods defined in an API.
"""


import endpoints
import json
from protorpc import messages
from protorpc import message_types
from protorpc import remote
import time
import urllib2
from google.appengine.api import mail

package = 'Hello'


class Input(messages.Message):
  titleName = messages.StringField(1, required = True)
  # imagesNumber = messages.IntegerField(2, required = True)
  # videosNumber = messages.IntegerField(3, required = True)
  # keywords = messages.IntegerField(4, required = True)
  # articleContent = messages.StringField(5, required = True)
  # day = messages.StringField(6, required = True)
  # category = messages.StringField(7, required = True)


class Output(messages.Message):
  """Greeting that stores a message."""
  shares = messages.IntegerField(1)

@endpoints.api(name='prediction', version='v1')
class HelloWorldApi(remote.Service):
  """Helloworld API v1."""

  @endpoints.method(message_types.VoidMessage, Greeting,
                    path='prediction', http_method='GET',
                    name='getting.tuple')
  def say_hello(self, unused_request):
    return Output(shares=5) 

  @endpoints.method(Input, Input,
                  path='prediction', http_method='POST',
                  name='sending.shares')
  def take_input(self, request):
    return Input(title=request.titleName)
   
APPLICATION = endpoints.api_server([HelloWorldApi])