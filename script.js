const fs = require('fs');
const { execSync } = require('child_process');

function automateGitOperations() {
    /**
     * Automate creating a file, performing git add/commit/push, deleting the file,
     * and repeating the git commands for a fixed number of 25 runs.
     */
    const runTimes = 25;

    for (let i = 1; i <= runTimes; i++) {
        const filename = `temp_file_${i}.txt`;

        // Step 1: Create a blank text file
        fs.writeFileSync(filename, '');

        // Step 2: Add, commit, and push the file to the repository
        try {
            execSync(`git add ${filename}`);
            execSync(`git commit -m "Add ${filename}"`);
            execSync(`git push`);
        } catch (error) {
            console.error(`Error during git operation: ${error.message}`);
            return;
        }

        // Step 3: Delete the file
        fs.unlinkSync(filename);

        // Step 4: Run git add, commit, and push again
        try {
            execSync(`git add -A`);
            execSync(`git commit -m "Remove ${filename}"`);
            execSync(`git push`);
        } catch (error) {
            console.error(`Error during git operation: ${error.message}`);
            return;
        }
    }
}

// Example usage
automateGitOperations();
