# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
In a sari-sari store inventory system, encapsulation bundles product details, such as product_name, price, and stock—inside a single Product class rather than keeping them in separate variables. Instead of allowing external code to modify stock directly, the variables are kept private and accessed through methods like update_stock. This prevents accidental bugs, such as setting inventory to a negative number or changing prices by mistake. Overall, it protects store data and ensures modifications follow defined rules.

### 2. Abstraction
Abstraction hides complex background logic and presents only essential features to the user. For instance, when a cashier records a sale, the system simply invokes a method like sell_item(quantity) on an object. The user does not need to see or manage the internal lines of code that recalculate stock, verify limits, or log receipts. By keeping the interface clean, the program becomes easier to read, maintain, and expand over ti

### 3. Inheritance
Inheritance allows the system to create a general base class and then derive specialized product types without retyping code. A general Product class handles basic items like canned goods, while a subclass like PerishableProduct handles items such as milk or bread. The subclass automatically inherits the name, price, and stock properties from Product, while allowing additional properties like expiration_date to be added. This reduces code repetition and maintains a clear project structure.

### 4. Polymorphism
Polymorphism enables different product types to execute their own specific behavior using a shared method name. For example, both a RegularProduct and a PerishableProduct can share a method named get_total_cost(quantity). However, the perishable item can override the method to automatically apply a discount if the item is near expiration. The main program can call get_total_cost() on any item in inventory without relying on repetitive conditional checks for product categories.

