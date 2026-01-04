# Django & DRF Interview Questions

## DJANGO QUESTIONS (32 Questions)

### 📌 Architecture & Core Concepts

#### Q1: What is the MTV architecture in Django?
- **A)** Model-Template-View, similar to MVC where Template is the View and View is the Controller 
- **B)** Model-Test-View
- **C)** Module-Template-Variable
- **D)** Model-Table-View

**Answer: A** — Django uses MTV: Model (data/business logic), Template (presentation), View (request handling/logic). The View acts like a Controller in traditional MVC.

---

#### Q2: What is the purpose of Django middleware?
- **A)** To connect to databases
- **B)** A framework of hooks into Django's request/response processing for modifying requests/responses globally 
- **C)** To create models
- **D)** To render templates

**Answer: B** — Middleware are hooks that process requests before views and responses after views. Examples include authentication, session handling, and CSRF protection.

---

### 📌 Models & Fields

#### Q3: What is the difference between `null=True` and `blank=True`?
- **A)** They are identical
- **B)** `null=True` allows NULL in database, `blank=True` allows empty value in forms/validation 
- **C)** `blank=True` is for databases
- **D)** `null=True` is for forms

**Answer: B** — `null` is database-level (stores NULL). `blank` is validation-level (allows empty form field). For strings, avoid `null=True`; use `blank=True` with `default=''`.

---

#### Q4: What is the difference between ForeignKey and OneToOneField?
- **A)** They are identical
- **B)** ForeignKey allows many-to-one relationships, OneToOneField enforces one-to-one (each related object is unique) 
- **C)** OneToOneField is deprecated
- **D)** ForeignKey is faster

**Answer: B** — ForeignKey creates a many-to-one relationship (many objects can relate to one). OneToOneField is like ForeignKey with `unique=True`, enforcing one-to-one.

---

#### Q5: What is the purpose of `on_delete` parameter in ForeignKey?
- **A)** To delete the model
- **B)** To specify behavior when the referenced object is deleted (CASCADE, PROTECT, SET_NULL, etc.) 
- **C)** To enable soft delete
- **D)** To delete the database

**Answer: B** — `on_delete` defines what happens when the referenced object is deleted. CASCADE deletes related objects, PROTECT prevents deletion, SET_NULL sets to null, etc.

---

#### Q6: What is Django's ContentType framework used for?
- **A)** Managing file content types
- **B)** Creating generic relations between models without hardcoding relationships 
- **C)** Handling HTTP content types
- **D)** Template content management

**Answer: B** — ContentType framework tracks all models in the project, enabling generic foreign keys that can point to any model instance.

---

### 📌 Managers & QuerySets

#### Q7: What is a Django Manager?
- **A)** A user management system
- **B)** An interface through which database query operations are provided to Django models 
- **C)** A project manager
- **D)** A file manager

**Answer: B** — Managers provide the interface for database queries. The default manager is `objects`. Custom managers can add custom querysets and methods.

---

#### Q8: How do you create a custom Manager in Django?
- **A)** Override the Model class
- **B)** Create a class extending `models.Manager` and assign it to a model attribute 
- **C)** Modify settings.py
- **D)** Create a new database

**Answer: B** — Create a class inheriting from `models.Manager`, define custom methods/querysets, and assign it as a model attribute (e.g., `objects = CustomManager()`).

---

#### Q9: What is the purpose of `get_queryset()` in a Manager?
- **A)** To get a single object
- **B)** To return the base QuerySet that the Manager uses, which can be customized 
- **C)** To delete querysets
- **D)** To cache queries

**Answer: B** — `get_queryset()` returns the base QuerySet. Override it to modify default behavior, like automatically filtering active records.

---

### 📌 Query Optimization

#### Q10: What does `select_related()` do in Django ORM and when should you use it?
- **A)** Selects specific fields from a model
- **B)** Creates a SQL JOIN to fetch related ForeignKey/OneToOne objects in a single query, reducing database hits 
- **C)** Selects random objects
- **D)** Creates a subquery for related objects

**Answer: B** — `select_related()` creates a SQL JOIN and includes the fields of the related object in the SELECT statement. Use it for ForeignKey and OneToOneField relationships to avoid additional queries.

---

#### Q11: What is the difference between `select_related()` and `prefetch_related()`?
- **A)** `select_related` is for ManyToMany, `prefetch_related` is for ForeignKey
- **B)** `select_related` uses SQL JOIN for FK/O2O; `prefetch_related` uses separate queries for M2M and reverse FK, joining in Python 
- **C)** They are identical in functionality
- **D)** `prefetch_related` is deprecated

