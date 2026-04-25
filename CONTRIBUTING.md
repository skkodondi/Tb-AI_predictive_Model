# Contributing to TB-AI Predictive Model

Thank you for your interest in contributing to this project! We appreciate all contributions, whether they're bug reports, feature suggestions, or pull requests.

## 📋 Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Report Bugs](#how-to-report-bugs)
- [How to Suggest Enhancements](#how-to-suggest-enhancements)
- [Pull Request Process](#pull-request-process)
- [Development Guidelines](#development-guidelines)
- [Commit Message Format](#commit-message-format)

---

## Code of Conduct

This project is committed to providing a welcoming and inclusive environment for all contributors. Please be respectful and constructive in all interactions.

---

## Getting Started

### Prerequisites
- Python 3.11+
- Git
- Virtual environment (venv or conda)

### Setup Development Environment

1. **Fork the repository** on GitHub

2. **Clone your fork locally:**
```bash
git clone https://github.com/YOUR-USERNAME/Tb-AI_predictive_Model.git
cd Tb-AI_predictive_Model
```

3. **Add upstream remote:**
```bash
git remote add upstream https://github.com/skkodondi/Tb-AI_predictive_Model.git
```

4. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

5. **Install dependencies:**
```bash
pip install -r requirements_minimal.txt
```

6. **Create a feature branch:**
```bash
git checkout -b feature/your-feature-name
```

---

## How to Report Bugs

### Before Submitting a Bug Report
- Check the [existing issues](https://github.com/skkodondi/Tb-AI_predictive_Model/issues) to avoid duplicates
- Test the latest version to confirm the bug still exists

### Submitting a Good Bug Report

Create an issue and provide:

1. **Clear title** - Briefly describe the issue
2. **Description** - Detailed explanation of the bug
3. **Steps to reproduce** - Exact steps to reproduce the issue
4. **Expected behavior** - What should happen
5. **Actual behavior** - What actually happens
6. **Environment**:
   - Python version
   - OS (Windows, macOS, Linux)
   - Relevant library versions
7. **Attachments** - Error messages, screenshots, or logs
8. **Additional context** - Any other relevant information

**Example:**
```
Title: Model prediction fails with latitude/longitude outside Kenya

Description: The /predict endpoint crashes when receiving coordinates outside Kenya boundaries

Steps to reproduce:
1. Send POST request to /predict with latitude=45.0, longitude=45.0
2. Observe the error

Expected: Should return "Outside Kenya" county
Actual: Server returns 500 error

Environment:
- Python 3.11
- Ubuntu 22.04
- Flask 2.3.3
```

---

## How to Suggest Enhancements

1. **Check existing issues** - Look for similar suggestions
2. **Open a new issue** with the tag `enhancement`
3. **Provide details:**
   - Current behavior
   - Proposed enhancement
   - Why this would be useful
   - Example use case

**Example:**
```
Title: Add support for multiple country datasets

Description: Currently, the model only supports Kenya. It would be valuable to add 
support for other East African countries like Uganda, Tanzania, and Ethiopia.

Why: This would make the model applicable across the region and help with 
comparative analysis of TB prevalence.

Proposed solution: Extend the GeoJSON data structure and create a country selector.
```

---

## Pull Request Process

### Before Starting
1. Open an issue for the change (unless it's a small fix)
2. Wait for feedback or approval
3. Create a branch from the latest `main` branch

### Making Changes
1. Make your changes in your feature branch
2. Follow the [Development Guidelines](#development-guidelines)
3. Test thoroughly
4. Update documentation if needed
5. Keep commits clean and logical

### Submitting a Pull Request

1. **Update your branch:**
```bash
git fetch upstream
git rebase upstream/main
```

2. **Push to your fork:**
```bash
git push origin feature/your-feature-name
```

3. **Create a Pull Request** on GitHub with:
   - **Clear title** describing the change
   - **Description** explaining:
     - What changes were made
     - Why they were made
     - How to test the changes
     - Link to related issue(s)
   - **Checklist:**
     - [ ] Code follows style guidelines
     - [ ] Tests added/updated
     - [ ] Documentation updated
     - [ ] No new warnings introduced

**PR Description Template:**
```markdown
## Description
Brief description of the changes

## Related Issue
Fixes #(issue number)

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing
- [ ] Unit tests added
- [ ] Manual testing completed
- [ ] Test results: (describe)

## Checklist
- [ ] My code follows the style guidelines
- [ ] I have performed a self-review
- [ ] I have updated the documentation
- [ ] No new warnings have been generated
```

---

## Development Guidelines

### Code Style
- Follow **PEP 8** style guide
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Maximum line length: 100 characters

### Example:
```python
def predict_tb_risk(latitude: float, longitude: float, features: dict) -> dict:
    """
    Predict TB risk for given coordinates.
    
    Args:
        latitude: Y-coordinate of the location
        longitude: X-coordinate of the location
        features: Dictionary of model features
        
    Returns:
        Dictionary containing:
            - prediction: Risk score (float)
            - risk_level: Risk category (Low/Medium/High)
            - county: Detected county name
    """
    # Implementation
    pass
```

### Testing
- Write unit tests for new functions
- Place tests in a `tests/` directory
- Run tests before submitting PR:
```bash
pytest tests/
```

### Documentation
- Update README.md for user-facing changes
- Add docstrings to all functions
- Update API documentation if endpoints change
- Comment complex logic clearly

### File Structure
```
Tb-AI_predictive_Model/
├── app.py
├── requirements.txt
├── requirements_minimal.txt
├── data/
├── model/
├── templates/
├── static/
├── tests/
├── .gitignore
├── .env.example
├── README.md
└── CONTRIBUTING.md
```

---

## Commit Message Format

Use clear, descriptive commit messages:

```
<type>: <subject>

<body>

<footer>
```

### Types
- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation
- **style**: Code style (no logic change)
- **refactor**: Code refactoring
- **perf**: Performance improvement
- **test**: Adding/updating tests
- **chore**: Maintenance tasks

### Examples
```
feat: Add support for multiple countries in predictions

fix: Handle edge case when coordinates are outside Kenya boundaries

docs: Update API documentation with new endpoints

refactor: Extract county detection logic into separate function
```

---

## Helpful Resources

- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [PEP 8 Style Guide](https://pep8.org/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [scikit-learn Documentation](https://scikit-learn.org/)

---

## Questions or Need Help?

- Check existing [issues](https://github.com/skkodondi/Tb-AI_predictive_Model/issues)
- Open a new issue with the `question` tag
- Contact the maintainer: [skkodondi](https://github.com/skkodondi)

---

## Recognition

Contributors will be recognized in:
- Commit history
- Project README (for significant contributions)
- Release notes

Thank you for contributing! 🎉
