# Heroku

Heroku identifie une application python par la pr�sence des fichiers :
- ```requirements.txt```
- ```setup.py```
- ```Pipfile```

Les d�pendances sp�cifi�es dans le fichiers ```requirements.txt``` sont automatiquement install�es avant le d�marrage de l'application.

## D�ployer une application
Pour d�ployer une application il faut la cr�er.
```
$ heroku create [name]
```

Il faut ensuite d�ployer le code.
```
$ git push heroku main
```

Une fois l'application d�ploy�e il faut s'assure qu'au moins une instance de l'application d�marre.

```
$ heroku ps:scale web=1
```

L'application ets maintenant d�ploy�e et on peut y acc�der.
```
$ heroku open
```

Il est possible d'acc�der aux logs de l'application.
```
$ heroku logs --tail
```
<a href="https://devcenter.heroku.com/articles/logging"> > En savoir plus sur les logs</a>

Pour d�finir quelle commande doit �tre execut�e on utilise un fichier Procfile. Il d�clare un processus unique et la commande n�cessaire pour le d�marrer.
Le nom ```web``` est important car il d�clare que le processus sera attach� au routing HTTP de Heroku et qu'il recevra du traffic une fois d�ploy�.

Pour un d�veloppement local sur Microsoft Windows on trouve un fichier ```Procfile.windows```. Il permet de faire d�marrer un serveur web compatible avec Windows.
<br/><a href="https://devcenter.heroku.com/articles/procfile">> En savoir plus sur les fichiers Procfile</a>
<br/><a href="https://devcenter.heroku.com/articles/http-routing">> En savoir plus sur le routing HTTP</a>

Les application Heroku fonctionnent dans des conteneur Linux appel�s des <b>dynos</b>.
Actuellement l'application fonctionne sur un unique dyno. Grace � la commande ```ps``` on peut observer combien de dynos sont utilis�s.
<br/> <a href="https://devcenter.heroku.com/articles/dynos">> En savoir plus sur les dynos</a>


Il est possible de faire tourner les applications en local. Pour cela il faut avant tout installer les d�pendances requises par l'application grace au fichier ```requirements.txt```. Une fois install�es on peut lancer l'application en local.
```
$ heroku local web [-f Procfile.windows]
```

Pour d�ployer l'application apr�s des modifications effectu�es en local, on commence par push les modifications.
```
$ git add .
$ git commit -m "Nom"
$ git push heroku main
```

