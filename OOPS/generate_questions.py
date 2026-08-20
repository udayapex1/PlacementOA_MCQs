import json

def q(id_num, lang, diff, topic, companies, question, options, ans_idx, explanation):
    assert len(options) == 4, f"Question {id_num} must have exactly 4 options"
    assert 0 <= ans_idx <= 3, f"Question {id_num} answer index out of bounds"
    assert len(explanation.strip()) > 15, f"Question {id_num} explanation too short"
    return {
        "id": id_num,
        "language": lang,
        "difficulty": diff,
        "topic": topic,
        "companyPattern": companies,
        "question": question.strip(),
        "options": [opt.strip() for opt in options],
        "answer": ans_idx,
        "explanation": explanation.strip()
    }

questions = []

# ==============================================================================
# C++ QUESTIONS (1 - 84)
# ==============================================================================

# --- C++ Core & Access Specifiers ---
questions.append(q(
    len(questions) + 1, "C++", "Easy", "Access Specifiers",
    ["TCS", "Infosys", "Accenture"],
    "Which access specifier in C++ allows class members to be accessible only within the class itself and to friend classes/functions?",
    ["public", "protected", "private", "internal"],
    2,
    "The 'private' access specifier restricts access to members strictly within the declaring class and designated friend functions/classes. 'public' allows universal access, 'protected' allows access in derived classes, and 'internal' is not a valid C++ access specifier."
))

questions.append(q(
    len(questions) + 1, "C++", "Easy", "Constructors & Destructors",
    ["Cognizant", "Wipro", "Capgemini"],
    "What is the return type of a C++ constructor?",
    ["void", "int", "Pointer to the class", "Constructors do not have a return type"],
    3,
    "Constructors in C++ do not have any return type, not even void. They are automatically invoked upon object instantiation to initialize memory and instance data members."
))

questions.append(q(
    len(questions) + 1, "C++", "Medium", "Constructors & Destructors",
    ["Amazon", "Microsoft", "Oracle"],
    "What happens when a C++ class object goes out of scope?",
    ["Its constructor is called", "Its destructor is called automatically", "Memory is leaked unless free() is called", "The garbage collector reclaims it"],
    1,
    "In C++, stack-allocated objects follow RAII; when an object goes out of scope, its destructor is automatically called to perform cleanup. C++ does not have automatic garbage collection, and constructors are called during creation, not destruction."
))

questions.append(q(
    len(questions) + 1, "C++", "Hard", "Copy Constructor",
    ["Nvidia", "Qualcomm", "Intel"],
    "Why must the parameter of a copy constructor in C++ be passed by reference (e.g., ClassName(const ClassName &obj))?",
    ["To allow modification of the source object", "To prevent infinite recursion during pass-by-value initialization", "Because pointers cannot be passed to constructors", "To improve inline expansion by the compiler"],
    1,
    "If passed by value, passing the argument to the copy constructor would itself require creating a copy of the argument, which would invoke the copy constructor again, resulting in an infinite recursive call sequence at compile-time/runtime."
))

questions.append(q(
    len(questions) + 1, "C++", "Medium", "Shallow vs Deep Copy",
    ["Adobe", "Goldman Sachs", "SAP"],
    "Consider a C++ class allocating heap memory in its constructor. What occurs if a default copy constructor is used when copying an object?",
    ["A deep copy is performed automatically", "A shallow copy is performed, causing pointer aliasing and potential double free errors", "A compilation error occurs because heap memory requires virtual constructors", "Memory is allocated in the stack for the copied object"],
    1,
    "The default copy constructor performs a memberwise shallow copy. If a class holds raw pointers to heap memory, both objects end up pointing to the exact same memory location. When both objects are destroyed, a double free crash occurs."
))

questions.append(q(
    len(questions) + 1, "C++", "Medium", "Move Semantics",
    ["Google", "Meta", "Nvidia"],
    "In C++11, what is the primary parameter signature of a Move Constructor for class Buffer?",
    ["Buffer(Buffer obj)", "Buffer(const Buffer& obj)", "Buffer(Buffer&& obj) noexcept", "Buffer(Buffer* obj)"],
    2,
    "A move constructor accepts an rvalue reference Buffer&&. It transfers ownership of resources from a temporary object without reallocating memory, avoiding expensive deep copies."
))

questions.append(q(
    len(questions) + 1, "C++", "Easy", "Static Members",
    ["TCS", "HCL", "Tech Mahindra"],
    "How is a static data member of a C++ class shared among instantiated objects?",
    ["Each object gets its own copy of the static member", "A single instance of the static member exists for the entire class, shared by all objects", "Static members can only be accessed inside static member functions and cannot store state", "Static members are recreated on every function call"],
    1,
    "Static data members belong to the class itself rather than any specific object instance. Only one copy exists in memory throughout the program execution, shared across all instances."
))

questions.append(q(
    len(questions) + 1, "C++", "Medium", "Static Methods",
    ["Infosys", "Deloitte", "LTIMindtree"],
    "Which statement regarding static member functions in C++ is TRUE?",
    ["They have an implicit this pointer", "They can access non-static class members directly", "They can be called using the class name without creating an object", "They can be declared as virtual"],
    2,
    "Static member functions do not possess a this pointer and can be invoked using the class scope operator ClassName::function(). Consequently, they cannot access non-static members or be virtual."
))

questions.append(q(
    len(questions) + 1, "C++", "Hard", "This Pointer",
    ["Qualcomm", "Samsung", "Cisco"],
    "What is the type of the this pointer inside a const member function of class Widget?",
    ["Widget*", "const Widget*", "const Widget* const", "Widget* const"],
    2,
    "Inside a const member function, this is a constant pointer to a constant object (const Widget* const). This prevents modifying data members through this and prevents changing the pointer itself."
))

questions.append(q(
    len(questions) + 1, "C++", "Easy", "Friend Functions",
    ["Accenture", "Cognizant", "IBM"],
    "Which keyword is used in C++ to allow a non-member function to access private and protected members of a class?",
    ["public", "friend", "extern", "protected"],
    1,
    "The friend keyword grants a specific function or external class access to the private and protected encapsulation layers of the declaring class."
))

questions.append(q(
    len(questions) + 1, "C++", "Medium", "Friend Class",
    ["Oracle", "JPMorgan", "ServiceNow"],
    "If Class A is declared as a friend of Class B, and Class B is declared as a friend of Class C, which of the following is true in C++?",
    ["Class A is automatically a friend of Class C (transitive)", "Class C is automatically a friend of Class A (symmetric)", "Friendship is neither transitive nor symmetric", "Class C can access private members of Class A"],
    2,
    "Friendship in C++ is neither inherited, transitive, nor symmetric. A being a friend of B and B being a friend of C does not make A a friend of C unless explicitly specified."
))

questions.append(q(
    len(questions) + 1, "C++", "Easy", "Inline Functions",
    ["Wipro", "TCS", "Capgemini"],
    "What is the purpose of the inline keyword in C++ when applied to class methods?",
    ["To prevent method overriding", "To request the compiler to replace function calls with the actual function code to reduce invocation overhead", "To make the method run in a separate thread", "To dynamic bind the method at runtime"],
    1,
    "The inline hint requests the compiler to expand the function body inline at each call site, eliminating call overhead like stack frame push/pop for small, frequently called functions."
))

questions.append(q(
    len(questions) + 1, "C++", "Medium", "Explicit Keyword",
    ["Amazon", "Goldman Sachs", "VMware"],
    "What does the explicit specifier do when applied to a single-argument constructor in C++?",
    ["Forces the constructor to be executed in thread-safe mode", "Prevents implicit conversion operations during assignment or parameter passing", "Makes the constructor private", "Allows the constructor to be called without arguments"],
    1,
    "explicit prevents the compiler from performing implicit type conversions using constructors (e.g. Widget w = 10; is blocked if explicit Widget(int) is declared)."
))

questions.append(q(
    len(questions) + 1, "C++", "Hard", "Mutable Keyword",
    ["Nvidia", "Adobe", "Microsoft"],
    "What is the function of the mutable specifier on a C++ class data member?",
    ["It allows the member to be modified even inside const member functions", "It makes the member thread-safe", "It allows the variable to change data types dynamically", "It automatically allocates the variable on the heap"],
    0,
    "The mutable keyword allows a class member variable to be mutated even within const member functions, useful for internal caching, mutexes, or call counters that do not alter the logical state of the object."
))

questions.append(q(
    len(questions) + 1, "C++", "Medium", "Destructors",
    ["Tech Mahindra", "Infosys", "Deloitte"],
    "Can a C++ destructor take arguments or return a value?",
    ["Yes, it can take arguments but cannot return a value", "Yes, it can return int status codes", "No, destructors cannot take arguments or have return types", "Destructors can be overloaded with different parameter lists"],
    2,
    "In C++, a destructor never takes parameters and never returns a value. Because it takes no arguments, a class can have at most one destructor (destructors cannot be overloaded)."
))

# --- Inheritance & Polymorphism C++ ---
questions.append(q(
    len(questions) + 1, "C++", "Medium", "Diamond Problem",
    ["Amazon", "Oracle", "Cisco"],
    "How is the Diamond Problem (duplicate base class subobjects in multiple inheritance) resolved in C++?",
    ["By using private inheritance", "By making base class constructors static", "By using virtual inheritance (class B : virtual public A)", "By using namespaces"],
    2,
    "Virtual inheritance ensures that only one shared instance of the base class subobject exists in the derived class memory layout, resolving ambiguity and duplicate subobjects in diamond inheritance hierarchies."
))

questions.append(q(
    len(questions) + 1, "C++", "Hard", "Virtual Destructors",
    ["Qualcomm", "Nvidia", "Microsoft"],
    "What risk is incurred if a base class destructor is NOT declared as virtual when deleting a derived class object via a base class pointer (Base* p = new Derived(); delete p;)?",
    ["Compilation error occurs immediately", "Undefined behavior: only the base destructor runs, causing memory leaks/resource leaks of derived class members", "The derived constructor executes twice", "The program crashes during instantiation"],
    1,
    "Deleting a derived object through a non-virtual base pointer yields undefined behavior. Typically, the derived class destructor is not called, leading to memory leaks and unreleased resources held by the derived object."
))

questions.append(q(
    len(questions) + 1, "C++", "Medium", "Virtual Functions",
    ["Google", "Adobe", "Atlassian"],
    "How does C++ achieve runtime polymorphism for virtual functions under the hood?",
    ["Using RTTI and reflection tables", "Using vTable (Virtual Table) and vPtr (Virtual Pointer) per object", "By converting member functions into static C functions at compile time", "Using macros"],
    1,
    "C++ compilers construct a virtual table (vTable) containing function pointers for each class with virtual functions. Each object instance of such a class contains a hidden virtual pointer (vPtr) referencing its class vTable."
))

questions.append(q(
    len(questions) + 1, "C++", "Easy", "Pure Virtual Function",
    ["TCS", "Wipro", "Cognizant"],
    "How is a Pure Virtual Function declared in C++?",
    ["virtual void show() = 0;", "abstract void show();", "virtual void show() = abstract;", "pure virtual void show();"],
    0,
    "A pure virtual function is declared by assigning = 0 to a virtual function declaration in the class definition. Any class containing at least one pure virtual function becomes an abstract class."
))

questions.append(q(
    len(questions) + 1, "C++", "Medium", "Abstract Classes",
    ["Infosys", "Accenture", "IBM"],
    "Can you instantiate an object of an Abstract Class in C++?",
    ["Yes, if all data members are initialized", "No, abstract classes cannot be instantiated directly", "Yes, using the new keyword only", "Yes, but only inside friend functions"],
    1,
    "Abstract classes contain incomplete interface contracts (pure virtual functions) and cannot be directly instantiated. You can only instantiate concrete derived classes that implement all pure virtual functions."
))

questions.append(q(
    len(questions) + 1, "C++", "Hard", "Object Slicing",
    ["Goldman Sachs", "JPMorgan", "Morgan Stanley"],
    "What is Object Slicing in C++?",
    ["Dividing a class object across multiple threads", "When a derived class object is assigned to a base class object by value, stripping away derived-specific data members", "Deleting half of an object from memory", "Casting a base class pointer to derived class pointer"],
    1,
    "Object slicing occurs when a derived class instance is assigned to a base class instance by value (e.g. Base b = derivedObj;). The base assignment copy strips away all derived attributes, keeping only base members."
))

