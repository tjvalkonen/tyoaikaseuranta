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

## Projektin lisääminen

Käyttäjä syöttää lisättävän projektin Add project -sivulla.

## Projektin merkitseminen päättyneeksi

x
## Projektin tehdyt työt

Projektiin merkityt arviot työtunneista yhteensä

```
SELECT SUM(Task.time) FROM Task WHERE Task.project_id = :project_id AND Task.taskstatus = 'Estimate'
```

Projektiin merkityt toteutuneet työtunnit yhteensä

```
SELECT SUM(Task.time) FROM Task WHERE Task.project_id = :project_id AND Task.taskstatus = 'Actual'
```

## Tehdyn työn lisääminen projektiin

Käyttäjä valitsee projektit listalta projektin sen nimeä klikkaamalla.

Tehdyn työn voi lisätä projektin työt listan yllä olevalla lomakkeella.

Käyttäjä voi valita työn tyypiksi arvion työmäärästä (ESTIMATE) tai toteutunut työ (ACTUAL).
