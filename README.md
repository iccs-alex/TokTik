# Alex's TikTok Clone

### I have 4 submodules in my repo:

&nbsp;&nbsp;&nbsp;&nbsp;The frontend repo's relative path is **./frontend/codebase**

&nbsp;&nbsp;&nbsp;&nbsp;The backend repo's relative path is **./backend/codebase**

&nbsp;&nbsp;&nbsp;&nbsp;The repo for the video workers has the relative path **./TokTik_Workers**

&nbsp;&nbsp;&nbsp;&nbsp;The socketIO server repo's relative path is **./socketio**

<br/>
First, when you clone the project, make sure to clone the submodules as well.

<br/><br/>
Then, you need to build some images and start the K8S cluster.

<br/>

Run the following docker build commands from the root of the project (will take about 3 minutes):
  ```
    cd frontend/codebase && yarn && cd ../..

    docker build -t toktik-frontend:v1 frontend

    docker build -t toktik-backend:v1 backend

    docker build -t toktik-socketio:v1 socketio_server

    docker build -t toktik-conversion:v1 TokTik_Workers/conversion

    docker build -t toktik-processing:v1 TokTik_Workers/processing

    docker build -t toktik-thumbnail:v1 TokTik_Workers/thumbnail
  ```

<br/>

You need to have the traefik ingress controller running, the easiest way is to use helm by running the following commands:
  ```
    helm repo add traefik https://traefik.github.io/charts

    helm repo update

    helm install traefik traefik/traefik
  ```

<br/>

Finally, get the K8S cluster up and running with the following command:
  ```
    kubectl apply -R -f k8s
  ```

<br/>

Now, just open up a browser window and type 'localhost' as the URL (use '127.0.0.1' if there are issues).
