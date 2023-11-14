FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install --force-reinstall -v "aiogram==2.23.1"
RUN pip install requests
RUN pip install folium
RUN pip install markup