questions.append(q(
    len(questions) + 1, "C++", "Medium", "Operator Overloading",
    ["Samsung", "PayPal", "Walmart Global Tech"],
    "Which of the following operators CANNOT be overloaded in C++?",
    ["+", "==", ":: (Scope Resolution Operator)", "[]"],
    2,
    "In C++, the Scope Resolution Operator ::, Member Access Operator ., Pointer-to-member Operator .*, Conditional Operator ?:, and sizeof operator CANNOT be overloaded."
))

questions.append(q(
    len(questions) + 1, "C++", "Medium", "Operator Overloading",
    ["ServiceNow", "Flipkart", "Oracle"],
    "When overloading the prefix increment operator (++obj) vs postfix increment operator (obj++) in C++, how does the compiler differentiate their declarations?",
    ["Prefix takes a dummy int parameter; Postfix takes no parameters", "Postfix takes a dummy int parameter (operator++(int)); Prefix takes no parameters", "Prefix returns void; Postfix returns int", "Postfix uses the keyword post"],
    1,
    "The C++ standard distinguishes postfix increment from prefix increment by giving postfix a dummy integer parameter in signature: Type operator++() for prefix, and Type operator++(int) for postfix."
))

questions.append(q(
    len(questions) + 1, "C++", "Easy", "Inheritance Types",
    ["Capgemini", "HCL", "Tech Mahindra"],
    "In C++, if class B inherits privately from class A (class B : private A), what happens to public members of A inside B?",
    ["They become public members of B", "They become protected members of B", "They become private members of B", "They are removed from B"],
    2,
    "In private inheritance (private A), public and protected members of the base class A become private members within the derived class B and cannot be accessed outside B."
))

questions.append(q(
    len(questions) + 1, "C++", "Medium", "Function Overriding vs Overloading",
    ["Deloitte", "LTIMindtree", "Cognizant"],
    "What condition is required for Function Overriding to take place in C++?",
    ["Functions must have different parameter types in the same class", "Function in derived class must have exact same name, return type, and signature as a virtual function in base class", "Functions must be declared static", "Functions must be declared inside namespaces"],
    1,
    "Function overriding requires inheritance, identical signature (name, parameter types, qualifiers), identical/covariant return type, and the base function must be virtual."
))

# Output Prediction & Snippets C++
questions.append(q(
    len(questions) + 1, "C++", "Medium", "Output Prediction",
    ["Amazon", "Microsoft", "Directi"],
    """What is the output of the following C++ code?
#include <iostream>
using namespace std;
class Base {
public:
    void show() { cout << "Base "; }
};
class Derived : public Base {
public:
    void show() { cout << "Derived "; }
};
int main() {
    Base* ptr = new Derived();
    ptr->show();
    delete ptr;
    return 0;
}""",
    ["Base", "Derived", "Compilation Error", "Runtime Error"],
    0,
    "Because show() in Base is NOT declared virtual, early binding (compile-time binding) occurs based on the pointer type (Base*). Thus, Base::show() is called, printing 'Base'."
))

questions.append(q(
    len(questions) + 1, "C++", "Medium", "Output Prediction",
    ["TCS", "Infosys", "Accenture"],
    """What is the output of the following C++ code?
#include <iostream>
using namespace std;
class Base {
public:
    virtual void show() { cout << "Base "; }
};
class Derived : public Base {
public:
    void show() override { cout << "Derived "; }
};
int main() {
    Base* ptr = new Derived();
    ptr->show();
    delete ptr;
    return 0;
}""",
    ["Base", "Derived", "Derived Base", "Compilation Error"],
    1,
    "Since show() is marked virtual in Base, dynamic binding occurs at runtime based on the actual object type (Derived). Hence Derived::show() executes, printing 'Derived'."
))

questions.append(q(
    len(questions) + 1, "C++", "Hard", "Output Prediction",
    ["Qualcomm", "Nvidia", "Google"],
    """What is the output of the following C++ code?
#include <iostream>
using namespace std;
class Base {
public:
    Base() { show(); }
    virtual void show() { cout << "BaseConstruct "; }
};
class Derived : public Base {
public:
    Derived() { show(); }
    void show() override { cout << "DerivedConstruct "; }
};
int main() {
    Derived d;
    return 0;
}""",
    ["DerivedConstruct DerivedConstruct", "BaseConstruct DerivedConstruct", "DerivedConstruct BaseConstruct", "BaseConstruct BaseConstruct"],
    1,
    "During base class construction, the object is not yet a Derived instance. Calling a virtual function inside a base constructor executes the base class implementation (BaseConstruct). Then Derived constructor runs, calling Derived::show() (DerivedConstruct)."
))

questions.append(q(
    len(questions) + 1, "C++", "Hard", "Output Prediction",
    ["Adobe", "Goldman Sachs", "Amazon"],
    """What is the output of the following C++ snippet?
#include <iostream>
using namespace std;
class Test {
    static int count;
public:
    Test() { count++; }
    static int getCount() { return count; }
};
int Test::count = 5;
int main() {
    Test t1, t2;
    cout << Test::getCount();
    return 0;
}""",
    ["5", "6", "7", "Compilation Error"],
    2,
    "count is initialized to 5. Instantiating t1 increments count to 6, and t2 increments count to 7. getCount() returns 7."
))

questions.append(q(
    len(questions) + 1, "C++", "Medium", "Output Prediction",
    ["Capgemini", "Cognizant", "Wipro"],
    """What is the output of this code?
#include <iostream>
using namespace std;
class A {
public:
    A() { cout << "A"; }
    ~A() { cout << "~A"; }
};
class B : public A {
public:
    B() { cout << "B"; }
    ~B() { cout << "~B"; }
};
int main() {
    B obj;
    return 0;
}""",
    ["AB~B~A", "BA~A~B", "AB~A~B", "BA~B~A"],
    0,
    "Constructors are executed in top-down order (Base first, then Derived -> 'AB'). Destructors execute in reverse bottom-up order (Derived first, then Base -> '~B~A'). Total output: 'AB~B~A'."
))

questions.append(q(
    len(questions) + 1, "C++", "Hard", "Virtual Destructor Trap",
    ["Amazon", "Microsoft", "ServiceNow"],
    """What is printed by the following program?
#include <iostream>
using namespace std;
class Base {
public:
    ~Base() { cout << "~Base "; }
};
class Derived : public Base {
public:
    ~Derived() { cout << "~Derived "; }
};
int main() {
    Base* ptr = new Derived();
    delete ptr;
    return 0;
}""",
    ["~Derived ~Base ", "~Base ", "~Derived ", "Compilation Error"],
    1,
    "Because Base::~Base() is NOT virtual, executing delete ptr (where ptr is Base*) only invokes ~Base(), skipping ~Derived(). Output is '~Base '."
))

questions.append(q(
    len(questions) + 1, "C++", "Medium", "Templates",
    ["Oracle", "Cisco", "Tech Mahindra"],
    "What is the purpose of class templates in C++?",
    ["To generate dynamic runtime objects", "To allow a class to operate on generic data types without rewriting code for each type", "To automatically implement design patterns", "To force private inheritance"],
    1,
    "Templates support generic programming by enabling classes and functions to operate with generic data types specified at compile time."
))

questions.append(q(
    len(questions) + 1, "C++", "Medium", "Smart Pointers",
    ["Nvidia", "Qualcomm", "Intel"],
    "Which Smart Pointer in C++11 represents exclusive ownership of a dynamically allocated resource and CANNOT be copied?",
    ["std::shared_ptr", "std::weak_ptr", "std::unique_ptr", "std::auto_ptr"],
    2,
    "std::unique_ptr manages resources with unique (exclusive) ownership semantics. Copying is disabled (copy constructor deleted), but it can be moved using std::move."
))

questions.append(q(
    len(questions) + 1, "C++", "Hard", "Smart Pointers",
    ["Google", "Meta", "Adobe"],
    "What problem does std::weak_ptr solve in C++ smart pointer management?",
    ["It reduces memory fragmentation", "It breaks circular references (cyclic dependencies) caused by std::shared_ptr", "It speeds up smart pointer dereferencing", "It allows copying unique_ptr"],
    1,
    "When two objects hold std::shared_ptr references to each other, their reference counts never drop to zero, creating a memory leak. std::weak_ptr provides a non-owning reference that prevents cyclic reference leaks."
))

questions.append(q(
    len(questions) + 1, "C++", "Easy", "RAII Concept",
    ["Infosys", "TCS", "Accenture"],
    "What does RAII stand for in C++ programming?",
    ["Resource Allocation Is Immediate", "Resource Acquisition Is Initialization", "Runtime Access In Inheritance", "Reference Alignment In Interfaces"],
    1,
    "RAII stands for 'Resource Acquisition Is Initialization'. It ties resource management (file handles, memory, sockets) to object lifetime, releasing resources in destructors automatically."
))

