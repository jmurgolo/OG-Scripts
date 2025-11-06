// === CONFIGURATION ===
// Change this text to the heading you want to start AFTER.
const startElementText = "Eighth Inspection";

// Change this text to the heading you want to stop BEFORE.
const endElementText = "Eighth Ticket Details";

// Set the pause time in milliseconds (1000 = 1 second)
// Adjust this if the page needs more time to react to each click.
const delayInMilliseconds = 500;
// =====================


// --- Helper function for pausing ---
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// --- Main script logic (wrapped in an async function) ---
async function clickCheckboxes() {
    // 1. Find the start and end elements
    const startElement = Array.from(document.querySelectorAll('h5')).find(h => h.textContent.trim().includes(startElementText));
    const endElement = Array.from(document.querySelectorAll('h5')).find(h => h.textContent.trim().includes(endElementText));

    if (!startElement) {
        console.error(`Error: Could not find a start element with text "${startElementText}".`);
        return;
    }
    if (!endElement) {
        console.error(`Error: Could not find an end element with text "${endElementText}".`);
        return;
    }

    console.log('Found start element:', startElement);
    console.log('Found end element:', endElement);

    // 2. Find all checkboxes
    const allCheckboxes = document.querySelectorAll('input[type="checkbox"]');
    const boxesToClick = []; // We'll store the target boxes here

    // 3. Filter only the checkboxes between our elements
    allCheckboxes.forEach(checkbox => {
        const isAfterStart = startElement.compareDocumentPosition(checkbox) & Node.DOCUMENT_POSITION_FOLLOWING;
        const isBeforeEnd = endElement.compareDocumentPosition(checkbox) & Node.DOCUMENT_POSITION_PRECEDING;

        if (isAfterStart && isBeforeEnd) {
            boxesToClick.push(checkbox);
        }
    });

    if (boxesToClick.length === 0) {
        console.warn(`No checkboxes found between "${startElementText}" and "${endElementText}".`);
        return;
    }

    console.log(`Found ${boxesToClick.length} checkboxes to click. Starting now...`);

    // 4. Loop through and click each box one by one
    for (let i = 0; i < boxesToClick.length; i++) {
        const checkbox = boxesToClick[i];
        
        // Find the label text for logging
        const label = checkbox.closest('label');
        const labelText = label ? label.textContent.trim() : `(No label text found)`;

        console.log(`Clicking box ${i + 1} of ${boxesToClick.length}: "${labelText}"`);
        
        // This simulates a real user click, triggering any page events.
        checkbox.click(); 

        // Wait for the specified delay before continuing the loop
        await sleep(delayInMilliseconds);
    }

    console.log('--- All done! ---');
}

// Run the function
clickCheckboxes();