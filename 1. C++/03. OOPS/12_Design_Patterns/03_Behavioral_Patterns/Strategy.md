# Strategy Pattern in C++ - Complete Guide

## 📖 Overview

The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. It lets the algorithm vary independently from clients that use it. This pattern is particularly useful when you have multiple ways to perform an operation and want to choose the appropriate one at runtime.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Strategy** | Interface for all supported algorithms |
| **Concrete Strategy** | Implements specific algorithm |
| **Context** | Maintains reference to a Strategy object |
| **Client** | Selects and configures the Strategy |

---

## 1. **Basic Strategy Pattern**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <algorithm>
using namespace std;

// Strategy interface
class ISortStrategy {
public:
    virtual void sort(vector<int>& data) = 0;
    virtual ~ISortStrategy() = default;
};

// Concrete Strategy 1: Bubble Sort
class BubbleSort : public ISortStrategy {
public:
    void sort(vector<int>& data) override {
        cout << "Using Bubble Sort: ";
        for (size_t i = 0; i < data.size(); i++) {
            for (size_t j = 0; j < data.size() - i - 1; j++) {
                if (data[j] > data[j + 1]) {
                    swap(data[j], data[j + 1]);
                }
            }
        }
        print(data);
    }
    
private:
    void print(const vector<int>& data) {
        for (int val : data) cout << val << " ";
        cout << endl;
    }
};

// Concrete Strategy 2: Quick Sort
class QuickSort : public ISortStrategy {
public:
    void sort(vector<int>& data) override {
        cout << "Using Quick Sort: ";
        quickSort(data, 0, data.size() - 1);
        print(data);
    }
    
private:
    void quickSort(vector<int>& data, int left, int right) {
        if (left < right) {
            int pivot = partition(data, left, right);
            quickSort(data, left, pivot - 1);
            quickSort(data, pivot + 1, right);
        }
    }
    
    int partition(vector<int>& data, int left, int right) {
        int pivot = data[right];
        int i = left - 1;
        for (int j = left; j < right; j++) {
            if (data[j] <= pivot) {
                i++;
                swap(data[i], data[j]);
            }
        }
        swap(data[i + 1], data[right]);
        return i + 1;
    }
    
    void print(const vector<int>& data) {
        for (int val : data) cout << val << " ";
        cout << endl;
    }
};

// Concrete Strategy 3: Merge Sort
class MergeSort : public ISortStrategy {
public:
    void sort(vector<int>& data) override {
        cout << "Using Merge Sort: ";
        mergeSort(data, 0, data.size() - 1);
        print(data);
    }
    
private:
    void mergeSort(vector<int>& data, int left, int right) {
        if (left < right) {
            int mid = left + (right - left) / 2;
            mergeSort(data, left, mid);
            mergeSort(data, mid + 1, right);
            merge(data, left, mid, right);
        }
    }
    
    void merge(vector<int>& data, int left, int mid, int right) {
        vector<int> temp(right - left + 1);
        int i = left, j = mid + 1, k = 0;
        
        while (i <= mid && j <= right) {
            if (data[i] <= data[j]) temp[k++] = data[i++];
            else temp[k++] = data[j++];
        }
        
        while (i <= mid) temp[k++] = data[i++];
        while (j <= right) temp[k++] = data[j++];
        
        for (int i = 0; i < temp.size(); i++) {
            data[left + i] = temp[i];
        }
    }
    
    void print(const vector<int>& data) {
        for (int val : data) cout << val << " ";
        cout << endl;
    }
};

// Context
class Sorter {
private:
    unique_ptr<ISortStrategy> strategy;
    
public:
    void setStrategy(ISortStrategy* s) {
        strategy.reset(s);
    }
    
    void sort(vector<int>& data) {
        if (strategy) {
            strategy->sort(data);
        } else {
            cout << "No strategy set!" << endl;
        }
    }
};

