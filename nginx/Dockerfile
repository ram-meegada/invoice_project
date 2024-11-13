# Second stage: build the Nginx server
FROM nginx:1.23-alpine

# Copying your custom Nginx configuration file
COPY ./default.conf /etc/nginx/conf.d/default.conf

# Create a symlink to enable the configuration
# RUN ln -s /etc/nginx/sites-available/youtube_project /etc/nginx/sites-enabled/youtube_project

# Remove the default log files
RUN rm -f /var/log/nginx/*
