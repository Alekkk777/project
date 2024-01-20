let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:
//step 3
let generateTarget = () => {
    return Math.floor(Math.random() * 9);  
};

//step 4
let compareGuesses = (human, computer, target) => {
    const userG = Math.abs(target - human);
    const computerG = Math.abs(target - computer);
    return userG <= computerG;

    /*if (userG <= computerG) {
        updateScore('human');
    } else {
        updateScore('computer');
    }*/
};

//step 5
let updateScore = winner => {
    if (winner === 'human') {
        humanScore += 1;
    } else if (winner === 'computer') {
        computerScore += 1;
    }
};

//step 6
function advanceRound() {
    currentRoundNumber += 1;
};
