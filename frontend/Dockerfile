# Build stage
FROM node:16 as build
RUN mkdir /app
WORKDIR /app
COPY codebase .
RUN yarn run build

# Production stage
FROM nginx:1.21-alpine
WORKDIR /usr/share/nginx/html/
RUN rm -r ./*
#ADD ./default.conf /etc/nginx/
COPY --from=build /app/dist .