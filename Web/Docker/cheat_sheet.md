# Cheat Sheet - Docker
## Quickstart
- ```build``` : Cette commande permet la cr�ation d'une image � partir d'un Dockerfile et d'un "contexte". Le contexte repr�sente l'ensemble des fichiers se trouvant dans le r�pertoie ou � l'adresse indiqu�e. <br/> <a href="https://docs.docker.com/engine/reference/commandline/build/">=> Documentation Docker</a> 
- ```run``` : Cette commande permet de d�finir les ressources utilis�es par le conteneur. La commande doit s�pcifier une IMAGE. <br/><a href="https://docs.docker.com/engine/reference/run/">=> Documentaiton Docker</a>
- ```exec``` : Cette commande permet d'executer une commande dans le conteneur en cours d'utilisation. Une commande lanc�e de cette mani�re n'est pas red�marr�e si le conteneur est relanc�. <br/> <a href ="https://docs.docker.com/engine/reference/commandline/exec/">=> Documentation Docker</a>

Lors de la cr�ation ou du d�marrage d'un conteneur, celui-ci ne rend aucun de ses ports public. Afin d'acc�der au conteneur depuis l'ext�rieur il faut mapper un des ports du conteneur � un port de l'h�te externe. Pour cela on utilise l'option ```--publish``` ou ```--p```.<br/> <a href="https://docs.docker.com/config/containers/container-networking/#published-ports"> > Plus d'informations.</a>

## Docker
### Le fichier ```requirement.txt```
Ce fichier d�crit les d�pendances de l'application associ�es � une versions donn�e. <br/>
Il peut �tre g�n�r� avec la commande ```env1\bin\python -m pip freeze > requirements.txt```. <br/><a href="https://pip.pypa.io/en/stable/reference/pip_freeze/">> Plus d'informations.</a><br/>
Ce fichier est appel� par ligne ```RUN pip install - requirement.txt``` dans le Dockerfile afin d'installer les d�pendances li�es � l'applications.
### Les conteneurs / containers
Un conteneur est un processus isol� des autres processus de la machine h�te.
### Les images
Quand un conteneur est actif, il utilise un syst�me isol�. Ce syst�me est fourni par l'image du conteneur. L'image doit contenir tout ce qui est n�cessaire au fonctionnement de l'application ainsi que diff�rents configuratuions pour le conteneur tels que les variables d'environnement et diff�rentes m�tadonn�es.

