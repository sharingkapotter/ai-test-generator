"""
AI Test Assistant - Simple version
Generates API test cases using AI and testing best practices
"""
import os
from anthropic import Anthropic
from dotenv import load_dotenv
from pathlib import Path

# Load API key from .env file
load_dotenv()


class TestAssistant:
    """Generates pytest test cases for API endpoints"""
    
    def __init__(self):
        """Initialize with API key"""
        api_key = os.getenv('ANTHROPIC_API_KEY')
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in .env file")
        
        self.client = Anthropic(api_key=api_key)
    
    def generate_api_tests(self, endpoint_description: str) -> str:
        """
        Generate pytest tests for an API endpoint
        
        Args:
            endpoint_description: Description of the API endpoint
            
        Returns:
            Generated pytest test code
        """
        prompt = f"""Generate pytest tests for this API endpoint:

{endpoint_description}

IMPORTANT - Apply these testing best practices:
1. Test happy path (200 OK responses)
2. Test validation (400 Bad Request for invalid data)
3. Test authentication (401 Unauthorized)
4. Test edge cases (empty strings, null values, special characters)
5. Test boundary conditions (min/max values)
6. Use pytest fixtures for setup
7. Use clear, descriptive test names
8. Add assertions for status code AND response data

Generate complete, runnable pytest code with proper imports."""

        # Call Claude AI
        response = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}]
        )
        
        # Extract the code from response
        test_code = response.content[0].text
        
        # Remove markdown formatting if present
        if "```python" in test_code:
            test_code = test_code.split("```python")[1].split("```")[0]
        elif "```" in test_code:
            test_code = test_code.split("```")[1].split("```")[0]
        
        return test_code.strip()
    
    def save_tests(self, test_code: str, filename: str = "test_api.py") -> str:
        """
        Save generated tests to a file
        
        Args:
            test_code: The pytest code to save
            filename: Name of the test file
            
        Returns:
            Path to saved file
        """
        # Create tests folder if it doesn't exist
        tests_dir = Path("tests")
        tests_dir.mkdir(exist_ok=True)
        
        # Save the file
        filepath = tests_dir / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(test_code)
        
        return str(filepath)


# Simple CLI interface
def main():
    """Main function - simple command line interface"""
    print("=" * 60)
    print("AI Test Assistant for API Testing")
    print("=" * 60)
    
    # Create the assistant
    assistant = TestAssistant()
    
    # Get API description from user
    print("\nDescribe your API endpoint:")
    print("(Include: method, URL, parameters, expected responses)")
    print("\nExample:")
    print("POST /api/users - Create a new user")
    print("Parameters: username (string), email (string), age (integer)")
    print("Returns: 201 Created with user object\n")
    
    description = input("Your API description: ")
    
    if not description.strip():
        print("Error: Please provide an API description")
        return
    
    # Generate tests
    print("\n Generating tests with AI...")
    test_code = assistant.generate_api_tests(description)
    
    # Save tests
    filename = input("\nTest filename (default: test_api.py): ").strip()
    if not filename:
        filename = "test_api.py"
    if not filename.startswith("test_"):
        filename = f"test_{filename}"
    if not filename.endswith(".py"):
        filename = f"{filename}.py"
    
    filepath = assistant.save_tests(test_code, filename)
    
    print(f"\nTests saved to: {filepath}")
    print(f"\nTo run the tests:")
    print(f"  pytest {filepath} -v")
    print("\n💡 Review and customize the tests as needed!")


if __name__ == "__main__":
    main()
