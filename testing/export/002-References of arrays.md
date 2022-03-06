
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
<details>
<summary>Spoiler</summary><p>Every position <code>[0]</code> of <em>every single</em> sub array has the value <code>"Hello"</code>!
How can this be?</p>

<p>This is where the concept of a <strong>reference</strong> comes in.
When working with arrays and objects in JavaScript,
you have to take care
that you are working with what you think you are working with.</p>

<p>JavaScript happens to default to passing <em>references</em> to arrays and objects
instead of passing a <em>copy</em>.
Take for instance, this code:</p>

<pre><code>const a = []
const b = a
b[0] = 1
console.log(a)
</code></pre>

<p>What do you expect?</p>
<details>
<summary>Spoiler</summary><pre><code>[1]
</code></pre>

<p>This is because these lines</p>

<pre><code>const a = []
const b = a
</code></pre>

<p>Are telling JavaScript:</p>

<ul>
<li>Assign the <em>reference</em> of a new blank array to the variable <code>a</code>.</li>
<li>Assign the value of the variable <code>a</code> to the variable <code>b</code>.
The value of the variable <code>a</code> is a reference, so <code>b</code> becomes a reference too.</li>
<li>Now both <code>a</code> and <code>b</code> are just a reference to the <em>same array</em>.</li>
</ul>

<p>Copying arrays will be covered later!</p>
</details><p></p>
</details>