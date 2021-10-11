import markdown2

s = """
<div>
[ds](www.google.com)
(ds)[www.google.com]
**bold**
```
function(){
	console.log(print)
}
```
</div>
"""

out = markdown2.markdown(s, extras=["fenced-code-blocks"])
print(markdown2.markdown(out, extras=["fenced-code-blocks"]))