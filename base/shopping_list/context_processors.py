# myapp/context_processors.py
# To make the households available in the base template for the dropdown menu, you need to use a context processor or include the data in each view. Here, we’ll use a simple context processor.
from .models import Household

def households(request):
    return {'households': Household.objects.all()}