# Analytics App Backend

## Installation & Setup
1. Clone the repository
https://github.com/gaji-asif/analytics-app.git
cd analytics-app

2. Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Run migrations
python manage.py migrate

5. Run development Server
python manage.py runserver


