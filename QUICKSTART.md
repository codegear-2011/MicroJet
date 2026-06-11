# 🎯 MicroJet - ৫ মিনিটে শুরু করুন

এই গাইডটি আপনাকে ৫ মিনিটের মধ্যে MicroJet দিয়ে আপনার প্রথম অ্যাপ চালু করতে সাহায্য করবে।

## ✅ প্রয়োজনীয় জিনিস

- Python 3.7+
- এই ফাইলগুলি:
  - `microjet_core.py`
  - `jet`

## 🚀 দ্রুত শুরু (৫ ধাপ)

### ধাপ ১: ফাইল সাজান
```bash
# একটি নতুন ফোল্ডার তৈরি করুন
mkdir microjet_projects
cd microjet_projects

# এখানে রাখুন:
# - microjet_core.py
# - jet
```

### ধাপ ২: CLI কে এক্সিকিউটেবল করুন
```bash
chmod +x jet
```

### ধাপ ৩: নতুন প্রজেক্ট তৈরি করুন
```bash
./jet new hello_world
cd hello_world
```

**এটি তৈরি করবে:**
```
hello_world/
├── app.py          ← আপনার অ্যাপ্লিকেশন
├── components/     ← কাস্টম কম্পোনেন্ট
├── static/         ← CSS, JS ইত্যাদি
├── jet.json        ← প্রজেক্ট কনফিগ
└── README.md       ← প্রজেক্ট ডকুমেন্টেশন
```

### ধাপ ৪: সার্ভার চালান
```bash
./jet run
```

আপনি দেখবেন:
```
🚀 MicroJet server running at http://0.0.0.0:8000
   Press CTRL+C to quit
```

### ধাপ ৫: ব্রাউজারে দেখুন
আপনার ব্রাউজার খুলুন এবং যান: **http://localhost:8000**

দেখবেন:
```
🚀 Welcome to MicroJet!
Start building amazing web apps with React-like components!
```

**🎉 সম্পন্ন! আপনার প্রথম MicroJet অ্যাপ চলছে!**

---

## 🎨 অ্যাপ কাস্টমাইজ করুন

`app.py` খুলুন এবং এটি পরিবর্তন করুন:

```python
from microjet_core import MicroJet, HtmlComponent

app = MicroJet("আমার প্রথম অ্যাপ")  # ← এখানে নাম পরিবর্তন করুন

@app.route("/")
def home():
    """হোমপেজ"""
    page = HtmlComponent("html")
    body = HtmlComponent("body")
    
    h1 = HtmlComponent("h1")
    h1.add_child("👋 হ্যালো বিশ্ব!")  # ← বার্তা পরিবর্তন করুন
    body.add_child(h1)
    
    p = HtmlComponent("p")
    p.add_child("এটি আমার প্রথম MicroJet অ্যাপ!")  # ← বর্ণনা যোগ করুন
    body.add_child(p)
    
    page.add_child(body)
    
    return f"<!DOCTYPE html>{page.to_html()}"

if __name__ == "__main__":
    app.run()
```

পরিবর্তনের পরে সার্ভার স্বয়ংক্রিয়ভাবে রিলোড হবে (debug mode এ)।

---

## 📦 কম্পোনেন্ট যোগ করুন

ইনস্টল করুন প্রি-বিল্ট কম্পোনেন্ট:

```bash
# বর্তমান প্রজেক্ট ডিরেক্টরিতে থাকুন
./jet install button
./jet install card
./jet install form
```

এটি `components/` ফোল্ডারে ফাইল তৈরি করবে।

### ব্যবহার করুন:

```python
from components.button import Button
from components.card import Card

@app.route("/")
def home():
    page = HtmlComponent("html")
    body = HtmlComponent("body")
    
    # কার্ড তৈরি করুন
    card = Card()
    card.add_header("স্বাগত")
    card.add_body("এটি একটি সুন্দর কার্ড!")
    body.add_child(card)
    
    # বাটন তৈরি করুন
    btn = Button()
    btn.set_prop("className", "btn-primary")
    btn.add_child("ক্লিক করুন")
    body.add_child(btn)
    
    page.add_child(body)
    return f"<!DOCTYPE html>{page.to_html()}"
```

---

## 🔗 একাধিক রুট তৈরি করুন

```python
@app.route("/")
def home():
    # হোমপেজ
    return "<h1>হোম</h1>"

@app.route("/about")
def about():
    # আমাদের সম্পর্কে পেজ
    return "<h1>আমাদের সম্পর্কে</h1>"

@app.route("/user/:name")
def user(name):
    # ব্যবহারকারী প্রোফাইল পেজ
    return f"<h1>স্বাগতম, {name}!</h1>"

@app.route("/api/data")
def get_data():
    # JSON API
    return {"message": "হ্যালো!", "status": "ok"}
```