int main() {
    cout << "=== Basic Strategy Pattern ===" << endl;
    
    Sorter sorter;
    vector<int> data = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    
    cout << "\nOriginal array: ";
    for (int val : data) cout << val << " ";
    cout << endl;
    
    cout << "\n1. Using Bubble Sort:" << endl;
    vector<int> data1 = data;
    sorter.setStrategy(new BubbleSort());
    sorter.sort(data1);
    
    cout << "\n2. Using Quick Sort:" << endl;
    vector<int> data2 = data;
    sorter.setStrategy(new QuickSort());
    sorter.sort(data2);
    
    cout << "\n3. Using Merge Sort:" << endl;
    vector<int> data3 = data;
    sorter.setStrategy(new MergeSort());
    sorter.sort(data3);
    
    return 0;
}
```

**Output:**
```
=== Basic Strategy Pattern ===

Original array: 5 2 8 1 9 3 7 4 6 

1. Using Bubble Sort:
Using Bubble Sort: 1 2 3 4 5 6 7 8 9 

2. Using Quick Sort:
Using Quick Sort: 1 2 3 4 5 6 7 8 9 

3. Using Merge Sort:
Using Merge Sort: 1 2 3 4 5 6 7 8 9 
```

---

## 2. **Strategy with Lambda Functions**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <functional>
#include <cmath>
using namespace std;

class Calculator {
private:
    function<double(double, double)> operation;
    
public:
    void setOperation(function<double(double, double)> op) {
        operation = op;
    }
    
    double compute(double a, double b) {
        if (operation) {
            return operation(a, b);
        }
        return 0;
    }
};

class PaymentProcessor {
private:
    function<void(double)> paymentStrategy;
    
public:
    void setPaymentStrategy(function<void(double)> strategy) {
        paymentStrategy = strategy;
    }
    
    void processPayment(double amount) {
        if (paymentStrategy) {
            paymentStrategy(amount);
        } else {
            cout << "No payment method selected!" << endl;
        }
    }
};

int main() {
    cout << "=== Strategy with Lambda Functions ===" << endl;
    
    cout << "\n1. Calculator with different operations:" << endl;
    Calculator calc;
    
    calc.setOperation([](double a, double b) { return a + b; });
    cout << "Addition: 10 + 5 = " << calc.compute(10, 5) << endl;
    
    calc.setOperation([](double a, double b) { return a - b; });
    cout << "Subtraction: 10 - 5 = " << calc.compute(10, 5) << endl;
    
    calc.setOperation([](double a, double b) { return a * b; });
    cout << "Multiplication: 10 * 5 = " << calc.compute(10, 5) << endl;
    
    calc.setOperation([](double a, double b) { return a / b; });
    cout << "Division: 10 / 5 = " << calc.compute(10, 5) << endl;
    
    calc.setOperation([](double a, double b) { return pow(a, b); });
    cout << "Power: 2 ^ 3 = " << calc.compute(2, 3) << endl;
    
    cout << "\n2. Payment processing with different methods:" << endl;
    PaymentProcessor processor;
    
    processor.setPaymentStrategy([](double amount) {
        cout << "Processing credit card payment: $" << amount << endl;
    });
    processor.processPayment(100.0);
    
    processor.setPaymentStrategy([](double amount) {
        cout << "Processing PayPal payment: $" << amount << endl;
    });
    processor.processPayment(75.5);
    
    processor.setPaymentStrategy([](double amount) {
        cout << "Processing Bitcoin payment: $" << amount << endl;
    });
    processor.processPayment(50.0);
    
    return 0;
}
```

---

## 3. **Strategy with State (Compression Strategies)**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <chrono>
#include <sstream>
#include <iomanip>
using namespace std;

// Strategy interface
class ICompressionStrategy {
public:
    virtual string compress(const string& data) = 0;
    virtual string decompress(const string& data) = 0;
    virtual ~ICompressionStrategy() = default;
};

// Concrete Strategy 1: Run-Length Encoding
class RLECompression : public ICompressionStrategy {
public:
    string compress(const string& data) override {
        string result;
        int count = 1;
        
        for (size_t i = 0; i < data.length(); i++) {
            if (i + 1 < data.length() && data[i] == data[i + 1]) {
                count++;
            } else {
                result += data[i] + to_string(count);
                count = 1;
            }
        }
        
        cout << "RLE: Compressed " << data.length() << " to " << result.length() << " bytes" << endl;
        return result;
    }
    
