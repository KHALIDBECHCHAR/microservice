Pour construire une image Docker à partir du Dockerfile de la base de données MongoDB, utilisez la commande "docker build" en spécifiant le chemin vers le répertoire contenant le Dockerfile. Voici un exemple de commande :

# docker build -t nom_image:tag chemin_vers_le_dossier_contenant_le_Dockerfile

Par exemple, si votre Dockerfile est dans un dossier nommé "mongodb", et que vous souhaitez nommer votre image "mongo_db" avec la version "1.0", vous pouvez exécuter la commande suivante à partir du répertoire contenant le dossier "mongodb":

# docker build -t mongo_db:1.0 mongodb/

Cela construira une image Docker nommée "mongo_db" avec la version "1.0" en utilisant le Dockerfile 

Cette commande exécute un conteneur Docker à partir de l'image "mongo_db:1.0" que vous avez construite avec la commande "docker build". 
L'option "-it" permet de lancer le conteneur en mode interactif avec un terminal associé. 
L'option "--rm" permet de supprimer automatiquement le conteneur lorsque vous le quittez.

# docker run -d -p 27017:27017 mongo_db:1.0
