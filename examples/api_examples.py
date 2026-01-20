"""
Sample API Endpoint Descriptions for Testing
These are examples you can use to generate tests
"""

# Example 1: Simple User Creation API
USER_CREATION_API = """
POST /api/v1/users
Creates a new user in the system

Request Body (JSON):
{
    "username": "string (required, 3-50 chars)",
    "email": "string (required, valid email format)",
    "age": "integer (optional, 18-120)",
    "role": "string (optional, one of: admin, user, guest)"
}

Success Response (201 Created):
{
    "user_id": "uuid",
    "username": "string",
    "email": "string",
    "created_at": "datetime"
}

Error Responses:
- 400: Invalid input (missing fields, invalid format)
- 409: User already exists (duplicate username/email)
- 401: Unauthorized (missing or invalid auth token)
"""

# Example 2: Product Search API
PRODUCT_SEARCH_API = """
GET /api/v1/products/search
Searches for products by various criteria

Query Parameters:
- q: search query (string, required)
- category: product category (string, optional)
- min_price: minimum price (float, optional)
- max_price: maximum price (float, optional)
- limit: results per page (integer, default 20, max 100)
- offset: pagination offset (integer, default 0)

Success Response (200 OK):
{
    "results": [array of product objects],
    "total": integer,
    "limit": integer,
    "offset": integer
}

Error Responses:
- 400: Invalid parameters (invalid price range, limit too high)
- 401: Unauthorized (missing API key)
- 429: Too many requests (rate limit exceeded)
"""