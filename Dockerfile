#Using an official Nginx image as the base
FROM nginx:stable

#Maintainer or author
LABEL org.opencontainers.image.authors="Preston <cantupre@gmail.com>"

#Setting the working directory
WORKDIR /usr/share/nginx/html

#Defining a runtime enviroment vaiable for the port number
ENV http_port=80

#Exposing the port
EXPOSE ${http_port}

#Copying the new html file into the container 
COPY ./index.html ./index.html

#Setting the command to run when the container starts
CMD ["nginx","-g","daemon off;"]

#Adding a healthcheck
HEALTHCHECK --interval=5m --timeout=3s \
	CMD curl -f http://localhost:{http_port} || exit 1