    string decompress(const string& data) override {
        string result;
        for (size_t i = 0; i < data.length(); i++) {
            char c = data[i];
            i++;
            int count = 0;
            while (i < data.length() && isdigit(data[i])) {
                count = count * 10 + (data[i] - '0');
                i++;
            }
            i--;
            result.append(count, c);
        }
        return result;
    }
};

// Concrete Strategy 2: Simple Dictionary Compression
class DictionaryCompression : public ICompressionStrategy {
private:
    vector<pair<string, string>> dictionary;
    
    string compressWord(const string& word) {
        for (const auto& entry : dictionary) {
            if (entry.first == word) {
                return entry.second;
            }
        }
        string code = "[" + to_string(dictionary.size()) + "]";
        dictionary.push_back({word, code});
        return code;
    }
    
public:
    string compress(const string& data) override {
        dictionary.clear();
        stringstream ss(data);
        string word;
        string result;
        
        while (ss >> word) {
            result += compressWord(word) + " ";
        }
        
        cout << "Dictionary: Created " << dictionary.size() << " entries" << endl;
        return result;
    }
    
    string decompress(const string& data) override {
        stringstream ss(data);
        string token;
        string result;
        
        while (ss >> token) {
            if (token[0] == '[' && token.back() == ']') {
                int index = stoi(token.substr(1, token.length() - 2));
                if (index < dictionary.size()) {
                    result += dictionary[index].first + " ";
                }
            } else {
                result += token + " ";
            }
        }
        
        return result;
    }
};

// Context
class Compressor {
private:
    unique_ptr<ICompressionStrategy> strategy;
    
public:
    void setStrategy(ICompressionStrategy* s) {
        strategy.reset(s);
    }
    
    string compress(const string& data) {
        if (strategy) {
            return strategy->compress(data);
        }
        return data;
    }
    
    string decompress(const string& data) {
        if (strategy) {
            return strategy->decompress(data);
        }
        return data;
    }
};

int main() {
    cout << "=== Strategy with State (Compression) ===" << endl;
    
    string text = "AAAAABBBBBCCCCCDDDDDEEEEE";
    cout << "\nOriginal text: " << text << endl;
    
    Compressor compressor;
    
    cout << "\n1. RLE Compression:" << endl;
    compressor.setStrategy(new RLECompression());
    string compressed = compressor.compress(text);
    cout << "Compressed: " << compressed << endl;
    string decompressed = compressor.decompress(compressed);
    cout << "Decompressed: " << decompressed << endl;
    
    cout << "\n2. Dictionary Compression:" << endl;
    string sentence = "the quick brown fox jumps over the lazy dog";
    cout << "Original: " << sentence << endl;
    
    compressor.setStrategy(new DictionaryCompression());
    string compressed2 = compressor.compress(sentence);
    cout << "Compressed: " << compressed2 << endl;
    string decompressed2 = compressor.decompress(compressed2);
    cout << "Decompressed: " << decompressed2 << endl;
    
    return 0;
}
```

---

## 4. **Strategy with Context Data**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <map>
using namespace std;

// Strategy interface
class IRouteStrategy {
public:
    virtual double calculateTime(double distance, double speed) = 0;
    virtual double calculateCost(double distance) = 0;
    virtual string getDescription() = 0;
    virtual ~IRouteStrategy() = default;
};

// Concrete Strategy 1: Car
class CarStrategy : public IRouteStrategy {
public:
    double calculateTime(double distance, double speed) override {
        return distance / speed; // hours
    }
    
    double calculateCost(double distance) override {
        return distance * 0.5; // $0.5 per km
    }
    
    string getDescription() override {
        return "Car - Fastest, moderate cost";
    }
};

// Concrete Strategy 2: Bicycle
class BicycleStrategy : public IRouteStrategy {
public:
    double calculateTime(double distance, double speed) override {
        return distance / speed; // hours
    }
    
    double calculateCost(double distance) override {
        return 0; // Free
    }
    
    string getDescription() override {
        return "Bicycle - Slow, free, eco-friendly";
    }
};

// Concrete Strategy 3: Public Transport
class PublicTransportStrategy : public IRouteStrategy {
private:
    double baseFare;
    double perKmRate;
    
public:
    PublicTransportStrategy(double base, double rate) 
        : baseFare(base), perKmRate(rate) {}
    
    double calculateTime(double distance, double speed) override {
        return distance / speed + 0.5; // +30 min waiting
    }
    
    double calculateCost(double distance) override {
        return baseFare + distance * perKmRate;
    }
    
    string getDescription() override {
        return "Public Transport - Moderate, economical";
    }
};

// Context
class Navigator {
private:
    unique_ptr<IRouteStrategy> strategy;
    double averageSpeed;
    
public:
    Navigator(double speed) : averageSpeed(speed) {}
    
    void setStrategy(IRouteStrategy* s) {
        strategy.reset(s);
    }
    
    void calculateRoute(double distance) {
        if (!strategy) {
            cout << "No route strategy selected!" << endl;
            return;
        }
        
        cout << "\n=== Route Calculation ===" << endl;
        cout << "Strategy: " << strategy->getDescription() << endl;
        cout << "Distance: " << distance << " km" << endl;
        
        double time = strategy->calculateTime(distance, averageSpeed);
        double cost = strategy->calculateCost(distance);
        
        cout << "Estimated time: " << time << " hours" << endl;
        cout << "Estimated cost: $" << cost << endl;
    }
};

int main() {
    cout << "=== Strategy with Context Data ===" << endl;
    
    Navigator nav(60.0); // Average speed 60 km/h
    
    cout << "\nTrip from New York to Boston (300 km):" << endl;
    
    nav.setStrategy(new CarStrategy());
    nav.calculateRoute(300);
    
    nav.setStrategy(new BicycleStrategy());
    nav.calculateRoute(300);
    
    nav.setStrategy(new PublicTransportStrategy(2.5, 0.2));
    nav.calculateRoute(300);
    
    return 0;
}
```

