// static/app.js

const eventSource = new EventSource("http://127.0.0.1:8000/events");

// eventSource.addEventListener("message", (event) => {
//   console.log(event.data);
// });

eventSource.addEventListener("new_message", (event) => {
  console.log(`Custom Event: ${event.data}`);
  console.log(event);
});
eventSource.addEventListener("open", (event) => {
  console.log("EventSource connected");
});
// eventSource.addEventListener("error", (error) => {
//   console.log("EventSource failed:", error);
// });
eventSource.addEventListener("message", (event) => {
  //   console.log(event);
  //   eventSource.close();
});
