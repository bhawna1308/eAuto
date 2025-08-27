FROM python:3.10-slim

WORKDIR /project

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY model ./model
COPY app.py ./app.py

# Expose the Streamlit default port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--browser.serverAddress=localhost"]

# docker build -t streamlit-app  . // local
# docker run -p 8501:8501 streamlit-app
#http://127.0.0.1:8501

#docker hub
# docker build -t aibhawna/retail-forecasting:latest .  
# docker login
# docker push aibhawna/retail-forecasting:latest

# docker pull aibhawna/retail-forecasting:latest
# docker run -p 8501:8501 aibhawna/retail-forecasting:latest

