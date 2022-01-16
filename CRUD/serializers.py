"""CRUD app serializers"""

# Utils
import requests

# DRF
from rest_framework import serializers

# Flink
from .models import Company
from flink_test.settings import YAHOO_API_HEADERS, YAHOO_API_URL


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
        url = YAHOO_API_URL
        querystring = {
            "symbol": data["symbol"],
            "region": "US"
        }
        headers = YAHOO_API_HEADERS
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
