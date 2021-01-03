# todo-exercise

## Tech Stack
- Python 3.8
- [FastAPI](https://fastapi.tiangolo.com/)

## API Documentation
FastApi automatically create a swagger documentation, which is available at the following link: 
[http://localhost:5000/docs](http://localhost:5000/docs)
 
## Quickstart
### Running it locally via shell and vanilla Python & virtualenv 
```shell script
# Clone the repo and run the following commands from the project root folder
# The following command will use whichever Python 3 version you have in your system, the project was initially developed on Python 3.8, but Python 3.9 or Python 3.7 should work as well 
# If you have trouble managing your local Python versions, consider using a tool like pipenv: https://pypi.org/project/pipenv/
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --port 5000
```

### Running React frontend
Frontend can be accessed at: [http://localhost:5000/views/index.html](http://localhost:5000/views/index.html)

### Running tests
```shell script
pytest
```
