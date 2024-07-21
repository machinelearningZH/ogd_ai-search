## Über diese App
Mit dieser Applikation kann der [Datenkatalog für offene Behördendaten (OGD) des Kantons Zürich](https://www.zh.ch/de/politik-staat/statistik-daten/datenkatalog.html#/) durchsucht werden. Die Suche kombiniert eine **lexikalische Suche** nach exakten Stichworten mit einer semantischen Suche nach **inhaltlicher Bedeutung.** Die Suche arbeitet zudem **multilingual**. Es können Suchbegriffe in allen europäischen und vielen anderen Sprachen eingegeben werden. 

## Achtung
Die App schickt all deine Suchanfragen an eine sog. [Embedding-Schnittstelle (API) bei OpenAI](https://platform.openai.com/docs/guides/embeddings). Bitte beachte die entsprechenden rechtlichen Rahmenbedinungen.  

## 🔍 Was ist semantische Suche?
Im Gegensatz zu einer lexikalischen Suche nach Stichworten kann eine semantische Suche auch **inhaltlich ähnliche** Worte berücksichtigen, die nicht mit dem Suchwort übereinstimmen. Die semantische Suche nach dem Wort *Krankheit* kann z.B. Dokumente finden, die die Worte *Corona*, *Ärztin*, *Pfleger*, *Medikament* oder *Operation* enthalten, ohne dass das Wort *Krankheit* in diesen Dokumenten vorkommt.

Semantische Suche arbeitet mit statistischen Methoden und Machine Learning. Das System hat auf Basis von grossen Textmengen Wort- und Satzähnlichkeiten gelernt und kann diese Ähnlichkeiten für die Suche nach Dokumenten nutzen.<br><br>Eine semantische Suche hat viele Vorteile. Zugleich führt der Einsatz dieser Methode auch dazu, dass :red[**die Suche nicht exakt ist, sondern näherungsweise. Suchergebnisse sind nicht zwingend vollständig, sondern können lückenhaft sein oder auch falsche Treffer enthalten.**]

## Versionsverlauf
- Version 0.1 vom 1.08.2024 

## Verantwortlich
Dieser Prototyp ist Teil eines Projekts von Team Data, Statistisches Amt Kanton Zürich. Verantwortlich: Laure Stadler, Patrick Arnecke.
