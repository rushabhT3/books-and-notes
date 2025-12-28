## PYTHON / DJANGO INTERNALS (20 Questions)

### Q1: What is the GIL (Global Interpreter Lock) and how does it affect Django applications?

**Answer:**
The GIL is a mutex in CPython that allows only one thread to execute Python bytecode at a time, even on multi-core systems.
(A mutex (short for mutual exclusion) is a programming object that controls access to a shared resource)

**Impact on Django:**
- CPU-bound tasks cannot achieve true parallelism with threads
- I/O-bound tasks (database queries, API calls) are less affected because GIL is released during I/O
- Django handles this through multi-process deployment (Gunicorn workers)

**How I handled it at Polynomial AI:**
- Used Celery workers (separate processes) for OCR processing
- Each worker is a separate Python process with its own GIL
- Achieved 1000x faster processing by parallelizing across workers

---

### Q2: Explain Django's request-response cycle in detail.

**Answer:**
```
Client Request 
    → WSGI/ASGI Server (Gunicorn/Uvicorn)
    → Middleware (request phase, top to bottom)
    → URL Resolver (urls.py pattern matching)
    → View Function/Class
    → Model/ORM (database interaction)
    → Template Rendering (if applicable)
    → Response object created
    → Middleware (response phase, bottom to top)
    → WSGI/ASGI Server
    → Client Response
```

**Key Points:**
- Middleware order matters (SecurityMiddleware should be first)
- URL resolver uses regex/path converters
- Views can be function-based (FBV) or class-based (CBV)
- Response middleware runs in reverse order

---

### Q3: What is Django ORM's N+1 query problem and how do you solve it?

**Answer:**
**Problem:** Fetching related objects in a loop causes 1 query for parent + N queries for children.

```python
# BAD: N+1 queries (1 + 100 = 101 queries)
invoices = Invoice.objects.all()  # 1 query
for invoice in invoices:
    print(invoice.customer.name)  # 100 queries (one per invoice)
```

**Solutions:**

| Method | Use Case | SQL Result |
|--------|----------|------------|
| `select_related()` | ForeignKey, OneToOne | Single JOIN query |
| `prefetch_related()` | ManyToMany, Reverse FK | 2 queries + Python join |

```python
# GOOD: 1 query with JOIN
invoices = Invoice.objects.select_related('customer').all()

# GOOD: 2 queries for M2M
invoices = Invoice.objects.prefetch_related('line_items').all()
```

**At Polynomial AI:** Identified N+1 issues using Django Debug Toolbar, optimized 35+ APIs.

---

### Q4: Explain the difference between WSGI and ASGI.

**Answer:**

| Aspect | WSGI | ASGI |
|--------|------|------|
| Full Form | Web Server Gateway Interface | Asynchronous Server Gateway Interface |
| Type | Synchronous only | Sync + Async |
| Concurrency | One request per worker | Multiple concurrent connections |
| Protocol Support | HTTP only | HTTP, WebSocket, HTTP/2 |
| Servers | Gunicorn, uWSGI | Uvicorn, Daphne, Hypercorn |
| Django Support | All versions | Django 3.0+ |

**When to use ASGI:**
- WebSocket connections
- Long-polling
- Server-sent events
- High concurrency I/O-bound apps

---

### Q5: How does Celery work with Django for async task processing?

**Answer:**

**Architecture:**
```
Django App (Producer)
    → Message Broker (Redis/RabbitMQ)
    → Celery Worker (Consumer)
    → Result Backend (optional)
```

**Components:**
1. **Task Definition:** Functions decorated with `@app.task`
2. **Producer:** Django view calls `task.delay()`
3. **Broker:** Stores task in queue (Redis)
4. **Worker:** Separate process picks up and executes task
5. **Result Backend:** Stores return value

**At Polynomial AI:**
```python
@app.task
def process_ocr(document_id):
    document = Document.objects.get(id=document_id)
    # OCR processing logic
    return extracted_text

# In view
process_ocr.delay(document.id)  # Returns immediately
```

---

### Q6: What are Django signals and when should you use them?

**Answer:**
Signals allow decoupled applications to get notified when actions occur.

**Built-in Signals:**

| Signal | Triggered When |
|--------|----------------|
| `pre_save` | Before model save |
| `post_save` | After model save |
| `pre_delete` | Before model delete |
| `post_delete` | After model delete |
| `request_started` | HTTP request begins |
| `request_finished` | HTTP request ends |

**Example:**
```python
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Invoice)
def invoice_created(sender, instance, created, **kwargs):
    if created:
        send_notification_email(instance)
```

**When to use:**
- Decoupled side effects
- Third-party app hooks
- Audit logging

**When NOT to use:**
- Critical business logic (use explicit method calls)
- Performance-sensitive code (adds overhead)

---

### Q7: Explain Django middleware and how to create custom middleware.

**Answer:**
Middleware is a framework for processing requests/responses globally.

**Execution Order:**
```
Request:  SecurityMiddleware → SessionMiddleware → AuthMiddleware → ...
Response: ... → AuthMiddleware → SessionMiddleware → SecurityMiddleware
```

**Custom Middleware:**
```python
class RequestTimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Before view
        start_time = time.time()
        
        response = self.get_response(request)
        
        # After view
        duration = time.time() - start_time
        response['X-Request-Duration'] = str(duration)
        return response
    
    def process_exception(self, request, exception):
        # Handle exceptions
        pass
```

**At Polynomial AI:** Created middleware for API request logging and rate limiting.

---

### Q8: What is the difference between null=True and blank=True in Django models?

**Answer:**

| Attribute | Level | Purpose | Affects |
|-----------|-------|---------|---------|
| `null=True` | Database | Allow NULL in DB | Database column |
| `blank=True` | Validation | Allow empty in forms | Form validation |

