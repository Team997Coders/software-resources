The basic unit of all programming languages is the _variable_. A variable is very similar to the mathematical variable, except it can hold more than just a numerical value. A program is generally built upon operations between these variables.

However, not every operation is supported for every variable or combination of variables. For instance, the concept of adding a number to a word doesn't make any sense and the underlying computer doesn't know how to resolve this.

```
"Hello world!" + 3     <-- Makes no sense
``` 
[^1]

To fix this problem, variables come with a fundamental trait called their _type_. The type tells the underlying processor that translates into code a computer can execute (called the _compiler_) how to treat that variable, and prevents you from trying to run nonsensical operations.

## Creating a Variable
In Java, creating a variable follows the pattern:
```
type name = value;
```
The `=` means that we're assigning `name` to mean `value`. You can also assign a variable in the place of `value`, or use the result of an operation.

The semicolon at the end tells the Java compiler that that statement ends there. Unlike in some other programming languages, the spacing of symbols and lines is ignored.

The name of the variable should be reasonably concise and should describe what the variable represents well. If a variable corresponds to something that could use units of measurement those should be included in the name (e.g. `velocityMetersPerSecond`), even if this can be slightly verbose.

It is also valid to _declare_ a variable exists without giving it a value yet. Trying to use the value of that variable will result in an error though.
```
type name;
```

After a variable is declared (by either method), you can reassign it by writing:
```
name = newValue;
```

There are numerous types you can encounter while writing Java for FRC. These can corresponds to simple, small pieces of data, or to much more complex data structures. The next few sections will go into these types.

[^1]: This works in real life Java, but it's because the compiler makes an implicit cast of the number to a string.