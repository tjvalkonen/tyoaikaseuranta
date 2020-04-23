# Käyttötapaukset

## Käyttäjätunnukset

Käyttäjä lisää käyttäjätunnuksen (USER) käyttäjätunnuksen luontilomakkeella.

```
INSERT INTO account (date_created, date_modified, name, username, password, role) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?)
```

Ylläpitäjä (ADMIN) voi lisätä ylläpitäjä tunnuksen

Ylläpitäjä (ADMIN) voi poistaa tunnuksen

Ylläpitäjä (ADMIN) voi muokata tunnusta

Ylläpitäjä (ADMIN) voi listata järjestelmässä olevat tunnukset

Oman tunnuksen tietoja voi muokata

## Projektien listaaminen

Käyttäjä näkee järjestelmässä olevat projektit Projects List -sivulla

```
SELECT project.id AS project_id, project.date_created AS project_date_created, project.date_modified AS project_date_modified, project.name AS project_name, project.done AS project_done, project.account_id AS project_account_id 
FROM project
```

## Projektin lisääminen

Käyttäjä syöttää lisättävän projektin Add project -sivulla.

## Projektin merkitseminen päättyneeksi

x
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

## Työn lisääminen projektiin

Tehdyn työn voi lisätä projektin työt listan yllä olevalla lomakkeella.

```
INSERT INTO task (date_created, date_modified, tasktype, description, time, taskstatus, project_id, account_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?, ?)
```

Käyttäjä voi valita työn tyypiksi arvion työmäärästä (ESTIMATE) tai toteutunut työ (ACTUAL).
