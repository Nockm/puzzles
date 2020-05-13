/* 
	snooze() creates a promise that pauses
	the script for the given # of secs.
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
	Use the snooze() function to:
  
  - Snooze for 1 second
  - Print out "I slept for 1 second"
  
 	Note: Don't hardcode the # of seconds
        in the printout
*/

/*  
	Task 2.
	Use the snooze() function to:
  
  - Snooze for 1 second
  - Print out "I slept for 1 second"
  - Snooze for 2 seconds
  - Print out "I slept for 2 seconds"
  - Snooze for 3 seconds
  - Print out "I slept for 3 seconds"
*/


/* 
	Task 3.
	Do the same thing as #2 but use async/await
	
  Note: You will have to write your code inside
	      the specially-crafted main() method.
	      Ignore the stuff around it for now.
*/

async function main() {
	// Write your async/await code here.
}

(async () => { await main(); })().catch();

