FROM python:3.11
 
# Set the working directory in the container

WORKDIR /Geninsights_data_lens
 
# Copy the contents of the local directory into the container

COPY . /Geninsights_data_lens
 
# Set environment variable to indicate development environment

ENV env=dev
 
# Install virtualenv globally and upgrade pip

RUN pip install --upgrade pip && pip install virtualenv
 
# Create a virtual environment in the /env directory

RUN python3.11 -m virtualenv /data_lens_env
 
# Activate the virtual environment and install dependencies

RUN /data_lens_env/bin/pip install -r requirements.txt
 
# Set the PATH to prioritize the virtual environment

ENV PATH="/data_lens_env/bin:$PATH"
 
# Command to run the FastAPI application on port 8016

CMD ["uvicorn", "Geninsights_user_management.main:app", "--host", "0.0.0.0", "--port", "8016"]%    
