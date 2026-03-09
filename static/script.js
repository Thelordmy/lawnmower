function send(cmd) {
    fetch('/command', {
        method: 'POST',
        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        body: 'cmd=' + cmd
    })
    .then(r => r.text())
    .then(r => document.getElementById('status').innerText = 'Status: ' + r);
}
