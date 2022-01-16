This API has 5 different paths and functions:

# Api Overview

Returns the available API Url's in the project and a little description of how to use them.

**URL** : `''`

**Method** : `GET`

**Auth required** : `NO`

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "List": "/company-api/   GET method",
    "Detail View": "/company-api/detail/<str:pk>   GET method",
    "Create": "/company-api/create/   POST method",
    "Update": "company-api/update/<str:id>   PATCH method",
    "Delete": "/company-api/delete/<str:pk>   DELETE method"
}
```

# List

Used to display all companies information on the database.

**URL** : `'/company-api/'`

**Method** : `GET`

**Auth required** : `NO`

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "List": "/company-api/   GET method",
    "Detail View": "/company-api/detail/<str:pk>   GET method",
    "Create": "/company-api/create/   POST method",
    "Update": "company-api/update/<str:id>   PATCH method",
    "Delete": "/company-api/delete/<str:pk>   DELETE method"
}
```

# Detail

Used to return the detail of an specific company object on the database.

**URL** : `/company-api/detail/<str:pk>` where pk it's the uuid pk of the company object

**Method** : `GET`

**Auth required** : NO

**Request example**

```path
/company-api/detail/575ae0cf-a1f4-4f95-9bee-fb6876a60e00
```

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "id": "575ae0cf-a1f4-4f95-9bee-fb6876a60e00",
    "name": "Google",
    "description": "Technology Company",
    "symbol": "GOOG",
    "market_values": "[7, 23, 63, 1, 49, 89, 16, 19, 99, 98, 84, 86, 58, 61, 69, 94, 14, 3, 90, 66, 82, 68, 46, 75, 59, 64, 91, 17, 9, 50, 67, 81, 20, 35, 32, 6, 26, 24, 22, 21, 43, 85, 37, 79, 45, 30, 72, 51, 36, 18]"
}
```

## Error Response

**Code** : `404 NOT FOUND`

**Content** :

```json
{
    "error": "The Company ID 575ae0cf-a1f4-4f95-9bee-fb6876a60e00as does not exist."
}
```

# Create

Used to create a new company object on the database.

**URL** : `/company-api/create/`

**Method** : `POST`

**Auth required** : NO

**Data constraints**

```json
{
  "name": "[Company name (Max 50 characters)]",
  "description": "[Company description (Max 100 characters)]",
  "symbol": "[valid New York stock symbol of a company (Max 10 characters)]"
}
```

**Data example**

```json
{
  "name": "Tesla Inc.",
  "description": "Electric Car Company",
  "symbol": "TSLA"
}
```

## Success Response

**Code** : `201 CREATED`

**Content example**

```json
{
    "id": "c455802e-ac8d-4ce9-95fb-4b6d48031db6",
    "name": "Tesla Inc.",
    "description": "Electric Car Company",
    "symbol": "TSLA"
    "market_values": "[50, 20, 82, 35, 64, 24, 42, 72, 38, 32, 61, 28, 19, 43, 45, 67, 95, 85, 12, 90, 78, 56, 69, 26, 36, 94, 59, 27, 87, 21, 33, 86, 51, 8, 14, 88, 80, 60, 70, 89, 9, 23, 53, 3, 30, 76, 63, 62, 81, 91]"
}
```

## Error Response

**Conditions**
* `name` field has more than 50 characters.
* `description` field has more than 100 characters.
* `symbol` field has more than 10 characters.
* `symbol` field is not a valid New York Stock.

**Code** : `400 BAD REQUEST`

**Content** :

For name max_length validator
```json
{
    "error": "{'name': ['max_length']}"
}
```
For description max_length validator
```json
{
    "error": "{'description': ['max_length']}"
}
```
For symbol not found in stock API
```json
{
    "error": "{'non_field_errors': ['invalid']}"
}
```
For symbol max_length
```json
{
    "error": "{'symbol': ['max_length']}"
}
```

# Update

Used to update an existing company object on the database.

**URL** : `/company-api/update/<str:id>`

**Method** : `PATCH`

**Auth required** : NO

**Data constraints**

```json
{
  "name": "[Company name (Max 50 characters)]",
  "description": "[Company description (Max 100 characters)]",
  "symbol": "[valid New York stock symbol of a company (Max 10 characters)]"
}
```
**Request Example**

```path
/company-api/update/575ae0cf-a1f4-4f95-9bee-fb6876a60e00
```

**Data example**

```json
{
  "name": "Tesla Inc.",
  "description": "Electric Car Company",
  "symbol": "TSLA"
}
```

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "id": "575ae0cf-a1f4-4f95-9bee-fb6876a60e00",
    "name": "Tesla Inc.",
    "description": "Electric Car Company",
    "symbol": "TSLA"
    "market_values": "[50, 20, 82, 35, 64, 24, 42, 72, 38, 32, 61, 28, 19, 43, 45, 67, 95, 85, 12, 90, 78, 56, 69, 26, 36, 94, 59, 27, 87, 21, 33, 86, 51, 8, 14, 88, 80, 60, 70, 89, 9, 23, 53, 3, 30, 76, 63, 62, 81, 91]"
}
```

## Error Response

**Conditions**
* `name` field has more than 50 characters.
* `description` field has more than 100 characters.
* `symbol` field has more than 10 characters.
* `symbol` field is not a valid New York Stock.

**Code** : `400 BAD REQUEST`

**Content** :

For name max_length validator
```json
{
    "error": "{'name': ['max_length']}"
}
```
For description max_length validator
```json
{
    "error": "{'description': ['max_length']}"
}
```
For symbol not found in stock API
```json
{
    "error": "{'non_field_errors': ['invalid']}"
}
```
For symbol max_length
```json
{
    "error": "{'symbol': ['max_length']}"
}
```
For incorrect id
```json
{
    "error": "The Company ID does not exist."
}
```
For missing field
```json
{
    "error": "{'name': ['required'], 'description': ['required'], 'symbol': ['required']}"
}
```

# Delete

Used to delete an existing company object on the database.

**URL** : `/company-api/delete/<str:id>`

**Method** : `DELETE`

**Auth required** : NO

**Request Example**

```path
/company-api/delete/575ae0cf-a1f4-4f95-9bee-fb6876a60e00
```

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "message": "Company with id 575ae0cf-a1f4-4f95-9bee-fb6876a60e00 succesfully deleted"
}
```

## Error Response

**Code** : `400 BAD REQUEST`

**Content** :

For incorrect id
```json
{
    "error": "Company matching query does not exist."
}
```