**Common Combinations:**
```python
# String fields (use blank only, empty string preferred over NULL)
name = models.CharField(max_length=100, blank=True)

# Non-string fields (need both)
birth_date = models.DateField(null=True, blank=True)

# Required field
email = models.EmailField()  # Both False by default

# ForeignKey optional
customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
```

**Best Practice:** Avoid `null=True` for string fields; use empty string instead.

---

### Q9: Explain Django QuerySet lazy evaluation and caching.

**Answer:**
**Lazy Evaluation:** QuerySets don't hit the database until evaluated.

**When QuerySets are evaluated:**
1. Iteration (`for obj in queryset`)
2. Slicing with step (`queryset[::2]`)
3. `len()`, `list()`, `bool()`
4. Printing/repr

**QuerySet Caching:**
```python
# First evaluation - hits database
queryset = Invoice.objects.all()
for invoice in queryset:  # DB query here
    print(invoice.id)

# Second iteration - uses cache
for invoice in queryset:  # No DB query
    print(invoice.amount)
```

**Avoiding Cache:**
```python
# Forces re-evaluation
queryset.all()  # Returns new QuerySet

# iterator() for large datasets (no caching)
for invoice in Invoice.objects.iterator():
    process(invoice)
```

---

### Q10: What are Django managers and when would you create a custom one?

**Answer:**
Manager is the interface for database query operations. Default is `objects`.

**Custom Manager Use Cases:**
- Add custom query methods
- Modify default QuerySet
- Multiple managers per model

```python
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')
    
    def by_author(self, author):
        return self.get_queryset().filter(author=author)

class Article(models.Model):
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=20)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    objects = models.Manager()  # Default
    published = PublishedManager()  # Custom

# Usage
Article.objects.all()  # All articles
Article.published.all()  # Only published
Article.published.by_author(user)  # Published by specific author
```

---

### Q11: How does Django handle database transactions?

**Answer:**
**Default Behavior:** Django auto-commits each query.

**Transaction Control:**
```python
from django.db import transaction

# 1. Decorator (entire view)
@transaction.atomic
def transfer_money(request):
    # All queries in single transaction
    pass

# 2. Context manager (partial)
def complex_operation(request):
    # Auto-commit queries here
    
    with transaction.atomic():
        # These queries are transactional
        account.balance -= amount
        account.save()
        
        transfer = Transfer.objects.create(...)
    
    # Auto-commit queries here

# 3. Savepoints
with transaction.atomic():
    do_something()
    
    sid = transaction.savepoint()
    try:
        risky_operation()
    except Exception:
        transaction.savepoint_rollback(sid)
    
    do_something_else()
```

**At Coinearth (Node equivalent):** Similar transaction patterns for wallet operations.

---

### Q12: Explain Django REST Framework serializers and their validation.

**Answer:**
**Serializers:** Convert complex data types (QuerySets, model instances) to Python native types for JSON rendering.

**Types:**
| Type | Use Case |
|------|----------|
| `Serializer` | Manual field definition |
| `ModelSerializer` | Auto-generate from model |
| `HyperlinkedModelSerializer` | With URL relationships |

**Validation Levels:**
```python
class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'amount', 'customer', 'due_date']
    
    # 1. Field-level validation
    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be positive")
        return value
    
    # 2. Object-level validation
    def validate(self, data):
        if data['due_date'] < date.today():
            raise serializers.ValidationError("Due date cannot be in past")
        return data
    
    # 3. Custom create/update
    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)
```

**At Polynomial AI:** Created 20+ serializers for invoice processing APIs.

---

### Q13: What is Django's ContentType framework?

**Answer:**
ContentType allows generic relationships between models.

**Use Cases:**
- Generic foreign keys
- Permission system
- Activity logging
- Comments on any model

```python
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)
    
    # Generic FK components
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
    timestamp = models.DateTimeField(auto_now_add=True)

# Usage
invoice = Invoice.objects.get(id=1)
ActivityLog.objects.create(
    user=request.user,
    action='viewed',
    content_object=invoice  # Works with any model
)
```

---

### Q14: How does Django's authentication system work?

**Answer:**
**Components:**
```
User Model → Authentication Backends → Session/Token → Middleware → request.user
```

**Authentication Flow:**
1. User submits credentials
2. `authenticate()` checks backends in order
3. `login()` creates session
4. SessionMiddleware loads session on each request
5. AuthenticationMiddleware sets `request.user`

**Custom Backend:**
```python
class EmailBackend:
    def authenticate(self, request, email=None, password=None):
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
```

**At Polynomial AI:** Extended with JWT for API authentication.

---

### Q15: Explain Django's caching framework.

**Answer:**
**Cache Backends:**
| Backend | Use Case |
|---------|----------|
| `MemcachedCache` | Production, distributed |
| `RedisCache` | Production, feature-rich |
| `DatabaseCache` | When no memcached/redis |
| `FileBasedCache` | Development |
| `LocMemCache` | Single-process development |

**Caching Levels:**
```python
# 1. Low-level cache API
from django.core.cache import cache
cache.set('my_key', 'my_value', timeout=300)
value = cache.get('my_key')

# 2. View caching
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)  # 15 minutes
def my_view(request):
    pass

# 3. Template fragment caching
{% load cache %}
{% cache 500 sidebar request.user.id %}
    ... expensive template fragment ...
{% endcache %}

# 4. Per-site caching (middleware)
MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    ...
    'django.middleware.cache.FetchFromCacheMiddleware',
]
```

---

### Q16: What are Django class-based views (CBV) and their mixins?

**Answer:**
**CBV Hierarchy:**
```
View
├── TemplateView
├── RedirectView
├── DetailView (SingleObjectMixin)
├── ListView (MultipleObjectMixin)
├── FormView
├── CreateView (ModelFormMixin)
├── UpdateView (ModelFormMixin)
└── DeleteView
```

