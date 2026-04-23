# OOP Glossary - Comprehensive Terminology Reference

## 📖 Introduction

This glossary provides comprehensive definitions for all Object-Oriented Programming terms used throughout this learning resource. Terms are organized alphabetically for easy reference.

---

## 🔄 A

### **Abstraction**
The process of hiding complex implementation details while showing only essential features of the object. Abstraction helps manage complexity by allowing programmers to focus on interactions at a high level.

**Related**: [Abstract Classes](./07_Abstraction/01_Abstract_Classes.md), [Interfaces](./07_Abstraction/02_Interfaces_in_Cpp.md)

### **Access Specifier**
Keywords that define the accessibility of class members. C++ provides three access specifiers:
- `public`: Accessible from anywhere
- `private`: Accessible only within the class
- `protected`: Accessible within the class and derived classes

**Related**: [Access Specifiers](./02_Classes_and_Objects/03_Access_Specifiers.md)

### **Abstract Base Class (ABC)**
A class that contains at least one pure virtual function and cannot be instantiated directly. Serves as a base for other classes to inherit from.

**Related**: [Abstract Classes](./07_Abstraction/01_Abstract_Classes.md)

### **Aggregation**
A "has-a" relationship between classes where the child can exist independently of the parent. Represents a weak form of composition.

**Related**: [Composition vs Aggregation](./05_Inheritance/07_Is-A_vs_Has-A_Relationship.md)

### **Association**
A relationship between two classes that specifies a connection between them. Can be one-to-one, one-to-many, or many-to-many.

### **Attribute**
A data member of a class that represents a property or characteristic of an object.

**Related**: [Data Members](./02_Classes_and_Objects/04_Data_Members.md)

---

## 🔄 B

### **Base Class**
A class that is inherited from by another class (derived class). Also called parent class or superclass.

**Related**: [Basics of Inheritance](./05_Inheritance/01_Basics_of_Inheritance.md)

### **Behavior**
The functionality of an object, represented by its member functions or methods.

**Related**: [Member Functions](./02_Classes_and_Objects/05_Member_Functions.md)

### **Binding**
The process of connecting a function call to its implementation. Can be:
- **Early Binding**: At compile time (static)
- **Late Binding**: At runtime (dynamic)

**Related**: [Virtual Functions](./06_Polymorphism/02_Run_Time_Polymorphism/01_Virtual_Functions.md)

### **Bridge Pattern**
A structural design pattern that decouples an abstraction from its implementation, allowing both to vary independently.

**Related**: [Bridge Pattern](./12_Design_Patterns/02_Structural_Patterns/Bridge.md)

### **Builder Pattern**
A creational design pattern that separates the construction of a complex object from its representation.

**Related**: [Builder Pattern](./12_Design_Patterns/01_Creational_Patterns/Builder.md)

---

## 🔄 C

### **Class**
A blueprint for creating objects that defines properties (attributes) and behaviors (methods).

**Related**: [Class Declaration](./02_Classes_and_Objects/01_Class_Declaration.md)

### **Composition**
A "has-a" relationship where the child cannot exist without the parent. Represents a strong form of aggregation.

**Related**: [Is-A vs Has-A](./05_Inheritance/07_Is-A_vs_Has-A_Relationship.md)

### **Constructor**
A special member function that is automatically called when an object is created. Used to initialize object state.

**Related**: [Constructors](./03_Constructors_and_Destructors/)

### **Copy Constructor**
A constructor that creates a new object as a copy of an existing object.

**Related**: [Copy Constructor](./03_Constructors_and_Destructors/03_Copy_Constructor.md)

### **Const Correctness**
The practice of using the `const` keyword to ensure that objects cannot be modified when they shouldn't be.

**Related**: [Const Members](./02_Classes_and_Objects/07_Const_Members.md), [Const Correctness](./13_Best_Practices/02_Const_Correctness.md)

### **Concrete Class**
A class that can be instantiated, as opposed to an abstract class.

**Related**: [Abstract vs Concrete](./07_Abstraction/03_Abstract_vs_Concrete.md)

---

## 🔄 D

### **Data Hiding**
The practice of restricting access to an object's internal data, exposing only necessary information through a public interface.

**Related**: [Data Hiding](./04_Encapsulation/01_Data_Hiding.md)

### **Data Member**
A variable declared within a class that represents an object's state.

**Related**: [Data Members](./02_Classes_and_Objects/04_Data_Members.md)

### **Default Constructor**
A constructor that takes no arguments or provides default values for all parameters.

**Related**: [Default Constructor](./03_Constructors_and_Destructors/01_Default_Constructor.md)

### **Delegating Constructor**
A constructor that calls another constructor in the same class to initialize the object.

**Related**: [Delegating Constructors](./03_Constructors_and_Destructors/07_Delegating_Constructors.md)

