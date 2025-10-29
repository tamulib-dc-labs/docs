==============================
Generating Structures from CSV
==============================

Avalon allows you to create complex structures and ranges that it calls timeline. There is an editor to do this manually,
but often times our structures are simple.

A script like this:

.. code-block:: python

    from csv import DictReader
    from lxml import etree


    class StructureMaker:
        def __init__(self, my_csv, output):
            self.my_csv = my_csv
            self.output = output
            self.contents = self.read()

        def read(self):
            all_rows = []
            with open(self.my_csv) as csvfile:
                reader = DictReader(csvfile)
                for row in reader:
                    all_rows.append(row)
            return all_rows

        @staticmethod
        def normalize_time(t):
            parts = t.split(':')
            parts = [p.zfill(2) for p in parts]
            while len(parts) < 3:
                parts.insert(0, '00')
            return ':'.join(parts) + '.00'

        def make_xml(self):
            root = etree.Element("Item")
            root.set("label", "Questions")
            for content in self.contents:
                question = etree.SubElement(root, "Span")
                question.set("label", content["Questions:"])
                question.set("begin", self.normalize_time(content["Start"]))
                question.set("end", self.normalize_time(content["Stop"]))
            xml_bytes = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding="UTF-8")
            with open(self.output, "wb") as f:
                f.write(xml_bytes)


    if __name__ == "__main__":
        my_csv = "tracy-harris.csv"
        output = "tracy-harris.xml"
        x = StructureMaker(my_csv, output)
        x.make_xml()

With a CSV like:

.. code-block:: csv

    Questions:,Start,Stop
    What is your name?,0:50,0:51
    Where were you born?,0:56,0:58
    Where did you grow up?,1:01,1:11
    What are your earliest memories of art?,1:31,2:15
    Was your family supportive of the arts? Supportive of you in the arts?,2:22,3:11
    Was your elementary/high school supportive of the arts?,3:32,4:15
    Did you have mentors in these years that pushed you to further your interest or career in art?,4:16,4:21
    Where did you go to college?,4:27,4:28
    What brought you to that college and program?,4:35,6:05
    Who were the professors at the time?,6:11,8:11
    Did you have opportunities to show your work?,8:19,8:53
    What was your artistic medium? (1),7:04,7:58
    What was your artistic medium? (2),35:45,38:25
    Did you get out to see things in the city?,9:02,9:27
    What was the art scene like in Dallas?,9:28,10:20
    Where did you make your work in Dallas? What was your studio/working space like?,10:26,11:06
    When was the first time that you heard about the co-op?,11:22,11:59
    Were you invited? How did you join? Why did you join?,12:10,13:59
    "What was your role in starting/running the gallery, if any?",14:11,15:01
    "Outside of the co-op artist, who else helped? Who was supportive? Who were collectors?",20:27,21:14
    "Once you had graduated from college and/or joined the co-op, what else were you doing besides making art? Working? Teaching?",22:37,25:21:00
    What was the gallery like? The space itself (first and second space)?,18:00,19:13
    What are some of the fun thing you remember about running the gallery? Stories?,39:10,39:56
    "In your view, what made the gallery work?",19:20,20:17
    What was the public reception to the gallery in your opinion?,21:31,22:16
    "Did you have much interaction with the museums? Museum stass, curators, directors? (1)",25:39,26:14
    "Did you have much interaction with the museums? Museum stass, curators, directors? (2)",26:27,27:02
    "Looking back, what are some of the fondest memories of your time as a member of the co-op?",38:34,39:05
    How do you feel about this period in your life?,36:57,38:19
    "The world is very different now, but what advice would you give artists coming out of college or starting their careers now?",40:10,40:36
    "In 1988, Linda Samuels, the original director who had left in 1980, was asked to curate the ""last"" DW Gallery exhibition. What was this last show? Who was in it? What do you remember about it?",35:35,35:48
    What led to the closing of the gallery? It loooks like there was a small group that were trying to keep it going. What were the challenges?,27:20,38:09
    "In the years since you left, what have you done? Where have you been?",29:00,33:06

Will generate XML like:

