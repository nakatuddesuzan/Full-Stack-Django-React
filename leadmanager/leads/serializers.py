from rest_framework import serializers
from leadmanager.leads.models import Lead

# Lead serializer
class LeadSerializer(serializers.ModelSerializer):
    class meta:
        model = Lead
        fields = '__all__'