### **Derived Class**
A class that inherits from another class (base class). Also called child class or subclass.

**Related**: [Basics of Inheritance](./05_Inheritance/01_Basics_of_Inheritance.md)

### **Destructor**
A special member function that is automatically called when an object is destroyed. Used to clean up resources.

**Related**: [Destructor](./03_Constructors_and_Destructors/08_Destructor.md)

### **Diamond Problem**
An ambiguity that occurs in multiple inheritance when a class inherits from two classes that both inherit from the same base class.

**Related**: [Diamond Problem](./05_Inheritance/05_Diamond_Problem.md)

### **Dynamic Binding**
The process of determining which function to call at runtime based on the object's actual type.

**Related**: [Virtual Functions](./06_Polymorphism/02_Run_Time_Polymorphism/01_Virtual_Functions.md)

### **Dynamic Cast**
A C++ operator that performs runtime type checking and safe downcasting in polymorphic class hierarchies.

**Related**: [Type Conversion](./08_Advanced_OOP/08_Type_Conversion_in_OOP.md)

---

## 🔄 E

### **Encapsulation**
The bundling of data (attributes) and methods (behaviors) that operate on the data into a single unit (class).

**Related**: [Encapsulation](./04_Encapsulation/)

### **Exception**
An object that represents an error or unusual condition that occurs during program execution.

**Related**: [Exception Handling](./10_Exception_Handling_in_OOP/)

### **Explicit Keyword**
A C++ keyword that prevents implicit conversions and copy-initialization.

**Related**: [Explicit Keyword](./08_Advanced_OOP/03_Explicit_Keyword.md)

---

## 🔄 F

### **Friend Function**
A function that is not a member of a class but has access to its private and protected members.

**Related**: [Friend Functions](./08_Advanced_OOP/01_Friend_Functions_and_Classes.md)

### **Friend Class**
A class that is granted access to the private and protected members of another class.

**Related**: [Friend Classes](./08_Advanced_OOP/01_Friend_Functions_and_Classes.md)

### **Function Overloading**
Having multiple functions with the same name but different parameters.

**Related**: [Function Overloading](./06_Polymorphism/01_Compile_Time_Polymorphism/01_Function_Overloading.md)

### **Function Template**
A blueprint for creating functions that can work with different data types.

**Related**: [Function Templates](./09_Templates_and_Generic_Programming/01_Function_Templates.md)

---

## 🔄 G

### **Generic Programming**
A style of programming where algorithms are written in terms of types to-be-specified-later, typically using templates.

**Related**: [Templates](./09_Templates_and_Generic_Programming/)

### **Getter**
A member function that returns the value of a private data member (accessor).

**Related**: [Getters and Setters](./04_Encapsulation/02_Getters_and_Setters.md)

---

## 🔄 H

### **Hierarchical Inheritance**
A type of inheritance where multiple classes inherit from a single base class.

**Related**: [Hierarchical Inheritance](./05_Inheritance/02_Types_of_Inheritance/Hierarchical_Inheritance.md)

### **Hybrid Inheritance**
A combination of multiple types of inheritance.

**Related**: [Hybrid Inheritance](./05_Inheritance/02_Types_of_Inheritance/Hybrid_Inheritance.md)

---

## 🔄 I

### **Implementation**
The actual code that defines how a class or function works.

### **Inheritance**
The mechanism by which one class acquires the properties and behaviors of another class.

**Related**: [Inheritance](./05_Inheritance/)

### **Inline Function**
A function that is expanded in place at the point of call, potentially improving performance.

**Related**: [Inline Functions](./02_Classes_and_Objects/08_Inline_Functions.md)

### **Interface**
A pure abstract class that defines a set of methods that implementing classes must provide.

**Related**: [Interfaces in C++](./07_Abstraction/02_Interfaces_in_Cpp.md)

### **Is-A Relationship**
A relationship where one class is a specialized version of another, typically implemented through inheritance.

**Related**: [Is-A vs Has-A](./05_Inheritance/07_Is-A_vs_Has-A_Relationship.md)

---

## 🔄 L

### **Late Binding**
See Dynamic Binding.

---

## 🔄 M

### **Member Function**
A function that is defined within a class and operates on class objects.

**Related**: [Member Functions](./02_Classes_and_Objects/05_Member_Functions.md)

### **Method**
Another term for a member function.

### **Multiple Inheritance**
A type of inheritance where a class inherits from multiple base classes.

**Related**: [Multiple Inheritance](./05_Inheritance/02_Types_of_Inheritance/Multiple_Inheritance.md)

### **Multilevel Inheritance**
A type of inheritance where a class is derived from another derived class.

**Related**: [Multilevel Inheritance](./05_Inheritance/02_Types_of_Inheritance/Multilevel_Inheritance.md)

### **Mutable Keyword**
A C++ keyword that allows a data member to be modified even in const member functions.

