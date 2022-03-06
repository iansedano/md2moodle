Now you should have a rendered board,
and this board should log messages to the console
every time you click somewhere on the board.
The log will also tell you where on the board you clicked.

What information do you need to update the board?

[SPOILER]

- The position.
- The player whose turn it is.

What things need to be checked before updating the board?

[SPOILER]

- If the position is empty
- The the position is valid, i.e. You can't have position `15, 20`
if the board is 10 x 10.

So how would you go about implementing all this?

[SPOILER]

```javascript

// GLOBAL VARIABLES
const boardSize = 15
const board = buildBoard(boardSize)
let turn = 1

/**
* Places a stone at given coordinates
* @param {number} row 
* @param {number} col 
*/
function updateBoard(row, col) {
	const currentValue = board[row][col]
	
	if (currentValue === 0) {
		board[row][col] = turn
	} else throw "invalid move"
	
	updateTurn()
}

/**
* Takes the global turn value and flip flops it between 1 or 2
*/
function updateTurn() {
	if (turn == 1) {
		turn = 2
	} else if (turn == 2) {
		turn = 1
	} else {
		throw "Invalid turn value"
	}
}
```

Woah, what's all this fancy stuff above each function?
TODO write about comments and JSDoc maybe in new lesson
What's with the Global Variables part?
TODO write about global variables and why we might want to avoid.

[/SPOILER]
[/SPOILER]
[/SPOILER]
