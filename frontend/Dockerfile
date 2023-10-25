# Build stage
FROM node:16 as build
RUN mkdir /app
WORKDIR /app
COPY ./codebase .
RUN npm install --legacy-peer-deps
RUN yarn build

# Production stage
FROM nginx:1.21-alpine
WORKDIR /usr/share/nginx/html/
RUN rm -r ./*
COPY --from=build /app/dist .
