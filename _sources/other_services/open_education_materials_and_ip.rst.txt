===============================
Open Education Materials and IP
===============================

When developing curricula, who owns the intellectual property?

The flowchart below was developed based on policy `17.01.01 Ownership of Intellectual Property and Tangible Research Property <https://policies.tamus.edu/17-01-01.pdf>`_.


.. mermaid::

    flowchart TD
        A[Start: Faculty wants to release curriculum] --> B{Created as part of normal teaching duties?}
        B -- No --> C{Commissioned or work-for-hire?}
        B -- Yes --> D{Created using significant University resources?}

        C -- Yes --> E[University likely owns the work. Cannot release unilaterally]
        C -- No --> D

        D -- Yes --> E
        D -- No --> F{Subject to grant, contract, or sponsored research agreement assigning IP?}

        F -- Yes --> E
        F -- No --> G{Any co-creators?}

        G -- Yes --> H[All co-creators must agree before release]
        G -- No --> I[Faculty owns copyright and can release to public domain]
