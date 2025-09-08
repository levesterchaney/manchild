# Stage 1: Build the Vue.js application
FROM node:lts-alpine as build-stage

WORKDIR /app

COPY package*.json ./

RUN yarn install

COPY . .

# Build the Vue.js application for production
RUN yarn run build

# Stage 2: Serve the built application with Nginx
FROM nginx:stable-alpine as production-stage

# Copy the built Vue.js application from the build-stage to Nginx's web root
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Expose port 80 for the web server
EXPOSE 80