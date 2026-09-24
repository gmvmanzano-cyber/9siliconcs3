# Advanced Class Relationships

## Previous Activities
[classAttrib](classAttributesMethods.md)


[classRel](classRelationships.md)


## Existing System Description:
### 1. What classes currently exist in your system?
Class 1: Song       Class 2: Album

### 2. What problem or limitation exists in your current design?

If I were to want to add other types of audio, I would need to copy the same functions over and over again for each variation.


## Inheritance Relationship
Parent: Audio_track


Child: Song


Explanation: A Song IS-A Audio_track. Audio_track can provide the properties and playback controls that any audio track can need. The Song inherits these properties and adds music meta data like artist and writer.


## Inheritance UML
![Inheritance](images/inheritanceDiagram.png)


## Composition/Aggregation
Relationship: Aggregation


Explanation: An Album aggregates Song objects (amounts to). This has a weak reltationship because Song can exist independently of Album. If Album is removed, Song would still exist standalone.


## Advanced UML Diagram
![Advanced UML](images/advancedClassDiagram.png)


## Python Implementation
[Source Code](advancedRelationships.py)


## Test Run
![Test](images/advancedTestRun.png)


## Object Diagram
![Objects](images/advancedObjectDiagram.png)

## Reflection
Answers:
### 1. Why did you choose your inheritance relationship? Explain why your child class is a type of your parent class.
I chose Audio_track as parent because any Song needs a title, duration and track position. A Song is a type of Audio_track because it simply adds only a little bit of metadata specific to music and inherits the rest.
### 2. How did inheritance reduce duplicate code? Identify attributes or methods that were reused.
Instead of redifining attributes like duration, current_position, etc. I used methods in the Song class and reallocated them to the Audio_track class. 
### 3. Why is your HAS-A relationship Composition or Aggregation? Explain the lifecycle relationship between the two objects.
It is Aggregation because the Song is independent to the Album. The Album just receives the Song objects rather than reinitializing new ones. If Album is deleted, Song still remains.
### 4. What is the difference between Association from Part III and the advanced relationship you implemented?
Association meant two or more classes communicated in a way. By saying it is Aggregation, I expounded what ownership, establishing that the Album is just a container, and it does not own Song's existences.
### 5. How does your design follow the DRY principle?
The DRY principle is used in isolating the primary methods into the class Audio_track. If I ever add new audio file types later, I won't need to rewrite methods already initialized.