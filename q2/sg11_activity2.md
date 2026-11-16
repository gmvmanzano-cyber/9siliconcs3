1. Answer the following questions:
    a. What is duck typing, as explained in the video?
        - Duck typing is a form of polymorphism without inheritance from class. It  is defined as objects can be treated a specific type as long as they possess the required attributes and methods called. It comes from the phrase "If it looks like a duck, quacks like a duck, it must be a duck."
    b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?
        - The car class needs to implement minimum required attributes and methods needed by the loop. Renaming horn to speak and having the alive attribute is needed so it could not hit the AttributeError.

2. Create the [Python code](sg11_activity2.py) that:
    a. Creates three classes: Car, Boat, and Drone with a method move(). move() in the Car class prints "The car drives on the road." move() in the Boat class prints "The boat sails on water." move() in the Drone class prints "The drone flies in the sky."

    b. Has a function named start_trip(vehicle), with a parameter vehicle, that simply calls themove() method: vehicle.move().

    c. Creates one object of each class.
    
    d. Calls the start_trip() method for each object.

3. How does the code in 2.2 demonstrate polymorphism?
    - The code demonstrates polymorphism in the sense of duck typing. This is because the start_trip() function operates differing objects through a shared way (move()). It does this without requiring them to inherit it from parent class.