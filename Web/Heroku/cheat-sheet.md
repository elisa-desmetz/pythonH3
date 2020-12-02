# Heroku

Heroku identifie une application python par la présence des fichiers :
- ```requirements.txt```
- ```setup.py```
- ```Pipfile```

Les dépendances spécifiées dans le fichiers ```requirements.txt``` sont automatiquement installées avant le démarrage de l'application.

## Déployer une application
Pour déployer une application il faut la créer.
```
$ heroku create [name]
```

Il faut ensuite déployer le code.
```
$ git push heroku main
```

Une fois l'application déployée il faut s'assure qu'au moins une instance de l'application démarre.

```
$ heroku ps:scale web=1
```

L'application ets maintenant déployée et on peut y accéder.
```
$ heroku open
```

Il est possible d'accéder aux logs de l'application.
```
$ heroku logs --tail
```
<a href="https://devcenter.heroku.com/articles/logging"> > En savoir plus sur les logs</a>

Pour définir quelle commande doit être executée on utilise un fichier Procfile. Il déclare un processus unique et la commande nécessaire pour le démarrer.
Le nom ```web``` est important car il déclare que le processus sera attaché au routing HTTP de Heroku et qu'il recevra du traffic une fois déployé.

Pour un développement local sur Microsoft Windows on trouve un fichier ```Procfile.windows```. Il permet de faire démarrer un serveur web compatible avec Windows.
<br/><a href="https://devcenter.heroku.com/articles/procfile">> En savoir plus sur les fichiers Procfile</a>
<br/><a href="https://devcenter.heroku.com/articles/http-routing">> En savoir plus sur le routing HTTP</a>

Les application Heroku fonctionnent dans des conteneur Linux appelés des <b>dynos</b>.
Actuellement l'application fonctionne sur un unique dyno. Grace à la commande ```ps``` on peut observer combien de dynos sont utilisés.
<br/> <a href="https://devcenter.heroku.com/articles/dynos">> En savoir plus sur les dynos</a>


Il est possible de faire tourner les applications en local. Pour cela il faut avant tout installer les dépendances requises par l'application grace au fichier ```requirements.txt```. Une fois installées on peut lancer l'application en local.
```
$ heroku local web [-f Procfile.windows]
```

Pour déployer l'application après des modifications effectuées en local, on commence par push les modifications.
```
$ git add .
$ git commit -m "Nom"
$ git push heroku main
```

