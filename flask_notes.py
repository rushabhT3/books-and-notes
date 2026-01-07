Here is the comprehensive guide for all five intermediate patterns commonly found in HackerRank Flask/REST API challenges.

---

### 1. Consuming an External API (The Aggregator)

HackerRank often hosts data on a `jsonmock` endpoint. Your task is usually to loop through **multiple pages** of that API, aggregate the data, and perform a calculation.

```python
import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/stats', methods=['GET'])
def get_movie_stats():
    url = "https://jsonmock.hackerrank.com/api/movies"
    response = requests.get(url).json()
    total_pages = response['total_pages']
    
    year_counts = {}

    # Loop through all pages to aggregate data
    for page in range(1, total_pages + 1):
        page_data = requests.get(f"{url}?page={page}").json()
        for movie in page_data['data']:
            year = movie['Year']
            year_counts[year] = year_counts.get(year, 0) + 1
    
    # Logic: Find the year with the maximum movies
    max_year = max(year_counts, key=year_counts.get)
    
    return jsonify({
        "most_productive_year": max_year,
        "movies_count": year_counts[max_year]
    }), 200

```

---

### 2. Request Data Validation

HackerRank test cases will intentionally send "broken" JSON to see if your API crashes or handles it with a `400 Bad Request`.

```python
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    # 1. Check if body exists
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    
    # 2. Check for required fields
    required_fields = ['name', 'email']
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({"error": f"Field '{field}' is missing or empty"}), 400
            
    # Logic to add user (omitted for brevity)
    return jsonify({"message": "User created successfully"}), 201

```

---

### 3. Searching (Partial Match)

Unlike filtering (which is exact), searching usually requires case-insensitive partial matches.

```python
@app.route('/api/search', methods=['GET'])
def search_users():
    query = request.args.get('q', '').lower()
    
    # If no query, return empty list or all users based on requirements
    if not query:
        return jsonify([])

    # Logic: Search for substring in 'name'
    results = [u for u in users if query in u['name'].lower()]
    
    return jsonify(results), 200

```

---

### 4. Filtering and Sorting

This handles multiple query parameters simultaneously to narrow down a dataset.

```python
@app.route('/api/products', methods=['GET'])
def filter_products():
    category = request.args.get('category')
    sort_key = request.args.get('sort', 'price') # Default sort
    order = request.args.get('order', 'asc')

    # Filtering
    filtered = [p for p in products if p['category'] == category] if category else products
    
    # Sorting
    is_desc = (order == 'desc')
    filtered.sort(key=lambda x: x.get(sort_key), reverse=is_desc)
    
    return jsonify(filtered), 200

```

---

### 5. Pagination

To prevent performance issues, you must limit the number of items returned. This involves calculating `start` and `end` indices.

```python
@app.route('/api/items', methods=['GET'])
def paginate_items():
    # Get parameters with defaults
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)

    # Calculate indices
    start = (page - 1) * per_page
    end = start + per_page
    
    # Slice the list
    paginated_items = items_list[start:end]
    
    return jsonify({
        "current_page": page,
        "total_items": len(items_list),
        "data": paginated_items
    }), 200

```

---

### Summary Checklist for Intermediate Level

* **Status Codes:** Always return `200` for success, `201` for created, `400` for bad input, and `404` for not found.
* **Data Types:** Use `type=int` in `request.args.get()` to prevent string math errors.
* **Edge Cases:** Always check if a list is empty or if an external API call fails (returns a non-200 code).

**Would you like me to create a mock "Full Solution" that combines several of these into one script to practice?**
