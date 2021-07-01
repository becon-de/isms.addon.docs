#################
ISMS-Objekttypen
#################

Das ISMS-Add-on führt sechs neue Objekttypen ein, die alle in der Objekttypgruppe "ISMS" eingeordnet werden:

******************
Objekttyp Audit
******************

.. image:: img/audit_100x100.jpg
     :class: floatright

Der Objekttyp "Audit" dient der Erfassung von Audits und deren Ergebnissen und Abweichungen:

**Abweichungen** 
    In dieser Multivalue-Kategorie können die beim Audit festgestellten Abweichungen dokumentiert werden. Initial sind die Abweichungstypen "Hauptabweichung", "Nebenabweichung", "Empfehlung" und "Hinweis" eingereichtet.
**Allgemein** *(i-doit Standardkategorie)* 
    Gehört zu jedem Objekt.
**Audit** 
    In dieser Kategorie können die Daten eines Audits hinterlegt werden, wie z.B. Audittype, Auditkriterium, Prüfzeitraum und Prüfbericht.

********************
Objekttyp Bedrohung
********************

.. image:: img/threat_100x100.jpg
     :class: floatright

Der Objekttyp "Bedrohung" bildet die Bedrohungen für die Risikoeinschätzungen ab. In der Standardkonfiguration gehören folgende Kategorien zu Objekten vom Typ Bedrohung:

**Allgemein** *(i-doit Standardkategorie)*
    Gehört zu jedem Objekt.
**Bedrohung**  
    Hier können Kennzeichnung, Kategorie, Katalog, Kapitel und Abschnitt der Bedrohung dokumentiert werden, was sinnvoll ist, wenn diese aus einem Katalog (z.B. dem Grundschutz-Kompendium) stammt. Außerdem können die Schutzziele (Vertaulichkeit, Intigrität, Verfügbarkeit) dokumentiert werden.
**Empfehlungen nach ISO27002** 
    Diese Kategorie halt zwei Textfelder für die Empfehlungen nach ISO27002 bereit. Entsprechende Importe können wir derzeit aus Lizenzgründen leider nicht anbieten.
**ISMS: Wird verwendet in** 
    Ein variabler Report, der alle Objekte auflistet, die diese Bedrohung "benutzen".
**Typische Schwachstellen**
    Ist eine Multi-Value Kategorie, in der Schwachstellen aus der Liste aller vorhanden Schwachstellen ausgewählt werden können.
**Zugriff** *(i-doit Standardkategorie)* 
    Über die Zugriffs-Kategorie kann die Bedrohung z.B. mit der Beschreibung auf der Internetseite des IT-Grundschutzkompendiums des BSI verlinkt werden.

******************
Objekttyp Bewertungskriterium
******************

.. image:: img/protection_category_100x100.jpg
     :class: floatright

Der Objekttyp "Bewertungskriterium" bildet die Grundlage zur Bewertung von Risiken. In der Standardkonfiguration gehören folgende Kategorien zu Objekten vom Typ Bewertungskriterium:

**Allgemein** *(i-doit Standardkategorie)* 
    Gehört zu jedem Objekt.
**Bewertungskriterium** 
    Hier muss das Level festgesetzt werden, das für die Berechnung der Risikohöhe ausschlaggebend ist. Das Level ist die Berechnungsgrundlage für die Berechnung der Risikohöhe. Außerdem können eine Beschreibung der Eintrittswahrscheinlichkeit und eine Benennung der Schadensaußmaß für das Bewertungskriterium festlegegt werden.

********************
Objekttyp Ereignis
********************

.. image:: img/event_100x100.jpg
     :class: floatright

Mit dem Objekttypen Ereignis können Risikoereignisse für eine Ereignis-basierte Risikoidentifikation abgebildet werden.
In der Standardkonfiguration gehören folgende Kategorien zu Objekten vom Typ Ereignis:

**Allgemein** *(i-doit Standardkategorie)*
    Gehört zu jedem Objekt.
