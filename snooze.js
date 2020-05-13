/*
    Background

    snooze() creates a promise that pauses the script for the given # of secs.
*/

function snooze(snoozeTimeSecs) {
    return new Promise((resolveFunc, rejectFunc) => {
        setTimeout(() => {
            resolveFunc(snoozeTimeSecs);
        }, snoozeTimeSecs * 1000)
    });
}



/* 
    Task 1
    
    Use the snooze() function help you:
    
    - Snooze for 1 second
    - Print out "I slept for 1 second"

    Note: Use ".then()" Promise chaining.
          Don't hardcode the # of seconds in the printout.
*/

//
// Write your code here.
//



/*  
    Task 2
    
    Use the snooze() function to help you:
    
    - Snooze for 1 second
    - Print out "I slept for 1 second"
    - Snooze for 2 seconds
    - Print out "I slept for 2 seconds"
    - Snooze for 3 seconds
    - Print out "I slept for 3 seconds"
    
    Note: Use ".then()" Promise chaining.
          Don't hardcode the # of seconds in the printout.
          Expect the code to get pretty messy.
*/

//
// Write your code here.
//



/* 
    Task 3
    
    Do the same as #2 but use async/await.
    
    Note: Write your code inside the specially-crafted main() method.
          Ignore the surrounding code for now.
          Don't hardcode the # of seconds in the printout.
          Expect the code to look neater than the code in Task 2.
*/

async function main() {
    //
    // Write your code here.
    //
}

(async () => { await main(); })().catch();
