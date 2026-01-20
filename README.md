# 🤖 AI Test Assistant for API Testing

A simple, powerful tool that uses AI to generate comprehensive pytest test cases for API endpoints.

## What It Does

Describe your API endpoint → AI generates professional pytest tests → Run them immediately

## Quick Start

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Add your API key to `.env`:
```
ANTHROPIC_API_KEY=your-key-here
```

3. Run the assistant:
```
python src\test_assistant.py
```

4. Describe your API when prompted

5. Run the generated tests:
```
pytest tests\test_api.py -v
```

## Author

Built by Sunil - SDET with 20 years of experience in test automation, API testing, and performance testing.