# Filling C++ Topics data
cpp_topics_data = [
    ("Default Arguments in Methods", "Medium", ["IBM", "Deloitte"], "In C++, if a function has default arguments, where must they be specified in the parameter list?", ["At the beginning of the list", "At the end of the parameter list", "Anywhere in the list", "Only for integer arguments"], 1, "Default arguments must be specified from right to left (at the end of the parameter list). You cannot have a non-default parameter after a default parameter."),
    ("Copy Elision / RVO", "Hard", ["Microsoft", "Amazon"], "What is Return Value Optimization (RVO) / Copy Elision in C++?", ["A compiler technique that optimizes loop bounds", "A compiler optimization that eliminates unnecessary copying of temporary objects returned by functions", "A method to compress class data members", "A garbage collection pass"], 1, "Copy elision/RVO allows the compiler to construct the return object directly in the memory allocated for the caller's target variable, bypassing copy/move constructors."),
    ("Const Member Functions", "Easy", ["TCS", "Wipro"], "Can a const member function invoke a non-const member function of the same class in C++?", ["Yes, always", "No, it causes a compilation error", "Yes, if the function is inline", "Yes, if casted explicitly"], 1, "A const member function guarantees not to modify the object state. Invoking a non-const member function could break this guarantee, so the compiler prohibits it."),
    ("Virtual Base Class", "Medium", ["Cognizant", "HCL"], "What is the key syntax to declare virtual base inheritance in C++?", ["class Derived : virtual public Base", "class Derived : public Base virtual", "class Derived : abstract Base", "class Derived : Base(virtual)"], 0, "The virtual keyword is placed before or after access specifiers during class derivation: class Derived : virtual public Base."),
    ("Pure Virtual Destructor", "Hard", ["Adobe", "Qualcomm"], "Is it legal in C++ to declare a Pure Virtual Destructor, and if so, what is required?", ["Illegal; destructors cannot be pure virtual", "Legal; but a body for the pure virtual destructor must still be provided outside the class", "Legal; and no body can be provided under any circumstance", "Legal; but the class becomes non-inheritable"], 1, "A pure virtual destructor is legal (virtual ~Base() = 0;), but derived destructors implicitly call the base destructor, so a base destructor body MUST be defined outside the class declaration."),
    ("Namespaces", "Easy", ["Infosys", "Capgemini"], "What problem do namespaces solve in C++?", ["Memory overflow errors", "Name collisions/naming conflicts between libraries or code modules", "Pointer aliasing", "Slow compilation speeds"], 1, "Namespaces prevent naming conflicts by grouping entities like classes, functions, and variables into distinct named scopes."),
    ("Static Cast vs Dynamic Cast", "Hard", ["Goldman Sachs", "Nvidia"], "Which C++ cast operator performs runtime type checking using RTTI when casting pointers down an inheritance hierarchy?", ["static_cast", "const_cast", "reinterpret_cast", "dynamic_cast"], 3, "dynamic_cast safely casts down or across polymorphism hierarchies at runtime using RTTI. If the cast is invalid, it returns nullptr for pointers or throws std::bad_cast for references."),
    ("Reinterpret Cast", "Medium", ["JPMorgan", "Samsung"], "Which C++ cast operator should be used to convert a pointer of one type directly to a pointer of an unrelated type without type safety checks?", ["static_cast", "reinterpret_cast", "dynamic_cast", "const_cast"], 1, "reinterpret_cast converts any pointer type to any other pointer type bitwise without type checking. It is low-level and inherently unsafe."),
    ("Const Cast", "Easy", ["Accenture", "LTIMindtree"], "Which cast operator in C++ is specifically designed to add or remove const or volatile qualifiers from a variable?", ["const_cast", "static_cast", "dynamic_cast", "reinterpret_cast"], 0, "const_cast is the only C++ cast operator that can explicitly cast away or add constness or volatileness."),
    ("Delegating Constructors", "Medium", ["Oracle", "ServiceNow"], "In C++11, what is a Delegating Constructor?", ["A constructor that delegates object creation to a factory function", "A constructor that calls another constructor of the same class in its member initializer list", "A constructor that runs asynchronously", "A constructor inherited from a friend class"], 1, "C++11 delegating constructors allow one constructor of a class to call another constructor of the same class in its initialization list to eliminate code duplication."),
    ("Inheriting Constructors", "Medium", ["Atlassian", "Flipkart"], "How can a derived class in C++11 inherit all constructors from its base class?", ["using Base::Base;", "inherit Base::Constructors;", "Base() = default;", "using namespace Base;"], 0, "With using Base::Base;, C++11 derived classes automatically inherit all constructors from the base class Base."),
    ("Override Keyword", "Easy", ["TCS", "Tech Mahindra"], "What benefit does appending override to a derived class method provide in C++11?", ["It speeds up virtual function call dispatch", "The compiler verifies that the method actually overrides a virtual base method, flagging mismatches as errors", "It makes the method inline", "It prevents further overriding in derived classes"], 1, "The override specifier ensures compile-time checking. If the base function signature changes or doesn't match, the compiler emits an error instead of silently creating a new overloaded function."),
    ("Final Keyword", "Easy", ["Wipro", "Cognizant"], "What does the final specifier achieve when applied to a C++ class definition (class Base final { ... };)?", ["It prevents the class from being instantiated", "It prevents any derived class from inheriting from this class", "It makes all class members private", "It allocates the class in read-only memory"], 1, "final on a class prevents further inheritance. Applied to a virtual function, it prevents derived classes from overriding that function."),
    ("Member Initializer List", "Medium", ["Amazon", "Deloitte"], "Why is it mandatory to use a Member Initializer List for const members and reference members in C++ constructors?", ["Because const and reference members must be initialized at point of creation, not assigned inside the body", "Because it improves execution speed by 50%", "Because non-initializer list assignment throws a runtime exception", "Because const variables are stored in registers"], 0, "Const variables and reference members cannot be default-constructed and subsequently assigned; they must be initialized at creation time via the initializer list before the constructor body executes."),
    ("Order of Initialization", "Hard", ["Qualcomm", "Nvidia"], "In C++, in what order are class data members initialized by a constructor?", ["In the order they appear in the Member Initializer List", "In the order they are declared in the class definition", "In alphabetical order of variable names", "Static members first, then in reverse order of declaration"], 1, "Data members are ALWAYS initialized in the exact order of their declaration in the class definition, regardless of their order in the constructor initializer list."),
    ("Struct vs Class", "Easy", ["Infosys", "IBM"], "What is the ONLY default difference between struct and class in C++?", ["struct cannot have member functions; class can", "struct members and inheritance are public by default; class members and inheritance are private by default", "struct is stored on stack; class is stored on heap", "struct does not support constructors"], 1, "In C++, struct and class are identical except that struct defaults to public member access and public inheritance, while class defaults to private."),
    ("Union in C++", "Medium", ["Capgemini", "Tech Mahindra"], "What characterizes a union in C++?", ["All members share the same memory location, holding only one active member value at a time", "Members are arranged sequentially in memory like a struct", "Unions cannot contain primitive types", "Unions support virtual inheritance"], 0, "A union allocates memory equal to its largest data member; all members overlay the same memory space, so writing to one overwrites the others."),
    ("Placement New", "Hard", ["Google", "Meta"], "What is the purpose of Placement New (new (buffer) Widget()) in C++?", ["It allocates memory on the GPU", "It constructs an object at a pre-allocated memory address without allocating fresh memory", "It creates thread-local objects", "It bypasses constructor calls"], 1, "Placement new constructs an object inside a pre-allocated memory buffer provided by the caller, frequently used in custom memory allocators and high-performance applications."),
    ("Deleting Functions", "Easy", ["Wipro", "TCS"], "In C++11, how do you explicitly disable the copy constructor for a class NoCopy?", ["NoCopy(const NoCopy&) = delete;", "NoCopy(const NoCopy&) = private;", "NoCopy(const NoCopy&) = void;", "virtual NoCopy(const NoCopy&) = 0;"], 0, "= delete explicitly marks a function as deleted, instructing the compiler to generate a compilation error if any code attempts to invoke it."),
    ("Defaulting Functions", "Easy", ["Accenture", "Infosys"], "How do you request the compiler to generate the default constructor in C++11?", ["Widget() = default;", "Widget() = auto;", "Widget() = inline;", "Widget() = create;"], 0, "= default instructs the compiler to generate the default implementation of a special member function (constructor, destructor, copy/move assignment)."),
    ("Function Overloading Resolution", "Medium", ["Cognizant", "Oracle"], "In C++, can two functions be overloaded based solely on their return types (e.g. int calc() and double calc())?", ["Yes, the compiler resolves based on left-hand side assignment", "No, return type alone is insufficient for function overloading and produces a compile error", "Yes, but only if marked inline", "Yes, if declared inside a template"], 1, "Function overloading requires distinct parameter signatures (number, type, or sequence of parameters). Differing return types alone results in a compilation ambiguity error."),
    ("Virtual Functions Performance", "Medium", ["Amazon", "Microsoft"], "What is the performance overhead of calling a virtual function compared to a non-virtual function in C++?", ["10x slower execution", "Pointer indirection via vPtr/vTable lookup and inability to inline the function call", "High garbage collection overhead", "No overhead at all"], 1, "Virtual function calls incur a small overhead due to dereferencing the vPtr to access the vTable array, plus the compiler usually cannot inline virtual calls when invoked via pointers/references."),
    ("RTTI (typeid)", "Hard", ["Goldman Sachs", "Morgan Stanley"], "Which header and operator in C++ provide Run-Time Type Information to inspect object types at runtime?", ["<typeinfo> and typeid", "<rtti> and typeof", "<type_traits> and is_type", "<iostream> and decltype"], 0, "The typeid operator (defined in header <typeinfo>) queries the dynamic type of an object at runtime when RTTI is enabled for polymorphic types."),
    ("Decltype Keyword", "Medium", ["ServiceNow", "Adobe"], "What does the decltype keyword in C++11 do?", ["It casts a variable to a reference type", "It inspects and yields the declared type of an expression at compile time", "It dynamically allocates variable storage", "It deletes pointers safely"], 1, "decltype extracts the compile-time type of an entity or expression without evaluating the expression."),
    ("Friend Template", "Hard", ["Nvidia", "Qualcomm"], "Can a template function be declared as a friend of a non-template class in C++?", ["No, templates cannot be friends", "Yes, template functions can be declared as friends of non-template classes", "Only if the class is abstract", "Only if template parameters are integers"], 1, "C++ permits declaring function templates or specific template instantiations as friends inside a class definition."),
    ("Pure Virtual Function Body", "Hard", ["Intel", "Cisco"], "Can a Pure Virtual Function in C++ have an implementation body?", ["No, absolute prohibition by compiler", "Yes, a pure virtual function can have a body defined outside the class body", "Yes, but only inline inside the class declaration", "Only if marked static"], 1, "Surprisingly, C++ permits defining a body for a pure virtual function outside the class body (e.g. void Base::show() { ... }). Derived classes must still override it, but can chain call Base::show()."),
    ("Static Local Variables in Methods", "Medium", ["Walmart Global Tech", "Flipkart"], "What is the scope and lifetime of a static variable declared inside a class member function?", ["Scope: entire class; Lifetime: function duration", "Scope: local to the function; Lifetime: entire program execution across all instances", "Scope: global; Lifetime: object instantiation", "Scope: local; Lifetime: destroyed when function returns"], 1, "A static local variable in a method is initialized once on first execution and persists for the program duration across all class instances, scoped locally to that method."),
    ("Multiple Inheritance Ambiguity", "Medium", ["TCS", "Infosys"], "If Class C inherits from Class A and Class B, both having a public method display(), how is display() called unambiguously on an object c of Class C?", ["c.display()", "c.A::display()", "c->A.display()", "c.display(A)"], 1, "Ambiguity in multiple inheritance is explicitly resolved using scope resolution: c.A::display() or c.B::display()."),
    ("Object Slicing Prevention", "Hard", ["Amazon", "Microsoft"], "How can Object Slicing be prevented when passing objects to functions in C++?", ["By passing objects by value", "By passing objects by reference or pointer (const Base &obj or Base *obj)", "By using static member functions", "By making all data members public"], 1, "Passing derived objects by reference or pointer prevents copying into a value base object, preserving polymorphism and avoiding slicing."),
    ("Copy Assignment Operator", "Medium", ["Accenture", "Cognizant"], "What is the return type of a standard C++ copy assignment operator (operator=)?", ["void", "ClassName", "ClassName&", "const ClassName"], 2, "The copy assignment operator returns a reference to the invoking object (ClassName&) returning *this to enable assignment chaining (e.g. a = b = c;)."),
    ("Self Assignment Guard", "Medium", ["IBM", "Deloitte"], "Why is checking for self-assignment (if (this == &rhs) return *this;) crucial in a custom assignment operator handling heap resources?", ["To avoid syntax errors", "To prevent deallocating resources of the object before copying them onto itself", "To speed up pointer arithmetic", "To bypass virtual table lookups"], 1, "Without a self-assignment check (a = a;), freeing existing heap memory inside operator= would delete the source data before it can be copied, causing memory corruption."),
    ("Move Assignment Operator", "Hard", ["Qualcomm", "Samsung"], "What is the typical signature for a Move Assignment Operator in class String?", ["String& operator=(const String& rhs)", "String& operator=(String&& rhs) noexcept", "void operator=(String&& rhs)", "String operator=(String rhs)"], 1, "A move assignment operator takes an rvalue reference parameter String&& rhs, releases current resources, steals rhs resources, resets rhs pointers, and returns *this by reference."),
    ("Constexpr Keyword", "Medium", ["Nvidia", "Adobe"], "What does the constexpr keyword indicate when applied to a C++ function or constructor?", ["The function executes in a separate thread", "The function expression can be evaluated at compile time if inputs are constant expressions", "The function cannot be overloaded", "The function returns a const pointer"], 1, "constexpr specifies that the value of a function or variable can be evaluated at compile time, enabling high-performance compile-time computations."),
    ("Volatile Keyword", "Medium", ["Intel", "Qualcomm"], "What does the volatile keyword inform the C++ compiler about a member variable?", ["That the variable is stored on the stack", "That the variable may be modified externally (e.g., hardware/interrupts), instructing the compiler not to optimize away reads/writes", "That the variable is thread-locked", "That the variable is constant"], 1, "volatile prevents compiler optimizations like caching variable values in CPU registers because the variable's value can change outside the compiler's control."),
    ("Friend Function Scope", "Medium", ["Capgemini", "Wipro"], "Is a friend function declared inside a class considered a member function of that class?", ["Yes, it has access to the this pointer", "No, it is a non-member function that is granted access to private/protected members", "Yes, but only if declared public", "Yes, if it is static"], 1, "A friend function is NOT a member function of the class; it does not possess a this pointer and cannot be invoked using object dot notation (obj.friendFunc())."),
    ("Exception Handling in Destructors", "Hard", ["Amazon", "Google"], "Why should C++ destructors NEVER throw exceptions that leave the destructor body?", ["Because it results in compile time errors", "Because throwing an exception during stack unwinding (e.g., during another exception) causes std::terminate() to abort the program", "Because thrown exceptions leak vTables", "Because destructors run in kernel space"], 1, "If a destructor throws an exception while stack unwinding is already in progress from another active exception, C++ calls std::terminate(), crashing the program immediately."),
    ("Smart Pointers make_shared", "Medium", ["Microsoft", "Oracle"], "Why is std::make_shared<T>() preferred over std::shared_ptr<T>(new T())?", ["It bypasses constructor calls", "It performs a single memory allocation for both the control block and object, improving cache efficiency and exception safety", "It creates unique pointers automatically", "It turns off reference counting"], 1, "make_shared combines object creation and shared reference control block creation into one atomic allocation step, reducing overhead and preventing memory leaks if an exception occurs during construction."),
    ("Anonymous Namespaces", "Medium", ["JPMorgan", "Goldman Sachs"], "What is the primary benefit of an anonymous (unnamed) namespace in C++ source files?", ["It makes functions global across all translation units", "It limits the internal linkage of contained symbols strictly to the current translation unit (file scope)", "It enables fast string parsing", "It prevents garbage collection"], 1, "Entities defined inside an unnamed namespace have internal linkage, replacing static global declarations and isolating symbols to the single source file."),
    ("C++ Polymorphism Type", "Easy", ["TCS", "Accenture"], "Function overloading and Operator overloading in C++ are examples of which type of polymorphism?", ["Runtime Polymorphism", "Compile-Time (Static) Polymorphism", "Ad-hoc Virtual Polymorphism", "Dynamic Subtyping"], 1, "Overloading is resolved at compile time based on method signatures, making it Compile-Time (Static) Polymorphism. Method overriding with virtual functions is Runtime (Dynamic) Polymorphism."),
    ("Default Member Initialization", "Easy", ["Infosys", "Tech Mahindra"], "In C++11, can you initialize non-static data members directly at their declaration in the class body?", ["No, initialization must occur in constructors only", "Yes, using in-class member initializers (e.g. int count = 0;)", "Only if the variable is marked const", "Only if the variable is public"], 1, "C++11 introduced in-class member initializers, permitting non-static variables to be given default initial values directly in the class definition."),
    ("Final Method Overriding", "Medium", ["Cognizant", "Deloitte"], "What happens if a derived class attempts to override a virtual function marked with final in the base class?", ["The virtual function is silently ignored", "A compilation error occurs", "A runtime exception is thrown", "The base function is deleted"], 1, "Marking a virtual function as final prohibits any further derived classes from overriding it; doing so results in a compilation error."),
    ("Virtual Functions Default Arguments Trap", "Hard", ["Adobe", "Meta"], "What happens when a virtual function with a default parameter is overridden in a derived class with a DIFFERENT default parameter, and called via a Base pointer?", ["The derived default argument is used", "The base default argument is evaluated at compile time, but the derived function body runs at runtime", "A runtime exception occurs", "Compilation error occurs"], 1, "Default arguments are bound statically at compile time based on the pointer type (Base*), while the virtual method is bound dynamically at runtime. This causes the derived function body to run with the BASE default parameter!"),
    ("Typeid polymorphic object", "Hard", ["Nvidia", "Qualcomm"], "If ptr is a Base* pointing to a Derived object, what does typeid(*ptr).name() evaluate to if Base has virtual functions?", ["Base", "The dynamic derived type (Derived)", "nullptr", "Compilation error"], 1, "When Base contains at least one virtual function (polymorphic class), typeid(*ptr) uses RTTI at runtime to inspect the actual dynamic object type (Derived)."),
    ("Protected Access in Inheritance", "Medium", ["Capgemini", "LTIMindtree"], "If Class B inherits protected from Class A (class B : protected A), how are public members of A accessed outside B?", ["They remain public outside B", "They cannot be accessed outside B (they become protected in B)", "They become private in B", "They cause compilation error"], 1, "In protected inheritance, public and protected members of base class A become protected inside B, meaning they can be accessed by B and B's derived classes, but NOT directly from outside objects."),
    ("Constructors in Abstract Classes", "Medium", ["Wipro", "HCL"], "Can an abstract class in C++ have constructors?", ["No, abstract classes cannot have constructors", "Yes, abstract class constructors exist to initialize base class data members when derived objects are instantiated", "Only if the constructor is virtual", "Only static constructors are allowed"], 1, "Abstract classes CAN have constructors. Even though abstract classes cannot be instantiated directly, their constructors run when derived class objects are instantiated."),
    ("Pure Virtual Destructor requirement", "Hard", ["Microsoft", "Amazon"], "If a base class has a pure virtual destructor (virtual ~Base() = 0;), must derived classes explicitly override it?", ["Yes, derived classes must explicitly define ~Derived() = 0", "No, the compiler automatically generates a derived destructor which satisfies the requirement", "Yes, derived classes cannot be compiled without explicit virtual destructor override", "No, pure virtual destructors are illegal"], 1, "Derived classes automatically receive a compiler-generated destructor if not explicitly written, which implicitly overrides the base destructor and satisfies abstract requirements."),
    ("Size of Empty Class", "Medium", ["TCS", "Infosys"], "What is sizeof(Empty) for an empty class class Empty {}; in C++?", ["0 bytes", "1 byte (to ensure unique memory addresses for distinct object instances)", "4 bytes", "8 bytes"], 1, "In C++, an empty class has a non-zero size (typically 1 byte) to guarantee that two distinct object instances have different memory addresses."),
    ("Empty Class with Virtual Function Size", "Hard", ["Goldman Sachs", "Qualcomm"], "What is sizeof(Demo) for class Demo { virtual void foo(); }; on a 64-bit architecture?", ["1 byte", "4 bytes", "8 bytes (size of vPtr pointer)", "16 bytes"], 2, "Introducing a virtual function adds a hidden vPtr pointer to the object instance layout. On a 64-bit system, pointer size is 8 bytes, so sizeof(Demo) is 8 bytes."),
    ("Static Data Member Definition", "Medium", ["IBM", "Tech Mahindra"], "Where must non-const static data members of a C++ class be defined and allocated memory?", ["Inside the constructor", "Outside the class definition in a single source file (int ClassName::member = 0;)", "Inside the main function", "Memory is allocated on the heap automatically"], 1, "Static data members must be declared inside the class, but defined and allocated storage outside the class definition at file scope (unless they are inline static in C++17)."),
    ("Conversion Constructor", "Medium", ["Accenture", "Cognizant"], "What is a conversion constructor in C++?", ["A constructor with a return type", "A constructor that can be called with a single argument, allowing implicit type conversion unless marked explicit", "A virtual constructor that returns derived instances", "A constructor defined inside a template"], 1, "Any constructor that can be invoked with a single parameter acts as a conversion constructor, allowing the compiler to convert values of the parameter type into object instances implicitly."),
    ("Rule of Three", "Hard", ["Adobe", "Amazon"], "What is the C++ Rule of Three for resource management?", ["If a class manages resources, it should explicitly define: Destructor, Copy Constructor, and Copy Assignment Operator", "A class must have 3 constructors", "A class must inherit from 3 base classes", "A class should use 3 design patterns"], 0, "The Rule of Three states that if a class requires a custom Destructor, Copy Constructor, or Copy Assignment Operator, it almost certainly requires all three to correctly manage resources."),
    ("Rule of Five", "Hard", ["Nvidia", "Google"], "What two special member functions were added to the Rule of Three to form the C++11 Rule of Five?", ["Move Constructor and Move Assignment Operator", "Default Constructor and Friend Constructor", "Virtual Constructor and Virtual Destructor", "Inline Destructor and Static Assignment"], 0, "With C++11 move semantics, the Rule of Three expanded to the Rule of Five: Destructor, Copy Constructor, Copy Assignment Operator, Move Constructor, and Move Assignment Operator."),
    ("Interface in C++", "Easy", ["Wipro", "Capgemini"], "How is an Interface conceptually created in C++?", ["Using the interface keyword", "By defining a class that contains ONLY pure virtual functions and a virtual destructor", "By declaring all variables static", "By using namespaces"], 1, "C++ does not have a dedicated interface keyword like Java. An interface is represented by a class containing exclusively pure virtual functions and a virtual destructor."),
    ("Covariant Return Types", "Hard", ["Microsoft", "Oracle"], "What are Covariant Return Types in C++ method overriding?", ["Allowing derived overriding functions to return a pointer/reference to a derived class type instead of the base class return type", "Allowing return types to change from int to double", "Forcing functions to return void", "Overloading methods based on return type"], 0, "Covariant return types permit an overriding derived method to return a pointer or reference to a derived type Derived* when the base virtual method returns Base*."),
    ("Object Slicing Vector Trap", "Hard", ["Amazon", "Goldman Sachs"], "What happens if you store Derived objects inside a std::vector<Base> by value?", ["Polymorphism works seamlessly", "Object slicing occurs; derived data members and virtual behavior are stripped during insertion", "Compilation error", "Vector crashes dynamically"], 1, "Storing derived objects in std::vector<Base> by value slices off the derived portion of each object. To preserve polymorphism, store smart pointers: std::vector<std::unique_ptr<Base>>."),
    ("Static Method Virtual Trap", "Medium", ["Infosys", "Deloitte"], "Can a static method in C++ be declared virtual?", ["Yes, to allow static overriding", "No, compilation error: static methods cannot be virtual because they lack instance binding and this pointers", "Yes, if marked inline", "Only in template classes"], 1, "Static methods belong to the class scope and lack instance this pointers/vPtrs. Declaring a static method virtual produces a compilation error."),
    ("Friend Class Inheritance", "Medium", ["Tech Mahindra", "Cognizant"], "If class Child inherits from class Parent, does Child automatically inherit Parent's friend relationships?", ["Yes, friends are inherited automatically", "No, friendship is not inherited in C++", "Yes, if inheritance is public", "Only if marked virtual"], 1, "Friendship is not inherited. If class F is a friend of Parent, F does NOT automatically have friend access to private/protected members of derived class Child."),
    ("Dynamic Cast Null Pointer Check", "Medium", ["Qualcomm", "Samsung"], "What does dynamic_cast<Derived*>(basePtr) return if basePtr does NOT point to a Derived instance?", ["Throws std::bad_cast exception", "Returns nullptr", "Returns uninitialized garbage pointer", "Causes segmentation fault"], 1, "When dynamic_cast fails on pointer types, it safely returns nullptr. (When used on reference types dynamic_cast<Derived&>, failure throws std::bad_cast)."),
    ("Constructors Exception Safety", "Hard", ["Adobe", "ServiceNow"], "If an exception is thrown inside a C++ constructor before completion, will that object's destructor be called?", ["Yes, the destructor runs automatically", "No, because the object was never fully constructed; destructors for already-constructed subobjects run, but not the object's own destructor", "Yes, if using try-catch inside destructor", "The process terminates immediately"], 1, "In C++, an object's destructor is only invoked if its constructor successfully completes. If a constructor throws, destructors of fully constructed member subobjects are called, but the main destructor is NOT."),
]

