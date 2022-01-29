env:
	pip install --upgrade pip
	pip install setuptools
	pip install -r requirements.txt

start:
	uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
	#uvicorn app.main:app --reload --host 137.184.26.165 --port 8000

restart-service:
	cp etc/mywebsite.service /etc/systemd/system/
	systemctl daemon-reload
	systemctl enable mywebsite.service
	systemctl start mywebsite.service

stop-service:
	systemctl disable mywebsite.service

.PHONY: env start restart-service stop-service
