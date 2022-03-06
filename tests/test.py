import markdown2


s = """
## Heading

[SPOILER]

```js
console.log("hello world")
```

[/SPOILER]


[INFO]
```js
console.log("hello world")
```

[/INFO]


[SPOILER]
```js
console.log("hello world")
```

[NOTE]
```js
console.log("hello world")
```

[/NOTE]

_herl_
[/SPOILER]

"""

out = markdown2.markdown(s, extras=["fenced-code-blocks"])
print(markdown2.markdown(out, extras=["fenced-code-blocks"]))