**Answer: B** — 
- **select_related()**: Works via SQL JOIN for single-valued relationships (ForeignKey, OneToOne). Creates one query.
- **prefetch_related()**: Does separate lookups and joins in Python. Suitable for many-valued relationships (ManyToMany, reverse ForeignKey).

---

#### Q12: What is Django's Prefetch object used for?
- **A)** Prefetching static files
- **B)** Customizing the queryset used in `prefetch_related()` with filtering, different attributes, or custom querysets 
- **C)** Caching
- **D)** Preloading templates

**Answer: B** — Prefetch allows customization of `prefetch_related()` by specifying a custom queryset, attribute name, or filtering the prefetched objects. Example: `Prefetch('comments', queryset=Comment.objects.filter(active=True))`

---

#### Q13: What is the N+1 query problem in Django ORM, and how do you solve it?
- **A)** It's a database constraint issue, solved by adding indexes
- **B)** It's when N additional queries are made for N objects when accessing related data; solved using `select_related()` or `prefetch_related()` 
- **C)** It's a pagination issue, solved by using Paginator
- **D)** It's a memory issue, solved by using `iterator()`

**Answer: B** — The N+1 problem occurs when you fetch N objects and then access a related object on each, resulting in N additional queries. Using `select_related()` or `prefetch_related()` fetches related data upfront in fewer queries.

---

#### Q14: What is Django's `defer()` method?
- **A)** Delays query execution
- **B)** Excludes specified fields from the SELECT, loading them lazily only when accessed 
- **C)** Defers validation
- **D)** Postpones migrations

**Answer: B** — `defer()` excludes specified fields from the initial query. Those fields are loaded from the database when accessed. Opposite of `only()`.

---

#### Q15: What is Django's `only()` method?
- **A)** Limits results to one
- **B)** Loads only the specified fields immediately; other fields are deferred 
- **C)** Only runs in debug mode
- **D)** Returns only unique values

**Answer: B** — `only()` specifies which fields to load immediately. All other fields are deferred and loaded when accessed. Opposite of `defer()`.

---

### 📌 Query Expressions (F, Q objects)

#### Q16: What is Django's ORM `F()` expression used for?
- **A)** Filtering by function
- **B)** Referencing model field values directly in the database without loading them into Python, enabling atomic operations 
- **C)** Formatting output
- **D)** Creating foreign keys

**Answer: B** — `F()` expressions allow you to reference model field values and perform database operations using them without pulling data into Python memory. This enables atomic updates, field comparisons, and calculations without race conditions.

---

#### Q17: What is the output query for this code?
```python
from django.db.models import F
Product.objects.filter(price__gt=F('discounted_price'))
```
- **A)** Products where price > 0
- **B)** Products where price field value is greater than discounted_price field value 
- **C)** All products
- **D)** Error

**Answer: B** — `F('discounted_price')` references the discounted_price field value in the database, comparing it with price at the database level.

---

#### Q18: What is the correct way to perform an atomic increment in Django?
```python
# Option A
product.stock += 1
product.save()

# Option B
from django.db.models import F
Product.objects.filter(id=product.id).update(stock=F('stock') + 1)

# Option C
with transaction.atomic():
    product.stock += 1
    product.save()
```
- **A)** Option A
- **B)** Option B 
- **C)** Option C
- **D)** Option D

**Answer: B** — Option B uses `F()` expression which performs the increment at the database level atomically, preventing race conditions. Option A and C can have race conditions.

---

#### Q19: What is the purpose of Q objects in Django?
- **A)** To query strings
- **B)** To build complex queries with OR, AND, and NOT operations 
- **C)** To queue queries
- **D)** To quote strings

**Answer: B** — Q objects allow complex lookups with `|` (OR), `&` (AND), and `~` (NOT), enabling queries that can't be expressed with simple filter kwargs. Example: `Q(status='active') | Q(priority__gt=5)`

---

### 📌 QuerySet Methods

#### Q20: What will be the output of the following Django ORM query?
```python
User.objects.filter(age__gt=25).exclude(status='inactive').count()
```
- **A)** Returns all users with age > 25 OR status != 'inactive'
- **B)** Returns count of users with age > 25 AND status != 'inactive' 
- **C)** Returns a queryset of filtered users
- **D)** Raises an error

**Answer: B** — The query filters users with age greater than 25, then excludes those with status 'inactive', and returns the count of remaining users.

---

