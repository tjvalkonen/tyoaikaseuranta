# Käyttötapaukset

## Käyttäjätunnukset

Käyttäjä lisää käyttäjätunnuksen (USER) käyttäjätunnuksen luontilomakkeella.

```
INSERT INTO account (date_created, date_modified, name, username, password, role) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?)
```

Ylläpitäjä (ADMIN) voi lisätä ylläpitäjä tunnuksen (ADMIN ominaisuudet toteuttamatta)

Ylläpitäjä (ADMIN) voi poistaa tunnuksen (ADMIN ominaisuudet toteuttamatta)

Ylläpitäjä (ADMIN) voi muokata tunnusta (ADMIN ominaisuudet toteuttamatta)

Ylläpitäjä (ADMIN) voi listata järjestelmässä olevat tunnukset (ADMIN ominaisuudet toteuttamatta)

Oman tunnuksen tietoja voi muokata

Oman tunnuksen merkitsemät tehdyt työt näytetään projekteittain

```
SELECT Project.id, Project.name, Project.done, SUM(Task.time) FROM Project LEFT JOIN Task ON Task.project_id = Project.id WHERE (Task.taskstatus IS 'Actual') AND (Task.account_id = ?) GROUP BY Project.id
```

## Projektien listaaminen

Käyttäjä näkee järjestelmässä olevat projektit Projects List -sivulla.

```
SELECT project.id AS project_id, project.date_created AS project_date_created, project.date_modified AS project_date_modified, project.name AS project_name, project.done AS project_done, project.account_id AS project_account_id
```

Käyttäjä näkee toisessa listassa tehdyt työmäärät summattina projekteittain.

```
SELECT Project.id, Project.name, Project.done, SUM(Task.time) FROM Project LEFT JOIN Task ON Task.project_id = Project.id WHERE (Task.taskstatus IS 'Actual') GROUP BY Project.id
```

## Projektin lisääminen

Käyttäjä syöttää lisättävän projektin Add project -sivulla.

```
INSERT INTO project (date_created, date_modified, name, done, account_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)
```

## Projektin merkitseminen päättyneeksi

Toistaiseksi käyttämätön ominaisuus. Jatkossa projektin voisi sulkea ja tehdyt työt ja arviot arkistoitaisiin.

## Projektin työt

Käyttäjä valitsee projektit listalta projektin sen nimeä klikkaamalla.

Projektiin merkityt työt listana

```
SELECT Task.id, Task.tasktype, Task.description, Task.time, Task.taskstatus, Task.project_id FROM Task WHERE Task.project_id = ?
```

Projektiin merkityt arviot työtunneista yhteensä

```
SELECT SUM(Task.time) FROM Task WHERE Task.project_id = :project_id AND Task.taskstatus = 'Estimate'
```

Projektiin merkityt toteutuneet työtunnit yhteensä

```
SELECT SUM(Task.time) FROM Task WHERE Task.project_id = :project_id AND Task.taskstatus = 'Actual'
```

Kirjautuneen käyttäjän projektiin merkityt toteutuneet työtunnit yhteensä

```
SELECT SUM(Task.time) FROM Task WHERE Task.project_id = ? AND Task.taskstatus = 'Actual' AND Task.account_id =?
```

Kirjautuneen käyttäjän projektiin merkityt arvioidut työtunnit yhteensä

```
SELECT SUM(Task.time) FROM Task WHERE Task.project_id = ? AND Task.taskstatus = 'Estimate' AND Task.account_id =?
```

## Työn lisääminen projektiin

Tehdyn työn voi lisätä projektin työt listan yllä olevalla lomakkeella.

```
INSERT INTO task (date_created, date_modified, tasktype, description, time, taskstatus, project_id, account_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?, ?)
```

Käyttäjä voi valita työn tyypiksi arvion työmäärästä (ESTIMATE) tai toteutunut työ (ACTUAL).
