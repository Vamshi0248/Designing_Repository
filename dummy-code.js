// Dummy code for feature/buttons branch
// This file contains sample code for button component implementation

class ButtonComponent {
  constructor(label, onClick, type = 'primary') {
    this.label = label;
    this.onClick = onClick;
    this.type = type;
  }
  
  render() {
    const button = document.createElement('button');
    button.textContent = this.label;
    button.className = `btn btn-${this.type}`;
    button.addEventListener('click', this.onClick);
    return button;
  }
  
  addToDOM(selector) {
    const container = document.querySelector(selector);
    if (container) {
      container.appendChild(this.render());
      console.log(`Button "${this.label}" added to DOM`);
    }
  }
}

// Usage example
const submitButton = new ButtonComponent('Submit', () => {
  console.log('Form submitted!');
}, 'primary');

const cancelButton = new ButtonComponent('Cancel', () => {
  console.log('Action cancelled');
}, 'secondary');
