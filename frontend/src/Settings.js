import React, { useState, useEffect } from 'react';

function SettingsModal({ onClose }) {
  const [theme, setTheme] = useState('dark');
  const [voiceEnabled, setVoiceEnabled] = useState(false);

  // Load settings from backend
  useEffect(() => {
    fetch('/api/settings')
      .then(res => res.json())
      .then(data => {
        setTheme(data.theme || 'dark');
        setVoiceEnabled(data.voiceEnabled || false);
      });
  }, []);

  const saveSettings = async () => {
    await fetch('/api/settings', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ theme, voiceEnabled })
    });
    onClose();
  };

  return (
    <div className="modal">
      <h2>Settings</h2>
      <label>
        Theme:
        <select value={theme} onChange={e => setTheme(e.target.value)}>
          <option value="dark">Dark</option>
          <option value="light">Light</option>
        </select>
      </label>
      <label>
        Voice Input:
        <input
          type="checkbox"
          checked={voiceEnabled}
          onChange={e => setVoiceEnabled(e.target.checked)}
        />
      </label>
      <button onClick={saveSettings}>Save</button>
      <button onClick={onClose}>Cancel</button>
    </div>
  );
}

export default SettingsModal;

