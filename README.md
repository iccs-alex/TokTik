## Alex's TikTok Clone

I have 4 submodules in my repo:

The frontend repo's relative path is ./frontend/codebase
The backend repo's relative path is ./backend/codebase
The repo for the video workers has the relative path ./TokTik_Workers
The socketIO server repo's relative path is ./socketio


First, when you clone the project, make sure to clone the submodules as well.


Then, you need to build some images and start the K8S cluster.

Run the following docker build commands from the root of the project:
  ```
       docker build -t toktik-frontend:v1 frontend 
       docker build -t toktik-backend:v1 backend 
       docker build -t toktik-socketio:v1 socketio
       docker build -t toktik-conversion:v1 TokTik_Workers/conversion
       docker build -t toktik-processing:v1 TokTik_Workers/processing
       docker build -t toktik-thumbnail:v1 TokTik_Workers/thumbnail
  ```
You need to have the traefik ingress controller running, the easiest way is to use helm by running the following commands:
```
       helm repo add traefik https://traefik.github.io/charts

       helm repo update

       helm install traefik traefik/traefik
```

Finally, get the K8S cluster up and running with the following command:
```
       kubectl apply -R -f k8s
```

Now, just open up a browser window and type 'localhost' as the URL (use '127.0.0.1' if there are issues).