---

## 5. **Practical Example: Validation Strategies**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <regex>
#include <functional>
using namespace std;

// Strategy interface
class IValidationStrategy {
public:
    virtual bool validate(const string& value) = 0;
    virtual string getErrorMessage() = 0;
    virtual ~IValidationStrategy() = default;
};

// Concrete Strategy 1: Required Field
class RequiredValidation : public IValidationStrategy {
public:
    bool validate(const string& value) override {
        return !value.empty();
    }
    
    string getErrorMessage() override {
        return "This field is required";
    }
};

// Concrete Strategy 2: Email Validation
class EmailValidation : public IValidationStrategy {
private:
    regex emailRegex;
    
public:
    EmailValidation() : emailRegex(R"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})") {}
    
    bool validate(const string& value) override {
        return regex_match(value, emailRegex);
    }
    
    string getErrorMessage() override {
        return "Invalid email format";
    }
};

// Concrete Strategy 3: Min Length Validation
class MinLengthValidation : public IValidationStrategy {
private:
    int minLength;
    
public:
    MinLengthValidation(int length) : minLength(length) {}
    
    bool validate(const string& value) override {
        return value.length() >= minLength;
    }
    
    string getErrorMessage() override {
        return "Minimum length is " + to_string(minLength) + " characters";
    }
};

// Concrete Strategy 4: Numeric Range Validation
class RangeValidation : public IValidationStrategy {
private:
    int min;
    int max;
    
public:
    RangeValidation(int minVal, int maxVal) : min(minVal), max(maxVal) {}
    
    bool validate(const string& value) override {
        try {
            int num = stoi(value);
            return num >= min && num <= max;
        } catch (...) {
            return false;
        }
    }
    
    string getErrorMessage() override {
        return "Value must be between " + to_string(min) + " and " + to_string(max);
    }
};

// Context
class Validator {
private:
    vector<pair<unique_ptr<IValidationStrategy>, string>> strategies;
    
public:
    void addStrategy(IValidationStrategy* strategy, const string& fieldName) {
        strategies.emplace_back(strategy, fieldName);
    }
    
    bool validate(const string& value) {
        for (const auto& [strategy, fieldName] : strategies) {
            if (!strategy->validate(value)) {
                cout << "Validation failed for " << fieldName << ": " 
                     << strategy->getErrorMessage() << endl;
                return false;
            }
        }
        return true;
    }
};

