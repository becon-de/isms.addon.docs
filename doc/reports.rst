#######
Reports
#######

Durch das ISMS-Add-on wird ein variabler Report installiert, der der Report-Kategorie "Global" zugeordnet wird, wenn diese vorhanden ist. Außerdem werden 9 Report-Views mit ausgeliefert, die den Typ ISMS haben:

**Report: ISMS Risikoeinschätzung (Gruppe)**
    Dieser variable Report zeigt die Risikoeinschätzungen von allen Objektgruppen, denen das Objekt mit dem der Report aufgerufen wird zugeordnet ist. Er ist an die gleichnamige benutzerdefinierte Kategorie gebunden, die verschiedenen Objekttypen zugeordnet werden kann. Da der Report mit dem Abfrage-Editor bearbeitet werden kann, ist er auch an die individuellen Bedürfnisse anpassbar.
..  note::
  Wollen sie die Risikoeinschätzungen z.B. an den Servicekomponenten von Services sehen, duplizieren Sie den Report "ISMS-Risikoeinschätzung (Gruppe)" und ändern   Sie   für den Report "ISMS-Risikoeinschätzung (Servicekomponente)" die Bedingung:
  Wählen sie die Kategorie "Service Komponenten (Service)" und setzten Sie für das Attribut "Zugewiesenes Objekt" den Feldplatzhalter Objekt ID.
    
**Report-View: ISMS Risiko nach Risikoklasse**
    Diese Report View zeigt alle Objekte/Objektgruppen mit Risikoeinschätzungen und Risikohöhen, wenn der Umsetzungstatus "Unbearbeitet" ist.

    Die Ausgabe kann nach Risikoklasse sowie nach dem Anwendungsbereich gefiltert werden. Für diese View ist auch der Standortfilter einstellbar, der die Ansicht auf Risikoeinschätzungen unterhalb des ausgewählten Objektes einschränkt.

**Report-View: Erkärung zur Anwendbarkeit (SOA)**
    Diese Report View listet zunächst alle Maßnahmen Anhang A auf (wenn vorhanden). Dabei wird nach Kapiteln und Unterkapiteln gegliedert. Die Maßnahmen ewrden mit ihrer Anwendbarkeit, Grund für die Einbeziehung/Nichteinbeziehung und dem Umsetzungstatus aufgelistet.
    Werden Anhang A Maßnahmen durch SOA-Maßnahmen umgesetzt, so werden die zugewiesenen SOA-Maßnahmen unter der Anhang A Maßnahme dargestellt, ebenfalls mit den dokumentierten Werten zur Anwendbarkeit, Grund für die Einbeziehung/Nichteinbeziehung und dem Umsetzungstatus.
    Im Anschluss an die Anhang A-Maßnahmen werden alle SOA-Maßnahmen aufgeführt.

    Diese View stellt keine Filter bereit, berücksichtigt jedoch -wenn die entsprechende Option in den Mandanteneinstellungen aktiviert ist und die Maßnahmen einen Standort haben- die Rechte des Users auf den Standort.

**Report-View: SOA Vollständigkeitsprüfung**
    Diese Report View verhält sich ähnlich zur Report-View: Erkärung zur Anwendbarkeit (SOA). Es sind alle Maßnahmen Anhang A und SOA Maßnahmen aufgeführt. Pro Maßnahme ist aufgeführt und farblich markiert, ob die Maßnahme hinreichend dokumentiert ist.

    Diese View stellt keine Filter bereit, berücksichtigt jedoch -wenn die entsprechende Option in den Mandanteneinstellungen aktiviert ist und die Maßnahmen einen Standort haben- die Rechte des Users auf den Standort.

**Report-View: ISMS Risikomatrix**
    Diese Report View stellt die Risikomatrix vor Risikobehandlung und nach Risikobehandlung dar. Die Achsenbeschriftungen ergeben sich dabei aus den definierten Bewertungskriterien. Bei Klick auf die Anzahl der Risikoeinschätzungen einer bestimmten Eintittswahrscheinlichkeit/Auswirkungs-Kombination wird die Report-View "ISMS Risikoeinschätzung" reduziert auf die betroffenen Risikoeinschätzungen dargestellt.

    ..  image:: img/risk_matrix.PNG 

    Die Risikomatrix kann auch nach Anwendungsbereich und nach Standort gefiltert werden.

**Report-View: ISMS Risikoeinschätzung**
    Diese Report View stellt alle Risikoeinschätzungen dar, die in i-doit an Objekten vorgenommen wurden. Dabei steht in der ersten Spalte die ID der Risikoeinschätzung, in der zweiten Spalte an welchem Objekt die Risikoeinschätzung vorgenommen wurde. Es folgen diverse Attribute aus der Risikoeinschätzung selbst: Bedrohung, Schwachstelle, Werteeigentümer, Risikoeigentümer, die Bewertungen der Schadenszenarien, die Auswirkung die sich daraus ergibt, die Eintrittswahrscheinlichkeit und die Risikohöhe (farblich hinterlegt). Es folgen die exisiterenden Maßnahmen, Risikobehandlung, Auswahl der Maßnahme, der/die Verantwortliche für die Umsetzung, Notwendige Ressourcen, das Umsetzungsdatum, die Priorisierung und die Einschätzungen der einzelnen Schadenszenarien nach der Behandlung mit dem sich daraus ergebenden Wert. Die Eintrittswahrscheinlichkeit nach Behandlung und farblich hinterlegte Restrisikohöhe bilden die letzen beiden Spalten der Report-View.

    Diese Report-View kann auch nach Anwendungsbereich und nach Standort gefiltert werden.

**Report-View: ISMS Risikobehandlungsplan (RTP)**
    Diese Report View ist auf die Risikobehandlung fokussiert. Es werden in der ersten Spalte alle Bedrohungen aufgelistet, in der zweiten Spalte sind die Objekte aufgeführt, bei denen diese Bedrohung "anliegt". Nach Informationen zu den Maßnahmen folgt die Spalte Risikobehandlung. Hier sind im Standard die Werte aus der ISO 31000 zu finden. Es folgen die Begründung der Risikoeinschätzung, der Risk Owner, die Dringlichkeit der Umsetzung und das späteste Umsetzungsdatum.

    Der Risikobehandlungsplan kann auch nach Anwendungsbereich und nach Standort gefiltert werden.

**Report-View: ISMS Geltungsbereich**
    Diese Report View listet alle Objekte mit Objekttyp und Standort auf, bei denen die ISMS-Relevanz auf "Ja" gesetzt ist.

    Diese Report-View kann auch nach Anwendungsbereich und nach Standort gefiltert werden.

**Report-View: ISMS Risikoeinschätzung objektbasiert**
    Diese Report View zeigt die gleichen Informationen an, wie die View "ISMS Risikoeinschätzung", kann jedoch auf einzelne Objekte gefiltert werden. Diese Report-View bietet außerdem einen CSV-Export an.

**Report-View: ISMS Restrisiko nach Level**
    Diese Report View funktioniert analog zur Report-View "ISMS Risiko nach Level" mit dem einzigen Unterschied, dass hier das Restrisiko, also das Risiko nach Behandlung durch Maßnahmen dargestellt wird.