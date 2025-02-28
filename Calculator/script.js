// JavaScript Code
let display = document.getElementById('display');
let currentInput = '';
let operator = null;
let previousInput = '';

// Append numbers to the display
function appendNumber(number) {
    if (currentInput.includes('.') && number === '.') return; // Prevent multiple decimals
    currentInput += number;
    updateDisplay();
}

// Append operators
function appendOperator(op) {
    if (currentInput === '') return; // Prevent operator without number
    if (previousInput !== '') calculateResult(); // Calculate if there's a previous input
    operator = op;
    previousInput = currentInput;
    currentInput = '';
}

// Calculate the result
function calculateResult() {
    if (currentInput === '' || previousInput === '') return; // Prevent calculation without inputs
    let result;
    const prev = parseFloat(previousInput);
    const current = parseFloat(currentInput);

    switch (operator) {
        case '+':
            result = prev + current;
            break;
        case '-':
            result = prev - current;
            break;
        case '*':
            result = prev * current;
            break;
        case '/':
            result = prev / current;
            break;
        default:
            return;
    }

    currentInput = result.toString();
    operator = null;
    previousInput = '';
    updateDisplay();
}

// Clear the display
function clearDisplay() {
    currentInput = '';
    operator = null;
    previousInput = '';
    updateDisplay();
}

// Update the display
function updateDisplay() {
    display.textContent = currentInput || '0';
}