for topic, diff, comps, q_text, opts, ans, exp in cpp_topics_data:
    questions.append(q(len(questions) + 1, "C++", diff, topic, comps, q_text, opts, ans, exp))

print(f"C++ Questions Generated: {len(questions)}")

# ==============================================================================
# JAVA QUESTIONS (85 - 167)
# ==============================================================================

questions.append(q(
    len(questions) + 1, "Java", "Easy", "Access Modifiers",
    ["TCS", "Infosys", "Wipro"],
    "Which access modifier in Java restricts member visibility to the containing class AND its subclasses, as well as classes within the same package?",
    ["private", "default (package-private)", "protected", "public"],
    2,
    "'protected' grants access to classes in the same package and subclasses in outside packages. 'private' is restricted to class scope, default is restricted to package scope, and public is unrestricted."
))

questions.append(q(
    len(questions) + 1, "Java", "Medium", "Super & This Keywords",
    ["Cognizant", "Accenture", "Capgemini"],
    "Inside a Java subclass constructor, which statement regarding super() and this() constructor calls is TRUE?",
    ["Both super() and this() can be called in any order inside a constructor", "super() or this() must be the very first statement in a constructor, and cannot both be called in the same constructor", "super() can only be called from static methods", "this() is used to call base class constructors"],
    1,
    "In Java, constructor chaining via this() or base initialization via super() MUST be the first statement in a constructor. Because both demand the first position, they cannot both appear in the same constructor."
))

questions.append(q(
    len(questions) + 1, "Java", "Medium", "Abstract Class vs Interface",
    ["Amazon", "Oracle", "IBM"],
    "Prior to Java 8, what was a primary distinction between an Abstract Class and an Interface?",
    ["Interfaces could hold instance state fields; abstract classes could not", "Abstract classes could contain concrete methods with implementations; interfaces could contain only abstract methods", "Abstract classes support multiple inheritance; interfaces do not", "Interfaces can have constructors; abstract classes cannot"],
    1,
    "Before Java 8, interfaces could only declare public abstract methods (no method bodies). Abstract classes can provide full concrete implementations, constructors, and instance fields."
))

questions.append(q(
    len(questions) + 1, "Java", "Easy", "Interface Default Methods",
    ["Infosys", "Deloitte", "LTIMindtree"],
    "Starting from Java 8, how can an interface provide a default method implementation without breaking implementing classes?",
    ["Using the concrete keyword", "Using the default keyword in the method signature (public default void log() { ... })", "Using static abstract blocks", "Using the final keyword"],
    1,
    "Java 8 introduced default methods in interfaces (default void msg() { ... }) allowing interfaces to add new functional implementations without breaking backward compatibility of existing implementing classes."
))

