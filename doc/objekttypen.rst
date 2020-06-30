#################
ISMS-Objekttypen
#################

Das ISMS-Add-on führt sechs neue Objekttypen ein, die alle in der Objekttypgruppe "IT-Grundschutz" eingeordnet werden:

******************
Objekttyp Bewertungskriterium
******************

.. image:: img/protection_category_100x100.jpg
     :class: floatright

Der Objekttyp "Bewertungskriterium" bildet die Grundlage zur Bewertung von Risiken. In der Standardkonfiguration gehören folgende Kategorien zu Objekten vom Typ Bewertungskriterium:

**Allgemein** *(i-doit Standardkategorie)* 
    Gehört zu jedem Objekt.
**Bewertungskriterium** 
    Hier muss das Level festgesetzt werden, das für die Berechnung der Risikohöhe ausschlaggebend ist. Außerdem können eine Beschreibung der Eintrittswahrscheinlichkeit und eine Benennung der Schadensaußmaß für das Bewertungskriterium festlegegt werden.

*********************
Objekttyp Schadensszenario
*********************

.. image:: img/incident_scenario_100x100.jpg
     :class: floatright

Der Objekttyp "Anforderung" bildet die Anforderungen aus den Bausteinen des Grundschutzkompendium ab. In der Standardkonfiguration gehören folgende Kategorien zu Objekten vom Typ Anforderung:

**Allgemein** *(i-doit Standardkategorie)*
    Gehört zu jedem Objekt.
**Schadenszenario** 
    Hier kann eine Kennzeichnung (Ganzzahl) eingestellt werden. Diese dient lediglich der Sortierung bzw. Darstellung der Schadenszenarien in der Risikobewertung.
**Bewertungskriterien**  
    Diese Multi-Value-Kategorie verknüpft das Schadenszenario mit den Bewertungskriterien. Für jedes Bewertungskriterium kann eine Ausprägung festgelegt werden.

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
**ISMS: Wird verwendet in** *(i-doit Standardkategorie)* 
    Ein variabler Report, der alle Objekte auflistet, die diese Bedrohung "benutzen".
**Typische Schwachstellen** *(i-doit Standardkategorie)* 
    Ist eine Multi-Value Kategorie, in der Schwachstellen aus der Liste aller vorhanden Schwachstellen ausgewählt werden können.
**Zugriff** *(i-doit Standardkategorie)* 
    Über die Zugriffs-Kategorie kann die Bedrohung z.B. mit der Beschreibung auf der Internetseite des IT-Grundschutzkompendiums des BSI verlinkt werden.

********************
Objekttyp Schwachstelle
********************

.. image:: img/vulnerability_100x100.jpg
     :class: floatright

Der Objekttyp "Schwachstelle" bildet die Schwachstellen für die Risikoeinschätzungen ab. Dieser Objekttyp kann in bestimmten Fällen Optional sein, z.B. wenn als Bedrohungen die Gefährdungen aus dem IT-Grundschutz verwendet werden, die schon eine Kombination aus Bedrohung und Schwachstelle darstellen.
In der Standardkonfiguration gehören folgende Kategorien zu Objekten vom Typ Schwachstelle:

**Allgemein** *(i-doit Standardkategorie)*
    Gehört zu jedem Objekt.
**Schwachstelle**  
    Hier können Kennzeichnung, Kategorie, Katalog, Kapitel und Abschnitt der Schwachstelle dokumentiert werden.
**ISMS: Wird verwendet in** *(i-doit Standardkategorie)* 
    Ein variabler Report, der alle Objekte auflistet, die diese Schwachstelle "benutzen".
**Zugriff** *(i-doit Standardkategorie)* 
    Über die Zugriffs-Kategorie kann die Bedrohung z.B. mit der Beschreibung auf der Internetseite des IT-Grundschutzkompendiums des BSI verlinkt werden.

********************
Objekttyp SOA-Maßnahme
********************

.. image:: img/control_100x100.jpg
     :class: floatright

Der Objekttyp SOA-Maßnahme wurde vor allem für selbst definierte Maßnahmen geschaffen. Natürlich können Sie hier auch Maßnahmen aus Katalogen importieren, es ist jedoch sinnvoll hier auch bereits im Unternehmen bestehende Maßnahmen zu dokumentieren, da die SOA-Maßnahmen die Anhang-A Maßnahmen aus der ISO 27001 umsetzen können.
In der Standardkonfiguration gehören folgende Kategorien zu Objekten vom Typ SOA-Maßnahme:

**Allgemein** *(i-doit Standardkategorie)*
    Gehört zu jedem Objekt.
**Empfehlungen nach ISO27002** 
    Diese Kategorie halt zwei Textfelder für die Empfehlungen nach ISO27002 bereit. Entsprechende Importe können wir derzeit aus Lizenzgründen leider nicht anbieten.
**Maßnahme**  
    Hier können Kennzeichnung, Referenz, Stammdaten, Genehmigung, Kapitel und Abschnitt der Maßnahme dokumentiert werden. Weiterhin sollten die für die SOA relevanten Felder Anwendbarkeit und Begründung der Anwendbarkeit gepflegt werden. Der Umsetzungsstatus und eine Bemerkung zur Umsetzung kann man ebenfalls dokumentieren, wobei für den Umsetzungstatus keine vordefinierten Werte im Auslieferungszustand enthalten sind.
**ISMS: Wird verwendet in** *(i-doit Standardkategorie)* 
    Ein variabler Report, der alle Objekte auflistet, die diese SOA-Maßnahme "benutzen".
**Zugriff** *(i-doit Standardkategorie)* 
    Über die Zugriffs-Kategorie kann die Bedrohung z.B. mit der Beschreibung auf der Internetseite des IT-Grundschutzkompendiums des BSI verlinkt werden.

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