**Common Mixins:**
| Mixin | Purpose |
|-------|---------|
| `LoginRequiredMixin` | Require authentication |
| `PermissionRequiredMixin` | Check permissions |
| `UserPassesTestMixin` | Custom test function |
| `SingleObjectMixin` | Get single object |
| `MultipleObjectMixin` | Get queryset |

**Example:**
```python
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

class InvoiceListView(LoginRequiredMixin, ListView):
    model = Invoice
    template_name = 'invoices/list.html'
    context_object_name = 'invoices'
    paginate_by = 20
    
    def get_queryset(self):
        return Invoice.objects.filter(user=self.request.user)
```

---

### Q17: How do you handle file uploads in Django?

**Answer:**
**Configuration:**
```python
# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# For large files
FILE_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024  # 5MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024  # 10MB
```

**Model:**
```python
class Document(models.Model):
    file = models.FileField(upload_to='documents/%Y/%m/%d/')
    image = models.ImageField(upload_to='images/')
```

**View:**
```python
def upload_document(request):
    if request.method == 'POST':
        file = request.FILES['document']
        
        # Validate
        if file.size > 10 * 1024 * 1024:  # 10MB
            return HttpResponse("File too large", status=400)
        
        document = Document.objects.create(file=file)
        return redirect('success')
```

**At Polynomial AI:** Integrated with AWS S3 using django-storages for invoice storage.

---

### Q18: Explain Django's migration system.

**Answer:**
**Migration Commands:**
| Command | Purpose |
|---------|---------|
| `makemigrations` | Create migration files |
| `migrate` | Apply migrations |
| `showmigrations` | List migrations and status |
| `sqlmigrate` | Show SQL for migration |
| `migrate --fake` | Mark as applied without running |

**Migration Operations:**
```python
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('app', '0001_initial'),
    ]
    
    operations = [
        # Schema changes
        migrations.AddField(...),
        migrations.RemoveField(...),
        migrations.AlterField(...),
        
        # Data migrations
        migrations.RunPython(forwards_func, reverse_func),
        
        # Raw SQL
        migrations.RunSQL('ALTER TABLE ...'),
    ]
```

**Data Migration:**
```python
def populate_slugs(apps, schema_editor):
    Article = apps.get_model('blog', 'Article')
    for article in Article.objects.all():
        article.slug = slugify(article.title)
        article.save()

class Migration(migrations.Migration):
    operations = [
        migrations.RunPython(populate_slugs, migrations.RunPython.noop),
    ]
```

---

### Q19: What is Django's testing framework and best practices?

**Answer:**
**Test Classes:**
| Class | Features |
|-------|----------|
| `SimpleTestCase` | No database |
| `TestCase` | Database, transactions |
| `TransactionTestCase` | Real transactions |
| `LiveServerTestCase` | Running server for Selenium |

**Example:**
```python
from django.test import TestCase, Client
from django.urls import reverse

class InvoiceAPITests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'password')
        self.client.login(username='test', password='password')
    
    def test_create_invoice(self):
        response = self.client.post(
            reverse('invoice-create'),
            {'amount': 100, 'customer_id': 1},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Invoice.objects.filter(amount=100).exists())
    
    def test_unauthorized_access(self):
        self.client.logout()
        response = self.client.get(reverse('invoice-list'))
        self.assertEqual(response.status_code, 401)
```

**At Polynomial AI:** Comprehensive testing ensured stability of data migration systems.

---

### Q20: How do you optimize Django application performance?

**Answer:**
**Database Optimization:**
```python
# 1. Select only needed fields
Invoice.objects.only('id', 'amount')
Invoice.objects.defer('large_text_field')

# 2. Use values/values_list for simple data
Invoice.objects.values_list('id', flat=True)

# 3. Bulk operations
Invoice.objects.bulk_create([...])
Invoice.objects.bulk_update([...], ['status'])

# 4. Indexes
class Invoice(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['customer', '-created_at']),
        ]
```

**Caching:**
- Redis for session and cache
- Cache expensive queries
- Template fragment caching

**Async Processing:**
- Celery for background tasks
- Django 4.1+ async views for I/O-bound

**At Polynomial AI:** Achieved 1000x faster OCR by combining PyMuPDF + Celery + caching.

---

# Additional Django Interview Questions (10 Key Questions)

## 1. **Q1: Explain Django's ModelForm and how it differs from regular forms**

**Answer:**
**ModelForm** automatically generates form fields from model definitions, while regular forms require manual field definition.

```python
# Regular Form
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

# ModelForm (auto-generated from model)
class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        # Or exclude = ['created_at']
    
    # Can still add custom validation
    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@company.com'):
            raise forms.ValidationError("Must be company email")
        return email

# In view
def contact_view(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            # Saves directly to database
            contact = form.save()
            # OR save with commit=False to modify before saving
            contact = form.save(commit=False)
            contact.ip_address = request.META['REMOTE_ADDR']
            contact.save()
```

**Advantages of ModelForm:**
- Automatic field generation from model
- Built-in save() method
- Automatic validation from model constraints
- Less boilerplate code

---

## 2. **Q2: What is Django's Middleware and when would you use process_template_response()?**

**Answer:**
**Middleware** sits between request/response cycle. `process_template_response()` is called after view execution but before template rendering.

```python
class ResponseTimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_template_response(self, request, response):
        # Only called if response has render() method
        if hasattr(response, 'render'):
            # Add context data to all template responses
            response.context_data['server_time'] = timezone.now()
            response.context_data['request_id'] = str(uuid.uuid4())
        
        # Can also modify response.template_name here
        if request.user.is_staff:
            response.template_name = 'admin/' + response.template_name
        
        return response

# Use Cases:
# 1. Add global context data to all templates
# 2. Modify template based on user/request
# 3. A/B testing different templates
# 4. Inject analytics data
```

**When to use vs `process_response()`:**
- `process_template_response()`: Before template rendering
- `process_response()`: After template rendering (final response)