questions.append(q(
    len(questions) + 1, "Java", "Hard", "Interface Multiple Inheritance Trap",
    ["Microsoft", "Goldman Sachs", "Amazon"],
    "If a Java class implements two interfaces InterfaceA and InterfaceB that both declare an identical default method void show(), what happens?",
    ["InterfaceA show() takes priority automatically", "Compilation error occurs due to duplicate default methods unless the implementing class explicitly overrides show()", "Runtime exception is thrown when calling show()", "The compiler deletes both default methods"],
    1,
    "This is Java's interface default method conflict (diamond problem). The compiler cannot guess which default implementation to choose and emits a compilation error unless the implementing class explicitly overrides the conflicting method."
))

questions.append(q(
    len(questions) + 1, "Java", "Medium", "Final Keyword",
    ["Tech Mahindra", "Wipro", "TCS"],
    "What effect does declaring a Java class as final (public final class Security) have on inheritance?",
    ["The class cannot be instantiated", "The class cannot be subclassed/extended by any other class", "All methods of the class automatically become abstract", "The class can only contain static members"],
    1,
    "The final keyword applied to a class prevents inheritance (e.g. java.lang.String is final). When applied to a method, it prevents overriding; when applied to a variable, it makes it immutable/constant."
))

questions.append(q(
    len(questions) + 1, "Java", "Medium", "Static Keyword",
    ["Cognizant", "Accenture", "HCL"],
    "Can a static method in Java be overridden by a subclass?",
    ["Yes, runtime polymorphism applies to static methods", "No, static methods are bound at compile time; redeclaring a static method in a subclass hides it (method hiding) rather than overriding it", "Yes, if marked with @Override", "Only if the class is abstract"],
    1,
    "Static methods in Java belong to the class, not object instances. They are resolved via static binding at compile time. Defining a matching static method in a subclass results in 'method hiding', not overriding."
))

questions.append(q(
    len(questions) + 1, "Java", "Hard", "Covariant Return Type",
    ["Google", "Meta", "Adobe"],
    "What is a Covariant Return Type in Java method overriding?",
    ["Changing a method return type from primitive int to double in derived class", "Overriding a method with a return type that is a subclass of the return type declared in the parent class method", "Forcing a method to return Object", "Returning multiple values using tuples"],
    1,
    "Since Java 5, an overriding method in a subclass can declare a return type that is a subtype (derived class) of the return type declared in the superclass method."
))

questions.append(q(
    len(questions) + 1, "Java", "Medium", "Object Class equals and hashCode",
    ["JPMorgan", "Walmart Global Tech", "PayPal"],
    "What is the contract between equals() and hashCode() in Java?",
    ["If two objects are equal according to equals(), they MUST have the same hashCode() value", "If two objects have the same hashCode(), they MUST be equal according to equals()", "equals() and hashCode() are completely independent", "Overriding equals() automatically overrides hashCode()"],
    0,
    "The Java contract specifies: If objA.equals(objB) is true, then objA.hashCode() == objB.hashCode() MUST be true. However, equal hashCodes do NOT guarantee object equality due to hash collisions."
))

questions.append(q(
    len(questions) + 1, "Java", "Easy", "Encapsulation",
    ["TCS", "Infosys", "Capgemini"],
    "How is strict Encapsulation achieved in a Java JavaBean/POJO class?",
    ["By making all class variables public and methods private", "By declaring instance variables private and providing public getter and setter methods", "By marking the class as static", "By inheriting from java.lang.Encapsulated"],
    1,
    "Encapsulation hides internal object state by making instance variables private and exposing controlled access via public getter/setter accessor methods."
))

# Java Output Prediction
questions.append(q(
    len(questions) + 1, "Java", "Medium", "Output Prediction",
    ["TCS", "Wipro", "Infosys"],
    """What is the output of the following Java snippet?
class Test {
    public static void main(String[] args) {
        System.out.println(10 + 20 + "Java" + 10 + 20);
    }
}""",
    ["1020Java1020", "30Java1020", "30Java30", "Compilation Error"],
    1,
    "Expression evaluation proceeds left to right: 10 + 20 evaluates to integer 30. 30 + 'Java' performs string concatenation yielding '30Java'. Subsequent + 10 and + 20 concatenate as strings: '30Java1020'."
))

questions.append(q(
    len(questions) + 1, "Java", "Hard", "Output Prediction",
    ["Amazon", "Microsoft", "ServiceNow"],
    """What is the output of this Java initialization code?
class Parent {
    static { System.out.print("P_Static "); }
    { System.out.print("P_Init "); }
    Parent() { System.out.print("P_Cons "); }
}
class Child extends Parent {
    static { System.out.print("C_Static "); }
    { System.out.print("C_Init "); }
    Child() { System.out.print("C_Cons "); }
    public static void main(String[] args) {
        new Child();
    }
}""",
    ["P_Static C_Static P_Init P_Cons C_Init C_Cons", "P_Static P_Init P_Cons C_Static C_Init C_Cons", "C_Static P_Static C_Init C_Cons P_Init P_Cons", "P_Init P_Cons C_Init C_Cons P_Static C_Static"],
    0,
    "Initialization order in Java: 1. Parent Static block -> 2. Child Static block -> 3. Parent Instance init block -> 4. Parent Constructor -> 5. Child Instance init block -> 6. Child Constructor. Output: 'P_Static C_Static P_Init P_Cons C_Init C_Cons'."
))

questions.append(q(
    len(questions) + 1, "Java", "Medium", "Output Prediction",
    ["Oracle", "Cisco", "Qualcomm"],
    """What is the output of the following code?
class A {
    void print() { System.out.print("A "); }
}
class B extends A {
    void print() { System.out.print("B "); }
}
public class Test {
    public static void main(String[] args) {
        A obj = new B();
        obj.print();
    }
}""",
    ["A ", "B ", "A B ", "Compilation Error"],
    1,
    "In Java, all non-static methods are virtual by default. Dynamic method dispatch binds obj.print() to the actual runtime object B, printing 'B '."
))

questions.append(q(
    len(questions) + 1, "Java", "Hard", "Output Prediction Overloading Trap",
    ["Google", "Goldman Sachs", "Atlassian"],
    """What is the output of the following Java program?
public class OverloadTest {
    static void test(Object obj) { System.out.print("Object "); }
    static void test(String str) { System.out.print("String "); }
    public static void main(String[] args) {
        test(null);
    }
}""",
    ["Object ", "String ", "Compilation Error: Ambiguous", "NullPointerException at runtime"],
    1,
    "When resolving overloaded methods with null, Java compiler picks the MOST SPECIFIC matching method type. Since String is a subclass of Object, String is more specific, so test(String) is invoked, outputting 'String '."
))

questions.append(q(
    len(questions) + 1, "Java", "Medium", "Output Prediction",
    ["Accenture", "Cognizant", "Deloitte"],
    """What is the output of the following snippet?
class Parent {
    int x = 10;
}
class Child extends Parent {
    int x = 20;
}
public class Main {
    public static void main(String[] args) {
        Parent p = new Child();
        System.out.println(p.x);
    }
}""",
    ["10", "20", "0", "Compilation Error"],
    0,
    "In Java, variables (fields) are NOT polymorphic! Variable access is resolved statically at compile time based on the reference type (Parent p). Therefore, p.x accesses Parent.x, printing 10."
))

