# Cheat Sheet - Docker
## Quickstart
- ```build``` : Cette commande permet la création d'une image à partir d'un Dockerfile et d'un "contexte". Le contexte représente l'ensemble des fichiers se troiuvant dans le répertoie ou à l'adresse indiquée. <br/> <a href="https://docs.docker.com/engine/reference/commandline/build/">=> Documentation Docker</a> 
- ```run``` : Cette commande permet de définir les ressources utilisées par le conteneur. La commande doit sépcifier une IMAGE. <br/><a href="https://docs.docker.com/engine/reference/run/">=> Documentaiton Docker</a>
- ```exec``` : Cette commande permet d'executer une commande dans le conteneur en cours d'utilisation. Une commande lancée de cette manière n'est pas redémarrée si le conteneur est relancé. <br/> <a href ="https://docs.docker.com/engine/reference/commandline/exec/">=> Documentation Docker</a>

Lors de la création ou du démarrage d'un conteneur, celui-ci ne rend aucun de ses ports public. Afin d'accéder au conteneur depuis l'extérieur il faut mapper un des ports du conteneur à un port de l'hôte externe. Pour cela on utilise l'option ```--publish``` ou ```--p```.<br/> <a href="https://docs.docker.com/config/containers/container-networking/#published-ports"> > Plus d'informations.</a>

## Docker
### Le fichier ```requirement.txt```
Ce fichier décrit les dépendances de l'application associées à une versions donnée. <br/>
Il peut être généré avec la commande ```env1\bin\python -m pip freeze > requirements.txt```. <br/><a href="https://pip.pypa.io/en/stable/reference/pip_freeze/">> Plus d'informations.</a><br/>
Ce fichier est appelé par ligne ```RUN pip install - requirement.txt``` dans le Dockerfile afin d'installer les dépendances liées à l'applications.
### Les conteneurs / containers
Un conteneur est un processus isolé des autres processus de la machine hôte.
### Les images
Quand un conteneur est actif, il utilise un système isolé. Ce système est fourni par l'image du conteneur. L'image doit contenir tout ce qui est nécessaire au fonctionnement de l'application ainsi que différents configuratuions pour le conteneur tels que les variables d'environnement et différentes métadonnées.

