# Mixed-Level-Class-Grouping
My partner is a teacher and wanted a way to create groups with diverse reading levels and gender distributions. I wrote a quick Python script to help out!


# Design
## Gathering Requirements
My partner came to me asking if I could help write a program to help with something in the classroom. She had kids with differing levels of reading and math abilities, and wanted a way to easily create groups that made sure they could teach each other.

From here, I took what I consider to be an important step: I recognized that my partner is not a product manager, engineer, or even customer. She's not familiar with the lingo we use in the software industry. As a result, "gathering requirements" was going to be a little different than usual.

Rather than asking for expected input and output or anything like that, I asked her to describe the problem in detail and show me how she currently does things. Once I felt I understood she was trying to create diverse groups, I went through a few input and output examples with her to verify that the groups I was making by hand were what she had in mind. I'm glad we went through this process, because it turned out she also wanted diversity in gender balancing as well, which didn't change things too much but was good to know early on.

## Separation of Concerns
I wanted to keep the balancing algorithm separate from the input separate from the file handling and data modeling. 

To make this easy for my partner, I had her input the students' names, genders, and ability levels into a spreadsheet and exported that to a CSV. 

From there, I parse the file and load the student ability levels data in and load those into a data model that ensures the ability levels are "sorted" from A-Z as the education sector uses them. 

After that, I created ranges (`LevelRange`s) indicating whether they were below grade level, at grade level, or above grade level. 

Those levels along with the student's gender are assigned to `Student` objects. We then pass that student and leveling data directly to the balancing algorithm which places `Student`s into `StudentGroup`s.

## Balancing Algorithm
We want groups that are balancing both by reading level and by gender. To do so, we iterate over all the groups, and select a group that doesn't have too many students at the same ability level or gender.

We then validate that all groups are valid (just in case) by iterating over all groups and raising an exception if any group has too many members, too many of a specific gender, or too large a mismatch in ability levels.


# Results
My partner used this program at least four times during the remainder of the school year! She reports that it's a lot easier doing it this way instead of manually assigning students.
