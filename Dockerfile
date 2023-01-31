FROM python:3.11

# Install dependencies
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Run the application
CMD ["python", "main.py"]