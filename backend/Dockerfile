# BUILD STAGE
FROM maven:3.9.4-amazoncorretto-20 AS build
WORKDIR /usr/src/toktik
COPY codebase/pom.xml .
RUN mvn -B dependency:go-offline
COPY ./codebase/src ./src
RUN mvn clean install -Dmaven.test.skip=true


# RUN STAGE
FROM openjdk:17
WORKDIR /toktik
COPY --from=build /usr/src/toktik/target/toktik-1.0.jar ./toktik.jar
EXPOSE 5000
CMD ["java","-jar","/toktik/toktik.jar"]