**Risikoeinschätzung (Ereignis)** 
    Diese Kategorie entspricht weitestgehend der Kategorie `_Risikoeinschätzung <risikoeinschaetzung.html>`_. Statt Bedrohung und Schwachstelle müssen jedoch eine Risikobeschreibung und die Risikoquelle(n) angegeben werden.


********************
Objekttyp Maßnahme Anhang A
********************

.. image:: img/control_annex_a_100x100.jpg
     :class: floatright

Der Objekttyp Anhang A Maßnahme sollte nach der :doc:`einrichtung` des Add-ons die 114 Anhang A Maßnahmen aus der ISO27001 beinhalten. Hauptzweck der Anhang A Maßnahmen ist der Abgleich mit den SOA-Maßnahmen.
In der Standardkonfiguration gehören folgende Kategorien zu Objekten vom Typ Maßnahme Anhang A:

**Allgemein** *(i-doit Standardkategorie)*
    Gehört zu jedem Objekt.
**Anwendbarkeit** 
    Diese Kategorie ist eine der wichtigsten im ISMS-Add-on. Hier wird gepflegt, ob die Maßnahme einbezogen wird oder nicht. Dafür muss eine Begründung hinterlegt werden. Es können außerdem SOA-Maßnahmen ausgewählt werden, die diese Anhang A Maßnahme umsetzen. Außerdem wird der Umsetzungsstatus für die Anhang A-Maßnahme an dieser Stelle dokumentiert. Alle diese Werte finden sich später in der Report-View "Erkärung der Anwendbarkeit (SOA)" wieder.
**Maßnahme Anhang A**  
    Hier können Kennzeichnung, Abschnitt, Kapitel eine Beschreibung der Maßnahme dokumentiert werden.


*********************
Objekttyp Schadensszenario
*********************

.. image:: img/incident_scenario_100x100.jpg
     :class: floatright

Der Objekttyp "Schadensszenario" bildet die Schadensszenarien/Schadenskategorien ab, in denen man die Schadensauswirkung einschätzen kann. In der Standardkonfiguration gehören folgende Kategorien zu Objekten vom Typ Schadensszenario:

**Allgemein** *(i-doit Standardkategorie)*
    Gehört zu jedem Objekt.
**Schadenszenario** 
    Hier muss eine Kennzeichnung (Ganzzahl) eingestellt werden. Diese dient lediglich der Sortierung bzw. Darstellung der Schadenszenarien in der Risikobewertung. Dieser Wert darf aber nicht 0 sein.
**Bewertungskriterien**  
    Diese Multi-Value-Kategorie verknüpft das Schadenszenario mit den Bewertungskriterien. Für jedes Bewertungskriterium kann eine textuelle Ausprägung festgelegt werden.

..  list-table::
    :name Beispiel:
    :header-rows:1:
    *- Kennzeichnung
     - 1
    *- Bezeichnung
     - Finzanzielle Auswirkungen
    *-Bewertungskriterium
     - Gering: Weniger als 5.000 EUR
     - Normal: Von 5.000 bis 50.000 EUR
     - Hoch: Von 50.000 bis 500.000 EUR
     - Sehr hoch: Mehr als 500.000 EUR

********************
Objekttyp Schwachstelle
********************

.. image:: img/vulnerability_100x100.jpg
     :class: floatright

Der Objekttyp "Schwachstelle" bildet die Schwachstellen für die Risikoeinschätzungen ab. Dieser Objekttyp kann in bestimmten Fällen optional sein, z.B. wenn als Bedrohungen die Gefährdungen aus dem IT-Grundschutz verwendet werden, die schon eine Kombination aus Bedrohung und Schwachstelle darstellen.
In der Standardkonfiguration gehören folgende Kategorien zu Objekten vom Typ Schwachstelle:

**Allgemein** *(i-doit Standardkategorie)*
    Gehört zu jedem Objekt.