টেস্ট করুন:
- http://localhost:8000/
- http://localhost:8000/about
- http://localhost:8000/user/আহমেদ
- http://localhost:8000/api/data

---

## 💡 প্রায়শই জিজ্ঞাসিত প্রশ্ন

### Q: কিভাবে স্টাইল যোগ করি?

**A:** CSS ফাইল তৈরি করুন `static/css/` এ:

```css
/* static/css/my-style.css */
body {
    font-family: "Segoe UI", Tahoma;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: #333;
}

h1 {
    color: #fff;
    text-align: center;
}
```

তারপর `app.py` এ লিংক করুন:

```python
<link rel="stylesheet" href="/static/css/my-style.css">
```

### Q: কিভাবে JavaScript যোগ করি?

**A:** JS ফাইল তৈরি করুন `static/js/` এ:

```javascript
// static/js/my-script.js
document.addEventListener('DOMContentLoaded', () => {
    console.log('পেজ লোড হয়েছে!');
});
```

এবং লিংক করুন:

```html
<script src="/static/js/my-script.js"></script>
```

### Q: ডাটাবেস যোগ করতে পারি?

**A:** হাঁ! Python এর যেকোনো ডাটাবেস লাইব্রেরি ব্যবহার করুন:

```python
import sqlite3

@app.route("/api/posts")
def get_posts():
    conn = sqlite3.connect("blog.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    conn.close()
    return {"posts": posts}
```

### Q: ডিপ্লয় কিভাবে করি?

**A:** Heroku, PythonAnywhere, বা যেকোনো WSGI-সামঞ্জস্যপূর্ণ হোস্টিংয়ে:

```bash
# Procfile তৈরি করুন
echo "web: python app.py" > Procfile

# Git এ পুশ করুন
git push heroku main
```

---

## 📚 পরবর্তী ধাপ

১. **প্রোজেক্ট আরও বাড়ান**
   - নতুন রুট যোগ করুন
   - কাস্টম কম্পোনেন্ট তৈরি করুন
   - CSS স্টাইল করুন

২. **ডকুমেন্টেশন পড়ুন**
   - `README.md` - সম্পূর্ণ গাইড
   - `MICROJET_DOCS.md` - API রেফারেন্স
   - `example_blog_app.py` - সম্পূর্ণ উদাহরণ

৩. **আপনার নিজের প্রজেক্ট তৈরি করুন**
   - একটি পোর্টফোলিও সাইট
   - একটি ব্লগ প্ল্যাটফর্ম
   - একটি টুডু অ্যাপ
   - একটি API সার্ভার

৪. **শেয়ার করুন**
   - GitHub এ আপলোড করুন
   - বন্ধুদের দেখান
   - অগ্রদূত প্রতিক্রিয়া পান

---

## 🆘 সমস্যার সমাধান

### সমস্যা: `Permission denied`
```bash
chmod +x jet
./jet new myapp
```

### সমস্যা: পোর্ট ৮০০০ ব্যবহৃত
```python
# app.py এর শেষে:
app.run(port=8001)  # অন্য পোর্ট ব্যবহার করুন
```

### সমস্যা: মডিউল পাওয়া যায় না
নিশ্চিত করুন `microjet_core.py` আপনার প্রজেক্ট ডিরেক্টরিতে আছে।

---

## 🎯 আপনার লক্ষ্য

এই টিউটোরিয়ালের পরে আপনি পারবেন:

✅ নতুন MicroJet প্রজেক্ট তৈরি করতে  
✅ রুট এবং এন্ডপয়েন্ট তৈরি করতে  
✅ কম্পোনেন্ট ব্যবহার ও তৈরি করতে  
✅ CSS এবং JS যোগ করতে  
✅ আপনার অ্যাপ কাস্টমাইজ করতে  
✅ আপনার প্রজেক্ট ডিপ্লয় করতে  

**এখন যান এবং তৈরি করুন!** 🚀

---

<div align="center">

### প্রশ্ন? সাহায্য প্রয়োজন?

📖 ডকুমেন্টেশন: `README.md` এবং `MICROJET_DOCS.md`  
💻 উদাহরণ: `example_blog_app.py`  
🐛 সমস্যা: সমস্যা সমাধান বিভাগ দেখুন  

**Happy coding! 💜**

</div>
