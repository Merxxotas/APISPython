# Use the image
#FROM jenkins/jenkins:lts
# jenkins/jenkins:alpine3.19-jdk21

# Switch to root user to perform privileged operations
#USER root

# Install any dependencies or perform custom setup
# For example, if you want to install Docker CLI to use it within Jenkins:
#RUN apt-get update && \
#    apt-get install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common && \
#    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
#    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" && \
#    apt-get update && \
#    apt-get install -y docker-ce-cli

# Copy any configuration files, plugins, or scripts that you want to include in the image
# COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
# RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt

# Optionally, you can add volumes to ensure data persists across container restarts
# Note: Volumes are typically managed in docker-compose.yml or the Docker run command, not in the Dockerfile.
#VOLUME /var/jenkin-data

# Switch back to the jenkins user for security
#USER jenkins

# Expose the default Jenkins port 8000
#EXPOSE 8000

# Expose the Jenkins slave agent port (optional)
#EXPOSE 50000

# Start Jenkins as usual
#CMD ["jenkins.sh"]

# Use the image
FROM jenkins/jenkins:alpine3.19-jdk21

# Switch to root user to perform privileged operations
USER root

# Install Docker CLI
RUN apk update && \
    apk add --no-cache docker-cli

# Copy any configuration files, plugins, or scripts that you want to include in the image
# COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
# RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt

# Optionally, you can add volumes to ensure data persists across container restarts
# Note: Volumes are typically managed in docker-compose.yml or the Docker run command, not in the Dockerfile.
VOLUME /var/jenkins-data

# Switch back to the jenkins user for security
USER jenkins

# Expose the default Jenkins port 8080
EXPOSE 8000

# Expose the Jenkins slave agent port (optional)
EXPOSE 50000

# Start Jenkins as usual
CMD ["jenkins.sh"]
