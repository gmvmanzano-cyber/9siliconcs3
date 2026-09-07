# Class Attributes and Methods


## Previous Design
Link to my previous activity:
[classObjectUML.md](\q1\classObjectUML.md)


## Design Revision
No major changes were applied. The properties and core mechanisms were retained, but current_position attribute was added to accurately manage or track skipping/playback states. The duration and current_position are now protected using private visibility to prevent improper modification.


## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
|title |string |Public |Anyone can read or display title without risk of bugs |
|artist |string |Public |It is safe to access publicly since changing artist name does not break playback |
|writer |string |Public |Publically accessible data that does not impact playback |
|duration |integer |Private |Private to prevent from setting to invalid or negative lengths |
|current_position|integer|private|Hidden to ensure track position can only update through official means, such as forwarding or rewinding|

## Updated UML Class Diagram
![Class Diagram](Images\classDiagramSG5.png)


## Python Implementation
[View Python Source](classImplementation.py)


## Test Run
![Test Run](Images\classTestRun.png)


## Object Diagram
![Object Diagram](Images\objectDiagram.png)


## Analysis
### Why did you make your chosen attribute private?
I made duration and current position as private to protect track data from external modifications. If other parts of the program changed these attributes, they could set a negative duration or jump past the total length of the song.
### Which method changes the state of your object?
The forward() method changes the internal state of the object by modifying the __current_position attribute. It receives seconds parameter and increments __curent_position, ensuring the new value never exceeds the total __duration of the song.
### How did your two objects demonstrate that instances are independent?
When forward(15) was executed on the song, its remained at 0 seconds. The test output shows both objects printed side-by-side, proving that changing internal attributes on one objet does not alter the state of another instance created from the same class.
### What is the difference between your class diagram and your object diagram?
My class diagram is an abstract blueprint showing overall property names, data types, visibilities, and method signatures for the Song class. In contrast, my object diagram given the moment in execution, showing actual assigned values like "Bohemian Rhapsody" and its runtime position.
