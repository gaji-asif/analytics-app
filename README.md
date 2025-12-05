# Analytics App Backend

## Installation & Setup
### 1. Clone the repository
https://github.com/gaji-asif/analytics-app.git<br>
cd analytics-app<br><br>

### 2. Create Virtual Environment
python -m venv venv<br>
source venv/bin/activate   # Mac/Linux<br>
venv\Scripts\activate      # Windows<br><br>

### 3. Install dependencies
pip install -r requirements.txt<br><br>

### 4. Run migrations
python manage.py migrate<br><br>

### 5. Run development Server
python manage.py runserver<br><br>


# API Endpoints

## API #1 — Blog Views
{{base_url}}/analytics/blog-views/?object_type=user<br>
{{base_url}}/analytics/blog-views/?object_type=user&range=month<br>
{{base_url}}/analytics/blog-views/?object_type=user&user=charlie<br>
{{base_url}}/analytics/blog-views/?object_type=user&user=alice&range=week<br>
{{base_url}}/analytics/blog-views/?object_type=country<br>
{{base_url}}/analytics/blog-views/?object_type=country&range=year<br>
{{base_url}}/analytics/blog-views/?object_type=country&country=USA<br>
{{base_url}}/analytics/blog-views/?object_type=country&country=India&range=month<br>

## API #2 — Top
{{base_url}}/analytics/top/?top=blog<br>
{{base_url}}/analytics/top/?top=country<br>
{{base_url}}/analytics/top/?top=blog<br>
{{base_url}}/analytics/top/?top=blog&range=month<br>
{{base_url}}/analytics/top/?top=blog&user=john<br>
{{base_url}}/analytics/top/?top=user&country=Finland<br>

## API #3 — Performance
{{base_url}}/analytics/performance/
{{base_url}}/analytics/performance/?compare=week
{{base_url}}/analytics/performance/?compare=day
{{base_url}}/analytics/performance/?compare=year
{{base_url}}/analytics/performance/?user=john
{{base_url}}/analytics/performance/?country=India
{{base_url}}/analytics/performance/?compare=month&user=john&country=USA




