## DevOps Engineering: Πρακτικές ανάπτυξης λογισμικού και λειτουργίες πληροφορικής

# Final Project

**Ημερομηνία:** 06/04/2024

**Όνομα:** Ελένη Αθανασοπούλου

**github repository του project:** https://github.com/engelat/webapp


Η εφαρμογή που χρησιμοποιήθηκε είναι ένα Python Flask web application, που δίνει realtime πληροφορίες και κάνει monitor  CPU, memory, IO και process information
https://github.com/benc-uk/python-demoapp (όπως στην ενότητα 9)


**Στοιχεία deployment server:**

digital ocean droplet
ubuntu server
public IP: 161.35.78.56

**docker hub repository:** https://hub.docker.com/repository/docker/engelat/webapp/general


**ci/cd**
Δημιουργήθηκε ci/cd workflow, που μπορεί να βρεθεί εδώ:
https://github.com/engelat/webapp/blob/main/.github/workflows/github-ci.yaml
το οποίο εκτελείται όταν γίνεται push στο main branch του repository ή με manual trigger, με χρηση workflow_dispatch
Αποτελείται από 3 jobs:
1 test: Εκτελεί τα test και τον έλεγχο κώδικα (linting) στην εφαρμογή. Αρχικά γίνεται checkout του κώδικα από το repository. Στη συνέχεια, εγκαθίστανται τα απαραίτητα Python dependencies από το requirements.txt, εκτελούνται τα τεστ με το pytest και γίνεται ο έλεγχος του κώδικα με τα εργαλεία linting Flake8 και Pylint
2 build-and-push: Το job αυτό προυποθέτει το προηγούμενο. Συνδέεται στο docker hub και κάνει push το image με tag latest
3 deploy: Αυτό το job εξαρτάται από το προηγούμενο job, build-and-push. Στα βήματα περιλαμβάνεται η ρύθμιση του SSH, η σύνδεση στο Droplet και η εκτέλεση εντολών για να τρέξει την εφαρμογή εκεί.
