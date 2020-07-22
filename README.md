# junk-ai
Junk.ai

### Setup
**Use of virtual environment highly recommended.** Requires pip version >19.0 (`pip install --upgrade pip`):
`pip install -r requirements.txt`

### Run:
With python: `python run.py`
With gunicorn: `gunicorn run:app`
(Running with `gunicorn --workers 1 run:app` may resolve issues relating to server CPU and RAM limits)