# MicroJet - Web Framework Documentation

## 📚 মিডিয়াম সারসংক্ষেপ

**MicroJet** হল একটি হালকা Python ওয়েব ফ্রেমওয়ার্ক যা Bottle.py এর মত সহজ এবং React এর মত কম্পোনেন্ট সিস্টেম ব্যবহার করে। এটি আপনাকে দ্রুত এবং সহজে আধুনিক ওয়েব অ্যাপ্লিকেশন তৈরি করতে সাহায্য করে।

## 🎯 বৈশিষ্ট্য

- ✅ **সহজ রুটিং সিস্টেম** - Bottle.py এর মত decorator-based routing
- ✅ **React-like কম্পোনেন্ট** - পুনর্ব্যবহারযোগ্য কম্পোনেন্ট তৈরি করুন
- ✅ **বিল্ট-ইন কম্পোনেন্ট লাইব্রেরি** - Button, Card, NavBar, Form, Alert এবং আরও অনেক কিছু
- ✅ **সহজ CLI** - প্রজেক্ট এবং কম্পোনেন্ট ম্যানেজমেন্ট
- ✅ **স্টেটিক ফাইল সাপোর্ট** - CSS, JS, ইমেজ ইত্যাদি
- ✅ **মিডলওয়্যার সাপোর্ট** - কাস্টম মিডলওয়্যার তৈরি করুন
- ✅ **এরর হ্যান্ডলিং** - কাস্টম এরর হ্যান্ডলার

## 🚀 শুরু করুন

### ইনস্টলেশন

```bash
# microjet_core.py এবং jet CLI ফাইল ডাউনলোড করুন
python jet --help
```

### নতুন প্রজেক্ট তৈরি করুন

```bash
jet new my_app
cd my_app
```

### কম্পোনেন্ট ইনস্টল করুন

```bash
jet install button
jet install card
jet install navbar
```

### ডেভেলপমেন্ট সার্ভার চালান

```bash
jet run
```

আপনার ব্রাউজারে `http://localhost:8000` খুলুন।

## 📖 বেসিক ব্যবহার

### সাধারণ রুট

```python
from microjet_core import MicroJet, HtmlComponent

app = MicroJet("My App")

@app.route("/")
def home():
    page = HtmlComponent("html")
    body = HtmlComponent("body")
    h1 = HtmlComponent("h1")
    h1.add_child("Hello World!")
    body.add_child(h1)
    page.add_child(body)
    return f"<!DOCTYPE html>{page.to_html()}"

if __name__ == "__main__":
    app.run()
```

### প্যারামিটার সহ রুট

```python
@app.route("/user/:name")
def user_page(name):
    page = HtmlComponent("html")
    body = HtmlComponent("body")
    p = HtmlComponent("p")
    p.add_child(f"Hello, {name}!")
    body.add_child(p)
    page.add_child(body)
    return f"<!DOCTYPE html>{page.to_html()}"
```

### JSON রেসপন্স

```python
@app.route("/api/users")
def get_users():
    return {
        "users": [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"}
        ]
    }
```

## 🧩 কম্পোনেন্ট সিস্টেম

### বিল্ট-ইন কম্পোনেন্ট ব্যবহার করুন

```python
from microjet_core import div, h1, p, button

# HTML তৈরি করুন
page = div(className="container")
header = h1()
header.add_child("Welcome!")
page.add_child(header)

content = p()
content.add_child("This is a paragraph")
page.add_child(content)

btn = button()
btn.add_child("Click me")
page.add_child(btn)

# Render করুন
html = page.to_html()
```

### কাস্টম কম্পোনেন্ট তৈরি করুন

**components/greeting.py**
```python
from microjet_core import HtmlComponent

class Greeting(HtmlComponent):
    def __init__(self, props=None):
        super().__init__("div", props or {"className": "greeting"})
    
    def set_message(self, message):
        self.add_child(message)
        return self
```

**app.py**
```python
from components.greeting import Greeting

@app.route("/hello")
def hello():
    greeting = Greeting()
    greeting.set_message("Hey there!")
    return f"<!DOCTYPE html><html><body>{greeting.to_html()}</body></html>"
```

### কম্পোনেন্ট App এ রেজিস্টার করুন

```python
app.register_component("greeting", Greeting)

# এখন যেকোনো জায়গা থেকে ব্যবহার করুন
comp = app.get_component("greeting")
```

