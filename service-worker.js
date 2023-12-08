// Listen for a click on the camera icon. On that click, take a screenshot.
chrome.action.onClicked.addListener(async function () {
  const screenshotUrl = await chrome.tabs.captureVisibleTab();
  const viewTabUrl = chrome.runtime.getURL("screenshot.html");
  let targetId = null;

  chrome.tabs.onUpdated.addListener(function listener(tabId, changedProps) {
    if (tabId != targetId || changedProps.status != "complete") return;

    chrome.tabs.onUpdated.removeListener(listener);

    // Send screenshotUrl to the tab.
    chrome.tabs.sendMessage(tabId, { msg: "screenshot", data: screenshotUrl });
  });

  const tab = await chrome.tabs.create({ url: viewTabUrl });
  targetId = tab.id;
});
