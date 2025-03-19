**Comandi per la disallineazione di config.json contenente il vero token**
Comando per non far tracciare config.json
    git update-index --assume-unchanged config.json
Comando per far tracciare config.json
    git update-index --no-assume-unchanged config.json

**In seguito alla creazione del nuovo branch develop**:
1. Assicurati di essere nel branch che desideri mantenere (solitamente master):
    git checkout master
2. Fai un pull per essere sicuro di avere l'ultima versione del branch:
    git pull origin master
3. Unisci il branch develop nel branch master:
    git merge develop
4. Gestisci eventuali conflitti (se ci sono modifiche che si sovrappongono nei due branch, Git ti chiederà di risolvere i conflitti manualmente).
5. Fai il commit dell'unione (se necessario, dopo aver risolto i conflitti):
    git commit -m "Merge branch 'develop' into master"
6. Pusha le modifiche sul repository remoto:
    git push origin master