class FormField {
private:
    string name;
    string value;
    Validator validator;
    
public:
    FormField(const string& n) : name(n) {}
    
    void addValidation(IValidationStrategy* strategy) {
        validator.addStrategy(strategy, name);
    }
    
    void setValue(const string& v) {
        value = v;
    }
    
    bool isValid() {
        return validator.validate(value);
    }
    
    string getName() const { return name; }
    string getValue() const { return value; }
};

class RegistrationForm {
private:
    FormField username;
    FormField email;
    FormField age;
    
public:
    RegistrationForm() 
        : username("Username"), email("Email"), age("Age") {
        
        username.addValidation(new RequiredValidation());
        username.addValidation(new MinLengthValidation(3));
        
        email.addValidation(new RequiredValidation());
        email.addValidation(new EmailValidation());
        
        age.addValidation(new RequiredValidation());
        age.addValidation(new RangeValidation(18, 120));
    }
    
    void setUsername(const string& value) { username.setValue(value); }
    void setEmail(const string& value) { email.setValue(value); }
    void setAge(const string& value) { age.setValue(value); }
    
    bool validate() {
        cout << "\n=== Validating Registration Form ===" << endl;
        bool valid = true;
        
        if (!username.isValid()) valid = false;
        if (!email.isValid()) valid = false;
        if (!age.isValid()) valid = false;
        
        if (valid) {
            cout << "All fields are valid!" << endl;
        }
        
        return valid;
    }
    
    void submit() {
        if (validate()) {
            cout << "\nForm submitted successfully!" << endl;
            cout << "Username: " << username.getValue() << endl;
            cout << "Email: " << email.getValue() << endl;
            cout << "Age: " << age.getValue() << endl;
        } else {
            cout << "\nForm submission failed. Please correct errors." << endl;
        }
    }
};

int main() {
    cout << "=== Validation Strategies ===" << endl;
    
    RegistrationForm form;
    
    cout << "\nTest 1: Valid data:" << endl;
    form.setUsername("john_doe");
    form.setEmail("john@example.com");
    form.setAge("25");
    form.submit();
    
    cout << "\nTest 2: Invalid username (too short):" << endl;
    RegistrationForm form2;
    form2.setUsername("jo");
    form2.setEmail("jane@example.com");
    form2.setAge("30");
    form2.submit();
    
    cout << "\nTest 3: Invalid email:" << endl;
    RegistrationForm form3;
    form3.setUsername("jane_doe");
    form3.setEmail("invalid-email");
    form3.setAge("25");
    form3.submit();
    
    cout << "\nTest 4: Invalid age (under 18):" << endl;
    RegistrationForm form4;
    form4.setUsername("bob_smith");
    form4.setEmail("bob@example.com");
    form4.setAge("16");
    form4.submit();
    
    return 0;
}
```

---

## 📊 Strategy Pattern Summary

| Component | Description |
|-----------|-------------|
| **Strategy** | Interface for algorithms |
| **Concrete Strategy** | Implements specific algorithm |
| **Context** | Maintains reference to strategy |
| **Client** | Selects and configures strategy |

---

## ✅ Best Practices

1. **Use Strategy** when you have multiple algorithms
2. **Encapsulate algorithms** in separate classes
3. **Use lambda functions** for simple strategies
4. **Allow runtime switching** of strategies
5. **Keep strategy interface** consistent

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Too many strategies** | Code bloat | Use lambdas for simple cases |
| **Strategy knows context** | Tight coupling | Pass only needed data |
| **Client must know strategies** | Coupling | Use factory to create strategies |

---

## ✅ Key Takeaways

1. **Strategy pattern** encapsulates interchangeable algorithms
2. **Open/Closed Principle** - add new strategies without modifying context
3. **Runtime selection** of algorithm
4. **Lambda functions** provide lightweight strategies
5. **Useful for** sorting, validation, compression, routing
6. **Eliminates** conditional statements for algorithm selection

---
---

## Next Step

- Go to [README.md](/1.%20C++/03.%20OOPS/13_Best_Practices/README.md) to learn the best practices of how to use OOPS.
