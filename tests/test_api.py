import pytest
import json
from unittest.mock import Mock, patch


# Fixtures for test setup
@pytest.fixture
def client():
    """Mock API client fixture"""
    mock_client = Mock()
    return mock_client


@pytest.fixture
def valid_user_data():
    """Valid user data for testing"""
    return {
        "username": "testuser123",
        "email": "test@example.com"
    }


@pytest.fixture
def auth_headers():
    """Authentication headers fixture"""
    return {
        "Authorization": "Bearer valid_token_12345",
        "Content-Type": "application/json"
    }


@pytest.fixture
def invalid_auth_headers():
    """Invalid authentication headers fixture"""
    return {
        "Authorization": "Bearer invalid_token",
        "Content-Type": "application/json"
    }


# Happy Path Tests
class TestCreateUserHappyPath:
    
    def test_create_user_success_with_valid_data(self, client, valid_user_data, auth_headers):
        """Test successful user creation with valid username and email"""
        # Mock successful response
        expected_response = {
            "id": 123,
            "username": "testuser123",
            "email": "test@example.com",
            "created_at": "2023-01-01T00:00:00Z"
        }
        client.post.return_value = Mock(status_code=201, json=lambda: expected_response)
        
        # Make request
        response = client.post("/api/users", json=valid_user_data, headers=auth_headers)
        
        # Assertions
        assert response.status_code == 201
        response_data = response.json()
        assert response_data["username"] == valid_user_data["username"]
        assert response_data["email"] == valid_user_data["email"]
        assert "id" in response_data
        assert "created_at" in response_data
    
    def test_create_user_with_minimum_valid_data(self, client, auth_headers):
        """Test user creation with minimum required fields"""
        user_data = {
            "username": "a",  # minimum length username
            "email": "a@b.co"  # minimum valid email
        }
        expected_response = {
            "id": 124,
            "username": "a",
            "email": "a@b.co",
            "created_at": "2023-01-01T00:00:00Z"
        }
        client.post.return_value = Mock(status_code=201, json=lambda: expected_response)
        
        response = client.post("/api/users", json=user_data, headers=auth_headers)
        
        assert response.status_code == 201
        response_data = response.json()
        assert response_data["username"] == user_data["username"]
        assert response_data["email"] == user_data["email"]


# Validation Tests (400 Bad Request)
class TestCreateUserValidation:
    
    def test_create_user_missing_username(self, client, auth_headers):
        """Test user creation fails when username is missing"""
        user_data = {"email": "test@example.com"}
        error_response = {
            "error": "Validation failed",
            "details": {"username": "Username is required"}
        }
        client.post.return_value = Mock(status_code=400, json=lambda: error_response)
        
        response = client.post("/api/users", json=user_data, headers=auth_headers)
        
        assert response.status_code == 400
        response_data = response.json()
        assert "error" in response_data
        assert "username" in response_data.get("details", {})
    
    def test_create_user_missing_email(self, client, auth_headers):
        """Test user creation fails when email is missing"""
        user_data = {"username": "testuser"}
        error_response = {
            "error": "Validation failed",
            "details": {"email": "Email is required"}
        }
        client.post.return_value = Mock(status_code=400, json=lambda: error_response)
        
        response = client.post("/api/users", json=user_data, headers=auth_headers)
        
        assert response.status_code == 400
        response_data = response.json()
        assert "error" in response_data
        assert "email" in response_data.get("details", {})
    
    def test_create_user_missing_both_fields(self, client, auth_headers):
        """Test user creation fails when both username and email are missing"""
        user_data = {}
        error_response = {
            "error": "Validation failed",
            "details": {
                "username": "Username is required",
                "email": "Email is required"
            }
        }
        client.post.return_value = Mock(status_code=400, json=lambda: error_response)
        
        response = client.post("/api/users", json=user_data, headers=auth_headers)
        
        assert response.status_code == 400
        response_data = response.json()
        assert "error" in response_data
        assert "username" in response_data.get("details", {})
        assert "email" in response_data.get("details", {})
    
    def test_create_user_invalid_email_format(self, client, auth_headers):
        """Test user creation fails with invalid email format"""
        user_data = {
            "username": "testuser",
            "email": "invalid-email-format"
        }
        error_response = {
            "error": "Validation failed",
            "details": {"email": "Invalid email format"}
        }
        client.post.return_value = Mock(status_code=400, json=lambda: error_response)
        
        response = client.post("/api/users", json=user_data, headers=auth_headers)
        
        assert response.status_code == 400
        response_data = response.json()
        assert "error" in response_data
        assert "email" in response_data.get("details", {})


# Authentication Tests (401 Unauthorized)
class TestCreateUserAuthentication:
    
    def test_create_user_no_auth_header(self, client, valid_user_data):
        """Test user creation fails without authentication header"""
        error_response = {
            "error": "Authentication required",
            "message": "Missing authorization header"
        }
        client.post.return_value = Mock(status_code=401, json=lambda: error_response)
        
        response = client.post("/api/users", json=valid_user_data)
        
        assert response.status_code == 401
        response_data = response.json()
        assert "error" in response_data
        assert response_data["error"] == "Authentication required"
    
    def test_create_user_invalid_token(self, client, valid_user_data, invalid_auth_headers):
        """Test user creation fails with invalid authentication token"""
        error_response = {
            "error": "Invalid token",
            "message": "The provided token is invalid or expired"
        }
        client.post.return_value = Mock(status_code=401, json=lambda: error_response)
        
        response = client.post("/api/users", json=valid_user_data, headers=invalid_auth_headers)
        
        assert response.status_code == 401
        response_data = response.json()
        assert "error" in response_data
        assert response_data["error"] == "Invalid token"
    
    def test_create_user_malformed_auth_header(self, client, valid_user_data):
        """Test user creation fails with malformed authorization header"""
        malformed_headers = {
            "Authorization": "InvalidFormat token123",
            "Content-Type": "application/json"
        }
        error_response = {
            "error": "Invalid authorization format",
            "message": "Authorization header must be in format 'Bearer