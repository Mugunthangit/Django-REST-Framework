from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

def http_miss(self):
	res_data = dict(status=415, success=False)
	return res_data