.. code-block:: xml

    <Item label="Questions">
      <Span label="What is your name?" begin="00:00:50.00" end="00:00:51.00"/>
      <Span label="Where were you born?" begin="00:00:56.00" end="00:00:58.00"/>
      <Span label="Where did you grow up?" begin="00:01:01.00" end="00:01:11.00"/>
      <Span label="What are your earliest memories of art?" begin="00:01:31.00" end="00:02:15.00"/>
      <Span label="Was your family supportive of the arts? Supportive of you in the arts?" begin="00:02:22.00" end="00:03:11.00"/>
      <Span label="Was your elementary/high school supportive of the arts?" begin="00:03:32.00" end="00:04:15.00"/>
      <Span label="Did you have mentors in these years that pushed you to further your interest or career in art?" begin="00:04:16.00" end="00:04:21.00"/>
      <Span label="Where did you go to college?" begin="00:04:27.00" end="00:04:28.00"/>
      <Span label="What brought you to that college and program?" begin="00:04:35.00" end="00:06:05.00"/>
      <Span label="Who were the professors at the time?" begin="00:06:11.00" end="00:08:11.00"/>
      <Span label="Did you have opportunities to show your work?" begin="00:08:19.00" end="00:08:53.00"/>
      <Span label="What was your artistic medium? (1)" begin="00:07:04.00" end="00:07:58.00"/>
      <Span label="What was your artistic medium? (2)" begin="00:35:45.00" end="00:38:25.00"/>
      <Span label="Did you get out to see things in the city?" begin="00:09:02.00" end="00:09:27.00"/>
      <Span label="What was the art scene like in Dallas?" begin="00:09:28.00" end="00:10:20.00"/>
      <Span label="Where did you make your work in Dallas? What was your studio/working space like?" begin="00:10:26.00" end="00:11:06.00"/>
      <Span label="When was the first time that you heard about the co-op?" begin="00:11:22.00" end="00:11:59.00"/>
      <Span label="Were you invited? How did you join? Why did you join?" begin="00:12:10.00" end="00:13:59.00"/>
      <Span label="What was your role in starting/running the gallery, if any?" begin="00:14:11.00" end="00:15:01.00"/>
      <Span label="Outside of the co-op artist, who else helped? Who was supportive? Who were collectors?" begin="00:20:27.00" end="00:21:14.00"/>
      <Span label="Once you had graduated from college and/or joined the co-op, what else were you doing besides making art? Working? Teaching?" begin="00:22:37.00" end="25:21:00.00"/>
      <Span label="What was the gallery like? The space itself (first and second space)?" begin="00:18:00.00" end="00:19:13.00"/>
      <Span label="What are some of the fun thing you remember about running the gallery? Stories?" begin="00:39:10.00" end="00:39:56.00"/>
      <Span label="In your view, what made the gallery work?" begin="00:19:20.00" end="00:20:17.00"/>
      <Span label="What was the public reception to the gallery in your opinion?" begin="00:21:31.00" end="00:22:16.00"/>
      <Span label="Did you have much interaction with the museums? Museum stass, curators, directors? (1)" begin="00:25:39.00" end="00:26:14.00"/>
      <Span label="Did you have much interaction with the museums? Museum stass, curators, directors? (2)" begin="00:26:27.00" end="00:27:02.00"/>
      <Span label="Looking back, what are some of the fondest memories of your time as a member of the co-op?" begin="00:38:34.00" end="00:39:05.00"/>
      <Span label="How do you feel about this period in your life?" begin="00:36:57.00" end="00:38:19.00"/>
      <Span label="The world is very different now, but what advice would you give artists coming out of college or starting their careers now?" begin="00:40:10.00" end="00:40:36.00"/>
      <Span label="In 1988, Linda Samuels, the original director who had left in 1980, was asked to curate the &quot;last&quot; DW Gallery exhibition. What was this last show? Who was in it? What do you remember about it?" begin="00:35:35.00" end="00:35:48.00"/>
      <Span label="What led to the closing of the gallery? It loooks like there was a small group that were trying to keep it going. What were the challenges?" begin="00:27:20.00" end="00:38:09.00"/>
      <Span label="In the years since you left, what have you done? Where have you been?" begin="00:29:00.00" end="00:33:06.00"/>
    </Item>