#### Q21: What is the purpose of `values()` and `values_list()` in Django?
- **A)** Return model instances
- **B)** `values()` returns dictionaries, `values_list()` returns tuples of specified field values instead of model instances 
- **C)** Validate values
- **D)** Set default values

**Answer: B** — Both return specific fields instead of full model instances. `values()` returns dictionaries, `values_list()` returns tuples (use `flat=True` for single field).

---

#### Q22: What is `exists()` in Django ORM and when should you use it?
- **A)** Checks if model exists
- **B)** Returns True if QuerySet contains any results, more efficient than `len()` or `bool()` for existence checks 
- **C)** Checks file existence
- **D)** Validates objects

**Answer: B** — `exists()` executes a minimal query to check for at least one result. More efficient than retrieving all objects just to check existence.

---

#### Q23: What is Django's `annotate()` used for and how does it differ from `aggregate()`?
- **A)** They are identical
- **B)** `annotate` adds calculated values per object in QuerySet; `aggregate` returns a single dictionary of values for entire QuerySet 
- **C)** `aggregate` is deprecated
- **D)** `annotate` is faster

**Answer: B** — 
- **annotate()**: Adds a calculated field to each object in the queryset (e.g., comment count per post)
- **aggregate()**: Computes a single value across the entire queryset (e.g., total count, average of all)

---

### 📌 CRUD & Bulk Operations

#### Q24: What is the purpose of `get_or_create()` in Django?
- **A)** Only gets objects
- **B)** Retrieves an object matching the lookup, or creates one if it doesn't exist, returning tuple (object, created) 
- **C)** Only creates objects
- **D)** Deletes then creates

**Answer: B** — `get_or_create()` is atomic (with proper database support) and returns a tuple of (object, created_boolean). Useful for avoiding race conditions.

---

#### Q25: What is `update_or_create()` in Django?
- **A)** Updates all objects
- **B)** Updates an object matching lookup with defaults, or creates a new object if none exists 
- **C)** Creates then updates
- **D)** Deletes and recreates

**Answer: B** — `update_or_create()` finds matching objects and updates them with defaults dict, or creates a new object. Returns (object, created_boolean).

---

#### Q26: What are Django's `bulk_create()` and `bulk_update()` methods used for?
- **A)** Creating bulk emails
- **B)** Efficiently inserting/updating multiple objects in single database queries 
- **C)** Creating backups
- **D)** Bulk validation

**Answer: B** — 
- **bulk_create()**: Inserts multiple objects in one query
- **bulk_update(objs, fields)**: Updates specified fields of multiple objects efficiently

Note: Neither calls `save()` or triggers signals, and `bulk_create` may not return IDs on all databases.

---

### 📌 Transactions

#### Q27: What does `@transaction.atomic` decorator do in Django?
- **A)** Makes the view function run faster
- **B)** Ensures all database operations in the block succeed or all are rolled back 
- **C)** Prevents concurrent access to the view
- **D)** Caches the database results

**Answer: B** — `@transaction.atomic` creates an atomic block where all database operations either complete successfully together or are all rolled back if any exception occurs.

---

### 📌 Signals

#### Q28: What are Django signals and when should you use them?
- **A)** Error signals
- **B)** Decoupled notifications allowing senders to notify receivers when actions occur (like model save/delete) 
- **C)** HTTP status signals
- **D)** Log signals

**Answer: B** — Signals provide decoupled communication between applications. Common uses include `post_save`, `pre_delete` actions. Use cautiously as they can make code harder to follow.

---

#### Q29: What is the difference between `pre_save` and `post_save` signals?
- **A)** They are identical
- **B)** `pre_save` fires before the model's `save()` method (can modify instance), `post_save` fires after save() completes (instance has PK) 
- **C)** `post_save` is deprecated
- **D)** `pre_save` is for forms only

**Answer: B** — 
- **pre_save**: Triggered before database save - can modify the instance
- **post_save**: Triggered after save completes - instance has a primary key, includes `created` argument (True for new instances)

---

### 📌 Migrations

#### Q30: What is a Django migration and what's the difference between `makemigrations` and `migrate`?
- **A)** Moving Django to another server; they are identical commands
- **B)** A way to propagate model changes to database schema; `makemigrations` creates files, `migrate` applies them 
- **C)** A data backup
- **D)** A code refactoring tool

**Answer: B** — 
- **Migrations**: Python files that describe changes to models, version-controlled
- **makemigrations**: Detects model changes and creates migration files
- **migrate**: Executes migrations against the database