---

## 3. **Q3: Explain Django's F() expressions and Q() objects**

**Answer:**
**F() expressions** reference model field values directly in database queries. **Q() objects** enable complex query lookups.

```python
from django.db.models import F, Q, Count, Sum

# F() - Avoids race conditions
Product.objects.filter(stock__lt=F('min_stock'))
# Updates in database without fetching to Python
Product.objects.update(price=F('price') * 1.1)

# Q() - Complex lookups
from django.db.models import Q

# OR conditions
Invoice.objects.filter(
    Q(status='PAID') | Q(status='PARTIAL') | Q(due_date__lt=timezone.now())
)

# AND conditions
User.objects.filter(
    Q(is_active=True) & Q(date_joined__gte='2023-01-01')
)

# Complex combinations
orders = Order.objects.filter(
    Q(status='SHIPPED') & 
    (Q(total__gt=1000) | Q(customer__is_vip=True))
).exclude(
    Q(payment_method='COD') & Q(shipping_country='REMOTE')
)

# Q() with annotations
from django.db.models import Count, Case, When, Value

top_customers = Customer.objects.annotate(
    order_count=Count('orders'),
    total_spent=Sum('orders__total')
).filter(
    Q(order_count__gt=10) | Q(total_spent__gt=10000)
)
```

**Real-world use at Polynomial AI:**
```python
# Mark invoices as overdue using F() to avoid race conditions
Invoice.objects.filter(
    due_date__lt=timezone.now(),
    status='PENDING'
).update(status='OVERDUE', late_fee=F('amount') * 0.1)

# Complex search with Q()
def search_invoices(query, user):
    return Invoice.objects.filter(
        Q(invoice_number__icontains=query) |
        Q(customer__name__icontains=query) |
        Q(description__icontains=query),
        Q(user=user) | Q(shared_with=user),
        ~Q(status='DRAFT')
    )
```

---

## 4. **Q4: How does Django handle static files in production vs development?**

**Answer:**
**Development:**
```python
# settings.py (Development)
DEBUG = True
INSTALLED_APPS = [
    'django.contrib.staticfiles',  # Serves static files
]
# Run: python manage.py collectstatic (not needed in dev)
# Static files served by Django dev server
```

**Production:**
```python
# settings.py (Production)
DEBUG = False
STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/myapp/static/'  # Where collectstatic copies files
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # Additional static directories
]

# Production setup:
# 1. Run: python manage.py collectstatic
# 2. Configure web server (Nginx/Apache) to serve static files
# 3. Use WhiteNoise for serving from Python (alternative)

# Nginx configuration example:
"""
location /static/ {
    alias /var/www/myapp/static/;
    expires 1y;
    add_header Cache-Control "public, immutable";
}

location /media/ {
    alias /var/www/myapp/media/;
    expires 30d;
}
"""

# Using WhiteNoise (Python-only solution):
# MIDDLEWARE = ['whitenoise.middleware.WhiteNoiseMiddleware']
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

**Best Practices:**
- Use CDN for static files in production
- Enable compression (Whitenoise or web server)
- Set long cache headers for static assets
- Use ManifestStaticFilesStorage for cache busting

---

## 5. **Q5: Explain Django's template inheritance and template tags**

**Answer:**
**Template Inheritance:**
```django
<!-- base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
    {% block extra_head %}{% endblock %}
</head>
<body>
    <header>{% include "header.html" %}</header>
    
    <main>
        {% block content %}
        <!-- Default content can go here -->
        {% endblock %}
    </main>
    
    <footer>
        {% block footer %}
            {% include "footer.html" %}
        {% endblock %}
    </footer>
    
    {% block javascript %}{% endblock %}
</body>
</html>

<!-- child.html -->
{% extends "base.html" %}

{% block title %}My Page Title{% endblock %}

{% block extra_head %}
    <link rel="stylesheet" href="{% static 'css/custom.css' %}">
{% endblock %}

{% block content %}
    <h1>Welcome to my page</h1>
    {{ block.super }}  <!-- Renders parent block content -->
    <p>Additional content here</p>
{% endblock %}

{% block javascript %}
    <script src="{% static 'js/custom.js' %}"></script>
{% endblock %}
```

**Custom Template Tags:**
```python
# templatetags/custom_filters.py
from django import template
from django.utils import timezone
import markdown

register = template.Library()

# Simple filter
@register.filter(name='currency')
def currency_format(value, currency_symbol='$'):
    return f"{currency_symbol}{value:,.2f}"

# Filter with arguments
@register.filter
def multiply(value, arg):
    return value * arg

# Simple tag
@register.simple_tag
def current_time(format_string):
    return timezone.now().strftime(format_string)

# Inclusion tag (renders another template)
@register.inclusion_tag('tags/recent_posts.html')
def show_recent_posts(count=5):
    posts = Post.objects.filter(published=True)[:count]
    return {'posts': posts}

# Assignment tag (stores in variable)
@register.simple_tag(takes_context=True)
def get_user_preferences(context):
    request = context['request']
    return request.user.preferences

# Usage in template:
"""
{% load custom_filters %}

{{ invoice.total|currency:"₹" }}
{{ 5|multiply:3 }}

{% current_time "%Y-%m-%d" as current_date %}
Today is {{ current_date }}

{% show_recent_posts 10 %}

{% get_user_preferences as prefs %}
Theme: {{ prefs.theme }}
"""
```

---

## 6. **Q6: What is Django's database routing and when would you use it?**

**Answer:**
**Database routing** allows directing models to different databases (read replicas, sharding, multi-tenancy).

```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'primary_db',
    },
    'replica': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'replica_db',
    },
    'analytics': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'analytics_db',
    }
}

DATABASE_ROUTERS = ['myapp.routers.DatabaseRouter']

