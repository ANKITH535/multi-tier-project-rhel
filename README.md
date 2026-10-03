# RHEL Linux Multi-Tier Web Application

A hands-on Linux project demonstrating deployment of a multi-tier web application on Rocky Linux 9.

## Architecture

```text
                    Client / Browser
                           |
                           v
                  +------------------+
                  |   Apache HTTPD   |
                  |     Port 80      |
                  |    Web Tier      |
                  +--------+---------+
                           |
                    Reverse Proxy
                           |
                           v
                  +------------------+
                  |  Flask App       |
                  |    Port 5000     |
                  | Application Tier |
                  +--------+---------+
                           |
                           v
                  +------------------+
                  |      MySQL       |
                  |    Port 3306     |
                  |   Database Tier  |
                  +------------------+
Technologies Used
Rocky Linux 9
Apache HTTP Server
Python
Flask
MySQL
systemd
Apache Reverse Proxy
Linux firewall and networking
Bash/Linux command line
Git and GitHub
Project Structure
multi-tier-project-rhel/
├── app/
│   └── app.py
├── frontend/
│   └── index.html
├── systemd/
│   └── myapp.service
├── apache/
│   └── myapp.conf
├── .env.example
├── .gitignore
└── README.md
Application Flow
A client sends a request to Apache on port 80.
Apache receives the HTTP request.
Apache reverse-proxies the request to the Flask application on port 5000.
Flask connects to the MySQL database.
The application queries the students table.
The database response is returned through Flask and Apache to the client.
Apache Configuration

Apache is configured as a reverse proxy using:

ProxyPass / http://127.0.0.1:5000/
ProxyPassReverse / http://127.0.0.1:5000/

This allows Apache to act as the Web Tier while Flask handles application requests.

Flask Application

The Flask application is located at:

/opt/myapp/app.py

The application:

Runs on port 5000
Connects to MySQL
Queries the students table
Returns database results to the client

Database credentials are supplied through the DB_PASSWORD environment variable instead of being stored directly in the public repository.

systemd Service

The Flask application is managed as a Linux systemd service.

Service:

myapp.service

The service provides:

Automatic application startup
Service management through systemctl
Automatic restart configuration
Integration with the Linux boot process

Useful commands:

systemctl start myapp
systemctl stop myapp
systemctl restart myapp
systemctl status myapp
systemctl enable myapp
Apache Service Management
systemctl start httpd
systemctl stop httpd
systemctl restart httpd
systemctl status httpd
systemctl enable httpd
Testing

Check Apache:

curl http://localhost

Check the Flask application:

curl http://127.0.0.1:5000

Check Apache configuration:

httpd -t

Check listening ports:

ss -ltnp

Check the Flask service:

systemctl status myapp
Security

Sensitive information is not stored in the public repository.

The project uses:

.env

for local environment variables and excludes it through .gitignore.

A safe example is provided as:

.env.example

Never commit real passwords, API keys, or other credentials to GitHub.

Skills Demonstrated
Linux server administration
Apache web server configuration
Reverse proxy configuration
Python Flask deployment
MySQL integration
systemd service management
Linux networking
Service troubleshooting
Environment variables and basic secret management
Git version control
GitHub repository management
Project Outcome

Successfully deployed and tested a multi-tier web application on a Rocky Linux server using Apache, Flask, and MySQL, with the Flask application managed through systemd and Apache configured as a reverse proxy.