java_topics_data = [
    ("Anonymous Inner Class", "Medium", ["Infosys", "Wipro"], "What is an Anonymous Inner Class in Java?", ["A class declared without a name that is instantiated inline, often implementing an interface or extending a class", "A private static inner class", "A class created by garbage collector", "A class without any methods"], 0, "An anonymous inner class in Java allows declaring and instantiating a class on the fly without assigning it an explicit type name, commonly used for event listeners and thread runnables."),
    ("Static Inner Class vs Member Inner Class", "Hard", ["Amazon", "Microsoft"], "What is the key structural difference between a static nested class and an inner class in Java?", ["Static nested classes can access outer instance variables directly; member inner classes cannot", "Member inner classes hold an implicit reference to an instance of the outer class; static nested classes do not", "Static nested classes cannot have constructors", "Member inner classes cannot implement interfaces"], 1, "A member inner class is bound to an outer class instance and holds a reference to Outer.this. A static nested class is independent of outer instance state and cannot access non-static outer members directly."),
    ("Marker Interface", "Easy", ["TCS", "Accenture"], "What is a Marker Interface in Java?", ["An interface with default methods only", "An interface with zero fields and zero methods, used to convey metadata to the JVM (e.g. Serializable, Cloneable)", "An interface that marks a class as final", "An interface with static methods"], 1, "Marker (or tag) interfaces contain no method declarations. They act as type flags indicating to the JVM or frameworks that implementing classes possess specific runtime behaviors (e.g., Cloneable, Serializable)."),
    ("Functional Interface", "Easy", ["Cognizant", "Capgemini"], "What defines a Functional Interface in Java 8?", ["An interface with only default methods", "An interface containing exactly ONE abstract method (can be annotated with @FunctionalInterface)", "An interface that returns lambdas", "An interface marked static"], 1, "A Functional Interface in Java contains exactly one abstract method, making it eligible to be instantiated via Lambda expressions or method references."),
    ("Method Overloading Rules", "Medium", ["Tech Mahindra", "IBM"], "Can method overloading in Java be achieved by changing ONLY the access modifier of a method?", ["Yes, changing public to private overloads the method", "No, changing only the access modifier yields a compile error due to duplicate method signature", "Yes, if the method is static", "Yes, in abstract classes"], 1, "Method overloading requires changing the parameter list (number, type, or order of arguments). Altering access modifiers or return types alone produces a duplicate method compilation error."),
    ("Method Overriding Access Rules", "Hard", ["Oracle", "JPMorgan"], "When overriding a method in Java, what restriction applies to the access modifier of the derived class method?", ["The derived method must have a MORE restrictive access modifier", "The derived method CANNOT have a more restrictive access modifier than the superclass method", "The derived method must be declared private", "Access modifiers must be removed"], 1, "An overriding method cannot reduce the visibility of the base method. For example, if a base method is protected, the overriding method can be protected or public, but NOT default or private."),
    ("Instanceof Operator", "Easy", ["Wipro", "HCL"], "What does the instanceof operator in Java test?", ["Whether an object belongs to a class or implements an interface at runtime", "The size of an object in memory", "Whether a variable is static", "Whether an object is garbage collected"], 0, "The instanceof keyword tests whether an object reference is an instance of a specific class, subclass, or interface, returning a boolean true or false."),
    ("Composition vs Inheritance", "Medium", ["Deloitte", "LTIMindtree"], "Why is 'Composition over Inheritance' considered a recommended Object-Oriented design principle?", ["Composition allows dynamic change of behaviors at runtime ('has-a') and avoids tight coupling of inheritance ('is-a')", "Inheritance is deprecated in modern Java", "Composition speeds up compilation time", "Composition eliminates private access"], 0, "Composition builds complex objects by combining simpler objects ('has-a' relationship). It avoids fragile base class issues and tight coupling associated with inheritance hierarchies ('is-a')."),
    ("Aggregation vs Composition", "Hard", ["Goldman Sachs", "Amazon"], "What is the key difference between Aggregation and Composition in OOP?", ["In Aggregation, child objects cannot exist without parent; in Composition, they can", "In Composition, child objects cannot exist independently of parent object lifetime (strong relationship); in Aggregation, children exist independently (weak relationship)", "Aggregation applies to interfaces; Composition applies to abstract classes", "There is no difference"], 1, "Composition represents a strong ownership relationship (e.g. House and Room: if House is destroyed, Rooms perish). Aggregation represents a weak relationship (e.g. Department and Teacher: Teachers exist independently if Department closes)."),
    ("Immutable Class Creation", "Hard", ["Google", "ServiceNow"], "Which of the following steps is REQUIRED to create a custom Immutable Class in Java?", ["Declare class as final, make fields private final, do not provide setters, and perform deep defensive copies of mutable fields in getters/constructors", "Make all methods static", "Inherit from java.lang.Immutable", "Implement Cloneable"], 0, "Creating immutable classes (like String) requires a final class, private final fields, no setters, and defensive copying of mutable objects (like Date or List) during construction and access."),
    ("Upcasting and Downcasting", "Medium", ["Infosys", "TCS"], "In Java, what happens when performing Downcasting without type checking (Child c = (Child) parentObj;) when parentObj is actually an instance of Parent?", ["Compilation error occurs", "ClassCastException is thrown at runtime", "c becomes null", "Object is sliced automatically"], 1, "Downcasting an object reference to a derived type that it does not actually instantiate compiles successfully, but throws a ClassCastException at runtime."),
    ("Abstract Class Constructor", "Medium", ["Accenture", "Cognizant"], "Can an abstract class in Java have constructors, and how are they executed?", ["No, abstract classes cannot have constructors", "Yes, abstract class constructors exist and are called when a concrete subclass is instantiated via super()", "Yes, but they can only be invoked statically", "Only default private constructors are allowed"], 1, "Abstract classes have constructors to initialize fields defined in the abstract class. They run automatically during subclass instantiation when super() executes."),
    ("Interface Static Methods", "Easy", ["Wipro", "Capgemini"], "Can static methods in Java 8 interfaces be overridden by implementing classes?", ["Yes, they behave like default methods", "No, static interface methods cannot be overridden or inherited; they must be invoked using the interface name (InterfaceName.method())", "Yes, if annotated with @Override", "Only in functional interfaces"], 1, "Static interface methods in Java belong strictly to the interface namespace. They are not inherited by implementing classes and cannot be overridden."),
    ("Final Variable Initialization", "Medium", ["Tech Mahindra", "IBM"], "Where MUST a blank final instance variable in Java be initialized?", ["Inside the main() method", "Either at declaration time or inside all class constructors (or instance initializer block)", "In a static block", "It is automatically initialized to zero"], 1, "A blank final instance variable must be assigned a value exactly once before constructor execution completes (either at field declaration, in instance initializer block, or in every constructor)."),
    ("Finalize Method Deprecation", "Medium", ["Oracle", "Cisco"], "Why was the finalize() method deprecated in Java 9?", ["Because it caused compilation errors", "Because it is unpredictable, unsafe, introduces performance degradation, and can cause deadlocks/object resurrection issues", "Because Java eliminated garbage collection", "Because interfaces replaced it"], 1, "finalize() execution timing is non-deterministic and unreliable. Java 9 deprecated it in favor of explicit resource cleanup mechanisms like AutoCloseable and Cleaner."),
    ("Try with Resources", "Easy", ["Deloitte", "LTIMindtree"], "What interface must a Java class implement to be used within a Try-With-Resources block (try (Resource r = new Resource()))?", ["java.lang.Cloneable", "java.lang.AutoCloseable (or Closeable)", "java.io.Serializable", "java.lang.Runnable"], 1, "Try-With-Resources automatically closes managed resources when exiting the block. Any class used must implement AutoCloseable or Closeable."),
    ("Shallow vs Deep Copy in Java", "Medium", ["JPMorgan", "Amazon"], "What is performed by the default Object.clone() method in Java?", ["Deep copy of all nested object references", "Shallow copy (field-by-field copy of primitives and reference addresses)", "Serializes object to JSON", "Returns an uninitialized instance"], 1, "Object.clone() creates a shallow copy. Primitives are copied by value, but object reference fields copy only pointer references, resulting in shared mutable subobjects."),
    ("Garbage Collection and OOP", "Easy", ["TCS", "Infosys"], "Does calling System.gc() in Java guarantee immediate garbage collection of unreachable objects?", ["Yes, it forces instant memory deallocation", "No, it is merely a request/hint to the JVM to run garbage collection; execution is not guaranteed", "Yes, if memory is low", "It throws a runtime exception"], 1, "System.gc() suggests to the JVM that garbage collection be run, but the JVM specification does not guarantee that the GC will execute immediately or at all."),
    ("Package-Private Access", "Easy", ["Cognizant", "Accenture"], "What is the access level of a class member in Java if no access modifier keyword (public, protected, private) is specified?", ["public", "private", "default / package-private (accessible only within the same package)", "protected"], 2, "If no access modifier is specified, the member defaults to package-private access, meaning it is accessible to all classes in the same package, but hidden from outside packages."),
    ("Static Block Execution", "Medium", ["Capgemini", "IBM"], "When is a static initialization block in a Java class executed?", ["When an object of the class is created", "Exactly once when the JVM loads the class into memory", "Every time a static method is called", "When garbage collector cleans the class"], 1, "Static initializer blocks run exactly once when the class is loaded into the JVM by the ClassLoader, prior to any object instantiation or method calls."),
    ("Constructor Chaining", "Medium", ["Wipro", "HCL"], "What is Constructor Chaining in Java?", ["Calling static methods from constructors", "The process of calling one constructor from another constructor within the same class (using this()) or base class (using super())", "Linking multiple classes together", "Inheriting constructors from interfaces"], 1, "Constructor chaining allows constructors to pass initialization responsibilities up the class hierarchy or across overloaded constructors in the same class."),
    ("Strictfp Keyword", "Hard", ["Goldman Sachs", "Nvidia"], "What was the purpose of the strictfp keyword in Java?", ["To enforce strict thread synchronization", "To restrict floating-point calculations to IEEE 754 standards across different CPU architectures for consistent results", "To force strict memory management", "To restrict subclassing"], 1, "strictfp (strict floating point) ensured that floating-point calculations produced identical results across all hardware platforms by adhering strictly to IEEE 754 floating-point standards."),
    ("Transient Keyword", "Medium", ["PayPal", "ServiceNow"], "What does the transient keyword signify when applied to an instance variable in a Java class?", ["The variable is stored in temporary CPU registers", "The variable should be skipped (ignored) during object Serialization", "The variable is shared across threads", "The variable cannot be modified"], 1, "Marking a variable transient prevents it from being persisted during serialization, useful for sensitive data (passwords) or dynamic cache fields."),
    ("Volatile Keyword Java", "Hard", ["Amazon", "Google"], "What guarantee does the volatile keyword provide for a variable in Java multithreading?", ["Ensures atomic operation for complex calculations", "Guarantees read/write visibility directly from main memory across threads, preventing thread-caching in CPU registers", "Locks the variable with a mutex", "Prevents garbage collection"], 1, "volatile guarantees visibility of changes to variables across threads by forcing reads and writes directly to main memory instead of CPU caches. It does NOT guarantee atomicity for compound operations (e.g. count++)."),
    ("Polymorphism Definition", "Easy", ["Infosys", "TCS"], "Dynamic Method Dispatch in Java is a mechanism by which a call to an overridden method is resolved at:", ["Compile time", "Runtime", "Link time", "Packaging time"], 1, "Dynamic method dispatch is Java's runtime polymorphism mechanism where calls to overridden instance methods are resolved dynamically at runtime based on the actual object type."),
    ("Abstract Method Rules", "Easy", ["Accenture", "Cognizant"], "Can a method in Java be declared both abstract and final?", ["Yes, to enforce override rules", "No, compile error: abstract mandates overriding while final prohibits overriding", "Yes, in interfaces only", "Yes, if the method is private"], 1, "abstract demands that subclasses override the method body, whereas final prohibits overriding. Declaring a method both abstract and final causes an immediate compilation conflict."),
    ("Private Method Overriding Trap", "Medium", ["Deloitte", "LTIMindtree"], "If a superclass has a private void display() method, and a subclass defines a public void display() method, is this considered Method Overriding?", ["Yes, it is runtime overriding", "No, private methods are hidden from subclasses; the subclass method is an independent new method, not an override", "Compilation error due to access mismatch", "Yes, with covariant return type"], 1, "Private methods are not visible to subclasses and cannot be overridden. The subclass method simply creates a new, unrelated method in its own scope."),
    ("Interface Variables", "Easy", ["Wipro", "Tech Mahindra"], "All variables declared inside a Java interface are implicitly:", ["private static final", "public static final", "protected final", "public volatile"], 1, "Fields in interfaces are automatically public static final constants, regardless of whether those keywords are explicitly written."),
    ("Diamond Inheritance in Interfaces", "Medium", ["Oracle", "Cisco"], "Why does Java permit multiple interface inheritance but forbid multiple class inheritance?", ["Interfaces do not carry instance state (fields), avoiding state duplication/ambiguity inherent in class multiple inheritance", "Interfaces run faster", "Classes use virtual tables", "Interfaces cannot have methods"], 0, "Class multiple inheritance introduces state collisions (duplicate fields). Since interfaces historically held no state fields, Java allowed multiple interface implementation without diamond state corruption."),
    ("Enum in Java OOP", "Medium", ["Capgemini", "IBM"], "Can Java enum types implement interfaces and declare methods/constructors?", ["No, enums are primitive constants only", "Yes, Java enums are full-fledged classes that can have methods, constructors, fields, and implement interfaces", "Enums can implement interfaces but cannot have constructors", "Enums can extend abstract classes"], 1, "In Java, enum is a rich class type. Enums can implement interfaces, hold private constructors, possess instance fields, and define concrete or abstract methods."),
    ("Class Load Order Static Trap", "Hard", ["Goldman Sachs", "Amazon"], "What happens if a static field initializer calls a static method of the same class before that static block completes?", ["NullPointerException", "Method executes using default initial values (e.g. 0 or null) of uninitialized static fields", "Compilation error", "Infinite recursion"], 1, "Static fields are initialized in textual order. If a method reads a static variable before its static initializer has executed, it receives the default type value (0, false, null)."),
    ("Default Constructor Generation", "Easy", ["TCS", "Infosys"], "When does the Java compiler automatically generate a zero-argument Default Constructor for a class?", ["Always for every class", "ONLY when NO explicit constructors are defined in the class body", "When the class is marked public", "When the class extends another class"], 1, "If a class defines NO constructors, the compiler inserts a public no-arg default constructor. Once any custom constructor (e.g., parameterized) is declared, the default constructor is NOT generated automatically."),
    ("Inner Class Static Declaration", "Medium", ["Cognizant", "Accenture"], "Prior to Java 16, could a non-static member inner class declare static methods or static fields (non-constant)?", ["Yes, freely", "No, non-static inner classes could not declare static members (unless static final constants) compile error", "Yes, if marked private", "Yes, in abstract classes"], 1, "Before Java 16, non-static inner classes were tied to outer instances and could not contain static members (except compile-time static final constants). Java 16 relaxed this restriction."),
    ("Anonymous Class Interface Trap", "Medium", ["Wipro", "HCL"], "Can an anonymous class in Java implement multiple interfaces simultaneously during instantiation?", ["Yes, using the & operator", "No, an anonymous class can extend exactly one class OR implement exactly one interface at instantiation time", "Yes, using comma separation", "Only if interfaces are marker interfaces"], 1, "The syntax for anonymous classes (new InterfaceName() { ... }) allows extending one class or implementing one single interface per expression."),
    ("Super In Static Context Trap", "Easy", ["Deloitte", "LTIMindtree"], "What happens if you attempt to use super or this inside a static method in Java?", ["It accesses static parent variables", "Compilation error: non-static variable super/this cannot be referenced from a static context", "Runtime exception", "Accesses global namespace"], 1, "static methods exist independently of object instances and lack instance context (this or super). Referencing this or super inside static methods causes a compile error."),
    ("Equals method signature trap", "Hard", ["Adobe", "Microsoft"], "What is the mistake in this code: public boolean equals(Student s) { return this.id == s.id; }?", ["Method overloads Object.equals(Object) instead of overriding it, causing polymorphic collections (like HashSet) to call Object.equals()", "Syntax error in parameter", "Equals cannot return boolean", "Should be static"], 0, "The correct method signature for overriding Object.equals is equals(Object obj). Parameterizing with Student s overloads the method instead of overriding, breaking polymorphic collections."),
    ("Overriding Exception Rules", "Hard", ["Amazon", "Goldman Sachs"], "If a superclass method declares void process() throws IOException, what checked exceptions can an overriding subclass method declare?", ["Any checked exception including Exception", "Only IOException, any subclass of IOException, or NO checked exceptions at all", "Must declare exactly IOException", "Must declare RuntimeException only"], 1, "An overriding method can declare fewer or narrower checked exceptions than the superclass method, or no checked exceptions at all. It CANNOT declare new or broader checked exceptions."),
    ("Pass by Value Java Trap", "Medium", ["Infosys", "TCS"], "Is Java 'Pass-by-Value' or 'Pass-by-Reference' when passing object references to methods?", ["Pass-by-Reference", "Pass-by-Value (the object reference copy is passed by value)", "Pass-by-Reference for objects, Pass-by-Value for primitives", "Pass-by-Name"], 1, "Java is strictly Pass-by-Value. When passing an object, a copy of the reference pointer is passed by value. Reassigning the parameter pointer inside the method does not change the caller's reference."),
    ("Records in Java 14+", "Medium", ["Oracle", "ServiceNow"], "What feature was introduced in Java 14/16 (public record Point(int x, int y) {}) to simplify immutable data carrier classes?", ["Dataclasses", "Records (automatically generating getters, equals, hashCode, toString, and final fields)", "Structs", "Tuples"], 1, "Java Records provide a concise syntax for creating immutable data transfer objects (DTOs), automatically creating private final fields, constructor, getters, equals(), hashCode(), and toString()."),
    ("Sealed Classes Java 17", "Hard", ["Google", "Meta"], "What is the primary function of sealed classes introduced in Java 17 (public sealed class Shape permits Circle, Square)?", ["To restrict which subclasses are permitted to extend or implement the class/interface", "To encrypt class bytecode", "To prevent class loading at runtime", "To enforce singleton pattern"], 0, "Sealed classes restrict class inheritance hierarchies by explicitly defining via permits which subclasses are authorized to extend the sealed parent."),
]

