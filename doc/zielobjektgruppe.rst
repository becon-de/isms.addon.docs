##########################
Objekttyp Zielobjektgruppe
##########################

.. image:: img/targetgroup_100x100.jpg
     :class: floatright

Im Rahmen der Strukturanalyse sollen "ähnliche" Zielobjekte zur Komplexitätsreduzierung gruppiert werden. Der Objekttyp Zielobjektgruppe dient der Abbildung dieser Gruppierung von Zielobjekten. In der Standardkonfiguration gehören folgende Kategorien zu Objekten vom Typ Zielobjektgruppe:

**Allgemein** *(i-doit Standardkategorie)* 
    Gehört zu jedem Objekt.
**IT-Grundschutz (Zielobjekte)** 
    Dies ist eine Kategorien-Gruppe, die die folgenden sieben Kategorien beinhaltet:
    
    **Informationsverbünde**
        Diese Multivalue-Kategorie zeigt alle Informationsverbünde an, denen diese Zielobjektgruppe zugewiesen ist (über die rückwärtige Kategorie "Infrastrukturanalyse"). Auch wenn es technisch möglich ist, die Zielobjektgruppe mehreren Informationsverbünden zuzuweisen, sollte eine Zielobjektgrupp ein der Regel nur einem Informationsverbund zugeordnet werden. Mehr dazu findet man unter :doc:`strukturanalyse`.
    **IT-Grundschutz-Check**
        Die Übersichtsseite zeigt alle durch die Bausteine zugewiesenen Anforderungen, sortiert nach Baustein und Anforderungsnummer. Mehr dazu findet man unter :doc:`it-grundschutz-check`.
    **Klassifikation von Informationen**
        Hier kann die Klassifikation der Informationen vorgenommen werden, die laut BSI Standard 200-2 Teil der Dokumentation des Sicherheitsprozesses ist.
    **Schutzbedarfsfeststellung**
        Hier kann der Schutzbedarf für dieses Objekt oder diese Objektgruppe in den definierten Grundwerten festgelegt und begründed werden. Mehr dazu findet man unter :doc:`schutzbedarfsfeststellung`.
    **Zugeordnete Bausteine**
        Hier können die Bausteine zugeordneten werden, die für dieses Objekt oder diese Objektgruppe gelten sollen. In der Regel werden hier Systembausteine zugeordnet, es ist aber auch möglich hier Prozessbausteine zuzuweisen, wenn es für dieses Objekt oder diese Objektgruppe Abweichungen von den im Informationsverbund zugewiesenen Prozessbausteinen gibt. Mehr dazu findet man unter :doc:`strukturanalyse`.
    **Zugewiesene Anforderungen**
        Dies ist eine virtuelle Kategorie, die alle Anforderungen anzeigt, die durch die zugeordneten Bausteine zugewiesen werden.
    **Zugewiesene Gefährdungen**
        Dies ist eine virtuelle Kategorie, die alle Gefährdungen anzeigt, die durch die zugeordneten Bausteine zugewiesen werden.
**Kontaktzuweisung** *(i-doit Standardkategorie)* 
    Hier können die entsprechenden Ansprechpartner oder andere Rollen für diese Zielobjektgruppe eingetragen werden.
**Objektgruppe** *(i-doit Standardkategorie)* 
    Hier wird definiert, welche Objekte dieser Zielobjektgruppe zugeordnet sind. Bitte beachten, dass der Typ auf "statisch" gestellt sein muss, damit die ganzen :doc:`report` funktionieren.
