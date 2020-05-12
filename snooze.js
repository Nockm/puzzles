// This creates a promise that pauses
// the script for the given # of secs

function snooze(snoozeTimeSecs) {
  return new Promise((resolveFunc, rejectFunc) => {
    setTimeout(() => {
      resolveFunc(snoozeTimeSecs);
    }, snoozeTimeSecs * 1000)
  });
}

// 1.
// Create a promise to snooze for 3 seconds

// 2.
// Use the snooze() function to:
// - Snooze for 1 second
// - Print out "I slept for 1 second"
// - Snooze for 2 seconds
// - Print out "I slept for 2 seconds"
// - Snooze for 3 seconds
// - Print out "I slept for 3 seconds"
//
// Don't hardcode the # of seconds in the printout

// 3.
// Do the same thing as #2 but use async/await
// Note: You will have to write it inside
// the main() method specially crafted.
// Ignore the stuff around it for now.

async function main() {
	// Write your stuff here
}

(async () => { await main(); })().catch();