**Related**: [Mutable Keyword](./08_Advanced_OOP/02_Mutable_Keyword.md)

---

## 🔄 O

### **Object**
An instance of a class that has its own state and behavior.

**Related**: [Object Creation](./02_Classes_and_Objects/02_Object_Creation.md)

### **Object-Oriented Programming (OOP)**
A programming paradigm based on the concept of "objects" which contain data and methods.

**Related**: [What is OOP?](./01_Introduction/01_What_is_OOP.md)

### **Object Slicing**
The loss of information when a derived class object is assigned to a base class object.

**Related**: [Object Slicing](./08_Advanced_OOP/05_Object_Slicing.md)

### **Operator Overloading**
The process of defining custom behavior for C++ operators when used with user-defined types.

**Related**: [Operator Overloading](./06_Polymorphism/01_Compile_Time_Polymorphism/02_Operator_Overloading.md)

### **Overloading**
Having multiple functions or operators with the same name but different parameters.

**Related**: [Function Overloading](./06_Polymorphism/01_Compile_Time_Polymorphism/01_Function_Overloading.md)

### **Overriding**
Providing a new implementation for a virtual function in a derived class.

**Related**: [Virtual Functions](./06_Polymorphism/02_Run_Time_Polymorphism/01_Virtual_Functions.md)

---

## 🔄 P

### **Parameterized Constructor**
A constructor that takes one or more parameters to initialize object state.

**Related**: [Parameterized Constructor](./03_Constructors_and_Destructors/02_Parameterized_Constructor.md)

### **Pure Virtual Function**
A virtual function that has no implementation in the base class and must be overridden in derived classes.

**Related**: [Pure Virtual Functions](./06_Polymorphism/02_Run_Time_Polymorphism/04_Pure_Virtual_Functions.md)

### **Polymorphism**
The ability of an object to take on many forms. In C++, achieved through function overloading and virtual functions.

**Related**: [Polymorphism](./06_Polymorphism/)

### **Private Member**
A class member that is accessible only within the class itself and by friend functions/classes.

**Related**: [Access Specifiers](./02_Classes_and_Objects/03_Access_Specifiers.md)

### **Protected Member**
A class member that is accessible within the class, derived classes, and friend functions/classes.

**Related**: [Access Specifiers](./02_Classes_and_Objects/03_Access_Specifiers.md)

### **Public Member**
A class member that is accessible from anywhere the object is visible.

**Related**: [Access Specifiers](./02_Classes_and_Objects/03_Access_Specifiers.md)

---

## 🔄 R

### **RAII (Resource Acquisition Is Initialization)**
A programming pattern where resource acquisition is tied to object lifetime, ensuring automatic cleanup.

**Related**: [RAII](./10_Exception_Handling_in_OOP/05_RAII.md), [RAII Best Practices](./13_Best_Practices/03_RAII.md)

### **Reference**
An alias for another variable. In OOP, often used to pass objects efficiently to functions.

### **Rule of Three**
A C++ rule stating that if a class requires a user-defined destructor, copy constructor, or copy assignment operator, it probably needs all three.

**Related**: [Rule of Three/Five/Zero](./03_Constructors_and_Destructors/10_Rule_of_Three_Five_Zero.md)

### **Rule of Five**
An extension of the Rule of Three that includes move constructor and move assignment operator in C++11 and later.

**Related**: [Rule of Three/Five/Zero](./03_Constructors_and_Destructors/10_Rule_of_Three_Five_Zero.md)

### **Rule of Zero**
A modern C++ guideline stating that classes should avoid manual resource management and rely on smart pointers and RAII.

**Related**: [Rule of Three/Five/Zero](./03_Constructors_and_Destructors/10_Rule_of_Three_Five_Zero.md)

### **Runtime Polymorphism**
Polymorphism that is resolved at runtime through virtual functions and dynamic binding.

**Related**: [Runtime Polymorphism](./06_Polymorphism/02_Run_Time_Polymorphism/)

---

## 🔄 S

### **Setter**
A member function that modifies the value of a private data member (mutator).

**Related**: [Getters and Setters](./04_Encapsulation/02_Getters_and_Setters.md)

### **Single Inheritance**
A type of inheritance where a class inherits from only one base class.

**Related**: [Single Inheritance](./05_Inheritance/02_Types_of_Inheritance/Single_Inheritance.md)

### **Smart Pointer**
An object that acts like a pointer but provides automatic memory management through RAII.

**Related**: [Smart Pointers](./14_Modern_Cpp_OOP_Features/04_Smart_Pointers.md)

### **Static Binding**
See Early Binding.

### **Static Member**
A class member that is shared among all objects of the class rather than being individual to each object.

**Related**: [Static Members](./02_Classes_and_Objects/06_Static_Members.md)

