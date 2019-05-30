# Python Flask Sample

1. install Python 3.7
2. pip install virtualenv
3. virtualenv venv
4. source ./venv/bin/active (Linux)
5. pip install -r requirements.txt

```bash
export APP_SETTINGS=config.Config
python manage.py
curl -X GET http://localhost:5000/index
# {"data":"Hello"}
```