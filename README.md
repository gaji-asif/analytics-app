# Analytics App Backend

## Installation & Setup
### 1. Clone the repository
git clone https://github.com/gaji-asif/analytics-app.git<br>
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
GET   /analytics/blog-views/?object_type=user<br>
GET   /analytics/blog-views/?object_type=user&range=month<br>
GET   /analytics/blog-views/?object_type=user&user=charlie<br>
GET   /analytics/blog-views/?object_type=user&user=alice&range=week<br>
GET   /analytics/blog-views/?object_type=country<br>
GET   /analytics/blog-views/?object_type=country&range=year<br>
GET   /analytics/blog-views/?object_type=country&country=USA<br>
GET   /analytics/blog-views/?object_type=country&country=India&range=month<br>

## API #2 — Top
GET   /analytics/top/?top=blog<br>
GET   /analytics/top/?top=country<br>
GET   /analytics/top/?top=blog<br>
GET   /analytics/top/?top=blog&range=month<br>
GET   /analytics/top/?top=blog&user=john<br>
GET   /analytics/top/?top=user&country=Finland<br>

## API #3 — Performance
GET   /analytics/performance/<br>
GET   /analytics/performance/?compare=week<br>
GET   /analytics/performance/?compare=day<br>
GET   /analytics/performance/?compare=year<br>
GET   /analytics/performance/?user=john<br>
GET   /analytics/performance/?country=India<br>
GET   /analytics/performance/?compare=month&user=john&country=USA<br>




