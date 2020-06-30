#######
Reports
#######

Durch das ISMS-Addon wird ein variabler Report installiert, der der Report-Kategorie "Global" zugeordnet wird, wenn diese vorhanden ist. Außerdem werden 9 Report-Views mit ausgeliefert, die den Typ ISMS haben:

**Report: ISMS Risikoeinschätzung (Gruppe)**
    Dieser variable Report zeigt die Risikoeinschätzungen von allen Objektgruppen, denen das Objekt mit dem der Report aufgerufen wird zugeordnet ist. Er ist an die gleichnamige benutzerdefinierte Kategorie gebunden, die Sie verschiedenen Objekttypen zuordnen können. Auch den Report können Sie leicht individualisieren, da er mit dem Abfrage-Editor bearbeitet werden kann.
    .. note:: 
    Wollen sie die Risikoeinschätzungen z.B. an den Servicekomponenten von Services sehen, duplizieren Sie den Report "ISMS-Risikoeinschätzung (Gruppe)" und ändern Sie für den Report "ISMS-Risikoeinschätzung (Servicekomponente)" die Bedinung:
    Wählen sie die Kategorie Service Komponenten (Service) und setzten Sie für das Attribut Zugewiesenes Objekt den Feldplatzhalter Objekt ID.
    
**Report-View: ISMS Risiko nach Level**
    Diese Report View zeigt alle Zielobjektgruppen/Zielgruppen mit Ihren Risikoeinschätzungen und Risikohöhen, wenn der Umsetzungstatus "Unbearbeitet" ist.

    Sie haben die Möglichkeit nach Level bzw. Risikokategorie (z.B. rot, gelb, grün) sowie nach dem Anwendungsbereich zu Filtern. Für diese View ist auch der Standortfilter einstellbar, der die Ansicht auf Risikoeinschätzungen unterhalb des ausgewählten Objektes einschränkt.

**Report-View: Erkärung zur Anwendbarkeit (SOA)**
    Diese Report View listet zunächst alle Anhang A Maßnahmen auf. Dabei wird nach Kapiteln und Unterkapiteln gegliedert. Die Maßnahmen sind mit Ihrer Andwendbarkeit, Gründe für die Einbeziehung/Nichteinbeziehung und dem Umsetzungstatus einsehbar.
    Werden Anhang A Maßnahmen durch SOA-Maßnahmen umgesetzt, so werden die SOA-Maßnahmen unter der Anhang A Maßnahme dargestellt, ebenfalls mit den dokumentierten Werten zu Anwendbarkeit, Gründe für die Einbeziehung/Nichteinbeziehung und dem Umsetzungstatus.
    Im Anschluss an die Anhang A-Maßnahmen werden alle SOA-Maßnahmen aufgeführt.

    Diese View stellt keine Filter bereit, berücksichtigt jedoch wenn die entsprechende Option in den Mandanteneinstellungen aktiviert ist den Standort der Maßnahmen-Objekte.

**Report-View: SOA Vollständigkeitsprüfung**
    Diese Report View verhält sich ähnlich zur Report-View: Erkärung zur Anwendbarkeit (SOA). Es sind alle Anhang A Maßnahmen und SOA Maßnahmen aufgeführt. In den Spalten gibt es farblich hinterlegte Hinweise ob die Anwendbarkeit, Begründung zur Anwendbarkeit und Umsetzungsstatus ausreichend dokumentiert sind.

    Diese View stellt keine Filter bereit, berücksichtigt jedoch wenn die entsprechende Option in den Mandanteneinstellungen aktiviert ist den Standort der Maßnahmen-Objekte.

