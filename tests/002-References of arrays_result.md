 Now you should have a rendered board,
and this board should log messages to the console
every time you click somewhere on the board.
The log will also tell you where on the board you clicked.

What information do you need to update the board?
<details>
<summary>Spoiler</summary><ul>
<li>The position.</li>
<li>The player whose turn it is.</li>
</ul>

<p>What things need to be checked before updating the board?</p>
<details>
<summary>Spoiler</summary><ul>
<li>If the position is empty</li>
<li>The the position is valid, i.e. You can't have position <code>15, 20</code>
if the board is 10 x 10.</li>
</ul>

<p>So how would you go about implementing all this?</p>
<details>
<summary>Spoiler</summary><pre><code>
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
</code></pre>

<p>Woah, what's all this fancy stuff above each function?</p>
<p>What's with the Global Variables part?</p>
<p></p>
</details><p></p>
</details><p></p>
</details>
