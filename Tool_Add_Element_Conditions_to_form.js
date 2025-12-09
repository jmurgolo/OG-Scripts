const delay = ms => new Promise(res => setTimeout(res, ms));

async function runAutomation() {
    console.log("--- Starting Complete Automation ---");

    try {
        // ============================================================
        // STEP 1: Click "Add New Condition" Button
        // ============================================================
        const addBtn = document.querySelector('[data-testid="add-condition-button"]');
        if (!addBtn) throw new Error("Step 1 Error: 'Add New Condition' button not found.");
        
        addBtn.click();
        console.log("Step 1: Clicked 'Add New Condition'");
        await delay(1000); 


        // ============================================================
        // STEP 2 & 3: Select "Schedule xxxxxxx Inspection"
        // ============================================================
        const entityDropdown = document.querySelector('[role="combobox"][aria-label="entity-select"]');
        if (!entityDropdown) throw new Error("Step 2 Error: Entity Dropdown not found.");

        // Force open
        entityDropdown.dispatchEvent(new MouseEvent('mousedown', { bubbles: true, cancelable: true, view: window }));
        entityDropdown.click(); 
        console.log("Step 2: Opened Entity Dropdown");

        // Retry loop for option
        let entityOption = null;
        for (let i = 0; i < 15; i++) {
            await delay(200);
            const options = Array.from(document.querySelectorAll('li[role="option"]'));
            entityOption = options.find(el => el.textContent.includes("Schedule Thirteenth Inspection"));
            if (entityOption) break;
        }
        if (!entityOption) throw new Error("Step 3 Error: 'Schedule Thirteenth Inspection' option not found.");
        
        entityOption.click();
        console.log("Step 3: Selected 'Schedule Twelfth Inspection'");
        await delay(1000);


        // ============================================================
        // STEP 4 & 5: Select "is"
        // ============================================================
        const opDropdown = document.querySelector('[role="combobox"][aria-label="operator-select"]');
        if (!opDropdown) throw new Error("Step 4 Error: Operator Dropdown not found.");

        opDropdown.dispatchEvent(new MouseEvent('mousedown', { bubbles: true, cancelable: true, view: window }));
        opDropdown.click();
        console.log("Step 4: Opened Operator Dropdown");

        let isOption = null;
        for (let i = 0; i < 15; i++) {
            await delay(200);
            const options = Array.from(document.querySelectorAll('li[role="option"]'));
            isOption = options.find(el => el.getAttribute('data-value') === 'is' || el.textContent.trim() === 'is');
            if (isOption) break;
        }
        if (!isOption) throw new Error("Step 5 Error: Option 'is' not found.");

        isOption.click();
        console.log("Step 5: Selected 'is'");
        await delay(1000);


        // ============================================================
        // STEP 6 & 7: Select "true"
        // ============================================================
        const valDropdown = document.querySelector('[role="combobox"][aria-label="value-select"]');
        if (!valDropdown) throw new Error("Step 6 Error: Value Dropdown not found.");

        valDropdown.dispatchEvent(new MouseEvent('mousedown', { bubbles: true, cancelable: true, view: window }));
        valDropdown.click();
        console.log("Step 6: Opened Value Dropdown");

        let trueOption = null;
        for (let i = 0; i < 15; i++) {
            await delay(200);
            const options = Array.from(document.querySelectorAll('li[role="option"]'));
            trueOption = options.find(el => el.getAttribute('data-value') === 'true');
            if (trueOption) break;
        }
        if (!trueOption) throw new Error("Step 7 Error: Option 'true' not found.");

        trueOption.click();
        console.log("Step 7: Selected 'true'");
        await delay(500);


        // ============================================================
        // STEP 8: Click "Save"
        // ============================================================
        // We look for a button with exact text "Save"
        const allButtons = Array.from(document.querySelectorAll('button'));
        const saveBtn = allButtons.find(b => b.textContent.trim() === "Save");

        if (!saveBtn) throw new Error("Step 8 Error: 'Save' button not found.");

        saveBtn.click();
        console.log("Step 8: Clicked 'Save'");

        console.log("--- Automation Successfully Completed ---");

    } catch (error) {
        console.error(error.message);
    }
}

runAutomation();