**Report-View: ISMS Risikomatrix**
    Diese Report View stellt die Risikomatrix vor Risikobehandlung und nach Risikobehandlung dar. Die Achsenbeschriftungen ergeben sich dabei aus den definierten Bewertungskriterien. Bei Klick auf die Anzahl der Risikoeinschätzungen einer bestimmten Eintittswahrscheinlichkeit/Auswirkungs Kombination wird die Report-View "ISMS Risikoeinschätzung" reduziert auf die betroffenen Risikoeinschätzungen dargestellt.

    ..  image:: img/risk_matrix.PNG 

    Sie haben die Möglichkeit die Risikomatrix nach Anwendungsbereich zu Filtern. Für diese View ist auch der Standortfilter einstellbar, der die Ansicht auf Risikoeinschätzungen unterhalb des ausgewählten Objektes einschränkt.

**Report-View: ISMS Risikoeinschätzung**
    Diese Report View stellt alle Risikoeinschätzungen dar, die in i-doit an Objekten vorgenommen wurden. Dabei steht in der ersten Spalte die ID der Risikoeinschätzung, in der zweiten Spalte an welchem Objekt die Risikoeinschätzung vorgenommen wurde. Es folgen diverse Attribute aus der Risikoeinschätzung selbst: Bedrohung, Schwachstelle, Werteeigentümer, Risikoeigentümer, die Bewertungen der Schadenszenarien, die Auswirkung die sich daraus ergibt, die Eintrittswahrscheinlichkeit und die Risikohöhe (farblich hinterlegt). Es folgen die exisiterenden Maßnahmen, Risikobehandlung, Auswahl der Maßnahme, der/die Verantwortliche für die Umsetzung, Notwendige Ressourcen, das Umsetzungsdatum, die Priorisierung und die Einschätzungen der einzelnen Schadenszenarien nach der Behandlung mit dem sich daraus ergebenden Wert. Die Eintrittswahrscheinlichkeit nach Behandlung und farblich hinterlegte Restrisikohöhe bilden die letzen beiden Spalten der Report-View.

    Sie haben die Möglichkeit diese Report-View nach Anwendungsbereich zu Filtern. Für diese View ist auch der Standortfilter einstellbar, der die Ansicht auf Risikoeinschätzungen unterhalb des ausgewählten Objektes einschränkt.

**Report-View: ISMS Risikobehandlungsplan (RTP)**
    Diese Report View ist auf die Risikobehandlung fokkusiert. Es werden in der ersten Spalte alle Bedrohungen aufgelistet, in der zweiten Spalte sind die Objekte aufgeführt, bei denen diese Bedrohung "anliegt". Nach Informationen zu Maßnahme folgt die Spalte Risikobehandlung. Hier sind im Standard die Werte aus der ISO 31000 zu finden. Es folgen die Begründung der Risikoeinschätzung, der Risk Owner, die Dringlichkeit der Umsetzung und das späteste Umsetzungsdatum.

    Sie haben die Möglichkeit diese Report-View nach Anwendungsbereich zu Filtern. Für diese View ist auch der Standortfilter einstellbar, der die Ansicht auf Risikoeinschätzungen unterhalb des ausgewählten Objektes einschränkt.

**Report-View: ISMS Geltungsbereich**
    Diese Report View listet alle Objekte mit Objekttyp und Standort auf, bei denen die ISMS-Relevanz auf "Ja" gesetzt ist.

    Sie haben die Möglichkeit diese Report-View nach Anwendungsbereich zu Filtern. Für diese View ist auch der Standortfilter einstellbar, der die Ansicht auf Risikoeinschätzungen unterhalb des ausgewählten Objektes einschränkt.

**Report-View: ISMS Risikoeinschätzung objektbasiert**
    Diese Report View zeigt alle Risikoeinschätzungen aufgeschlüsselt nach den Assets an denen Sie erstellt wurden. Es sind alle Attribute aus der Risikoeinschätzung einsehbar.
    Sie haben die Möglichkeit diese Report-View nach Objektes zu Filtern.
    Außerdem ist dies bisher die Einzige Report-View die einen CSV-Export zulässt. 

**Report-View: ISMS Restrisiko nach Level**
    Diese Report View funktioniert analog zur Report-View "ISMS Risiko nach Level" mit dem einzigen Unterschied, dass hier das Restrisiko, also das Risiko nach Behandlung durch Maßnahmen dargestellt wird.