for topic, diff, comps, q_text, opts, ans, exp in java_topics_data:
    questions.append(q(len(questions) + 1, "Java", diff, topic, comps, q_text, opts, ans, exp))

print(f"Java Questions Generated: {len(questions)}")

# ==============================================================================
# PYTHON QUESTIONS (168 - 250)
# ==============================================================================

questions.append(q(
    len(questions) + 1, "Python", "Easy", "Constructors & init",
    ["TCS", "Infosys", "Wipro"],
    "In Python, what is the role of the __init__ method in a class?",
    ["To allocate memory for the object (constructor)", "To initialize instance attributes after object allocation", "To delete the object from memory", "To convert object to string"],
    1,
    "__init__ is the instance initializer method called immediately after the object has been created by __new__. It initializes the instance's attributes."
))

questions.append(q(
    len(questions) + 1, "Python", "Hard", "Object Creation __new__ vs __init__",
    ["Amazon", "Google", "Meta"],
    "What is the key difference between __new__ and __init__ in Python OOP?",
    ["__init__ creates the object and returns it; __new__ initializes attributes", "__new__ is the actual static creator method that returns a new instance; __init__ receives that instance (self) to initialize attributes", "__new__ is called after __init__", "There is no difference"],
    1,
    "__new__ is the actual constructor method responsible for instantiating and returning a new object instance. __init__ is the initializer called with self to set up instance attributes."
))

questions.append(q(
    len(questions) + 1, "Python", "Medium", "Self Parameter",
    ["Cognizant", "Accenture", "Capgemini"],
    "Why must instance methods in Python explicitly declare self as their first parameter?",
    ["self is a reserved CPython language keyword", "self represents the binding reference to the specific instance invoking the method", "Because Python does not support pointers", "To make methods public"],
    1,
    "Python passes the calling object instance automatically as the first argument when an instance method is called (obj.method() translates to Class.method(obj)). self is the conventional parameter name for this reference."
))

questions.append(q(
    len(questions) + 1, "Python", "Hard", "MRO & C3 Linearization",
    ["Meta", "Netflix", "Google"],
    "In Python multiple inheritance, what algorithm determines the Method Resolution Order (MRO)?",
    ["Depth-First Search (DFS)", "Breadth-First Search (BFS)", "C3 Linearization Algorithm", "Dijkstra's Shortest Path"],
    2,
    "Python 2.3+ uses the C3 Linearization Algorithm to compute Method Resolution Order (MRO), guaranteeing monotonic class precedence and respecting local precedence order."
))

questions.append(q(
    len(questions) + 1, "Python", "Medium", "Name Mangling",
    ["Adobe", "Goldman Sachs", "Amazon"],
    "How does Python perform Name Mangling for private attributes declared with double leading underscores (e.g., __secret) inside class Vault?",
    ["It encrypts the variable in memory", "It renames __secret internally to _Vault__secret to prevent accidental overriding by subclasses", "It throws an AttributeError if accessed anywhere", "It converts the attribute to a read-only tuple"],
    1,
    "Python mangles private identifiers containing at least two leading underscores by prefixing them with _ClassName. __secret inside Vault becomes _Vault__secret."
))

questions.append(q(
    len(questions) + 1, "Python", "Easy", "Class vs Instance Variables",
    ["Infosys", "TCS", "Wipro"],
    "What happens when you assign a value to a variable defined at class level via an object instance (obj.class_var = 10) in Python?",
    ["It updates the class variable for all instances", "It creates a new instance variable on obj that shadows the class variable", "It raises an AttributeError", "It modifies the class definition dynamically"],
    1,
    "Assigning via an instance (obj.class_var = 10) creates a new instance attribute on obj. The underlying class variable remains untouched for other instances."
))

questions.append(q(
    len(questions) + 1, "Python", "Medium", "Classmethod vs Staticmethod",
    ["Microsoft", "Oracle", "Cisco"],
    "What is the difference between @classmethod and @staticmethod decorators in Python?",
    ["@classmethod receives the class (cls) as implicit first argument; @staticmethod receives no implicit first argument", "@staticmethod receives self; @classmethod receives nothing", "@classmethod cannot access class variables", "@staticmethod can only be called from instances"],
    0,
    "@classmethod passes the class object (cls) automatically as first parameter (useful for factory methods). @staticmethod acts like an un-bound plain function scoped inside the class namespace."
))

questions.append(q(
    len(questions) + 1, "Python", "Medium", "Property Decorator",
    ["ServiceNow", "Flipkart", "PayPal"],
    "What is the primary use of the @property decorator in Python OOP?",
    ["To make a class immutable", "To define getter/setter methods that allow accessing methods using simple attribute dot notation (obj.attr)", "To register properties in a database", "To make variables thread-safe"],
    1,
    "The @property decorator converts a class method into a read-only getter attribute, allowing users to access obj.temperature instead of obj.get_temperature(), with optional @setter decorators."
))

questions.append(q(
    len(questions) + 1, "Python", "Hard", "Duck Typing",
    ["Google", "Uber", "Amazon"],
    "What concept in Python OOP is summarized by 'If it walks like a duck and quacks like a duck, it's a duck'?",
    ["Explicit Interface Inheritance", "Duck Typing (dynamic typing where an object's suitability is determined by presence of methods/attributes, not inheritance)", "Abstract Type Casting", "Metaclass Enforcement"],
    1,
    "Duck Typing prioritizes an object's behavior (methods and attributes) over its explicit class inheritance hierarchy. If an object implements read(), it can be treated as a file-like object regardless of its class."
))

questions.append(q(
    len(questions) + 1, "Python", "Easy", "Dunder Methods __str__ vs __repr__",
    ["TCS", "Accenture", "Cognizant"],
    "What is the functional difference between __str__ and __repr__ in Python?",
    ["__str__ is for developer debugging; __repr__ is for end users", "__str__ returns an informal user-friendly string; __repr__ returns an unambiguous representation (ideally valid Python code) for debugging", "__repr__ is called by print(); __str__ by repr()", "They are identical"],
    1,
    "__str__ targets human readability (called by str() and print()). __repr__ targets developer debugging and explicit representation (called by repr() or in interactive shells)."
))

# Python Output Prediction
questions.append(q(
    len(questions) + 1, "Python", "Medium", "Output Prediction",
    ["TCS", "Infosys", "Wipro"],
    """What is the output of the following Python code?
class Count:
    num = 0
    def __init__(self):
        Count.num += 1

c1 = Count()
c2 = Count()
c3 = Count()
print(c1.num, Count.num)""",
    ["1 3", "3 3", "1 1", "0 3"],
    1,
    "num is a class variable shared across all instances. Instantiating c1, c2, and c3 increments Count.num three times to 3. Accessing c1.num resolves to Count.num (since c1 has no instance shadow), printing '3 3'."
))

questions.append(q(
    len(questions) + 1, "Python", "Hard", "Output Prediction Mutable Default",
    ["Amazon", "Microsoft", "Python Technical"],
    """What is the output of this Python class snippet?
class Student:
    def __init__(self, name, marks=[]):
        self.name = name
        self.marks = marks
    def add_mark(self, mark):
        self.marks.append(mark)

s1 = Student("Alice")
s1.add_mark(90)
s2 = Student("Bob")
print(s2.marks)""",
    ["[]", "[90]", "None", "AttributeError"],
    1,
    "Mutable default arguments (marks=[]) in Python functions/methods are evaluated once at definition time, NOT per call! s1 and s2 share the exact same default list object in memory, so s2.marks prints [90]."
))

questions.append(q(
    len(questions) + 1, "Python", "Hard", "Output Prediction Super MRO",
    ["Google", "Meta", "Adobe"],
    """What is the output of the following MRO diamond code?
class A:
    def show(self):
        print("A", end="")

class B(A):
    def show(self):
        print("B", end="")
        super().show()

class C(A):
    def show(self):
        print("C", end="")
        super().show()

class D(B, C):
    def show(self):
        print("D", end="")
        super().show()

d = D()
d.show()""",
    ["DBCA", "DBAC", "DCBA", "DBA"],
    0,
    "Python's MRO for D(B, C) is [D, B, C, A, object]. super() delegates calls down the MRO chain: D prints 'D' -> super() calls B ('B') -> B's super() calls C ('C') -> C's super() calls A ('A'). Output: 'DBCA'."
))

questions.append(q(
    len(questions) + 1, "Python", "Medium", "Output Prediction Name Mangling",
    ["Goldman Sachs", "Qualcomm", "Nvidia"],
    """What happens when executing the following Python code?
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

acc = BankAccount(1000)
print(acc.__balance)""",
    ["1000", "AttributeError: 'BankAccount' object has no attribute '__balance'", "None", "0"],
    1,
    "Double underscores trigger name mangling. Attribute __balance is mangled to _BankAccount__balance. Accessing acc.__balance directly raises AttributeError."
))