---

### 📌 Python Fundamentals

#### Q31: In Python, what is the difference between `__str__` and `__repr__`?
- **A)** They are identical
- **B)** `__str__` is for end-users (readable), `__repr__` is for developers (unambiguous) 
- **C)** `__repr__` is deprecated
- **D)** `__str__` is only used in Python 2

**Answer: B** — `__str__` returns a human-readable string representation, while `__repr__` returns an unambiguous representation primarily for debugging and development.

---

#### Q32: What is the Global Interpreter Lock (GIL) in Python and how does it affect Django applications?
- **A)** It's a security feature
- **B)** It prevents multiple native threads from executing Python bytecodes simultaneously, limiting CPU-bound parallelism 
- **C)** It locks database connections globally
- **D)** It's deprecated

**Answer: B** — The GIL ensures only one thread executes Python bytecode at a time, which affects CPU-bound multi-threaded applications. For I/O-bound Django apps, this is less of an issue; for CPU-bound work, use multiprocessing or async.

---

#### Q33: What is the output of this code?
```python
def append_to(element, to=[]):
    to.append(element)
    return to

print(append_to(1))
print(append_to(2))
```
- **A)** `[1]` then `[2]`
- **B)** `[1]` then `[1, 2]` 
- **C)** Error
- **D)** `[1, 2]` then `[1, 2]`

**Answer: B** — Default mutable arguments in Python are evaluated once when the function is defined, not each time it's called. The same list object is reused across calls.

---

## DJANGO REST FRAMEWORK QUESTIONS (26 Questions)

### 📌 Request/Response Lifecycle

#### Q1: What is the DRF request processing order?
- **A)** View → Authentication → Permission → Throttling
- **B)** Authentication → Permission → Throttling → View 
- **C)** Permission → Authentication → View → Throttling
- **D)** Throttling → Permission → Authentication → View

**Answer: B** — DRF processes requests in order:
1. **Authentication** (who are you?)
2. **Permission** (are you allowed?)
3. **Throttling** (rate limiting)
4. **View** logic executes

---

#### Q2: What is content negotiation in DRF?
- **A)** Contract negotiation
- **B)** The process of selecting the best response format based on client request headers 
- **C)** Content moderation
- **D)** Database negotiation

**Answer: B** — Content negotiation examines Accept headers and URL suffix to determine which renderer to use for the response.

---

### 📌 Views & ViewSets

#### Q3: What is the difference between APIView and ViewSet in DRF?
- **A)** They are identical
- **B)** APIView uses HTTP method handlers (get, post); ViewSet uses actions (list, create, retrieve) with router integration 
- **C)** ViewSet is deprecated
- **D)** APIView doesn't support authentication

**Answer: B** — 
- **APIView**: Class-based view where you define `get()`, `post()`, etc. methods mapping to HTTP methods
- **ViewSet**: Combines related views into single class with `list()`, `create()`, `retrieve()`, etc. actions, works with Routers for automatic URL configuration

---

#### Q4: What does `perform_create()` do in DRF ViewSets?
- **A)** Validates data
- **B)** Hook for modifying how instance creation is performed, commonly used to add extra data like current user 
- **C)** Creates the database table
- **D)** Performs permission checks

**Answer: B** — `perform_create` is called by CreateModelMixin to save the serializer. Override it to pass additional data: `serializer.save(owner=self.request.user)`.

---

#### Q5: What is the purpose of `get_queryset()` in DRF ViewSets?
- **A)** Returns single object
- **B)** Returns the queryset that should be used for list views and for object lookups 
- **C)** Creates querysets
- **D)** Deletes querysets

**Answer: B** — `get_queryset()` returns the queryset used for listing and detail views. Override it for dynamic filtering based on user, request, etc.

---

#### Q6: What is `@action` decorator in DRF ViewSets and what's the difference between `detail=True` and `detail=False`?
- **A)** Animation decorator
- **B)** Creates custom endpoints on ViewSets; `detail=True` requires object ID, `detail=False` is collection-level 
- **C)** Deprecated decorator
- **D)** Performance decorator

**Answer: B** — 
- **@action**: Adds custom routes to ViewSets beyond standard CRUD operations
- **detail=True**: Routes for individual objects, requires pk (e.g., `/items/1/action/`)
- **detail=False**: Routes for entire collection (e.g., `/items/action/`)

---

### 📌 Serializers - Basics

