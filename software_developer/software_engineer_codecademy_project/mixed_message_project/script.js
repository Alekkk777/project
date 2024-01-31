// Message components
const messageParts = {
  beginnings: [
    "Believe in yourself",
    "Your limitation—it's only your imagination",
    "Push yourself",
    "Great things never come from comfort zones",
    "Dream it"
  ],
  middles: [
    "because success",
    "as the journey",
    "and all is possible",
    "so take the risk",
    "and work hard"
  ],
  ends: [
    "is waiting for you.",
    "is full of ups and downs.",
    "is the fruit of effort.",
    "to achieve greatness.",
    "to make it happen."
  ]
};

// Function to randomly select part of the message
function selectRandomMessagePart(partArray) {
  return partArray[Math.floor(Math.random() * partArray.length)];
}

// Function to generate the entire message
function generateMessage() {
  const beginning = selectRandomMessagePart(messageParts.beginnings);
  const middle = selectRandomMessagePart(messageParts.middles);
  const end = selectRandomMessagePart(messageParts.ends);

  return `${beginning}, ${middle} ${end}`;
}

// Generate and display the message
console.log(generateMessage());