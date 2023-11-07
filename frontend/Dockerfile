# Build stage
FROM node:16 as build
RUN mkdir /app
WORKDIR /app
COPY codebase .
RUN yarn run build

# Production stage
FROM nginx:1.21-alpine
ADD ./default.conf /etc/nginx/
WORKDIR /usr/share/nginx/html/
RUN rm -r ./*
COPY --from=build /app/dist .
