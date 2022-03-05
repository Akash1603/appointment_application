# appointment-application
Purpose of this application is to manage the appointments.
# Running the Project
Note: Assuming that you having python latest version in your system.

1. Create environment using following command.
* Run $ sudo apt install python3.9-venv command to install virtual environment.
* Run $ python3.9 -m venv env command to Create Virtual environment.
* Run source env/bin/activate command to Activate Virtual environment.
2. Install requirements of the project.
* Run pip install -r requirements.txt
# Running the Project API's 
Hostname = 127.0.0.1:8000

1. Endpoint for create appointment.
* http://{hostname}/new/

2. Endpoint to check the list of appointment.
* http://{hostname}/alist/

3. Endpoint to check the detail of appointment.
* http://{hostname}/vlist/11

4. Endpoint to update the appointment.
* http://{hostname}/ulist/11

5. Endpoint to delete the appointment.
* http://{hostname}/dlist/11