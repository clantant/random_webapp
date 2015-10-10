Design Document
Media consuming list - what episode, which game, etc I'm currently on
Radio button is for which kind of media and platform (steam, netflix, etc)
Genre is the check-boxes
Check box for completeness (true or false)
Admin page is where new genres and platforms can be added
Media must be changed system-side for now (maybe forever?)
Main page is where view is done, also priority can be changed from here
Add page is where a new item is added
Possible add_file page for adding from file
Edit page is where edits can be made
Entity structure is media -> type_of_media -> member
member is going to have: platform, genre, name, priority, episode, completeness
Completeness cannot be true and have a priority, priority can be none
If completeness is false then should have a priority
When adding, if priority given then item has that priority and all items
below it move down 1, if no priority then put as last item
When changing completeness or removing an item then priority is shifted up to replace it
Each type_of_media entity has its own priority
