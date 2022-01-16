"""CRUD app views"""

# Django
from django.core.exceptions import ValidationError, ObjectDoesNotExist

# DRF
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers

# Flink
from .serializers import CompanySerializer
from .models import Company


@api_view(['GET'])
def apiOverview(request):
    """Returns the available API Url's in the project and a little description
    of how to use them

    Returns:
        API Url's: Description and available method [JSON]
    """
    api_urls = {
        'List': '/company-api/   GET method',
        'Detail View': '/company-api/detail/<str:pk>   GET method',
        'Create': '/company-api/create/   POST method',
        'Update': 'company-api/update/<str:id>   PATCH method',
        'Delete': '/company-api/delete/<str:pk>   DELETE method',
    }

    return Response(api_urls)


@api_view(['GET'])
def companyList(request):
    """Get the total company list

    Returns:
        Company objects: Total Company objects [JSON]
    """
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def companyDetail(request, id):
    """Get a company detail

    Args:
        id: Path Variable [UUID4]

    Returns:
        Company object: Company object [JSON]
    """
    try:
        company = Company.objects.get(id=id)
        serializer = CompanySerializer(company, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response(
            {"error": f"The Company ID {id} does not exist."},
            status=status.HTTP_404_NOT_FOUND
        )
    except ValidationError:
        return Response(
            {"error": f"The Company ID {id} does not exist."},
            status=status.HTTP_404_NOT_FOUND
        )


@api_view(['POST'])
def companyCreate(request):
    """Create a company instance

    Args:
        data: Company object information [JSON]

    Returns:
        Company object: Company object [JSON]
    """
    try:
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
    except serializers.ValidationError as e:
        return Response(
            {"error": f"{e.get_codes()}"},
            status=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        return Response(
            {"error": f"{e}"},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['PATCH'])
def companyUpdate(request, id):
    """Update a company instance

    Args:
        id: Path Variable [UUID4]
        data: Company object information [JSON]

    Returns:
        Company object: Company object [JSON]
    """
    try:
        company = Company.objects.get(id=id)
        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    except serializers.ValidationError as e:
        return Response(
            {"error": f"{e.get_codes()}"},
            status=status.HTTP_400_BAD_REQUEST
        )
    except ValidationError:
        return Response(
            {"error": "The Company ID does not exist."},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response(
            {"error": f"{e}"},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['DELETE'])
def companyDelete(request, id):
    """Delete a company instance

    Args:
        id: Path Variable [UUID4]

    Returns:
        message: Result of the function [JSON]
    """
    try:
        company = Company.objects.get(id=id)
        company.delete()
        return Response(
            {"message": f"Company with id {id} succesfully deleted"},
            status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response(
            {"error": f"{e}"},
            status=status.HTTP_404_NOT_FOUND
        )