# routers.py
class DatabaseRouter:
    """
    A router to control all database operations
    """
    
    def db_for_read(self, model, **hints):
        """
        Reads go to replica
        """
        if model._meta.app_label == 'analytics':
            return 'analytics'
        return 'replica'  # Use replica for reads
    
    def db_for_write(self, model, **hints):
        """
        Writes go to primary
        """
        if model._meta.app_label == 'analytics':
            return 'analytics'
        return 'default'  # Use primary for writes
    
    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations only if same database
        """
        db1 = self._get_db_for_model(obj1.__class__)
        db2 = self._get_db_for_model(obj2.__class__)
        return db1 == db2
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Only allow migrations on appropriate databases
        """
        if app_label == 'analytics':
            return db == 'analytics'
        return db == 'default'  # Only migrate non-analytics to default
    
    def _get_db_for_model(self, model):
        if model._meta.app_label == 'analytics':
            return 'analytics'
        return 'default'

# Model usage with multiple databases
class UserProfile(models.Model):
    # Will use default/replica based on router
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    class Meta:
        app_label = 'main'

class AnalyticsEvent(models.Model):
    # Will use analytics database
    event_type = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        app_label = 'analytics'

# Manual database selection
AnalyticsEvent.objects.using('analytics').all()
UserProfile.objects.using('default').filter(...)
```

**Use Cases:**
1. **Read replicas** for scaling reads
2. **Analytics database** for reporting
3. **Multi-tenant applications** (different DB per tenant)
4. **Legacy database integration**
5. **Data sharding** across multiple databases

---

## 7. **Q7: Explain Django's Aggregate and Annotate functions**

**Answer:**
**Aggregate** performs calculations across entire queryset. **Annotate** adds calculations to each object.

```python
from django.db.models import (
    Count, Sum, Avg, Max, Min, StdDev, Variance,
    F, Q, Case, When, Value, IntegerField
)

# AGGREGATE - Returns single dict
from django.db.models import Count, Sum, Avg

# Basic aggregates
stats = Invoice.objects.aggregate(
    total_count=Count('id'),
    total_amount=Sum('amount'),
    average_amount=Avg('amount'),
    max_amount=Max('amount'),
    unpaid_count=Count('id', filter=Q(status='PENDING'))
)
# Returns: {'total_count': 100, 'total_amount': 50000.00, ...}

# Multiple aggregates with filters
year_stats = Invoice.objects.filter(
    created_at__year=2023
).aggregate(
    yearly_total=Sum('amount'),
    monthly_avg=Avg('amount') / 12,
    large_invoices=Count('id', filter=Q(amount__gt=10000))
)

# ANNOTATE - Adds field to each object
# Get invoices with customer's total spending
invoices = Invoice.objects.select_related('customer').annotate(
    customer_total=Sum('customer__invoices__amount'),
    invoice_count=Count('customer__invoices'),
    # Conditional annotation
    is_large=Case(
        When(amount__gt=10000, then=Value(True)),
        default=Value(False),
        output_field=models.BooleanField()
    ),
    # Percentage of customer total
    percentage_of_total=F('amount') * 100.0 / Sum('customer__invoices__amount')
).order_by('-amount')

# Complex annotation with subqueries
from django.db.models import Subquery, OuterRef

# Get last invoice date for each customer
last_invoice_subquery = Invoice.objects.filter(
    customer_id=OuterRef('pk')
).order_by('-created_at').values('created_at')[:1]

customers = Customer.objects.annotate(
    last_invoice_date=Subquery(last_invoice_subquery),
    total_invoices=Count('invoices'),
    total_amount=Sum('invoices__amount'),
    # Categorize customers
    customer_type=Case(
        When(total_amount__gt=100000, then=Value('VIP')),
        When(total_amount__gt=50000, then=Value('PREMIUM')),
        default=Value('STANDARD'),
        output_field=models.CharField()
    )
)

# Annotation with multiple aggregations
from django.db.models import FloatField, ExpressionWrapper

invoice_stats = Invoice.objects.values('customer').annotate(
    total=Sum('amount'),
    count=Count('id'),
    avg=Avg('amount'),
    # Calculate standard deviation
    variance=ExpressionWrapper(
        Sum(F('amount') * F('amount')) / Count('id') - 
        (Avg('amount') * Avg('amount')),
        output_field=FloatField()
    )
).order_by('-total')

# Real-world example from Polynomial AI
def get_invoice_analytics(start_date, end_date):
    return Invoice.objects.filter(
        created_at__range=(start_date, end_date),
        status__in=['PAID', 'PARTIAL']
    ).values('customer__country').annotate(
        country_total=Sum('amount'),
        invoice_count=Count('id'),
        avg_invoice=Avg('amount'),
        # Weighted average by amount
        weighted_avg=Sum(F('amount') * F('amount')) / Sum('amount')
    ).annotate(
        # Percentage of global total
        percentage=ExpressionWrapper(
            F('country_total') * 100.0 / 
            Sum('country_total'),
            output_field=FloatField()
        )
    ).order_by('-country_total')
```

---

## 8. **Q8: How do you implement search functionality in Django?**

**Answer:**
**Multiple approaches depending on scale:**

```python
# 1. Basic ORM Search (small datasets)
def basic_search(query):
    from django.db.models import Q
    
    return Product.objects.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query) |
        Q(sku__icontains=query) |
        Q(category__name__icontains=query)
    ).distinct()

# 2. Full-text Search with PostgreSQL
# settings.py
INSTALLED_APPS = [
    'django.contrib.postgres',  # Enable Postgres features
]

# Search with Postgres full-text search
from django.contrib.postgres.search import (
    SearchVector, SearchQuery, SearchRank, TrigramSimilarity
)