### **Subclass**
See Derived Class.

### **Superclass**
See Base Class.

---

## 🔄 T

### **Template**
A blueprint for creating functions or classes that can work with different data types.

**Related**: [Templates](./09_Templates_and_Generic_Programming/)

### **Template Specialization**
Providing a specific implementation of a template for particular types.

**Related**: [Template Specialization](./09_Templates_and_Generic_Programming/03_Template_Specialization.md)

### **This Pointer**
A pointer available in non-static member functions that points to the object on which the function was called.

**Related**: [Member Functions](./02_Classes_and_Objects/05_Member_Functions.md)

### **Type Conversion**
The process of converting an object from one type to another.

**Related**: [Type Conversion](./08_Advanced_OOP/08_Type_Conversion_in_OOP.md)

---

## 🔄 V

### **Variadic Template**
A template that can accept any number of template arguments.

**Related**: [Variadic Templates](./09_Templates_and_Generic_Programming/04_Variadic_Templates.md)

### **Virtual Base Class**
A base class specified as virtual to prevent multiple instances in multiple inheritance scenarios.

**Related**: [Virtual Base Class](./08_Advanced_OOP/04_Virtual_Base_Class.md)

### **Virtual Constructor**
A concept that doesn't exist in C++, but can be simulated using factory methods or clone patterns.

### **Virtual Destructor**
A destructor declared as virtual to ensure proper cleanup through base class pointers.

**Related**: [Virtual Destructor](./03_Constructors_and_Destructors/09_Virtual_Destructor.md)

### **Virtual Function**
A member function that can be overridden in derived classes and resolved at runtime.

**Related**: [Virtual Functions](./06_Polymorphism/02_Run_Time_Polymorphism/01_Virtual_Functions.md)

### **Virtual Inheritance**
A technique to solve the diamond problem in multiple inheritance.

**Related**: [Virtual Inheritance](./05_Inheritance/06_Virtual_Inheritance.md)

### **Virtual Table (vtable)**
A table of function pointers used to implement runtime polymorphism.

**Related**: [Virtual Table](./06_Polymorphism/02_Run_Time_Polymorphism/06_Virtual_Table.md)

---

## 🔄 U-Z

### **Upcasting**
Converting a derived class pointer/reference to a base class pointer/reference. Always safe.

### **User-Defined Type**
A type created by the programmer, typically a class or struct.

### **Virtual Function Table**
See Virtual Table.

---

## 📊 Quick Reference Tables

### Access Levels

| Specifier | Class Access | Derived Class Access | External Access |
|-----------|--------------|---------------------|------------------|
| `public` | ✅ | ✅ | ✅ |
| `protected` | ✅ | ✅ | ❌ |
| `private` | ✅ | ❌ | ❌ |

### Inheritance Types

| Type | Description | Example |
|------|-------------|---------|
| Single | One base, one derived | `class B : public A` |
| Multiple | Multiple bases, one derived | `class C : public A, public B` |
| Multilevel | Chain of inheritance | `class C : public B; class B : public A` |
| Hierarchical | One base, multiple derived | `class B : public A; class C : public A` |
| Hybrid | Combination of types | Complex hierarchies |

### Constructor Types

| Type | Purpose | Syntax |
|------|---------|--------|
| Default | No parameters | `ClassName()` |
| Parameterized | With parameters | `ClassName(int x)` |
| Copy | From another object | `ClassName(const ClassName& other)` |
| Move | From rvalue | `ClassName(ClassName&& other)` |

### OOP Principles

| Principle | Description | Implementation |
|-----------|-------------|----------------|
| Encapsulation | Bundle data and methods | Private data, public interface |
| Inheritance | Reuse code | Base/derived classes |
| Polymorphism | Multiple forms | Virtual functions |
| Abstraction | Hide complexity | Abstract classes, interfaces |

---

## 🔗 Cross-References

### Related Topics
- **SOLID Principles**: [SOLID Principles](./13_Best_Practices/05_SOLID_Principles.md)
- **Design Patterns**: [Design Patterns](./12_Design_Patterns/)
- **Modern C++**: [Modern C++ Features](./14_Modern_Cpp_OOP_Features/)
- **Best Practices**: [Best Practices](./13_Best_Practices/)

### Common Confusions
- **Composition vs Inheritance**: [Is-A vs Has-A](./05_Inheritance/07_Is-A_vs_Has-A_Relationship.md)
- **Overloading vs Overriding**: [Polymorphism](./06_Polymorphism/)
- **Abstract vs Interface**: [Abstract vs Concrete](./07_Abstraction/03_Abstract_vs_Concrete.md)

---

## 📝 Notes

- This glossary is continuously updated as new topics are added
- Terms are linked to their detailed explanations throughout the resource
- Examples and code snippets are provided in individual topic files
- Practice exercises are included in most topic sections

---