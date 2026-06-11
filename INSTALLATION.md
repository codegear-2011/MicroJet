# MicroJet ইনস্টলেশন গাইড

## দ্রুত শুরু

### Step 1: ফাইল ডাউনলোড করুন

নিম্নলিখিত ফাইলগুলি একটি ডিরেক্টরিতে রাখুন:
- `microjet_core.py` - মূল ফ্রেমওয়ার্ক
- `jet` - CLI টুল

### Step 2: CLI কে এক্সিকিউটেবল করুন

```bash
chmod +x jet
```

### Step 3: প্রথম প্রজেক্ট তৈরি করুন

```bash
./jet new my_first_app
cd my_first_app
```

### Step 4: ডেভেলপমেন্ট সার্ভার চালান

```bash
./jet run
```

আপনার ব্রাউজারে `http://localhost:8000` খুলুন এবং স্বাগত বার্তা দেখুন!

---

## ইনস্টলেশন অপশন

### অপশন ১: স্থানীয় ব্যবহার (সুপারিশকৃত)

শুধু ফাইল ডাউনলোড করুন এবং ব্যবহার করুন:

```bash
# CLI ব্যবহার করুন
./jet new myapp
cd myapp
./jet run
```

### অপশন ২: গ্লোবাল ইনস্টলেশন (Linux/Mac)

```bash
# jet CLI কে PATH-এ যোগ করুন
sudo ln -s /path/to/jet /usr/local/bin/jet

# এখন যেকোনো জায়গা থেকে ব্যবহার করুন
jet new myapp
```

### অপশন ৩: Python প্যাকেজ হিসেবে

```bash
# মূল ডিরেক্টরিতে থাকুন
pip install -e .

# এখন সব জায়গা থেকে ব্যবহার করুন
jet new myapp
cd myapp
jet run
```

---

## সিস্টেম রিকোয়ারমেন্ট

- **Python**: 3.7 বা তার উপরে
- **OS**: Linux, macOS, Windows
- **আন্তর্নেট সংযোগ**: শুধুমাত্র ডাউনলোডের সময়

কোনো বাহ্যিক ডিপেন্ডেন্সি প্রয়োজন নেই! শুধু Python স্ট্যান্ডার্ড লাইব্রেরি।

---

## সমস্যা সমাধান

### সমস্যা: `jet: command not found`

**সমাধান**: 
```bash
# CLI এর পূর্ণ পাথ ব্যবহার করুন
./jet new myapp

# অথবা এটিকে PATH-এ যোগ করুন
export PATH=$PATH:/path/to/jet/directory
```

### সমস্যা: `Permission denied`

**সমাধান**:
```bash
chmod +x jet
./jet new myapp
```

### সমস্যা: পোর্ট ৮০০০ ব্যবহৃত

**সমাধান**: `app.py` এ পোর্ট পরিবর্তন করুন:
```python
app.run(port=8001)  # অন্য পোর্ট ব্যবহার করুন
```

---

## প্রথম অ্যাপ কাস্টমাইজ করুন

প্রজেক্ট তৈরির পরে `app.py` সম্পাদনা করুন:

```python
from microjet_core import MicroJet, h1, p, div

app = MicroJet("আমার অ্যাপ")

@app.route("/")
def home():
    page = div()
    
    title = h1()
    title.add_child("স্বাগতম! 👋")
    page.add_child(title)
    
    description = p()
    description.add_child("এটি আমার প্রথম MicroJet অ্যাপ্লিকেশন")
    page.add_child(description)
    
    return f"<!DOCTYPE html><html><body>{page.to_html()}</body></html>"

if __name__ == "__main__":
    app.run()
```

---

## পরবর্তী ধাপ

১. **কম্পোনেন্ট ইনস্টল করুন**:
   ```bash
   jet install button
   jet install card
   ```

২. **উদাহরণ দেখুন**: `example_blog_app.py` চালান

3. **ডকুমেন্টেশন পড়ুন**: `MICROJET_DOCS.md` খুলুন

4. **নিজের প্রজেক্ট তৈরি করুন** এবং শেয়ার করুন!

---

## সহায়তা

যদি সমস্যা হয়:
- ডকুমেন্টেশন পড়ুন: `MICROJET_DOCS.md`
- উদাহরণ দেখুন: `example_blog_app.py`
- `jet --help` চালান সাহায্যের জন্য

---

**Happy coding! 💜 MicroJet দিয়ে দুর্দান্ত কিছু তৈরি করুন!**
