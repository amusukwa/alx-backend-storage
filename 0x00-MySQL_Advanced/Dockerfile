# Use Ubuntu 18.04 as base image
FROM ubuntu:18.04

# Install Python 3.7 and MySQL
RUN apt-get update && apt-get install -y python3.7 python3-pip mysql-server

# Expose MySQL port
EXPOSE 3306

# Start MySQL service when container starts
CMD ["service", "mysql", "start"]
