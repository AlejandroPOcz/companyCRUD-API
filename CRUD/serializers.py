"""CRUD app serializers"""

# Utils
import requests

# DRF
from rest_framework import serializers

# Flink
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

    def validate(self, data):
        """Modification in the CompanySerializer validation in order to map
        and raise the different possible errors

        Args:
            data [JSON]: Company object information (if needed)

        Raises:
            ValidationError
        """
        # Name Validation
        if len(data["name"]) > 50:
            raise serializers.ValidationError()

        # Description Validation
        elif len(data["description"]) > 100:
            raise serializers.ValidationError()

        # Symbol Validation
        url = "https://yh-finance.p.rapidapi.com/stock/v2/get-profile"
        querystring = {
            "symbol": data["symbol"],
            "region": "US"
        }
        headers = {
            'x-rapidapi-host': "yh-finance.p.rapidapi.com",
            'x-rapidapi-key': "ef5e61af6fmshb1c542323fac8bbp1039ebjsn76388d41ff10"
            }
        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=querystring
        )

        if response.status_code != 200:
            raise serializers.ValidationError()
        elif len(data["symbol"]) > 10:
            raise serializers.ValidationError()

        return data
