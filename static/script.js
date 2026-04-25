const state = {
  spray: false,
  mower: false,
  auto: false,
  override: false
};

function send(cmd) {
  fetch('/command', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: 'cmd=' + cmd
  })
  .then(r => r.text())
  .then(r => { document.getElementById('status-text').textContent = r; });
}

function toggle(name) {
  // Auto mode disables manual movement
  if (name === 'auto') {
    state.auto = !state.auto;
    const cmd = state.auto ? 'auto_on' : 'auto_off';
    send(cmd);
    document.getElementById('auto-btn').classList.toggle('active', state.auto);

    // Disable/enable dpad buttons when auto is on
    document.querySelectorAll('.dpad-btn').forEach(btn => {
      btn.disabled = state.auto;
      btn.style.opacity = state.auto ? '0.4' : '1';
    });
    return;
  }

  state[name] = !state[name];
  const cmd = state[name] ? name + '_on' : name + '_off';
  send(cmd);
  document.getElementById(name + '-btn').classList.toggle('active', state[name]);
}