**Schwachstelle**  
    Hier können Kennzeichnung, Kategorie, Katalog, Kapitel und Abschnitt der Schwachstelle dokumentiert werden.
**ISMS: Wird verwendet in** 
    Ein variabler Report, der alle Objekte auflistet, die diese Schwachstelle "benutzen".
**Zugriff** *(i-doit Standardkategorie)* 
    Über die Zugriffs-Kategorie kann die Bedrohung z.B. mit der Beschreibung auf der Internetseite des IT-Grundschutzkompendiums des BSI verlinkt werden.

********************
Objekttyp SOA-Maßnahme
********************

.. image:: img/control_100x100.jpg
     :class: floatright

Der Objekttyp SOA-Maßnahme beinhaltet die expliziten Maßnahmen, die im Unternehmen angewandt werden oder geplant sind anzuwenden. Natürlich können auch (SOA-)Maßnahmen aus Katalogen importiert werden. SOA-Maßnahmen können mit Maßnahmen Anhang A verknüpft werden.
In der Standardkonfiguration gehören folgende Kategorien zu Objekten vom Typ SOA-Maßnahme:

**Allgemein** *(i-doit Standardkategorie)*
    Gehört zu jedem Objekt.
**Empfehlungen nach ISO27002** 
    Diese Kategorie halt zwei Textfelder für die Empfehlungen nach ISO27002 bereit. Entsprechende Importe können wir derzeit aus Lizenzgründen leider nicht anbieten.
**Maßnahme**  
    Hier können Kennzeichnung, Referenz, Stammdaten, Genehmigung, Kapitel und Abschnitt der Maßnahme dokumentiert werden. Weiterhin sollten die für die SOA relevanten Felder Anwendbarkeit und Begründung der Anwendbarkeit gepflegt werden. Der Umsetzungsstatus und eine Bemerkung zur Umsetzung kann man ebenfalls dokumentieren, wobei für den Umsetzungstatus keine vordefinierten Werte im Auslieferungszustand enthalten sind.
**ISMS: Wird verwendet in** 
    Ein variabler Report, der alle Objekte auflistet, die diese SOA-Maßnahme "benutzen".
**Zugriff** *(i-doit Standardkategorie)* 
    Über die Zugriffs-Kategorie kann die Bedrohung z.B. mit der Beschreibung auf der Internetseite des IT-Grundschutzkompendiums des BSI verlinkt werden.

********************
Objekttyp Virtueller ISMS-Standort
********************

.. image:: img/virtual_location_100x100.jpg
     :class: floatright

Objekte vom Objekttyp Virtueller ISMS-Standort dienen hauptsächlich als Hilfsobjekt, um in ISMS-Systemen mit konfigurierten Standortrechten den Standortbaum übersichtlich zu halten. Wenn alle SOA-Maßnahmen aus Zugriffsgründen einem Standort zugeordnet werden müssen, können diese diesem virtuellen Standort zugewiesen, damit der eigentlich für Infrastrukturobjekte gedachte Standortbaum nicht durch hunderte von "virtuellen" Objekten zu unübersichtlich wird. Standardmäßig wird der Objekttyp ausgeblendet. Bei Bedarf kann der Objekttyp aber über die Objekttyp-Konfiguration hinzugefügt werden.
In der Standardkonfiguration gehören folgende Kategorien zu Objekten vom Typ Virtueller ISMS-Standort:

**Allgemein** *(i-doit Standardkategorie)*
    Gehört zu jedem Objekt.
**Räumlich zugeordnete Objekte** *(i-doit Standardkategorie)* 
    In dieser Kategorie werden alle Objekte angezeigt, die dieses Objekt als Standort eingetragen haben.
**Standort** *(i-doit Standardkategorie)*
    Hier wird der Standort des Objektes eingetragen. Wenn einem virtuellen ISMS-Standort Objekte untergeordnet werden sollen, muss der virtuelle ISMS-Standort auch einen Standort haben.