def postgres_fulltext_search(query):
    vector = SearchVector('name', weight='A') + \
             SearchVector('description', weight='B') + \
             SearchVector('category__name', weight='C')
    
    search_query = SearchQuery(query)
    
    results = Product.objects.annotate(
        search=vector,
        rank=SearchRank(vector, search_query),
        similarity=TrigramSimilarity('name', query)
    ).filter(
        Q(search=search_query) | Q(similarity__gt=0.3)
    ).order_by('-rank', '-similarity')
    
    return results

# 3. Django Haystack (supports Elasticsearch, Solr, etc.)
# Install: pip install django-haystack elasticsearch
"""
# search_indexes.py
class ProductIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    description = indexes.CharField(model_attr='description')
    category = indexes.CharField(model_attr='category__name')
    
    def get_model(self):
        return Product
    
    def index_queryset(self, using=None):
        return self.get_model().objects.all()

# templates/search/indexes/myapp/product_text.txt
{{ object.name }}
{{ object.description }}
{{ object.category.name }}

# views.py
from haystack.query import SearchQuerySet

def haystack_search(request):
    query = request.GET.get('q', '')
    results = SearchQuerySet().filter(content=query)
    return render(request, 'search_results.html', {'results': results})
"""

# 4. Elasticsearch with Django
# Using django-elasticsearch-dsl
"""
# documents.py
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

@registry.register_document
class ProductDocument(Document):
    name = fields.TextField(
        analyzer='english',
        fields={'raw': fields.KeywordField()}
    )
    description = fields.TextField(analyzer='english')
    category = fields.ObjectField(properties={
        'name': fields.TextField(),
        'slug': fields.KeywordField()
    })
    price = fields.FloatField()
    
    class Index:
        name = 'products'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}
    
    class Django:
        model = Product
        fields = ['id', 'sku', 'created_at']
    
    def get_queryset(self):
        return super().get_queryset().select_related('category')

# views.py
def elasticsearch_search(request):
    query = request.GET.get('q', '')
    search = ProductDocument.search().query(
        'multi_match', 
        query=query,
        fields=['name^3', 'description', 'category.name']
    )
    results = search.execute()
    return render(request, 'search_results.html', {'results': results})
"""

# 5. Advanced search with filters
class ProductSearchForm(forms.Form):
    query = forms.CharField(required=False)
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), 
        required=False
    )
    min_price = forms.DecimalField(required=False, min_value=0)
    max_price = forms.DecimalField(required=False, min_value=0)
    in_stock = forms.BooleanField(required=False)
    sort_by = forms.ChoiceField(
        choices=[
            ('relevance', 'Relevance'),
            ('price_asc', 'Price: Low to High'),
            ('price_desc', 'Price: High to Low'),
            ('newest', 'Newest'),
            ('popular', 'Most Popular')
        ],
        required=False
    )

def advanced_search(request):
    form = ProductSearchForm(request.GET)
    products = Product.objects.all()
    
    if form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            products = products.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )
        
        if form.cleaned_data.get('category'):
            products = products.filter(
                category=form.cleaned_data['category']
            )
        
        if form.cleaned_data.get('min_price'):
            products = products.filter(
                price__gte=form.cleaned_data['min_price']
            )
        
        if form.cleaned_data.get('max_price'):
            products = products.filter(
                price__lte=form.cleaned_data['max_price']
            )
        
        if form.cleaned_data.get('in_stock'):
            products = products.filter(stock_quantity__gt=0)
        
        # Sorting
        sort_by = form.cleaned_data.get('sort_by', 'relevance')
        if sort_by == 'price_asc':
            products = products.order_by('price')
        elif sort_by == 'price_desc':
            products = products.order_by('-price')
        elif sort_by == 'newest':
            products = products.order_by('-created_at')
        elif sort_by == 'popular':
            products = products.annotate(
                order_count=Count('order_items')
            ).order_by('-order_count')
    
    return render(request, 'search.html', {
        'form': form,
        'products': products
    })
```

---

## 9. **Q9: How do you handle internationalization (i18n) and localization (l10n) in Django?**
(Internationalization (i18n) is the process of designing your application to support multiple languages and regions, while localization (l10n) is the process of adapting that internationalized application to a specific language and cultural context. )

**Answer:**
**Complete i18n setup:**

```python
# settings.py
# Enable i18n
USE_I18N = True
USE_L10N = True  # Locale formatting
USE_TZ = True

# Available languages
LANGUAGES = [
    ('en', 'English'),
    ('es', 'Spanish'),
    ('fr', 'French'),
    ('de', 'German'),
    ('ja', 'Japanese'),
]

# Default language
LANGUAGE_CODE = 'en-us'

# Locale paths
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.locale.LocaleMiddleware',  # After SessionMiddleware
    # ...
]

# Template context processor
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.i18n',
            ],
        },
    },
]

# In code:
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as _l
from django.utils.translation import ngettext
import datetime

# Model fields
class Product(models.Model):
    name = models.CharField(_l("Product name"), max_length=100)
    description = models.TextField(_l("Description"))
    
    class Meta:
        verbose_name = _l("Product")
        verbose_name_plural = _l("Products")

# Views and functions
def welcome_view(request):
    # Simple translation
    message = _("Welcome to our store!")
    
    # Pluralization
    item_count = 5
    items_text = ngettext(
        "You have %(count)d item in your cart",
        "You have %(count)d items in your cart",
        item_count
    ) % {'count': item_count}
    
    # Context variables
    context = {
        'title': _("Home Page"),
        'current_time': datetime.datetime.now(),
    }
    return render(request, 'welcome.html', context)

