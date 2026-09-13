# PIMPL Idiom — Stable Interfaces and Compilation Firewalls

> **Minimum standard:** C++17
>
> **Canonical location:** C++ class-design practice.

## PIMPL — Hide Implementation Details
```cpp
// Widget.h — public header (no implementation details exposed)
#include <memory>
#include <string>

class Widget {
public:
    Widget();
    ~Widget();
    Widget(Widget&&) noexcept;
    Widget& operator=(Widget&&) noexcept;

    void setTitle(const std::string& title);
    void render() const;

private:
    class Impl;                    // forward declaration only
    std::unique_ptr<Impl> pImpl_;  // pointer to implementation
};

// Widget.cpp — implementation hidden from users
struct Widget::Impl {
    std::string title = "Untitled";
    int x = 0, y = 0, w = 800, h = 600;

    void render() const {
        std::cout << "Rendering Widget '" << title << "' at ("
                  << x << "," << y << ") size " << w << "x" << h << "\n";
    }
};

Widget::Widget()  : pImpl_(std::make_unique<Impl>()) {}
Widget::~Widget() = default;
Widget::Widget(Widget&&) noexcept            = default;
Widget& Widget::operator=(Widget&&) noexcept = default;

void Widget::setTitle(const std::string& t) { pImpl_->title = t; }
void Widget::render() const                 { pImpl_->render(); }

int main() {
    Widget w;
    w.setTitle("My App Window");
    w.render();
    return 0;
}
```

## Next Step

Return to the parent section README and continue along the canonical [C++ and DSA learning path](../../LEARNING_PATH.md).
