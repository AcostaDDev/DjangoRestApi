import json
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse

from products.models import Product

def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        return JsonResponse(model_to_dict(model_data, fields=['id', 'title', 'content', 'price']))
        """ data = model_to_dict(model_data, fields=['id', 'title', 'content', 'price'])
        json_data = json.dumps(data)
    return HttpResponse(json_data , headers={'content-type': 'application/json'}) """