# In templates:
"""
{% load i18n %}

<!-- Simple translation -->
<h1>{% trans "Welcome to our website" %}</h1>

<!-- With context -->
<p>{% trans "Search" context "verb" %}</p>
<p>{% trans "Search" context "noun" %}</p>

<!-- Pluralization -->
<p>
    {% blocktrans count counter=product_count %}
        There is {{ counter }} product available.
    {% plural %}
        There are {{ counter }} products available.
    {% endblocktrans %}
</p>

<!-- With variables -->
<p>
    {% blocktrans with username=user.username %}
        Hello, {{ username }}!
    {% endblocktrans %}
</p>

<!-- Inline translation -->
<img src="{% static 'logo.png' %}" alt="{% trans 'Company logo' %}">

<!-- Language selector -->
<form action="{% url 'set_language' %}" method="post">
    {% csrf_token %}
    <select name="language">
        {% get_current_language as LANGUAGE_CODE %}
        {% get_available_languages as LANGUAGES %}
        {% for lang_code, lang_name in LANGUAGES %}
            <option value="{{ lang_code }}" 
                {% if lang_code == LANGUAGE_CODE %}selected{% endif %}>
                {{ lang_name }}
            </option>
        {% endfor %}
    </select>
    <input type="submit" value="{% trans 'Change' %}">
</form>
"""

# Extract translations
# Terminal commands:
"""
# Extract strings from code and templates
python manage.py makemessages -l es -l fr -l de

# Create .po files in locale/ directory
# Edit .po files with translations

# Compile .po to .mo
python manage.py compilemessages

# For JavaScript translations
python manage.py makemessages -d djangojs -l es
"""

# JavaScript i18n:
"""
// In template
{% load i18n %}
<script type="text/javascript" src="{% url 'javascript-catalog' %}"></script>

// In JavaScript
const greeting = gettext('Hello World');
const count = 5;
const plural = ngettext('%(count)s item', '%(count)s items', count);
const formatted = interpolate(plural, {count: count}, true);
"""

# Format localization:
# settings.py
FORMAT_MODULE_PATH = [
    'myproject.formats',
]

# myproject/formats/en/formats.py
DATE_FORMAT = 'N j, Y'  # Dec 25, 2023
DATETIME_FORMAT = 'N j, Y, P'  # Dec 25, 2023, 4 p.m.
DECIMAL_SEPARATOR = '.'
THOUSAND_SEPARATOR = ','
NUMBER_GROUPING = 3

# In templates with localization filters:
"""
{{ price|floatformat:2 }}  # Uses local decimal separator
{{ date|date }}  # Uses local date format
{{ datetime|date:"SHORT_DATETIME_FORMAT" }}
"""

# Timezone handling:
from django.utils import timezone

def create_event(request):
    # Store in UTC
    event = Event.objects.create(
        name=request.POST['name'],
        start_time=timezone.now(),  # Automatically converts to UTC
    )
    
    # Display in user's timezone
    user_timezone = pytz.timezone(request.user.timezone)
    local_start = event.start_time.astimezone(user_timezone)
    
    return render(request, 'event.html', {
        'event': event,
        'local_time': local_start
    })
```

---

## 10. **Q10: How do you implement real-time features in Django?**

**Answer:**
**Multiple approaches for real-time functionality:**

```python
# 1. Django Channels (WebSockets)
# Install: pip install channels channels-redis

# settings.py
INSTALLED_APPS = [
    'channels',
    'django.contrib.auth',
    # ...
]

ASGI_APPLICATION = 'myproject.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

# asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import myapp.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            myapp.routing.websocket_urlpatterns
        )
    ),
})

# routing.py
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/notifications/', consumers.NotificationConsumer.as_asgi()),
    path('ws/chat/<int:room_id>/', consumers.ChatConsumer.as_asgi()),
]

# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.room_group_name = f'notifications_{self.user.id}'
        
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
    
    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'notification_message',
                'message': message
            }
        )
    
    async def notification_message(self, event):
        message = event['message']
        
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'type': 'notification'
        }))

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f'chat_{self.room_id}'
        
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
        
        # Send welcome message
        await self.send(text_data=json.dumps({
            'type': 'system',
            'message': f'Welcome to chat room {self.room_id}'
        }))
    
    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = self.scope['user'].username
        
        # Save message to database
        await self.save_message(message)
        
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'timestamp': str(timezone.now())
            }
        )
    
    async def chat_message(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'type': 'chat',
            'message': event['message'],
            'username': event['username'],
            'timestamp': event['timestamp']
        }))
    
    @database_sync_to_async
    def save_message(self, message):
        from .models import ChatMessage, ChatRoom
        room = ChatRoom.objects.get(id=self.room_id)
        ChatMessage.objects.create(
            room=room,
            user=self.scope['user'],
            message=message
        )

# Send notifications from views/models
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def send_notification(user_id, message):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f'notifications_{user_id}',
        {
            'type': 'notification_message',
            'message': message
        }
    )

# 2. Server-Sent Events (SSE)
# Simple alternative to WebSockets for one-way communication
def sse_stream(request):
    response = HttpResponse(
        content_type='text/event-stream',
        headers={'Cache-Control': 'no-cache', 'X-Accel-Buffering': 'no'}
    )
    
    def event_stream():
        while True:
            # Check for new data
            new_data = check_for_updates(request.user)
            if new_data:
                yield f"data: {json.dumps(new_data)}\n\n"
            time.sleep(1)  # Polling interval
    
    return StreamingHttpResponse(event_stream())

# 3. Long Polling
def long_poll_notifications(request):
    timeout = 30  # seconds
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        notifications = Notification.objects.filter(
            user=request.user,
            read=False,
            created_at__gt=request.GET.get('last_check')
        )
        
        if notifications.exists():
            data = NotificationSerializer(notifications, many=True).data
            return JsonResponse({'notifications': data})
        
        time.sleep(1)  # Check every second
    
    return JsonResponse({'notifications': []})

# 4. Django REST Framework with polling
from rest_framework.views import APIView
from rest_framework.response import Response