python_topics_data = [
    ("Abstract Base Classes (abc)", "Medium", ["Infosys", "Deloitte"], "How do you define an Abstract Class in Python?", ["By inheriting from abc.ABC and annotating methods with @abstractmethod", "Using the abstract class keyword", "By raising NotImplementedError in __init__", "By setting __abstract__ = True"], 0, "Python provides the abc module. An abstract class inherits from abc.ABC and marks abstract methods using the @abstractmethod decorator."),
    ("Slots Magic (__slots__)", "Hard", ["Meta", "Amazon"], "What is the primary memory optimization purpose of __slots__ in Python classes?", ["To restrict inheritance", "To replace the dynamic __dict__ dictionary with a fixed array of attributes, drastically saving memory for millions of instances", "To make methods static", "To speed up module imports"], 1, "By defining __slots__ = ('name', 'age'), Python prevents the creation of an instance __dict__, reducing memory footprint per object and preventing dynamic assignment of arbitrary attributes."),
    ("Dataclasses Python 3.7+", "Easy", ["Microsoft", "Oracle"], "What decorator was added in Python 3.7 (from dataclasses import dataclass) to automate __init__, __repr__, and __eq__ boilerplate code?", ["@dataclass", "@struct", "@record", "@model"], 0, "The @dataclass decorator automatically generates special boilerplate methods such as __init__(), __repr__(), and __eq__() based on class type annotations."),
    ("Operator Overloading Dunder", "Medium", ["TCS", "Accenture"], "Which magic method must be implemented to overload the addition operator (+) for custom class objects in Python?", ["__add__(self, other)", "__plus__(self, other)", "__concat__(self, other)", "__sum__(self, other)"], 0, "Implementing __add__(self, other) allows custom class objects to define behavior when operated on with the + arithmetic operator."),
    ("Callable Objects (__call__)", "Medium", ["Cognizant", "Wipro"], "What does implementing the __call__ method allow an instance of a Python class to do?", ["Be deleted by garbage collector", "Be invoked directly like a function (obj())", "Be converted to a dictionary", "Be executed inside a thread"], 1, "Implementing __call__(self, *args, **kwargs) makes an instance 'callable', allowing it to be invoked with parentheses like a regular function."),
    ("Context Managers (__enter__ and __exit__)", "Hard", ["Google", "ServiceNow"], "Which two magic methods must a class implement to support Python's with statement context management protocol?", ["__open__ and __close__", "__enter__ and __exit__", "__start__ and __stop__", "__init__ and __del__"], 1, "The context manager protocol requires __enter__(self) (executed upon entering with block) and __exit__(self, exc_type, exc_val, exc_tb) (executed upon leaving with block)."),
    ("Mixins in Python", "Medium", ["Flipkart", "PayPal"], "What is a Mixin class in Python OOP design?", ["A class that holds global main functions", "A small, focused parent class designed to provide optional reusable functionality to subclasses via multiple inheritance, without being instantiated standalone", "A class that mixes C and Python code", "An abstract class with no methods"], 1, "Mixins are specialized classes that offer discrete bundle of methods (e.g., JSONSerializerMixin) meant to be inherited alongside a primary base class."),
    ("Metaclasses Basics", "Hard", ["Nvidia", "Uber"], "What is a Metaclass in Python?", ["A subclass of object", "A class whose instances are classes themselves (a 'class of a class', typically inheriting from type)", "A class that generates C code", "A decorator for functions"], 1, "In Python, classes are themselves instances of metaclasses. The default metaclass is type. Metaclasses allow intercepting and customizing class creation behavior."),
    ("Iterators Protocol (__iter__ and __next__)", "Medium", ["Capgemini", "IBM"], "What two magic methods make a Python object an Iterator that can be used in a for loop?", ["__iter__ and __next__", "__start__ and __loop__", "__get__ and __set__", "__len__ and __getitem__"], 0, "The Iterator protocol requires __iter__() (returns the iterator object itself) and __next__() (returns the next item or raises StopIteration)."),
    ("Polymorphism via Duck Typing", "Easy", ["Tech Mahindra", "Infosys"], "Does Python require abstract interfaces or explicit base inheritance to achieve runtime polymorphism?", ["Yes, explicit interface declarations are mandatory", "No, Python relies on Duck Typing; as long as objects expose required method names, polymorphic calls succeed", "Yes, using C extensions", "Only if marked static"], 1, "Python is dynamically typed and leverages Duck Typing for polymorphism. Methods are resolved by name at runtime regardless of formal class hierarchy."),
    ("Isinstance vs Type in Python", "Medium", ["Wipro", "HCL"], "Why is isinstance(obj, Base) preferred over type(obj) == Base for checking object types in Python?", ["isinstance is 10x faster", "isinstance accounts for class inheritance (returns True for derived instances), whereas direct type() comparison fails for subclasses", "type() is deprecated", "isinstance works on C code only"], 1, "isinstance(obj, Class) returns True if obj is an instance of Class OR any subclass derived from Class, making it inheritance-aware."),
    ("Super() built-in Python 3", "Easy", ["TCS", "Deloitte"], "In Python 3, how do you invoke the base class constructor from inside a derived class __init__ method?", ["super().__init__()", "Parent.__init__()", "this.super()", "base().__init__()"], 0, "Python 3 simplifies super() calls: inside a method, calling super().__init__() automatically resolves the correct MRO base class and passes self implicitly."),
    ("Single Leading Underscore", "Easy", ["Cognizant", "LTIMindtree"], "What does a single leading underscore in a variable name (e.g. _internal_var) signify in Python?", ["It is strictly enforced by CPython compiler as private", "It is a naming convention indicating that the variable/method is intended for internal use only", "It deletes the variable automatically", "It makes the variable thread-local"], 1, "A single leading underscore _var is a strong PEP 8 convention signaling 'internal implementation detail'. It also prevents importing by from module import *."),
    ("Single Trailing Underscore", "Easy", ["Accenture", "Infosys"], "Why would a Python programmer append a single trailing underscore to a variable name (e.g., class_)?", ["To make it private", "To avoid naming conflicts with Python reserved keywords (e.g. class, def, in)", "To convert it to float", "To store it in slots"], 1, "PEP 8 recommends appending a single trailing underscore (e.g., class_, type_) to avoid collisions with Python built-in keywords."),
    ("Deleting Object Attributes", "Easy", ["IBM", "Wipro"], "Which statement deletes an attribute age from an instance person in Python?", ["del person.age", "remove person.age", "person.age = None", "delete(person.age)"], 0, "The del statement (del person.age) removes the attribute binding from the instance dictionary person.__dict__."),
    ("Copy module shallow vs deep", "Medium", ["Goldman Sachs", "Amazon"], "Which module function in Python creates a deep copy of a nested object graph containing custom class instances?", ["copy.copy()", "copy.deepcopy()", "clone()", "object.copy()"], 1, "copy.deepcopy() recursively copies compound objects and all nested object references, producing an independent object hierarchy."),
    ("Class Decorators", "Medium", ["Microsoft", "Oracle"], "What is a Class Decorator in Python?", ["A decorator applied to class definitions (@decorator class MyClass:) that receives the class object and can modify or wrap it", "A method decorator", "A decorator for variables", "A CSS style for classes"], 0, "A Class Decorator takes a class object as its argument, inspects or modifies its structure, and returns the modified or wrapped class."),
    ("Encapsulation via Getters/Setters", "Medium", ["JPMorgan", "ServiceNow"], "In Python, what is the idiomatic way to add validation to an existing attribute age without altering external client access code (obj.age)?", ["Refactor age to get_age() and update all callers", "Convert age into a @property with a @age.setter method containing validation logic", "Make age static", "Use C extensions"], 1, "Python's @property decorator allows wrapping attribute access with getter/setter methods transparently without breaking client code that uses attribute dot notation (obj.age = 25)."),
    ("Subclassing Built-in Types", "Hard", ["Google", "Meta"], "When inheriting from built-in Python types like dict or list, why is inheriting from collections.UserDict or collections.UserList often preferred?", ["Built-in C-implemented methods of dict often bypass overridden methods in Python subclasses", "UserDict is faster", "dict does not support inheritance", "UserDict supports static typing"], 0, "Built-in types implemented in C (like dict or list) often skip calls to overridden methods in subclasses when invoked by internal C routines. collections.UserDict is written in pure Python and guarantees method dispatch."),
    ("String representation Dunder trap", "Medium", ["TCS", "Infosys"], "If a class defines __repr__ but DOES NOT define __str__, what happens when str(obj) or print(obj) is called?", ["Python falls back to executing __repr__", "Raises AttributeError", "Prints memory address", "Returns empty string"], 0, "If __str__ is omitted, Python automatically falls back to calling __repr__ to generate string output for str() and print()."),
    ("Comparison Dunder Methods", "Medium", ["Cognizant", "Capgemini"], "Which magic method must be implemented to support the less-than operator (<) for custom objects in Python?", ["__lt__(self, other)", "__less__(self, other)", "__cmp__(self, other)", "__min__(self, other)"], 0, "__lt__(self, other) implements the < comparison operator. Python's @functools.total_ordering decorator can generate remaining comparison methods if __eq__ and __lt__ are provided."),
    ("Dict representation of instance", "Easy", ["Wipro", "Tech Mahindra"], "What attribute of a Python class instance holds its user-defined dynamic instance variables in dictionary format?", ["__dict__", "__vars__", "__slots__", "__map__"], 0, "An instance's user-defined attributes are stored in its writable dictionary attribute __dict__ (unless __slots__ is defined)."),
    ("Callable object state preservation", "Hard", ["Adobe", "ServiceNow"], "What advantage does a callable object (class implementing __call__) have over a standard function in Python?", ["It can maintain state across invocations within instance attributes", "It executes faster", "It can bypass Python GIL", "It supports static compilation"], 0, "Unlike plain functions, callable class instances maintain state across calls within self attributes, serving as object-oriented function closures."),
]

design_patterns_solid = [
    ("SOLID - Single Responsibility Principle", "Python", "Easy", "SOLID Principles", ["Amazon", "Microsoft"], "What does the Single Responsibility Principle (SRP) dictate?", ["A class should have one, and only one, reason to change (single responsibility)", "A class should have only one method", "A class should inherit from only one parent", "A class should be instantiated once"], 0, "SRP states that a class should be focused on a single logical responsibility, ensuring that changes to one feature domain do not break unrelated components."),
    ("SOLID - Open/Closed Principle", "Java", "Medium", "SOLID Principles", ["Google", "Oracle"], "According to the Open/Closed Principle (OCP), software entities should be:", ["Open for extension, but closed for modification", "Open for modification, but closed for extension", "Open for public access, but closed for private access", "Open for reading, closed for writing"], 0, "OCP dictates that classes should be designed so that new behavior can be added via extension (subclassing, interfaces, plugins) without modifying existing, tested source code."),
    ("SOLID - Liskov Substitution Principle", "C++", "Hard", "SOLID Principles", ["Meta", "Adobe"], "What is the core requirement of the Liskov Substitution Principle (LSP)?", ["Objects of a superclass should be replaceable with objects of a subclass without affecting program correctness", "Derived classes must always override all base methods", "Base class pointers must be cast using reinterpret_cast", "Subclasses must add new public methods"], 0, "LSP requires that derived types must be completely substitutable for their base types without breaking client code expectations or invariant contracts."),
    ("SOLID - Interface Segregation Principle", "Java", "Medium", "SOLID Principles", ["ServiceNow", "Flipkart"], "What does the Interface Segregation Principle (ISP) advocate?", ["Clients should not be forced to depend upon interfaces/methods they do not use (prefer small, specific interfaces)", "All classes must implement at least 5 interfaces", "Interfaces must inherit from Object", "Interfaces should contain large monolithic method groups"], 0, "ISP states that large, bloated interfaces should be split into smaller, specific interfaces so that implementing classes only need to care about methods relevant to them."),
    ("SOLID - Dependency Inversion Principle", "C++", "Hard", "SOLID Principles", ["Goldman Sachs", "JPMorgan"], "What does the Dependency Inversion Principle (DIP) state?", ["High-level modules should not depend on low-level modules; both should depend on abstractions (interfaces)", "Low-level modules should control high-level modules", "Classes should depend directly on concrete implementations", "Functions should invert control flow using goto"], 0, "DIP decouples high-level policy code from low-level execution details by introducing abstract interfaces between them, facilitating dependency injection."),
    ("Design Patterns - Singleton", "Java", "Medium", "Design Patterns", ["TCS", "Infosys"], "Which Design Pattern ensures a class has only ONE instance and provides a global point of access to it?", ["Factory Pattern", "Singleton Pattern", "Observer Pattern", "Builder Pattern"], 1, "The Singleton pattern restricts class instantiation to a single instance throughout the application lifecycle, usually via a private constructor and static getter."),
    ("Design Patterns - Factory", "Python", "Medium", "Design Patterns", ["Amazon", "Wipro"], "Which Design Pattern defines an interface for creating objects, but lets subclasses decide which class to instantiate?", ["Singleton Pattern", "Adapter Pattern", "Factory Method Pattern", "Observer Pattern"], 2, "The Factory Method pattern encapsulates object creation logic, allowing caller code to request objects through a common interface without knowing concrete instantiation details."),
    ("Design Patterns - Observer", "Java", "Medium", "Design Patterns", ["Adobe", "Microsoft"], "Which Design Pattern defines a one-to-many dependency where changing one object's state automatically notifies and updates dependents?", ["Observer Pattern", "Strategy Pattern", "Decorator Pattern", "Facade Pattern"], 0, "The Observer pattern (pub/sub) maintains a list of dependent observers and automatically notifies them of state changes via event dispatch."),
    ("Design Patterns - Strategy", "C++", "Hard", "Design Patterns", ["Google", "Nvidia"], "Which Design Pattern enables selecting an algorithm's behavior dynamically at runtime by encapsulating algorithms into interchangeable strategy classes?", ["Command Pattern", "Strategy Pattern", "State Pattern", "Template Method Pattern"], 1, "The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable at runtime without altering client code."),
    ("Design Patterns - Adapter", "Java", "Medium", "Design Patterns", ["Oracle", "Capgemini"], "Which Design Pattern acts as a wrapper to convert the interface of a class into another interface expected by clients?", ["Bridge Pattern", "Adapter Pattern", "Proxy Pattern", "Composite Pattern"], 1, "The Adapter pattern converts incompatible interfaces of existing classes into a compatible interface expected by caller applications."),
]

for topic, lang, diff, main_top, comps, q_text, opts, ans, exp in design_patterns_solid:
    questions.append(q(len(questions) + 1, lang, diff, main_top, comps, q_text, opts, ans, exp))

for topic, diff, comps, q_text, opts, ans, exp in python_topics_data:
    questions.append(q(len(questions) + 1, "Python", diff, topic, comps, q_text, opts, ans, exp))

print(f"Total Questions Generated: {len(questions)}")

# Write to questionBank.json
output_file = "/home/apexuday/Pictures/k/questionBank.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)

print(f"Successfully generated {len(questions)} questions in {output_file}")
