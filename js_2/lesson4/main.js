let text = `he said: 'Lorem Ipsum? It's simply dummy text of the printing and typesetting industry, isn't it?' 'Lorem Ipsum has been the industry's standard dummy text ever since the 1500s', - i responded`
console.log(`original text: \n ${text}`)
let regexp = /(\B')|('\B)/g
let newText = text.replace(regexp, '"')
console.log(`edited text: \n ${newText}`)