class NotificationPollView(APIView):
    authentication_classes = [SessionAuthentication]
    
    def get(self, request):
        last_id = request.GET.get('last_id', 0)
        
        # Get new notifications since last_id
        notifications = Notification.objects.filter(
            user=request.user,
            id__gt=last_id
        ).order_by('-created_at')[:10]
        
        data = {
            'notifications': NotificationSerializer(notifications, many=True).data,
            'last_id': notifications.first().id if notifications else last_id,
            'timestamp': timezone.now().isoformat()
        }
        
        return Response(data)

# 5. Using Django with Redis Pub/Sub
import redis
import json

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def publish_event(channel, event_type, data):
    message = {
        'type': event_type,
        'data': data,
        'timestamp': timezone.now().isoformat()
    }
    redis_client.publish(channel, json.dumps(message))

# Subscribe in a separate process/thread
def subscribe_to_events(channel):
    pubsub = redis_client.pubsub()
    pubsub.subscribe(channel)
    
    for message in pubsub.listen():
        if message['type'] == 'message':
            data = json.loads(message['data'])
            process_event(data)

# 6. Real-time dashboard with auto-refresh
# Using Django and JavaScript
"""
<!-- template.html -->
<div id="dashboard">
    <!-- Content will be updated -->
</div>

<script>
function updateDashboard() {
    fetch('/api/dashboard-data/')
        .then(response => response.json())
        .then(data => {
            document.getElementById('dashboard').innerHTML = data.html;
        });
}

// Update every 5 seconds
setInterval(updateDashboard, 5000);

// Or use WebSocket
const socket = new WebSocket('ws://' + window.location.host + '/ws/dashboard/');
socket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    updateChart(data);
};
</script>
"""

# Real-world example from Polynomial AI:
class RealTimeInvoiceConsumer(AsyncWebsocketConsumer):
    """Real-time updates for invoice processing"""
    
    async def connect(self):
        self.invoice_id = self.scope['url_route']['kwargs']['invoice_id']
        self.group_name = f'invoice_{self.invoice_id}'
        
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        
        await self.accept()
        
        # Send current status
        invoice = await self.get_invoice()
        await self.send(text_data=json.dumps({
            'type': 'status',
            'status': invoice.status,
            'progress': invoice.progress
        }))
    
    @database_sync_to_async
    def get_invoice(self):
        return Invoice.objects.get(id=self.invoice_id)
    
    async def invoice_update(self, event):
        await self.send(text_data=json.dumps({
            'type': 'update',
            'status': event['status'],
            'progress': event['progress'],
            'message': event.get('message', ''),
            'timestamp': event['timestamp']
        }))

# Send updates during processing
async def process_invoice(invoice_id):
    invoice = Invoice.objects.get(id=invoice_id)
    channel_layer = get_channel_layer()
    
    # Update status
    await channel_layer.group_send(
        f'invoice_{invoice_id}',
        {
            'type': 'invoice_update',
            'status': 'processing',
            'progress': 10
        }
    )
    
    # Process steps...
    for step in range(10):
        # Do processing
        await asyncio.sleep(1)
        
        # Send progress update
        await channel_layer.group_send(
            f'invoice_{invoice_id}',
            {
                'type': 'invoice_update',
                'status': 'processing',
                'progress': 10 * (step + 1),
                'message': f'Completed step {step + 1}'
            }
        )
```

---

## **Additions:**

### **1. Security Best Practices**
```python
# How do you prevent common security vulnerabilities in Django?
# - CSRF protection
# - XSS prevention
# - SQL injection (ORM handles, but raw SQL?)
# - Clickjacking
# - Security middleware
# - Rate limiting
# - Password hashing
```

### **2. Django in Microservices**
```python
# How would you split a monolithic Django app into microservices?
# - Service boundaries
# - Communication (REST vs gRPC vs messaging)
# - Shared authentication
# - Database per service
# - API Gateway integration
```

### **3. Monitoring & Observability**
```python
# How do you monitor Django applications in production?
# - Logging strategies
# - Metrics collection (Prometheus)
# - APM tools (New Relic, Datadog)
# - Health checks
# - Performance monitoring
```

### **4. Django with Docker/Kubernetes**
```python
# How do you containerize Django applications?
# - Dockerfile best practices
# - Multi-stage builds
# - Environment management
# - Database migrations in containers
# - ConfigMaps and Secrets
```

### **5. Legacy Django Upgrades**
```python
# How would you upgrade Django from 2.x to 4.x?
# - Breaking changes assessment
# - Dependency compatibility
# - Testing strategy
# - Phased rollout
# - Rollback procedures
```

## **Real Interview Scenarios:**

### **Technical Screening (30 mins):**
1. Explain Django's ORM N+1 problem (Q3)
2. Difference between WSGI/ASGI (Q4)
3. How Django handles authentication (Q14)

### **Take-Home Assignment:**
"Build a simple blog with user authentication, CRUD for posts, and commenting system" - tests Q1-10, Q14

### **On-site Technical (1 hour):**
1. Design a scalable e-commerce system with Django (covers Q20, Q27)
2. Debug a performance issue (covers Q3, Q9, Q15)
3. Design a real-time notification system (covers Q5, Q30)

### **System Design Round:**
"How would you design YouTube's video processing pipeline with Django?" - covers:
- Async tasks (Q5)
- File handling (Q17)
- Caching (Q15)
- Database design (Q11, Q27)
- Performance (Q20, Q26)

## **Industry-Specific Additions:**

### **For FinTech (like your Polynomial AI experience):**
```python
# Add: "How would you implement double-entry accounting in Django?"
# - Transaction models
# - ACID compliance
# - Audit trails
# - Reconciliation processes
```

### **For E-commerce:**
```python
# Add: "How would you design a cart/checkout system?"
# - Session vs database carts
# - Inventory management
# - Payment gateway integration
# - Order processing workflows
```

### **For SaaS/Multi-tenancy:**
```python
# Add: "How would you implement multi-tenancy?"
# - Database strategies (shared vs isolated)
# - Tenant isolation
# - Schema management
# - Tenant-aware queries
```