#### Q7: What is the difference between Serializer and ModelSerializer in DRF?
- **A)** They are identical
- **B)** ModelSerializer auto-generates fields from model, includes default create/update methods, and validators 
- **C)** Serializer is faster
- **D)** ModelSerializer doesn't support nested serialization

**Answer: B** — ModelSerializer is a shortcut that automatically generates:
- Fields based on the model
- Default implementations of `create()` and `update()`
- Simple default validators

---

#### Q8: What is the purpose of SerializerMethodField in DRF?
- **A)** Validates methods
- **B)** A read-only field that gets its value by calling a method on the serializer class 
- **C)** Creates method serializers
- **D)** Serializes HTTP methods

**Answer: B** — SerializerMethodField is read-only and calls `get_<field_name>(self, obj)` method on the serializer to compute its value dynamically.

---

#### Q9: What is the purpose of `get_serializer_context()` in DRF?
- **A)** Gets serializer class
- **B)** Returns a dictionary of extra context passed to the serializer, including request, view, and format 
- **C)** Creates context processors
- **D)** Validates context

**Answer: B** — `get_serializer_context()` provides context dict passed to serializers, typically containing 'request', 'format', and 'view'. Override to add custom context.

---

#### Q10: How do you implement nested serializers in DRF?
- **A)** Using StringRelatedField
- **B)** Include another serializer as a field, optionally with `many=True` for reverse relations 
- **C)** Using PrimaryKeyRelatedField only
- **D)** Nesting is not supported

**Answer: B** — Nest serializers by declaring them as fields:
- `author = AuthorSerializer(read_only=True)` for single object
- `comments = CommentSerializer(many=True)` for multiple objects

---

#### Q11: What is HyperlinkedModelSerializer?
- **A)** A faster serializer
- **B)** A serializer that uses hyperlinks for relationships instead of primary keys 
- **C)** A deprecated serializer
- **D)** A serializer for hyperlinks only

**Answer: B** — HyperlinkedModelSerializer uses URLs to represent relationships. It includes a `url` field and represents related models as hyperlinks instead of IDs.

---

### 📌 Serializers - Related Fields

#### Q12: What is the difference between PrimaryKeyRelatedField and SlugRelatedField?
- **A)** They are identical
- **B)** PrimaryKeyRelatedField uses the PK; SlugRelatedField uses a specified slug field for representation 
- **C)** SlugRelatedField is read-only
- **D)** PrimaryKeyRelatedField is deprecated

**Answer: B** — 
- **PrimaryKeyRelatedField**: Represents relations by ID
- **SlugRelatedField**: Uses any unique field (specified via `slug_field` parameter) for representation

---

### 📌 Serializers - Validation

#### Q13: How do you customize field validation in DRF?
- **A)** Only in the model
- **B)** Using `validate_<fieldname>()` method for single fields, `validate()` for multiple fields, or field-level validators 
- **C)** In settings.py
- **D)** Validation cannot be customized

**Answer: B** — DRF provides multiple validation levels:
1. **Field validators**: Passed to field definition
2. **validate_<field>()**: Method for single field validation
3. **validate()**: Method for cross-field validation

---

### 📌 Authentication

#### Q14: What is TokenAuthentication in DRF?
- **A)** JWT tokens
- **B)** Simple token-based HTTP authentication using a database-stored token per user 
- **C)** OAuth tokens
- **D)** Deprecated authentication

**Answer: B** — TokenAuthentication uses a simple token in the Authorization header. Tokens are stored in the database. Use with HTTPS only.

---

#### Q15: What is the purpose of `authentication_classes` in DRF views?
- **A)** Creates users
- **B)** Specifies which authentication methods are used to identify the requesting user 
- **C)** Validates passwords
- **D)** Encrypts data

**Answer: B** — `authentication_classes` defines which authentication schemes are tried. DRF attempts each in order until one succeeds or all fail.

---

#### Q16: What are `request.user` and `request.auth` in DRF?
- **A)** Always AnonymousUser and None
- **B)** `request.user` is the authenticated user (or AnonymousUser); `request.auth` is additional authentication context (like token instance) 
- **C)** The user model class and auth settings
- **D)** Request data only

**Answer: B** — 
- **request.user**: Authenticated user instance, or AnonymousUser if unauthenticated
- **request.auth**: Authentication context returned by authenticator (e.g., Token instance for TokenAuthentication)

---

### 📌 Permissions

