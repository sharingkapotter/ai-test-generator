 🤖 AI Test Assistant for API Testing

> An intelligent tool that generates comprehensive pytest test cases for API endpoints using AI, built by an SDET with 20 years of testing experience.

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Anthropic Claude](https://img.shields.io/badge/AI-Claude%20Sonnet%204-purple.svg)](https://www.anthropic.com/)

---

 📋 Table of Contents
- [Overview](overview)
- [Key Features](key-features)
- [Tech Stack](tech-stack)
- [Installation](installation)
- [Usage](usage)
- [Examples](examples)
- [Project Structure](project-structure)
- [How It Works](how-it-works)
- [Future Enhancements](future-enhancements)
- [Author](author)

---

 🎯 Overview

The Problem: Writing comprehensive API test cases is time-consuming. Tests often miss edge cases, error scenarios, and security validations.

The Solution: AI Test Assistant generates production-quality pytest test cases in seconds by combining AI capabilities with 20 years of testing best practices.

The Result: What takes 1-2 hours manually now takes 2 minutes, with better coverage.

---

 ✨ Key Features

- 🚀 Fast Generation: Create complete test suites in under 30 seconds
- 🎯 Comprehensive Coverage: Automatically includes happy path, error cases, edge cases, and boundary conditions
- 🔒 Security-First: Tests authentication, authorization, and input validation
- 📝 Clean Code: Generates pytest-compliant code with proper fixtures and assertions
- 🛠️ Customizable: Embedding testing best practices based on 20 years of SDET experience
- 💡 Learning Tool: See examples of professional test case patterns

---

 🔧 Tech Stack

| Technology | Purpose | Version |
|------------|---------|---------|
| Python | Core programming language | 3.11+ |
| Anthropic Claude API | AI test generation | Sonnet 4 |
| pytest | Testing framework | 8.3.4 |
| python-dotenv | Environment management | 1.0.1 |

---

 📥 Installation

 Prerequisites
- Python 3.11 or higher
- Anthropic API key ([Get one free](https://console.anthropic.com/))
- pip (Python package manager)

 Setup Steps

1. Clone the repository
```bash
git clone https://github.com/sharingkapotter/ai-test-generator
cd ai-test-assistant
```

2. Create virtual environment
```bash
python -m venv venv

 On Windows:
venv\Scripts\activate

 On Mac/Linux:
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure API key

Create a `.env` file in the project root:
```
ANTHROPIC_API_KEY=your-api-key-here
```

5. Verify installation
```bash
python src\test_assistant.py
```

---

 🚀 Usage

 Basic Usage

1. Run the assistant
```bash
python src\test_assistant.py
```

2. Describe your API endpoint

Example input:
```
POST /api/users - Create a new user
Parameters: username (string, required), email (string, required), age (integer, optional)
Returns: 201 Created with user object on success
Error responses: 400 for invalid data, 409 for duplicate user
```

3. Review generated tests

The tool creates a test file in the `tests/` directory.

4. Run the tests
```bash
pytest tests/test_api.py -v
```

 Advanced Usage

Use example templates:
```bash
 See pre-built examples
notepad examples\api_examples.py
```

Customize test naming:
```bash
python src\test_assistant.py
 When prompted for filename: test_user_api.py
```

---

 💡 Examples

 Example 1: Simple User API

Input:
```
POST /api/users
Body: {username: string, email: string}
Returns: 201 on success, 400 on invalid input
```

Generated Tests Include:
- ✅ Successful user creation (201)
- ✅ Missing required fields (400)
- ✅ Invalid email format (400)
- ✅ Duplicate username (409)
- ✅ SQL injection attempts
- ✅ XSS in username field
- ✅ Boundary testing (username length)

 Example 2: Product Search API

See `examples/api_examples.py` for more comprehensive examples.

---

 📁 Project Structure
```
ai-test-assistant/
│
├── src/
│   ├── __init__.py
│   └── test_assistant.py       Main application code (150 lines)
│
├── examples/
│   └── api_examples.py         Sample API descriptions
│
├── tests/
│   └── __init__.py             Generated tests go here
│
├── .env                        API keys (not committed)
├── .gitignore                  Git ignore rules
├── requirements.txt            Python dependencies
└── README.md                   This file
```

---

 🔍 How It Works

 Architecture
```
User Input → Test Assistant → Claude AI → Generated Tests → pytest
```

 Workflow

1. User describes API endpoint (method, parameters, responses)
2. Test Assistant constructs intelligent prompt with testing best practices
3. Claude AI generates pytest code following the specifications
4. Code is cleaned and saved to test file
5. User runs tests with pytest

 Key Design Decisions

Why Claude Sonnet 4?
- Fast response times (< 5 seconds)
- High-quality code generation
- Cost-effective for this use case

Why pytest?
- Industry standard for Python testing
- Rich fixture system
- Excellent reporting
- Widely used in professional environments

Why 150 lines of code?
- Maintainability - easy to understand and modify
- Focus - does one thing exceptionally well
- Teachability - great for demonstrating to others

---

 🚀 Future Enhancements

 Planned Features

 1. Automatic Test Updates
Status: Planned for v2.0

When application code changes, automatically update relevant tests.

Implementation approach:
- Git integration to monitor file changes
- Diff analysis to understand what changed
- Intelligent updates preserving manual customizations

Business value: Test maintenance is 60% of QA effort. This reduces it dramatically.

 2. Multiple Framework Support
- unittest
- nose2
- Robot Framework

 3. Advanced Features
- Test coverage analysis
- CI/CD pipeline integration (GitHub Actions, Jenkins)
- GraphQL and gRPC support
- Custom test templates library

---

 📊 Performance & Cost

| Metric | Value |
|--------|-------|
| Average generation time | 5-10 seconds |
| Tests per API description | 5-10 test functions |
| Cost per generation | $0.01 - $0.03 |
| Lines of test code generated | 50-150 lines |

---

 🎓 What I Learned

Building this project taught me:

- Prompt engineering: How to embed domain expertise in AI prompts
- AI integration: Working with Claude API effectively
- Tool design: Creating developer-friendly CLI tools
- Best practices: Codifying 20 years of testing knowledge

---

 🤝 Contributing

This is a portfolio project, but suggestions are welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

 📝 License

MIT License - Free to use for learning and professional development.

---

 👨‍💻 Author

Sunil
- 🔧 SDET with 20 years of experience
- 💼 Expertise: Test Automation, API Testing, Performance Testing, Security Testing
- 📧 Email: sunilsoftwareqa@gmail.com
- 💼 LinkedIn: https://www.linkedin.com/in/sunil-sodhi-30901a81/
- 🐙 GitHub: https://github.com/sharingkapotter

---

 🙏 Acknowledgments

- Built with [Anthropic Claude](https://www.anthropic.com/)
- Testing framework: [pytest](https://pytest.org/)
- Inspired by the need for faster, better test coverage
