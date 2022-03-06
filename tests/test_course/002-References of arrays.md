
Searching online with "how to create an array of a certain size javascript"
might lead you to take this approach:

```javascript
const boardSize = 10
const board = new Array()
const row = new Array(boardSize)

for(let i=0; i!=boardSize; i++){
	board.push(row)
}

console.log(board)
```

Can you see how these are different?
Can you see how this is a _serious_ problem?

Not only does this code have a fundamental problem,
but it also looks fine to start with!

This code is simple enough to copy into the browser console to experiment with.
Try it, and once you have the variable `board`,
try changing position `[0][0]` to the value `"Hello"`.
Then `console.log(board)` do you notice anything peculiar?

[SPOILER]

Every position `[0]` of _every single_ sub array has the value `"Hello"`!
How can this be?

This is where the concept of a **reference** comes in.
When working with arrays and objects in JavaScript,
you have to take care
that you are working with what you think you are working with.

JavaScript happens to default to passing _references_ to arrays and objects
instead of passing a _copy_.
Take for instance, this code:

```javascript
const a = []
const b = a
b[0] = 1
console.log(a)
```

What do you expect?

[SPOILER]

```javascript
[1]
```

This is because these lines

```javascript
const a = []
const b = a
```

Are telling JavaScript:

- Assign the _reference_ of a new blank array to the variable `a`.
- Assign the value of the variable `a` to the variable `b`.
The value of the variable `a` is a reference, so `b` becomes a reference too.
- Now both `a` and `b` are just a reference to the _same array_.

Copying arrays will be covered later!

[/SPOILER]
[/SPOILER]

TODO copying arrays, deep copy and shallow copy etc.
TODO Or check if they are covered later...