#### Q17: What is the difference between IsAuthenticated, IsAdminUser, and IsAuthenticatedOrReadOnly permissions?
- **A)** They are identical
- **B)** IsAuthenticated allows any authenticated user; IsAdminUser requires `is_staff=True`; IsAuthenticatedOrReadOnly allows read-only for unauthenticated 
- **C)** They are all deprecated
- **D)** Only IsAuthenticated works

**Answer: B** — 
- **IsAuthenticated**: Any authenticated user
- **IsAdminUser**: Requires `user.is_staff=True`
- **IsAuthenticatedOrReadOnly**: Authenticated users get full access; unauthenticated get read-only (GET, HEAD, OPTIONS)

---

#### Q18: How do you implement custom permissions in DRF and what's the difference between `has_permission` and `has_object_permission`?
- **A)** In settings.py only
- **B)** Extend BasePermission; `has_permission` checks view-level access, `has_object_permission` checks access to specific objects 
- **C)** Using decorators only
- **D)** Permissions cannot be customized

**Answer: B** — 
- Create class inheriting from **BasePermission**
- **has_permission()**: Runs on all requests (list, create) - view-level
- **has_object_permission()**: Runs only when accessing specific object (retrieve, update, delete) - object-level

---

### 📌 Throttling

#### Q19: What are throttling classes in DRF?
- **A)** Performance optimizers
- **B)** Classes that control the rate of requests a client can make to prevent abuse 
- **C)** Thread managers
- **D)** Database throttlers

**Answer: B** — Throttling implements rate limiting. Built-in classes include:
- **AnonRateThrottle**: For anonymous users
- **UserRateThrottle**: For authenticated users
- **ScopedRateThrottle**: Different rates for different API endpoints

---

### 📌 Filtering & Searching

#### Q20: What is `filter_backends` in DRF?
- **A)** Database backends
- **B)** Classes that filter and order querysets based on request parameters (search, ordering, filtering) 
- **C)** Backend servers
- **D)** Cache backends

**Answer: B** — Filter backends like SearchFilter, OrderingFilter, and DjangoFilterBackend provide automatic query filtering based on URL parameters.

---

#### Q21: What is DRF's SearchFilter used for?
- **A)** File searching
- **B)** Simple single-query text search across specified fields using `?search=` parameter 
- **C)** Database searching
- **D)** Log searching

**Answer: B** — SearchFilter enables simple search functionality. Configure `search_fields` on the view to specify searchable fields. Supports prefix modifiers like `^` (starts-with), `=` (exact), `@` (full-text search).

---

### 📌 Pagination

#### Q22: What is `pagination_class` in DRF?
- **A)** Page counter
- **B)** Class that controls how large result sets are split into individual pages of data 
- **C)** Page renderer
- **D)** Database pagination

**Answer: B** — Pagination classes control how results are paginated:
- **PageNumberPagination**: `?page=N`
- **LimitOffsetPagination**: `?limit=N&offset=M`
- **CursorPagination**: Encoded cursor for consistent ordering

---

#### Q23: What is CursorPagination and when should you use it?
- **A)** Mouse cursor position
- **B)** A pagination style using encoded cursors for consistent ordering, ideal for large/real-time datasets 
- **C)** Deprecated pagination
- **D)** Database cursor

**Answer: B** — CursorPagination provides consistent ordering even when new items are added. It's more efficient for large datasets and prevents page drift. Best for real-time feeds.

---

#### Q24: How do you implement custom pagination in DRF?
- **A)** Override the paginate method in the view
- **B)** Create a class extending PageNumberPagination and set `pagination_class` in the view 
- **C)** Set PAGINATION_CLASS in Django settings
- **D)** Pagination cannot be customized

**Answer: B** — Custom pagination is created by subclassing pagination classes like PageNumberPagination, configuring attributes like `page_size`, and setting it as `pagination_class` in views.

---

### 📌 Parsers & Renderers

#### Q25: What is the purpose of `parser_classes` in DRF?
- **A)** Parsing URLs
- **B)** Classes that handle parsing request body content of different media types (JSON, form data, etc.) 
- **C)** Query parsing
- **D)** Log parsing

**Answer: B** — Parser classes parse incoming request content. Default includes JSON and form parsers. Add MultiPartParser for file uploads.

---

#### Q26: What is the purpose of `renderer_classes` in DRF?
- **A)** Rendering templates
- **B)** Classes that handle rendering response data into different media types (JSON, HTML, etc.) 
- **C)** CSS rendering
- **D)** Image rendering

**Answer: B**
Explanation: Renderers control response format:
- **JSONRenderer**: Produces JSON
- **BrowsableAPIRenderer**: Produces HTML for the browsable API


---