# Contributing to DSA Repository

Thank you for your interest in contributing to this Data Structures and Algorithms repository! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Issues

- Use [GitHub Issues](../../issues) to report bugs or request features
- Provide clear and descriptive information
- Include steps to reproduce the issue
- Add screenshots if applicable

### Making Changes

1. **Fork the repository**
   ```bash
   # Fork the repository on GitHub, then clone your fork
   git clone https://github.com/YOUR_USERNAME/DSA.git
   cd DSA
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/issue-description
   ```

3. **Make your changes**
   - Follow the existing code style and structure
   - Add comments for complex algorithms
   - Include time/space complexity analysis
   - Test your code thoroughly

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: Brief description of your changes"
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**
   - Go to your fork on GitHub
   - Click "New Pull Request"
   - Provide a clear description of your changes
   - Link any related issues

## 📝 Contribution Guidelines

### What to Contribute

We welcome contributions in the following areas:

- **New algorithms and data structures**
- **Optimized solutions** for existing problems
- **Additional language implementations** (C++, Java, Python)
- **Bug fixes** and error corrections
- **Documentation improvements**
- **Practice problems** with solutions
- **Templates** for competitive programming
- **Theory notes** and explanations

### Code Style Guidelines

#### General Rules
- Use meaningful variable and function names
- Add proper comments for complex logic
- Include time and space complexity in comments
- Follow language-specific conventions
- Test with multiple test cases

#### C++ Guidelines
```cpp
// Use proper naming conventions
int binarySearch(const vector<int>& arr, int target) {
    // Time Complexity: O(log n)
    // Space Complexity: O(1)
    int left = 0, right = arr.size() - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        // ... implementation
    }
    return -1;
}
```

#### Java Guidelines
```java
// Use proper naming conventions and documentation
/**
 * Performs binary search on a sorted array.
 * Time Complexity: O(log n)
 * Space Complexity: O(1)
 */
public int binarySearch(int[] arr, int target) {
    int left = 0, right = arr.length - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        // ... implementation
    }
    return -1;
}
```

#### Python Guidelines
```python
def binary_search(arr, target):
    """
    Performs binary search on a sorted array.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        # ... implementation
    
    return -1
```

### File Organization

- Follow the existing directory structure
- Use descriptive file names
- Group related files together
- Include README files in subdirectories

### Documentation Standards

- Use clear and concise language
- Include examples and usage instructions
- Add complexity analysis
- Provide edge case handling

## 🧪 Testing

### Testing Guidelines
- Test your code with multiple test cases
- Include edge cases (empty input, single element, etc.)
- Verify time and space complexity
- Ensure code works across all supported languages

### Test Cases to Consider
- Normal cases
- Edge cases (empty, single element, maximum/minimum values)
- Boundary conditions
- Invalid inputs

## 📋 Pull Request Process

### Before Submitting
- [ ] Ensure your code follows the style guidelines
- [ ] Add tests for new functionality
- [ ] Update documentation if needed
- [ ] Verify all tests pass
- [ ] Check for any syntax errors

### Pull Request Template
```markdown
## Description
Brief description of changes made.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code optimization

## Testing
- [ ] Added test cases
- [ ] All tests pass
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
```

## 🚀 Getting Started

### Development Environment Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/DSA.git
   cd DSA
   ```

2. **Set up your development environment**
   - Install required compilers/interpreters
   - Set up your preferred IDE
   - Configure git settings

3. **Verify setup**
   ```bash
   # Test C++ compiler
   g++ --version
   
   # Test Java compiler
   javac -version
   
   # Test Python interpreter
   python --version
   ```

## 📞 Getting Help

- **Issues**: Report bugs or request features
- **Discussions**: Ask questions and share insights
- **Pull Requests**: Review and contribute code

## 🙏 Recognition

Contributors will be recognized in:
- Contributors section in README
- Release notes for significant contributions
- Special recognition for major features

## 📄 License

By contributing to this repository, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to this DSA learning repository! Your contributions help make DSA education accessible to everyone. 🚀