## 📦 প্রি-বিল্ট কম্পোনেন্ট

### Button Component

```python
from components.button import Button

btn = Button()
btn.render_text("Click Me!")
btn.set_prop("className", "btn-primary")
```

### Card Component

```python
from components.card import Card

card = Card()
card.add_header("Card Title")
card.add_body("Card content goes here")
```

### Form Component

```python
from components.form import Form

form = Form({"action": "/submit", "method": "POST"})
form.add_field("email", "Email Address", "email")
form.add_field("password", "Password", "password")
```

### Alert Component

```python
from components.alert import Alert

alert = Alert("This is an info message", "info")
alert.add_close_button()
```

### NavBar Component

```python
from components.navbar import NavBar

navbar = NavBar()
navbar.add_link("Home", "/")
navbar.add_link("About", "/about")
navbar.add_link("Contact", "/contact")
```

## 🔧 উন্নত বৈশিষ্ট্য

### মিডলওয়্যার ব্যবহার করুন

```python
@app.use_middleware
def log_requests(environ, handler):
    print(f"Request: {environ['REQUEST_METHOD']} {environ['PATH_INFO']}")
    return handler()
```

### এরর হ্যান্ডলার

```python
@app.error_handler(404)
def not_found():
    return "<h1>404 - Page Not Found</h1>"

@app.error_handler(500)
def server_error():
    return "<h1>500 - Server Error</h1>"
```

### স্টেটিক ফাইল সেবা করুন

```python
app.static("static")
```

এখন `/static/css/style.css` এ অ্যাক্সেস করা যাবে।

## 🎨 CSS স্টাইলিং

প্রতিটি প্রজেক্ট একটি প্রি-স্টাইল করা `style.css` সহ আসে। আপনার নিজের স্টাইল যোগ করুন:

```python
from microjet_core import HtmlComponent

styled_div = HtmlComponent("div", {"className": "my-custom-class"})
```

## 📁 প্রজেক্ট স্ট্রাকচার

```
my_app/
├── app.py                 # Main application
├── components/            # কাস্টম কম্পোনেন্ট
│   ├── button.py
│   ├── card.py
│   └── ...
├── static/               # স্টেটিক ফাইল
│   ├── css/
│   │   └── style.css
│   └── js/
├── jet.json              # প্রজেক্ট কনফিগ
└── README.md             # ডকুমেন্টেশন
```

## 🔄 CLI কমান্ড

| কমান্ড | ব্যবহার |
|--------|---------|
| `jet new <name>` | নতুন প্রজেক্ট তৈরি করুন |
| `jet install <component>` | কম্পোনেন্ট ইনস্টল করুন |
| `jet run` | ডেভেলপমেন্ট সার্ভার চালান |
| `jet list` | সব কম্পোনেন্ট দেখুন |

## 💡 উদাহরণ

### সম্পূর্ণ Todo অ্যাপ

```python
from microjet_core import MicroJet, div, h1, input_field, button, ul, li

app = MicroJet("Todo App")

todos = ["Learn MicroJet", "Build an app", "Deploy it"]

@app.route("/")
def index():
    page = div()
    
    title = h1()
    title.add_child("My Todo List")
    page.add_child(title)
    
    # Input form
    form = div()
    input_box = input_field(placeholder="Add a new todo...")
    form.add_child(input_box)
    btn = button()
    btn.add_child("Add")
    form.add_child(btn)
    page.add_child(form)
    
    # Todo list
    todo_list = ul()
    for todo in todos:
        item = li()
        item.add_child(todo)
        todo_list.add_child(item)
    page.add_child(todo_list)
    
    return f"<!DOCTYPE html><html><body>{page.to_html()}</body></html>"

if __name__ == "__main__":
    app.run()
```

## 🤝 অবদান এবং সাপোর্ট

MicroJet একটি ওপেন সোর্স প্রজেক্ট। আপনি কম্পোনেন্ট তৈরি করতে, বাগ রিপোর্ট করতে বা ডকুমেন্টেশন উন্নত করতে অবদান রাখতে পারেন।

## 📄 লাইসেন্স

MIT License - স্বাধীনভাবে ব্যবহার, পরিবর্তন এবং বিতরণ করুন।

---

**MicroJet দিয়ে আপনার অসাধারণ ওয়েব অ্যাপ্লিকেশন তৈরি করুন!** 🎉
